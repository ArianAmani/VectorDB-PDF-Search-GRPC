from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetaData(_message.Message):
    __slots__ = ("filename", "extension")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    filename: str
    extension: str
    def __init__(self, filename: _Optional[str] = ..., extension: _Optional[str] = ...) -> None: ...

class UploadFileRequest(_message.Message):
    __slots__ = ("metadata", "chunk_data")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: MetaData
    chunk_data: bytes
    def __init__(self, metadata: _Optional[_Union[MetaData, _Mapping]] = ..., chunk_data: _Optional[bytes] = ...) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ("metadata", "chunk_data", "name_space", "include_metadata", "top_k")
    METADATA_FIELD_NUMBER: _ClassVar[int]
    CHUNK_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    metadata: MetaData
    chunk_data: bytes
    name_space: str
    include_metadata: bool
    top_k: int
    def __init__(self, metadata: _Optional[_Union[MetaData, _Mapping]] = ..., chunk_data: _Optional[bytes] = ..., name_space: _Optional[str] = ..., include_metadata: bool = ..., top_k: _Optional[int] = ...) -> None: ...

class QueryTextRequest(_message.Message):
    __slots__ = ("text", "name_space", "include_metadata", "top_k")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NAME_SPACE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    text: str
    name_space: str
    include_metadata: bool
    top_k: int
    def __init__(self, text: _Optional[str] = ..., name_space: _Optional[str] = ..., include_metadata: bool = ..., top_k: _Optional[int] = ...) -> None: ...

class StringResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class InitializeRequest(_message.Message):
    __slots__ = ("api_key", "language_model_path", "summarization_model_path", "index_name", "metric", "environment")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_MODEL_PATH_FIELD_NUMBER: _ClassVar[int]
    INDEX_NAME_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    language_model_path: str
    summarization_model_path: str
    index_name: str
    metric: str
    environment: str
    def __init__(self, api_key: _Optional[str] = ..., language_model_path: _Optional[str] = ..., summarization_model_path: _Optional[str] = ..., index_name: _Optional[str] = ..., metric: _Optional[str] = ..., environment: _Optional[str] = ...) -> None: ...

class InitializeReply(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
