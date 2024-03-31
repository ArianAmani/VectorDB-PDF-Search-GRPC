from _utils import (upload_document,
                    search_text,
                    search_pdf,
                    init_model)
import argparse
import grpc

from inference_pb2_grpc import InferenceServerStub
import logging

import asyncio


logging.basicConfig(level=logging.INFO)


async def run(parser) -> None:
    args = parser.parse_args()
    
    # Establish connection to the gRPC server
    async with grpc.aio.insecure_channel('localhost:50052') as channel:
        stub = InferenceServerStub(channel)

        if args.action == "upload":
            if not args.document_path:
                parser.error("--document_path is required for 'upload' action")
            await upload_document(stub, args.document_path)
        elif args.action == "search":
            if args.search_format == "text":
                if not args.query_text:
                    parser.error(
                        "--query_text is required for 'search' action with 'text' format")
                await search_text(stub, args.query_text, args.namespace,
                            args.include_metadata, args.top_k)
            elif args.search_format == "pdf":
                if not args.query_file:
                    parser.error(
                        "--query_file is required for 'search' action with 'pdf' format")
                await search_pdf(stub,
                            args.query_file,
                            args.namespace,
                            args.include_metadata,
                            args.top_k)
        elif args.action == "initModel":
            if not args.api_key:
                parser.error("--api_key is required for 'initModel' action")
            if not args.language_model_path:
                parser.error(
                    "--language_model_path is required for 'initModel' action")
            if not args.summarization_model_path:
                parser.error(
                    "--summarization_model_path is required for 'initModel' action")
            if not args.index_name:
                parser.error("--index_name is required for 'initModel' action")
            if not args.environment:
                parser.error("--environment is required for 'initModel' action")
            
            await init_model(stub,
                       args.api_key,
                       args.language_model_path,
                       args.summarization_model_path,
                       args.index_name,
                       args.metric,
                       args.environment)

if __name__ == '__main__':
    # Parse command line examples
    # python client.py search --search_format=text --query_text "I am a Machine Learning Engineer" --namespace pdfvecdb --top_k 10
    # python client.py search --search_format=pdf --query_file "pdf/random_cell.pdf" --namespace pdfvecdb --top_k 10
    # python client.py upload --document_path "pdf/random_cell.pdf"
    # python client.py initModel --api_key "YOUR_API_KEY" --language_model_path "sentence-transformers/bert-base-nli-mean-tokens" --summarization_model_path "Falconsai/text_summarization" --index_name "pdfvecdb" --metric cosine --environment gcp-starter
    parser = argparse.ArgumentParser(
        description="Interact with gRPC client functions")
    parser.add_argument("action", choices=[
                        "upload", "search", "initModel"], help="Action to perform")
    parser.add_argument(
        "--document_path", help="Path to the PDF document (required for 'upload' action)")
    parser.add_argument("--search_format", choices=["text", "pdf"], default="text",
                        help="Format of the search query (required for 'search' action)")
    parser.add_argument(
        "--query_file", help="Path to the query file (required for 'search' action if search_format is 'pdf')")
    parser.add_argument(
        "--query_text", help="Query text (required for 'search' action if search_format is 'text')")
    parser.add_argument(
        "--namespace", help="Namespace for search (required for 'search' action)")
    parser.add_argument("--include_metadata", action="store_true",
                        help="Include metadata in search results", default=False)
    parser.add_argument("--top_k", type=int, default=10,
                        help="Number of results to return for search")
    parser.add_argument("--api_key", help="Pinecone API key")
    parser.add_argument("--language_model_path", help="Path to the language model")
    parser.add_argument("--summarization_model_path",
                        help="Path to the summarization model")
    parser.add_argument("--index_name", help="Name of the Pinecone index")
    parser.add_argument("--metric", help="Pinecone index metric")
    parser.add_argument("--environment", help="Pinecone environment")

    logging.basicConfig()
    asyncio.run(run(parser))