# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inference.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0finference.proto\"/\n\x08MetaData\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t\"S\n\x11UploadFileRequest\x12\x1d\n\x08metadata\x18\x01 \x01(\x0b\x32\t.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request\"\x91\x01\n\x0cQueryRequest\x12\x1d\n\x08metadata\x18\x01 \x01(\x0b\x32\t.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x12\x14\n\nname_space\x18\x03 \x01(\tH\x00\x12\x1a\n\x10include_metadata\x18\x04 \x01(\x08H\x00\x12\x0f\n\x05top_k\x18\x05 \x01(\x05H\x00\x42\t\n\x07request\"]\n\x10QueryTextRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nname_space\x18\x02 \x01(\t\x12\x18\n\x10include_metadata\x18\x03 \x01(\x08\x12\r\n\x05top_k\x18\x04 \x01(\x05\"!\n\x0eStringResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x9c\x01\n\x11InitializeRequest\x12\x0f\n\x07\x61pi_key\x18\x01 \x01(\t\x12\x1b\n\x13language_model_path\x18\x02 \x01(\t\x12 \n\x18summarization_model_path\x18\x03 \x01(\t\x12\x12\n\nindex_name\x18\x04 \x01(\t\x12\x0e\n\x06metric\x18\x05 \x01(\t\x12\x13\n\x0b\x65nvironment\x18\x06 \x01(\t\"\"\n\x0fInitializeReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\xea\x01\n\x0fInferenceServer\x12\x34\n\ninitialize\x12\x12.InitializeRequest\x1a\x10.InitializeReply\"\x00\x12\x37\n\x0c\x61\x64\x64_document\x12\x12.UploadFileRequest\x1a\x0f.StringResponse\"\x00(\x01\x12\x34\n\x0equery_document\x12\r.QueryRequest\x1a\x0f.StringResponse\"\x00(\x01\x12\x32\n\nquery_text\x12\x11.QueryTextRequest\x1a\x0f.StringResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'inference_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_METADATA']._serialized_start=19
  _globals['_METADATA']._serialized_end=66
  _globals['_UPLOADFILEREQUEST']._serialized_start=68
  _globals['_UPLOADFILEREQUEST']._serialized_end=151
  _globals['_QUERYREQUEST']._serialized_start=154
  _globals['_QUERYREQUEST']._serialized_end=299
  _globals['_QUERYTEXTREQUEST']._serialized_start=301
  _globals['_QUERYTEXTREQUEST']._serialized_end=394
  _globals['_STRINGRESPONSE']._serialized_start=396
  _globals['_STRINGRESPONSE']._serialized_end=429
  _globals['_INITIALIZEREQUEST']._serialized_start=432
  _globals['_INITIALIZEREQUEST']._serialized_end=588
  _globals['_INITIALIZEREPLY']._serialized_start=590
  _globals['_INITIALIZEREPLY']._serialized_end=624
  _globals['_INFERENCESERVER']._serialized_start=627
  _globals['_INFERENCESERVER']._serialized_end=861
# @@protoc_insertion_point(module_scope)