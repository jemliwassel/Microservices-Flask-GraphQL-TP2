# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x1c\n\x0cShowtimeDate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\",\n\x0cShowtimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2n\n\x08Showtime\x12\x33\n\x11GetShowtimeByDate\x12\r.ShowtimeDate\x1a\r.ShowtimeData\"\x00\x12-\n\x10GetListShowtimes\x12\x06.Empty\x1a\r.ShowtimeData\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SHOWTIMEDATE']._serialized_start=18
  _globals['_SHOWTIMEDATE']._serialized_end=46
  _globals['_SHOWTIMEDATA']._serialized_start=48
  _globals['_SHOWTIMEDATA']._serialized_end=92
  _globals['_EMPTY']._serialized_start=94
  _globals['_EMPTY']._serialized_end=101
  _globals['_SHOWTIME']._serialized_start=103
  _globals['_SHOWTIME']._serialized_end=213
# @@protoc_insertion_point(module_scope)
