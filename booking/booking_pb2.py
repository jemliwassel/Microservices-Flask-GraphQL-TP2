# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x19\n\x06UserID\x12\x0f\n\x07user_id\x18\x01 \x01(\t\":\n\x0b\x42ookingData\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x1a\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0b.MovieDates\"*\n\nMovieDates\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"D\n\x11\x41\x64\x64\x42ookingRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x10\n\x08movie_id\x18\x03 \x01(\t\"6\n\x12\x41\x64\x64\x42ookingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2x\n\x07\x42ooking\x12-\n\x12GetBookingByUserID\x12\x07.UserID\x1a\x0c.BookingData\"\x00\x12>\n\x11\x41\x64\x64\x42ookingForUser\x12\x12.AddBookingRequest\x1a\x13.AddBookingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=17
  _globals['_USERID']._serialized_end=42
  _globals['_BOOKINGDATA']._serialized_start=44
  _globals['_BOOKINGDATA']._serialized_end=102
  _globals['_MOVIEDATES']._serialized_start=104
  _globals['_MOVIEDATES']._serialized_end=146
  _globals['_ADDBOOKINGREQUEST']._serialized_start=148
  _globals['_ADDBOOKINGREQUEST']._serialized_end=216
  _globals['_ADDBOOKINGRESPONSE']._serialized_start=218
  _globals['_ADDBOOKINGRESPONSE']._serialized_end=272
  _globals['_BOOKING']._serialized_start=274
  _globals['_BOOKING']._serialized_end=394
# @@protoc_insertion_point(module_scope)
