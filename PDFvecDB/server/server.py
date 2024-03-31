import asyncio
import logging
import os
import grpc

from inference_pb2_grpc import InferenceServer, add_InferenceServerServicer_to_server
from inference_pb2 import (InitializeRequest,
                           InitializeReply,
                           UploadFileRequest,
                           StringResponse)

from inference import dp
from _utils import (get_filepath,)

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)


class InferenceService(InferenceServer):
    async def initialize(self, request: InitializeRequest, context) -> InitializeReply:
        dp.__init__(api_key=request.api_key,
                    language_model_path=request.language_model_path,
                    summarization_model_path=request.summarization_model_path,
                    index_name=request.index_name,
                    metric=request.metric,
                    environment=request.environment)
        return InitializeReply(message="Initialized")


    async def add_document(self, request_iterator, context):
        data = bytearray()
        filepath = 'dummy'

        async for request in request_iterator:
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(
                    request.metadata.filename, request.metadata.extension)
                continue
            data.extend(request.chunk_data)

        file_name = os.path.basename(filepath)
        filepath = os.path.join('server_files', file_name)
        if not os.path.exists('server_files'):
            os.makedirs('server_files')
        with open(filepath, 'wb') as f:
            f.write(data)

        dp.process_and_store(pdf_path=filepath)
        return StringResponse(message='Success!')

    async def query_document(self, request_iterator, context):
        data = bytearray()
        filepath = 'dummy'
        name_space = ''
        include_metadata = False
        top_k = 1
        
        i = -1
        async for request in request_iterator:
            i += 1
            if request.metadata.filename and request.metadata.extension:
                filepath = get_filepath(
                    request.metadata.filename, request.metadata.extension)
                continue
            if i == 1:
                name_space = request.name_space
                continue
            if i == 2:
                include_metadata = request.include_metadata
                continue
            if i == 3:
                top_k = request.top_k
                continue
            data.extend(request.chunk_data)
        file_name = os.path.basename(filepath)
        filepath = os.path.join('server_files', file_name)
        if not os.path.exists('server_files'):
            os.makedirs('server_files')
        with open(filepath, 'wb') as f:
            f.write(data)
        query_response = dp.query_document(pdf_path=filepath,
                                           name_space=name_space,
                                           include_metadata=include_metadata,
                                           top_k=top_k)
        return StringResponse(message=str(query_response))

    async def query_text(self, request, context):
        text = request.text
        name_space = request.name_space
        include_metadata = request.include_metadata
        top_k = request.top_k

        query_response = dp.query_text(text=text,
                                       name_space=name_space,
                                       include_metadata=include_metadata,
                                       top_k=top_k)
        return StringResponse(message=str(query_response))


async def serve():
    server = grpc.aio.server()
    add_InferenceServerServicer_to_server(InferenceService(), server)
    # using ip v6
    adddress = "[::]:50052"
    server.add_insecure_port(adddress)
    logger.info(f"[📡] Starting server on {adddress}")
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
