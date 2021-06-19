# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/level0/level0.proto

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
  name='facility/level0/level0.proto',
  package='dfs.facility.level0',
  syntax='proto3',
  serialized_options=_b('Z$cnlab.net/csst/proto/facility/level0'),
  serialized_pb=_b('\n\x1c\x66\x61\x63ility/level0/level0.proto\x12\x13\x64\x66s.facility.level0\x1a\x12\x63ommon/error.proto\"\x97\x02\n\x0cLevel0Record\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06obs_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x64\x65tector_no\x18\x03 \x01(\t\x12\x10\n\x08obs_type\x18\x04 \x01(\t\x12\x10\n\x08obs_time\x18\x05 \x01(\t\x12\x10\n\x08\x65xp_time\x18\x06 \x01(\x02\x12\x1a\n\x12\x64\x65tector_status_id\x18\x07 \x01(\x03\x12\x10\n\x08\x66ilename\x18\x08 \x01(\t\x12\x11\n\tfile_path\x18\t \x01(\t\x12\x12\n\nqc0_status\x18\n \x01(\r\x12\x10\n\x08qc0_time\x18\x0b \x01(\t\x12\x12\n\nprc_status\x18\x0c \x01(\r\x12\x10\n\x08prc_time\x18\r \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0e \x01(\t\"\xd1\x02\n\x11\x46indLevel0DataReq\x12\x0e\n\x06obs_id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65tector_no\x18\x02 \x01(\t\x12\x10\n\x08obs_type\x18\x03 \x01(\t\x12\x16\n\x0e\x65xp_time_start\x18\x04 \x01(\t\x12\x14\n\x0c\x65xp_time_end\x18\x05 \x01(\t\x12\x12\n\nqc0_status\x18\x06 \x01(\r\x12\x12\n\nprc_status\x18\x07 \x01(\r\x12\x11\n\tfile_name\x18\x08 \x01(\t\x12\r\n\x05limit\x18\t \x01(\r\x12U\n\x10other_conditions\x18\n \x03(\x0b\x32;.dfs.facility.level0.FindLevel0DataReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8b\x01\n\x12\x46indLevel0DataResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x32\n\x07records\x18\x04 \x03(\x0b\x32!.dfs.facility.level0.Level0Record\"\x1e\n\x10GetLevel0DataReq\x12\n\n\x02id\x18\x01 \x01(\x03\"F\n\x11GetLevel0DataResp\x12\x31\n\x06record\x18\x01 \x01(\x0b\x32!.dfs.facility.level0.Level0Record\"G\n\x12WriteLevel0DataReq\x12\x31\n\x06record\x18\x01 \x01(\x0b\x32!.dfs.facility.level0.Level0Record\"w\n\x13WriteLevel0DataResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x31\n\x06record\x18\x03 \x01(\x0b\x32!.dfs.facility.level0.Level0Record\"0\n\x12UpdateQc0StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"D\n\x13UpdateQc0StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xef\x03\n\tLevel0Srv\x12Y\n\x04\x46ind\x12&.dfs.facility.level0.FindLevel0DataReq\x1a\'.dfs.facility.level0.FindLevel0DataResp\"\x00\x12V\n\x03Get\x12%.dfs.facility.level0.GetLevel0DataReq\x1a&.dfs.facility.level0.GetLevel0DataResp\"\x00\x12\\\n\x05Write\x12\'.dfs.facility.level0.WriteLevel0DataReq\x1a(.dfs.facility.level0.WriteLevel0DataResp\"\x00\x12\x66\n\x0fUpdateQc0Status\x12\'.dfs.facility.level0.UpdateQc0StatusReq\x1a(.dfs.facility.level0.UpdateQc0StatusResp\"\x00\x12i\n\x10UpdateProcStatus\x12(.dfs.facility.level0.UpdateProcStatusReq\x1a).dfs.facility.level0.UpdateProcStatusResp\"\x00\x42&Z$cnlab.net/csst/proto/facility/level0b\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_LEVEL0RECORD = _descriptor.Descriptor(
  name='Level0Record',
  full_name='dfs.facility.level0.Level0Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.level0.Level0Record.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='dfs.facility.level0.Level0Record.obs_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.level0.Level0Record.detector_no', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_type', full_name='dfs.facility.level0.Level0Record.obs_type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_time', full_name='dfs.facility.level0.Level0Record.obs_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time', full_name='dfs.facility.level0.Level0Record.exp_time', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_status_id', full_name='dfs.facility.level0.Level0Record.detector_status_id', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.facility.level0.Level0Record.filename', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='dfs.facility.level0.Level0Record.file_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_status', full_name='dfs.facility.level0.Level0Record.qc0_status', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_time', full_name='dfs.facility.level0.Level0Record.qc0_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.facility.level0.Level0Record.prc_status', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='dfs.facility.level0.Level0Record.prc_time', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.facility.level0.Level0Record.create_time', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_start=74,
  serialized_end=353,
)


_FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.facility.level0.FindLevel0DataReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.facility.level0.FindLevel0DataReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.facility.level0.FindLevel0DataReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=639,
  serialized_end=693,
)

_FINDLEVEL0DATAREQ = _descriptor.Descriptor(
  name='FindLevel0DataReq',
  full_name='dfs.facility.level0.FindLevel0DataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='dfs.facility.level0.FindLevel0DataReq.obs_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.level0.FindLevel0DataReq.detector_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_type', full_name='dfs.facility.level0.FindLevel0DataReq.obs_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_start', full_name='dfs.facility.level0.FindLevel0DataReq.exp_time_start', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_end', full_name='dfs.facility.level0.FindLevel0DataReq.exp_time_end', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_status', full_name='dfs.facility.level0.FindLevel0DataReq.qc0_status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.facility.level0.FindLevel0DataReq.prc_status', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='dfs.facility.level0.FindLevel0DataReq.file_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.facility.level0.FindLevel0DataReq.limit', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.facility.level0.FindLevel0DataReq.other_conditions', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=693,
)


_FINDLEVEL0DATARESP = _descriptor.Descriptor(
  name='FindLevel0DataResp',
  full_name='dfs.facility.level0.FindLevel0DataResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.level0.FindLevel0DataResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.level0.FindLevel0DataResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.level0.FindLevel0DataResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.level0.FindLevel0DataResp.records', index=3,
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
  serialized_start=696,
  serialized_end=835,
)


_GETLEVEL0DATAREQ = _descriptor.Descriptor(
  name='GetLevel0DataReq',
  full_name='dfs.facility.level0.GetLevel0DataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.level0.GetLevel0DataReq.id', index=0,
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
  serialized_start=837,
  serialized_end=867,
)


_GETLEVEL0DATARESP = _descriptor.Descriptor(
  name='GetLevel0DataResp',
  full_name='dfs.facility.level0.GetLevel0DataResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.level0.GetLevel0DataResp.record', index=0,
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
  serialized_start=869,
  serialized_end=939,
)


_WRITELEVEL0DATAREQ = _descriptor.Descriptor(
  name='WriteLevel0DataReq',
  full_name='dfs.facility.level0.WriteLevel0DataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.level0.WriteLevel0DataReq.record', index=0,
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
  serialized_start=941,
  serialized_end=1012,
)


_WRITELEVEL0DATARESP = _descriptor.Descriptor(
  name='WriteLevel0DataResp',
  full_name='dfs.facility.level0.WriteLevel0DataResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.level0.WriteLevel0DataResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.level0.WriteLevel0DataResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.level0.WriteLevel0DataResp.record', index=2,
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
  serialized_start=1014,
  serialized_end=1133,
)


_UPDATEQC0STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc0StatusReq',
  full_name='dfs.facility.level0.UpdateQc0StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.level0.UpdateQc0StatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.facility.level0.UpdateQc0StatusReq.status', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1135,
  serialized_end=1183,
)


_UPDATEQC0STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc0StatusResp',
  full_name='dfs.facility.level0.UpdateQc0StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.level0.UpdateQc0StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.level0.UpdateQc0StatusResp.error', index=1,
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
  serialized_start=1185,
  serialized_end=1253,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='dfs.facility.level0.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.level0.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.facility.level0.UpdateProcStatusReq.status', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1255,
  serialized_end=1304,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='dfs.facility.level0.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.level0.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.level0.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1306,
  serialized_end=1375,
)

_FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY.containing_type = _FINDLEVEL0DATAREQ
_FINDLEVEL0DATAREQ.fields_by_name['other_conditions'].message_type = _FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY
_FINDLEVEL0DATARESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDLEVEL0DATARESP.fields_by_name['records'].message_type = _LEVEL0RECORD
_GETLEVEL0DATARESP.fields_by_name['record'].message_type = _LEVEL0RECORD
_WRITELEVEL0DATAREQ.fields_by_name['record'].message_type = _LEVEL0RECORD
_WRITELEVEL0DATARESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITELEVEL0DATARESP.fields_by_name['record'].message_type = _LEVEL0RECORD
_UPDATEQC0STATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['Level0Record'] = _LEVEL0RECORD
DESCRIPTOR.message_types_by_name['FindLevel0DataReq'] = _FINDLEVEL0DATAREQ
DESCRIPTOR.message_types_by_name['FindLevel0DataResp'] = _FINDLEVEL0DATARESP
DESCRIPTOR.message_types_by_name['GetLevel0DataReq'] = _GETLEVEL0DATAREQ
DESCRIPTOR.message_types_by_name['GetLevel0DataResp'] = _GETLEVEL0DATARESP
DESCRIPTOR.message_types_by_name['WriteLevel0DataReq'] = _WRITELEVEL0DATAREQ
DESCRIPTOR.message_types_by_name['WriteLevel0DataResp'] = _WRITELEVEL0DATARESP
DESCRIPTOR.message_types_by_name['UpdateQc0StatusReq'] = _UPDATEQC0STATUSREQ
DESCRIPTOR.message_types_by_name['UpdateQc0StatusResp'] = _UPDATEQC0STATUSRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Level0Record = _reflection.GeneratedProtocolMessageType('Level0Record', (_message.Message,), {
  'DESCRIPTOR' : _LEVEL0RECORD,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.Level0Record)
  })
_sym_db.RegisterMessage(Level0Record)

FindLevel0DataReq = _reflection.GeneratedProtocolMessageType('FindLevel0DataReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.level0.level0_pb2'
    # @@protoc_insertion_point(class_scope:dfs.facility.level0.FindLevel0DataReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDLEVEL0DATAREQ,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.FindLevel0DataReq)
  })
_sym_db.RegisterMessage(FindLevel0DataReq)
_sym_db.RegisterMessage(FindLevel0DataReq.OtherConditionsEntry)

FindLevel0DataResp = _reflection.GeneratedProtocolMessageType('FindLevel0DataResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL0DATARESP,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.FindLevel0DataResp)
  })
_sym_db.RegisterMessage(FindLevel0DataResp)

GetLevel0DataReq = _reflection.GeneratedProtocolMessageType('GetLevel0DataReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL0DATAREQ,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.GetLevel0DataReq)
  })
_sym_db.RegisterMessage(GetLevel0DataReq)

GetLevel0DataResp = _reflection.GeneratedProtocolMessageType('GetLevel0DataResp', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL0DATARESP,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.GetLevel0DataResp)
  })
_sym_db.RegisterMessage(GetLevel0DataResp)

WriteLevel0DataReq = _reflection.GeneratedProtocolMessageType('WriteLevel0DataReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL0DATAREQ,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.WriteLevel0DataReq)
  })
_sym_db.RegisterMessage(WriteLevel0DataReq)

WriteLevel0DataResp = _reflection.GeneratedProtocolMessageType('WriteLevel0DataResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL0DATARESP,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.WriteLevel0DataResp)
  })
_sym_db.RegisterMessage(WriteLevel0DataResp)

UpdateQc0StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc0StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC0STATUSREQ,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.UpdateQc0StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc0StatusReq)

UpdateQc0StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc0StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC0STATUSRESP,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.UpdateQc0StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc0StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'facility.level0.level0_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.level0.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDLEVEL0DATAREQ_OTHERCONDITIONSENTRY._options = None

_LEVEL0SRV = _descriptor.ServiceDescriptor(
  name='Level0Srv',
  full_name='dfs.facility.level0.Level0Srv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1378,
  serialized_end=1873,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.facility.level0.Level0Srv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDLEVEL0DATAREQ,
    output_type=_FINDLEVEL0DATARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.facility.level0.Level0Srv.Get',
    index=1,
    containing_service=None,
    input_type=_GETLEVEL0DATAREQ,
    output_type=_GETLEVEL0DATARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.facility.level0.Level0Srv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITELEVEL0DATAREQ,
    output_type=_WRITELEVEL0DATARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc0Status',
    full_name='dfs.facility.level0.Level0Srv.UpdateQc0Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC0STATUSREQ,
    output_type=_UPDATEQC0STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='dfs.facility.level0.Level0Srv.UpdateProcStatus',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEVEL0SRV)

DESCRIPTOR.services_by_name['Level0Srv'] = _LEVEL0SRV

# @@protoc_insertion_point(module_scope)
