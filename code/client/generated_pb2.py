# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generated.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgenerated.proto\"B\n\rTicketRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12 \n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x0e.BingoCategory\"(\n\x0b\x42ingoTicket\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"6\n\x13\x42ingoTicketResponse\x12\x1f\n\tgenerated\x18\x01 \x03(\x0b\x32\x0c.BingoTicket*@\n\rBingoCategory\x12\x0b\n\x07UKBINGO\x10\x00\x12\x0b\n\x07USBINGO\x10\x01\x12\n\n\x06IMAGES\x10\x02\x12\t\n\x05WORDS\x10\x03\x32<\n\tGenerated\x12/\n\x07Tickets\x12\x0e.TicketRequest\x1a\x14.BingoTicketResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'generated_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BINGOCATEGORY._serialized_start=185
  _BINGOCATEGORY._serialized_end=249
  _TICKETREQUEST._serialized_start=19
  _TICKETREQUEST._serialized_end=85
  _BINGOTICKET._serialized_start=87
  _BINGOTICKET._serialized_end=127
  _BINGOTICKETRESPONSE._serialized_start=129
  _BINGOTICKETRESPONSE._serialized_end=183
  _GENERATED._serialized_start=251
  _GENERATED._serialized_end=311
# @@protoc_insertion_point(module_scope)
