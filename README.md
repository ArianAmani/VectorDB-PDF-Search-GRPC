# gRPC Client-Server for Document Processing and Search

This repository contains a gRPC client-server implementation for document processing and search functionalities. It provides capabilities for uploading documents, searching text or PDF documents, and initializing the models required for processing and indexing documents.

## Features

- **Document Upload**: Upload PDF documents to the server for processing and indexing.
- **Text and PDF Search**: Search for text or PDF documents using specified query strings.
- **Model Initialization**: Initialize language and summarization models for document processing.

## Usage

### Prerequisites

- Python 3
- Docker (for containerization)

### Running the Server

#### Important: Change your initialization settings for the model to use in `server/inference.py`
* API_KEY
* language_model_path
* summarization_model_path
* index_name
* metric
* environment
  
1. Build the Docker image:

```bash
docker build -t your_image_name .
```

2. Run the Docker container:
```bash
docker run -d -p 50052:50052 your_image_name
```

### Running the Client
The client interacts with the server using gRPC calls. It supports various actions:

- Upload: Upload a PDF document to the server.

Example:
```bash
python client.py upload --document_path "pdf/file_name.pdf"
```

- Search: Search for documents based on text or PDF queries.

Example (text search):
```bash
python client.py search --search_format=text --query_text "Any text you want to use as query" --namespace pdfvecdb --top_k 10
```

Example (PDF search):
```bash
python client.py search --search_format=pdf --query_file "pdf/file_name.pdf" --namespace pdfvecdb --top_k 10
```

- InitModel: Initialize models required for document processing.

Example:
```bash
python client.py initModel --api_key "YOUR_API_KEY" --language_model_path "sentence-transformers/bert-base-nli-mean-tokens" --summarization_model_path "Falconsai/text_summarization" --index_name "pdfvecdb" --metric cosine --environment gcp-starter
```
