from pinecone import Pinecone, ServerlessSpec, PodSpec
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, AutoModel, pipeline

import os

import nltk
from nltk.corpus import stopwords

import torch


class DocumentProcessor:
    def __init__(self,
                 api_key,
                 language_model_path,
                 summarization_model_path,
                 index_name,
                 metric="cosine",
                 environment="gcp-starter"):
        self.api_key = api_key
        self.language_model_path = language_model_path
        self.summarization_model_path = summarization_model_path
        self.index_name = index_name
        self.metric = metric
        self.environment = environment

        self.tokenizer, self.model, self.dim = \
            self.load_language_model(language_model_path)

        self.summarizer = \
            self.load_summarization_model(summarization_model_path)

        self.index = self.init_pinecone_index()

    def load_language_model(self, path):
        tokenizer = AutoTokenizer.from_pretrained(path)
        model = AutoModel.from_pretrained(path)
        dim = model.config.hidden_size
        return tokenizer, model, dim

    def load_summarization_model(self, path):
        summarizer = pipeline("summarization", model=path)
        return summarizer

    def extract_text(self, file_path):
        loader = PyPDFLoader(file_path)
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0)
        documents = text_splitter.split_documents(data)
        texts = [str(doc) for doc in documents]
        return texts

    def clean_text(self, text):
        nltk.download('stopwords')
        stop_words = stopwords.words('english')
        text = text.lower()
        text = ' '.join([word for word in text.split()
                         if word not in stop_words])
        return text

    def summarize_text(self, text):
        if len(text) < 100:
            return text
        summary = self.summarizer(text)
        return summary[0]['summary_text']

    def get_embeddings(self, text):
        embeddings = []
        for summary in text:
            encoded_input = self.tokenizer(
                summary, return_tensors="pt")

            with torch.no_grad():
                output = self.model(**encoded_input)
            embeddings.append(output.last_hidden_state[0])
        embeddings = torch.cat(embeddings, dim=0)
        return embeddings.mean(axis=0)

    def store_embedding(self, doc_id, embedding, text):
        self.index.upsert([{"id": doc_id,
                            "values": embedding.tolist(),
                            'metadata': {'text': text}}],
                          self.index_name)

    def process_and_store(self, pdf_path):
        texts = self.extract_text(pdf_path)
        cleaned_texts = [self.clean_text(text) for text in texts]
        summary = [self.summarize_text(cleaned_text)
                   for cleaned_text in cleaned_texts]

        embedding = self.get_embeddings(summary)
        doc_id = os.path.basename(pdf_path)
        self.store_embedding(doc_id=doc_id,
                             embedding=embedding,
                             text=" ".join(cleaned_texts))

    def init_pinecone_index(self):
        pc = Pinecone(api_key=self.api_key)

        if self.index_name not in pc.list_indexes().names():
            # pc.delete_index(self.index_name)
            # time.sleep(10)
            pc.create_index(name=self.index_name,
                            dimension=self.dim,
                            metric=self.metric,
                            spec=PodSpec(environment=self.environment,))
        index = pc.Index(self.index_name)
        return index

    def query_text(self,
              text,
              name_space='',
              include_metadata=False,
              top_k=10):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(text)
        
        cleaned_texts = [self.clean_text(text) for text in texts]
        summary = [self.summarize_text(cleaned_text)
                   for cleaned_text in cleaned_texts]
        embedding = self.get_embeddings(summary)
        xq = embedding.tolist()
        xc = self.index.query(vector=xq,
                              namespace=name_space,
                              top_k=top_k,
                              include_metadata=include_metadata)
        return xc


    def query_document(self,
                       pdf_path,
                       name_space='',
                       include_metadata=False,
                       top_k=10):
        texts = self.extract_text(pdf_path)
        cleaned_texts = [self.clean_text(text) for text in texts]
        summary = [self.summarize_text(cleaned_text)
                   for cleaned_text in cleaned_texts]
        embedding = self.get_embeddings(summary)
        xq = embedding.tolist()
        xc = self.index.query(vector=xq,
                              namespace=name_space,
                              top_k=top_k,
                              include_metadata=include_metadata)
        return xc
