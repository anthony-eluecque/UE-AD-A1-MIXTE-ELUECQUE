# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: booking.proto
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
    'booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x1a\x1bgoogle/protobuf/empty.proto\"B\n\x11\x41\x64\x64\x42ookingRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\"5\n\x12\x41\x64\x64\x42ookingResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\":\n\x0e\x42ookingDetails\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x18\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\t.DateInfo\"(\n\x08\x44\x61teInfo\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\" \n\x0e\x42ookingRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\"o\n\x0f\x42ookingResponse\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12%\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x16.BookingResponse.Dates\x1a%\n\x05\x44\x61tes\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t2\xc0\x01\n\x07\x42ooking\x12;\n\x14GetBookingFromUserId\x12\x0f.BookingRequest\x1a\x10.BookingResponse\"\x00\x12\x39\n\x0bGetBookings\x12\x16.google.protobuf.Empty\x1a\x10.BookingResponse0\x01\x12=\n\x10\x41\x64\x64\x42ookingByUser\x12\x12.AddBookingRequest\x1a\x13.AddBookingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDBOOKINGREQUEST']._serialized_start=46
  _globals['_ADDBOOKINGREQUEST']._serialized_end=112
  _globals['_ADDBOOKINGRESPONSE']._serialized_start=114
  _globals['_ADDBOOKINGRESPONSE']._serialized_end=167
  _globals['_BOOKINGDETAILS']._serialized_start=169
  _globals['_BOOKINGDETAILS']._serialized_end=227
  _globals['_DATEINFO']._serialized_start=229
  _globals['_DATEINFO']._serialized_end=269
  _globals['_BOOKINGREQUEST']._serialized_start=271
  _globals['_BOOKINGREQUEST']._serialized_end=303
  _globals['_BOOKINGRESPONSE']._serialized_start=305
  _globals['_BOOKINGRESPONSE']._serialized_end=416
  _globals['_BOOKINGRESPONSE_DATES']._serialized_start=379
  _globals['_BOOKINGRESPONSE_DATES']._serialized_end=416
  _globals['_BOOKING']._serialized_start=419
  _globals['_BOOKING']._serialized_end=611
# @@protoc_insertion_point(module_scope)
