# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: showtime.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'showtime.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1c\n\x0cShowTimeDate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\",\n\x0cShowTimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t2z\n\x08ShowTime\x12\x33\n\x11GetShowTimeByDate\x12\r.ShowTimeDate\x1a\r.ShowTimeData\"\x00\x12\x39\n\x0cGetShowTimes\x12\x16.google.protobuf.Empty\x1a\r.ShowTimeData\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SHOWTIMEDATE']._serialized_start=47
  _globals['_SHOWTIMEDATE']._serialized_end=75
  _globals['_SHOWTIMEDATA']._serialized_start=77
  _globals['_SHOWTIMEDATA']._serialized_end=121
  _globals['_SHOWTIME']._serialized_start=123
  _globals['_SHOWTIME']._serialized_end=245
# @@protoc_insertion_point(module_scope)