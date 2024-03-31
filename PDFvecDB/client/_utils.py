import inference_pb2
import os


def get_filepath(filename, extension):
    return f'{filename}{extension}'


async def read_iterfile(filepath, chunk_size=1024):
    split_data = os.path.splitext(filepath)
    filename = split_data[0]
    extension = split_data[1]

    metadata = inference_pb2.MetaData(filename=filename, extension=extension)
    yield inference_pb2.UploadFileRequest(metadata=metadata)
    with open(filepath, mode="rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                entry_request = inference_pb2.UploadFileRequest(
                    chunk_data=chunk)
                yield entry_request
            else:  # The chunk was empty, which means we're at the end of the file
                return


async def read_iterfile_query(filepath, namespace='', include_metadata=False, top_k=10, chunk_size=1024):
    split_data = os.path.splitext(filepath)
    filename = split_data[0]
    extension = split_data[1]

    metadata = inference_pb2.MetaData(
        filename=filename, extension=extension)
    yield inference_pb2.QueryRequest(metadata=metadata)
    yield inference_pb2.QueryRequest(name_space=namespace)
    yield inference_pb2.QueryRequest(include_metadata=include_metadata)
    yield inference_pb2.QueryRequest(top_k=top_k)
    with open(filepath, mode="rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if chunk:
                entry_request = inference_pb2.QueryRequest(chunk_data=chunk)
                yield entry_request
            else:  # The chunk was empty, which means we're at the end of the file
                return


async def upload_document(stub, document_path):
    response = await stub.add_document(read_iterfile(document_path))
    print(response.message)
    return response


async def search_text(stub, query_text, namespace, include_metadata, top_k):
    request = inference_pb2.QueryTextRequest(
        text=query_text, name_space=namespace, include_metadata=include_metadata, top_k=top_k)
    response = await stub.query_text(request)
    print(response.message)
    return response


async def search_pdf(stub, query_file, namespace, include_metadata, top_k):
    response =  await stub.query_document(read_iterfile_query(query_file,
                                              namespace=namespace,
                                              include_metadata=include_metadata,
                                              top_k=top_k))
    print(response.message)
    return response


async def init_model(stub,
               api_key,
               language_model_path,
               summarization_model_path,
               index_name,
               metric,
               environment):
    request = inference_pb2.InitializeRequest(
        api_key=api_key,
        language_model_path=language_model_path,
        summarization_model_path=summarization_model_path,
        index_name=index_name,
        metric=metric,
        environment=environment)
    response = await stub.initialize(request)
    print(response.message)
    return response