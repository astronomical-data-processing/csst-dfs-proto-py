# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/misc/misc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/misc/misc.proto',
  package='dfs.common.misc',
  syntax='proto3',
  serialized_options=b'Z cnlab.net/csst/proto/common/misc',
  serialized_pb=b'\n\x16\x63ommon/misc/misc.proto\x12\x0f\x64\x66s.common.misc\"\x1d\n\x0bGetSeqIdReq\x12\x0e\n\x06prefix\x18\x01 \x01(\t\"\x1e\n\x0cGetSeqIdResp\x12\x0e\n\x06nextId\x18\x01 \x01(\x03\x32T\n\x07MiscSrv\x12I\n\x08GetSeqId\x12\x1c.dfs.common.misc.GetSeqIdReq\x1a\x1d.dfs.common.misc.GetSeqIdResp\"\x00\x42\"Z cnlab.net/csst/proto/common/miscb\x06proto3'
)




_GETSEQIDREQ = _descriptor.Descriptor(
  name='GetSeqIdReq',
  full_name='dfs.common.misc.GetSeqIdReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prefix', full_name='dfs.common.misc.GetSeqIdReq.prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=72,
)


_GETSEQIDRESP = _descriptor.Descriptor(
  name='GetSeqIdResp',
  full_name='dfs.common.misc.GetSeqIdResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nextId', full_name='dfs.common.misc.GetSeqIdResp.nextId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['GetSeqIdReq'] = _GETSEQIDREQ
DESCRIPTOR.message_types_by_name['GetSeqIdResp'] = _GETSEQIDRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSeqIdReq = _reflection.GeneratedProtocolMessageType('GetSeqIdReq', (_message.Message,), {
  'DESCRIPTOR' : _GETSEQIDREQ,
  '__module__' : 'common.misc.misc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.common.misc.GetSeqIdReq)
  })
_sym_db.RegisterMessage(GetSeqIdReq)

GetSeqIdResp = _reflection.GeneratedProtocolMessageType('GetSeqIdResp', (_message.Message,), {
  'DESCRIPTOR' : _GETSEQIDRESP,
  '__module__' : 'common.misc.misc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.common.misc.GetSeqIdResp)
  })
_sym_db.RegisterMessage(GetSeqIdResp)


DESCRIPTOR._options = None

_MISCSRV = _descriptor.ServiceDescriptor(
  name='MiscSrv',
  full_name='dfs.common.misc.MiscSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=106,
  serialized_end=190,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSeqId',
    full_name='dfs.common.misc.MiscSrv.GetSeqId',
    index=0,
    containing_service=None,
    input_type=_GETSEQIDREQ,
    output_type=_GETSEQIDRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_MISCSRV)

DESCRIPTOR.services_by_name['MiscSrv'] = _MISCSRV

# @@protoc_insertion_point(module_scope)
