# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sls/level0prc/level0prc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sls/level0prc/level0prc.proto',
  package='dfs.sls.level0prc',
  syntax='proto3',
  serialized_options=_b('Z\"cnlab.net/csst/proto/sls/level0prc'),
  serialized_pb=_b('\n\x1dsls/level0prc/level0prc.proto\x12\x11\x64\x66s.sls.level0prc\x1a\x12\x63ommon/error.proto\"\xb3\x01\n\x0fLevel0PrcRecord\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x13\n\x0bpipeline_id\x18\x03 \x01(\t\x12\x12\n\nprc_module\x18\x04 \x01(\t\x12\x18\n\x10params_file_path\x18\x05 \x01(\t\x12\x12\n\nprc_status\x18\x06 \x01(\x05\x12\x10\n\x08prc_time\x18\x07 \x01(\t\x12\x18\n\x10result_file_path\x18\x08 \x01(\t\"\xee\x01\n\x10\x46indLevel0PrcReq\x12\x11\n\tlevel0_id\x18\x01 \x01(\t\x12\x13\n\x0bpipeline_id\x18\x02 \x01(\t\x12\x12\n\nprc_module\x18\x03 \x01(\t\x12\x12\n\nprc_status\x18\x04 \x01(\x05\x12R\n\x10other_conditions\x18\x05 \x03(\x0b\x32\x38.dfs.sls.level0prc.FindLevel0PrcReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8b\x01\n\x11\x46indLevel0PrcResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x33\n\x07records\x18\x04 \x03(\x0b\x32\".dfs.sls.level0prc.Level0PrcRecord\"G\n\x11WriteLevel0PrcReq\x12\x32\n\x06record\x18\x01 \x01(\x0b\x32\".dfs.sls.level0prc.Level0PrcRecord\"w\n\x12WriteLevel0PrcResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x32\n\x06record\x18\x03 \x01(\x0b\x32\".dfs.sls.level0prc.Level0PrcRecord\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xa2\x02\n\x0cLevel0PrcSrv\x12S\n\x04\x46ind\x12#.dfs.sls.level0prc.FindLevel0PrcReq\x1a$.dfs.sls.level0prc.FindLevel0PrcResp\"\x00\x12V\n\x05Write\x12$.dfs.sls.level0prc.WriteLevel0PrcReq\x1a%.dfs.sls.level0prc.WriteLevel0PrcResp\"\x00\x12\x65\n\x10UpdateProcStatus\x12&.dfs.sls.level0prc.UpdateProcStatusReq\x1a\'.dfs.sls.level0prc.UpdateProcStatusResp\"\x00\x42$Z\"cnlab.net/csst/proto/sls/level0prcb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_LEVEL0PRCRECORD = _descriptor.Descriptor(
  name='Level0PrcRecord',
  full_name='dfs.sls.level0prc.Level0PrcRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level0prc.Level0PrcRecord.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.sls.level0prc.Level0PrcRecord.level0_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='dfs.sls.level0prc.Level0PrcRecord.pipeline_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_module', full_name='dfs.sls.level0prc.Level0PrcRecord.prc_module', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='params_file_path', full_name='dfs.sls.level0prc.Level0PrcRecord.params_file_path', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.sls.level0prc.Level0PrcRecord.prc_status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='dfs.sls.level0prc.Level0PrcRecord.prc_time', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_file_path', full_name='dfs.sls.level0prc.Level0PrcRecord.result_file_path', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=73,
  serialized_end=252,
)


_FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.sls.level0prc.FindLevel0PrcReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.sls.level0prc.FindLevel0PrcReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.sls.level0prc.FindLevel0PrcReq.OtherConditionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=439,
  serialized_end=493,
)

_FINDLEVEL0PRCREQ = _descriptor.Descriptor(
  name='FindLevel0PrcReq',
  full_name='dfs.sls.level0prc.FindLevel0PrcReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.sls.level0prc.FindLevel0PrcReq.level0_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='dfs.sls.level0prc.FindLevel0PrcReq.pipeline_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_module', full_name='dfs.sls.level0prc.FindLevel0PrcReq.prc_module', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.sls.level0prc.FindLevel0PrcReq.prc_status', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.sls.level0prc.FindLevel0PrcReq.other_conditions', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=493,
)


_FINDLEVEL0PRCRESP = _descriptor.Descriptor(
  name='FindLevel0PrcResp',
  full_name='dfs.sls.level0prc.FindLevel0PrcResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level0prc.FindLevel0PrcResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.sls.level0prc.FindLevel0PrcResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level0prc.FindLevel0PrcResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.sls.level0prc.FindLevel0PrcResp.records', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=496,
  serialized_end=635,
)


