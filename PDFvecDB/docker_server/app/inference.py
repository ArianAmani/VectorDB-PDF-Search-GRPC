from _model import DocumentProcessor

API_KEY = "YOUR_API_KEY"
dp = DocumentProcessor(
    api_key=API_KEY,
    language_model_path='sentence-transformers/bert-base-nli-mean-tokens',
    summarization_model_path='Falconsai/text_summarization',
    index_name="pdfvecdb",
    metric="cosine",
    environment="gcp-starter",
)
