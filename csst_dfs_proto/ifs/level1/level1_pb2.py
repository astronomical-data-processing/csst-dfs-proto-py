# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ifs/level1/level1.proto

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
  name='ifs/level1/level1.proto',
  package='dfs.ifs.level1',
  syntax='proto3',
  serialized_options=_b('Z\037cnlab.net/csst/proto/ifs/level1'),
  serialized_pb=_b('\n\x17ifs/level1/level1.proto\x12\x0e\x64\x66s.ifs.level1\x1a\x12\x63ommon/error.proto\"\xe6\x02\n\x0cLevel1Record\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\x12\n\ncor_sci_id\x18\x04 \x01(\x03\x12\x12\n\nprc_params\x18\x05 \x01(\t\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x11\n\tfile_path\x18\x07 \x01(\t\x12\x12\n\nqc1_status\x18\x08 \x01(\x05\x12\x10\n\x08qc1_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\x05\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x13\n\x0bpipeline_id\x18\r \x01(\t\x12\x34\n\x04refs\x18\x0e \x03(\x0b\x32&.dfs.ifs.level1.Level1Record.RefsEntry\x1a+\n\tRefsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"\xb8\x02\n\rFindLevel1Req\x12\x11\n\tlevel0_id\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\x19\n\x11\x63reate_time_start\x18\x03 \x01(\t\x12\x17\n\x0f\x63reate_time_end\x18\x04 \x01(\t\x12\x12\n\nqc1_status\x18\x05 \x01(\x05\x12\x12\n\nprc_status\x18\x06 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x07 \x01(\t\x12\r\n\x05limit\x18\x08 \x01(\x05\x12L\n\x10other_conditions\x18\t \x03(\x0b\x32\x32.dfs.ifs.level1.FindLevel1Req.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x01\n\x0e\x46indLevel1Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12-\n\x07records\x18\x04 \x03(\x0b\x32\x1c.dfs.ifs.level1.Level1Record\"\x1a\n\x0cGetLevel1Req\x12\n\n\x02id\x18\x01 \x01(\x03\"=\n\rGetLevel1Resp\x12,\n\x06record\x18\x01 \x01(\x0b\x32\x1c.dfs.ifs.level1.Level1Record\"L\n\x0eWriteLevel1Req\x12,\n\x06record\x18\x01 \x01(\x0b\x32\x1c.dfs.ifs.level1.Level1Record\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"n\n\x0fWriteLevel1Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12,\n\x06record\x18\x03 \x01(\x0b\x32\x1c.dfs.ifs.level1.Level1Record\"0\n\x12UpdateQc1StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc1StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xa7\x03\n\tLevel1Srv\x12G\n\x04\x46ind\x12\x1d.dfs.ifs.level1.FindLevel1Req\x1a\x1e.dfs.ifs.level1.FindLevel1Resp\"\x00\x12\x44\n\x03Get\x12\x1c.dfs.ifs.level1.GetLevel1Req\x1a\x1d.dfs.ifs.level1.GetLevel1Resp\"\x00\x12L\n\x05Write\x12\x1e.dfs.ifs.level1.WriteLevel1Req\x1a\x1f.dfs.ifs.level1.WriteLevel1Resp\"\x00(\x01\x12\\\n\x0fUpdateQc1Status\x12\".dfs.ifs.level1.UpdateQc1StatusReq\x1a#.dfs.ifs.level1.UpdateQc1StatusResp\"\x00\x12_\n\x10UpdateProcStatus\x12#.dfs.ifs.level1.UpdateProcStatusReq\x1a$.dfs.ifs.level1.UpdateProcStatusResp\"\x00\x42!Z\x1f\x63nlab.net/csst/proto/ifs/level1b\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_LEVEL1RECORD_REFSENTRY = _descriptor.Descriptor(
  name='RefsEntry',
  full_name='dfs.ifs.level1.Level1Record.RefsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.ifs.level1.Level1Record.RefsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.ifs.level1.Level1Record.RefsEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=422,
)

_LEVEL1RECORD = _descriptor.Descriptor(
  name='Level1Record',
  full_name='dfs.ifs.level1.Level1Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.ifs.level1.Level1Record.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.ifs.level1.Level1Record.level0_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dfs.ifs.level1.Level1Record.data_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cor_sci_id', full_name='dfs.ifs.level1.Level1Record.cor_sci_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_params', full_name='dfs.ifs.level1.Level1Record.prc_params', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.ifs.level1.Level1Record.filename', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='dfs.ifs.level1.Level1Record.file_path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.ifs.level1.Level1Record.qc1_status', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_time', full_name='dfs.ifs.level1.Level1Record.qc1_time', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.ifs.level1.Level1Record.prc_status', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='dfs.ifs.level1.Level1Record.prc_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.ifs.level1.Level1Record.create_time', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='dfs.ifs.level1.Level1Record.pipeline_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refs', full_name='dfs.ifs.level1.Level1Record.refs', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LEVEL1RECORD_REFSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=422,
)