_WRITELEVEL0PRCREQ = _descriptor.Descriptor(
  name='WriteLevel0PrcReq',
  full_name='dfs.sls.level0prc.WriteLevel0PrcReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.sls.level0prc.WriteLevel0PrcReq.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=637,
  serialized_end=708,
)


_WRITELEVEL0PRCRESP = _descriptor.Descriptor(
  name='WriteLevel0PrcResp',
  full_name='dfs.sls.level0prc.WriteLevel0PrcResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level0prc.WriteLevel0PrcResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level0prc.WriteLevel0PrcResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.sls.level0prc.WriteLevel0PrcResp.record', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=710,
  serialized_end=829,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='dfs.sls.level0prc.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level0prc.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.sls.level0prc.UpdateProcStatusReq.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=831,
  serialized_end=880,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='dfs.sls.level0prc.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level0prc.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level0prc.UpdateProcStatusResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=882,
  serialized_end=951,
)

_FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY.containing_type = _FINDLEVEL0PRCREQ
_FINDLEVEL0PRCREQ.fields_by_name['other_conditions'].message_type = _FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY
_FINDLEVEL0PRCRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDLEVEL0PRCRESP.fields_by_name['records'].message_type = _LEVEL0PRCRECORD
_WRITELEVEL0PRCREQ.fields_by_name['record'].message_type = _LEVEL0PRCRECORD
_WRITELEVEL0PRCRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITELEVEL0PRCRESP.fields_by_name['record'].message_type = _LEVEL0PRCRECORD
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['Level0PrcRecord'] = _LEVEL0PRCRECORD
DESCRIPTOR.message_types_by_name['FindLevel0PrcReq'] = _FINDLEVEL0PRCREQ
DESCRIPTOR.message_types_by_name['FindLevel0PrcResp'] = _FINDLEVEL0PRCRESP
DESCRIPTOR.message_types_by_name['WriteLevel0PrcReq'] = _WRITELEVEL0PRCREQ
DESCRIPTOR.message_types_by_name['WriteLevel0PrcResp'] = _WRITELEVEL0PRCRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Level0PrcRecord = _reflection.GeneratedProtocolMessageType('Level0PrcRecord', (_message.Message,), {
  'DESCRIPTOR' : _LEVEL0PRCRECORD,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.Level0PrcRecord)
  })
_sym_db.RegisterMessage(Level0PrcRecord)

FindLevel0PrcReq = _reflection.GeneratedProtocolMessageType('FindLevel0PrcReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'sls.level0prc.level0prc_pb2'
    # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.FindLevel0PrcReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDLEVEL0PRCREQ,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.FindLevel0PrcReq)
  })
_sym_db.RegisterMessage(FindLevel0PrcReq)
_sym_db.RegisterMessage(FindLevel0PrcReq.OtherConditionsEntry)

FindLevel0PrcResp = _reflection.GeneratedProtocolMessageType('FindLevel0PrcResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL0PRCRESP,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.FindLevel0PrcResp)
  })
_sym_db.RegisterMessage(FindLevel0PrcResp)

WriteLevel0PrcReq = _reflection.GeneratedProtocolMessageType('WriteLevel0PrcReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL0PRCREQ,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.WriteLevel0PrcReq)
  })
_sym_db.RegisterMessage(WriteLevel0PrcReq)

WriteLevel0PrcResp = _reflection.GeneratedProtocolMessageType('WriteLevel0PrcResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL0PRCRESP,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.WriteLevel0PrcResp)
  })
_sym_db.RegisterMessage(WriteLevel0PrcResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'sls.level0prc.level0prc_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level0prc.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDLEVEL0PRCREQ_OTHERCONDITIONSENTRY._options = None

_LEVEL0PRCSRV = _descriptor.ServiceDescriptor(
  name='Level0PrcSrv',
  full_name='dfs.sls.level0prc.Level0PrcSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=954,
  serialized_end=1244,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.sls.level0prc.Level0PrcSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDLEVEL0PRCREQ,
    output_type=_FINDLEVEL0PRCRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.sls.level0prc.Level0PrcSrv.Write',
    index=1,
    containing_service=None,
    input_type=_WRITELEVEL0PRCREQ,
    output_type=_WRITELEVEL0PRCRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='dfs.sls.level0prc.Level0PrcSrv.UpdateProcStatus',
    index=2,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEVEL0PRCSRV)

DESCRIPTOR.services_by_name['Level0PrcSrv'] = _LEVEL0PRCSRV

# @@protoc_insertion_point(module_scope)