_FINDLEVEL1REQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.ifs.level1.FindLevel1Req.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.ifs.level1.FindLevel1Req.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.ifs.level1.FindLevel1Req.OtherConditionsEntry.value', index=1,
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
  serialized_start=683,
  serialized_end=737,
)

_FINDLEVEL1REQ = _descriptor.Descriptor(
  name='FindLevel1Req',
  full_name='dfs.ifs.level1.FindLevel1Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.ifs.level1.FindLevel1Req.level0_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dfs.ifs.level1.FindLevel1Req.data_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time_start', full_name='dfs.ifs.level1.FindLevel1Req.create_time_start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time_end', full_name='dfs.ifs.level1.FindLevel1Req.create_time_end', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.ifs.level1.FindLevel1Req.qc1_status', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.ifs.level1.FindLevel1Req.prc_status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.ifs.level1.FindLevel1Req.filename', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.ifs.level1.FindLevel1Req.limit', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.ifs.level1.FindLevel1Req.other_conditions', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDLEVEL1REQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=737,
)


_FINDLEVEL1RESP = _descriptor.Descriptor(
  name='FindLevel1Resp',
  full_name='dfs.ifs.level1.FindLevel1Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.ifs.level1.FindLevel1Resp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.ifs.level1.FindLevel1Resp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.ifs.level1.FindLevel1Resp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.ifs.level1.FindLevel1Resp.records', index=3,
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
  serialized_start=740,
  serialized_end=870,
)


_GETLEVEL1REQ = _descriptor.Descriptor(
  name='GetLevel1Req',
  full_name='dfs.ifs.level1.GetLevel1Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.ifs.level1.GetLevel1Req.id', index=0,
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
  serialized_start=872,
  serialized_end=898,
)


_GETLEVEL1RESP = _descriptor.Descriptor(
  name='GetLevel1Resp',
  full_name='dfs.ifs.level1.GetLevel1Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.ifs.level1.GetLevel1Resp.record', index=0,
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
  serialized_start=900,
  serialized_end=961,
)


_WRITELEVEL1REQ = _descriptor.Descriptor(
  name='WriteLevel1Req',
  full_name='dfs.ifs.level1.WriteLevel1Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.ifs.level1.WriteLevel1Req.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dfs.ifs.level1.WriteLevel1Req.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=963,
  serialized_end=1039,
)


_WRITELEVEL1RESP = _descriptor.Descriptor(
  name='WriteLevel1Resp',
  full_name='dfs.ifs.level1.WriteLevel1Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.ifs.level1.WriteLevel1Resp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.ifs.level1.WriteLevel1Resp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.ifs.level1.WriteLevel1Resp.record', index=2,
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
  serialized_start=1041,
  serialized_end=1151,
)


_UPDATEQC1STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc1StatusReq',
  full_name='dfs.ifs.level1.UpdateQc1StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.ifs.level1.UpdateQc1StatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.ifs.level1.UpdateQc1StatusReq.status', index=1,
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
  serialized_start=1153,
  serialized_end=1201,
)


_UPDATEQC1STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc1StatusResp',
  full_name='dfs.ifs.level1.UpdateQc1StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.ifs.level1.UpdateQc1StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.ifs.level1.UpdateQc1StatusResp.error', index=1,
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
  serialized_start=1203,
  serialized_end=1271,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='dfs.ifs.level1.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.ifs.level1.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.ifs.level1.UpdateProcStatusReq.status', index=1,
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
  serialized_start=1273,
  serialized_end=1322,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='dfs.ifs.level1.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.ifs.level1.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.ifs.level1.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1324,
  serialized_end=1393,
)

_LEVEL1RECORD_REFSENTRY.containing_type = _LEVEL1RECORD
_LEVEL1RECORD.fields_by_name['refs'].message_type = _LEVEL1RECORD_REFSENTRY
_FINDLEVEL1REQ_OTHERCONDITIONSENTRY.containing_type = _FINDLEVEL1REQ
_FINDLEVEL1REQ.fields_by_name['other_conditions'].message_type = _FINDLEVEL1REQ_OTHERCONDITIONSENTRY
_FINDLEVEL1RESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDLEVEL1RESP.fields_by_name['records'].message_type = _LEVEL1RECORD
_GETLEVEL1RESP.fields_by_name['record'].message_type = _LEVEL1RECORD
_WRITELEVEL1REQ.fields_by_name['record'].message_type = _LEVEL1RECORD
_WRITELEVEL1RESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITELEVEL1RESP.fields_by_name['record'].message_type = _LEVEL1RECORD
_UPDATEQC1STATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['Level1Record'] = _LEVEL1RECORD
DESCRIPTOR.message_types_by_name['FindLevel1Req'] = _FINDLEVEL1REQ
DESCRIPTOR.message_types_by_name['FindLevel1Resp'] = _FINDLEVEL1RESP
DESCRIPTOR.message_types_by_name['GetLevel1Req'] = _GETLEVEL1REQ
DESCRIPTOR.message_types_by_name['GetLevel1Resp'] = _GETLEVEL1RESP
DESCRIPTOR.message_types_by_name['WriteLevel1Req'] = _WRITELEVEL1REQ
DESCRIPTOR.message_types_by_name['WriteLevel1Resp'] = _WRITELEVEL1RESP
DESCRIPTOR.message_types_by_name['UpdateQc1StatusReq'] = _UPDATEQC1STATUSREQ
DESCRIPTOR.message_types_by_name['UpdateQc1StatusResp'] = _UPDATEQC1STATUSRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Level1Record = _reflection.GeneratedProtocolMessageType('Level1Record', (_message.Message,), {

  'RefsEntry' : _reflection.GeneratedProtocolMessageType('RefsEntry', (_message.Message,), {
    'DESCRIPTOR' : _LEVEL1RECORD_REFSENTRY,
    '__module__' : 'ifs.level1.level1_pb2'
    # @@protoc_insertion_point(class_scope:dfs.ifs.level1.Level1Record.RefsEntry)
    })
  ,
  'DESCRIPTOR' : _LEVEL1RECORD,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.Level1Record)
  })
_sym_db.RegisterMessage(Level1Record)
_sym_db.RegisterMessage(Level1Record.RefsEntry)

FindLevel1Req = _reflection.GeneratedProtocolMessageType('FindLevel1Req', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDLEVEL1REQ_OTHERCONDITIONSENTRY,
    '__module__' : 'ifs.level1.level1_pb2'
    # @@protoc_insertion_point(class_scope:dfs.ifs.level1.FindLevel1Req.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDLEVEL1REQ,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.FindLevel1Req)
  })
_sym_db.RegisterMessage(FindLevel1Req)
_sym_db.RegisterMessage(FindLevel1Req.OtherConditionsEntry)

FindLevel1Resp = _reflection.GeneratedProtocolMessageType('FindLevel1Resp', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL1RESP,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.FindLevel1Resp)
  })
_sym_db.RegisterMessage(FindLevel1Resp)

GetLevel1Req = _reflection.GeneratedProtocolMessageType('GetLevel1Req', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL1REQ,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.GetLevel1Req)
  })
_sym_db.RegisterMessage(GetLevel1Req)

GetLevel1Resp = _reflection.GeneratedProtocolMessageType('GetLevel1Resp', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL1RESP,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.GetLevel1Resp)
  })
_sym_db.RegisterMessage(GetLevel1Resp)

WriteLevel1Req = _reflection.GeneratedProtocolMessageType('WriteLevel1Req', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL1REQ,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.WriteLevel1Req)
  })
_sym_db.RegisterMessage(WriteLevel1Req)

WriteLevel1Resp = _reflection.GeneratedProtocolMessageType('WriteLevel1Resp', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL1RESP,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.WriteLevel1Resp)
  })
_sym_db.RegisterMessage(WriteLevel1Resp)

UpdateQc1StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSREQ,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.UpdateQc1StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc1StatusReq)

UpdateQc1StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSRESP,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.UpdateQc1StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc1StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'ifs.level1.level1_pb2'
  # @@protoc_insertion_point(class_scope:dfs.ifs.level1.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_LEVEL1RECORD_REFSENTRY._options = None
_FINDLEVEL1REQ_OTHERCONDITIONSENTRY._options = None

_LEVEL1SRV = _descriptor.ServiceDescriptor(
  name='Level1Srv',
  full_name='dfs.ifs.level1.Level1Srv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1396,
  serialized_end=1819,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.ifs.level1.Level1Srv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDLEVEL1REQ,
    output_type=_FINDLEVEL1RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.ifs.level1.Level1Srv.Get',
    index=1,
    containing_service=None,
    input_type=_GETLEVEL1REQ,
    output_type=_GETLEVEL1RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.ifs.level1.Level1Srv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITELEVEL1REQ,
    output_type=_WRITELEVEL1RESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc1Status',
    full_name='dfs.ifs.level1.Level1Srv.UpdateQc1Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC1STATUSREQ,
    output_type=_UPDATEQC1STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='dfs.ifs.level1.Level1Srv.UpdateProcStatus',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEVEL1SRV)

DESCRIPTOR.services_by_name['Level1Srv'] = _LEVEL1SRV

# @@protoc_insertion_point(module_scope)
