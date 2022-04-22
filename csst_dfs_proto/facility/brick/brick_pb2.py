# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/brick/brick.proto

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
  name='facility/brick/brick.proto',
  package='dfs.facility.brick',
  syntax='proto3',
  serialized_options=_b('Z#cnlab.net/csst/proto/facility/brick'),
  serialized_pb=_b('\n\x1a\x66\x61\x63ility/brick/brick.proto\x12\x12\x64\x66s.facility.brick\x1a\x12\x63ommon/error.proto\"G\n\x0b\x42rickRecord\x12\n\n\x02id\x18\x01 \x01(\x03\x12\n\n\x02ra\x18\x02 \x01(\x02\x12\x0b\n\x03\x64\x65\x63\x18\x03 \x01(\x02\x12\x13\n\x0b\x62oundingbox\x18\x04 \x01(\t\"^\n\x14\x42rickObsStatusRecord\x12\x10\n\x08\x62rick_id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62\x61nd\x18\x02 \x01(\t\x12\x11\n\tcover_num\x18\x03 \x01(\x05\x12\x13\n\x0bupdate_time\x18\x04 \x01(\t\"j\n\x11\x42rickLevel1Record\x12\x10\n\x08\x62rick_id\x18\x01 \x01(\x03\x12\x11\n\tlevel1_id\x18\x02 \x01(\x03\x12\x0e\n\x06obs_id\x18\x03 \x01(\t\x12\x0e\n\x06module\x18\x04 \x01(\t\x12\x10\n\x08obs_time\x18\x05 \x01(\t\"\xa6\x01\n\x0c\x46indBrickReq\x12\r\n\x05limit\x18\x01 \x01(\x05\x12O\n\x10other_conditions\x18\x02 \x03(\x0b\x32\x35.dfs.facility.brick.FindBrickReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\rFindBrickResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x30\n\x07records\x18\x04 \x03(\x0b\x32\x1f.dfs.facility.brick.BrickRecord\"\x19\n\x0bGetBrickReq\x12\n\n\x02id\x18\x01 \x01(\x03\"?\n\x0cGetBrickResp\x12/\n\x06record\x18\x01 \x01(\x0b\x32\x1f.dfs.facility.brick.BrickRecord\"@\n\rWriteBrickReq\x12/\n\x06record\x18\x01 \x01(\x0b\x32\x1f.dfs.facility.brick.BrickRecord\"p\n\x0eWriteBrickResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12/\n\x06record\x18\x03 \x01(\x0b\x32\x1f.dfs.facility.brick.BrickRecord\"\xbf\x01\n\x10\x46indObsStatusReq\x12\x10\n\x08\x62rick_id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62\x61nd\x18\x02 \x01(\t\x12S\n\x10other_conditions\x18\x03 \x03(\x0b\x32\x39.dfs.facility.brick.FindObsStatusReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\x11\x46indObsStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x39\n\x07records\x18\x04 \x03(\x0b\x32(.dfs.facility.brick.BrickObsStatusRecord\"D\n\rFindLevel1Req\x12\x10\n\x08\x62rick_id\x18\x01 \x01(\x03\x12\x11\n\tlevel1_id\x18\x02 \x01(\x03\x12\x0e\n\x06module\x18\x03 \x01(\t\"\x8b\x01\n\x0e\x46indLevel1Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x36\n\x07records\x18\x04 \x03(\x0b\x32%.dfs.facility.brick.BrickLevel1Record2\xae\x03\n\x08\x42rickSrv\x12M\n\x04\x46ind\x12 .dfs.facility.brick.FindBrickReq\x1a!.dfs.facility.brick.FindBrickResp\"\x00\x12J\n\x03Get\x12\x1f.dfs.facility.brick.GetBrickReq\x1a .dfs.facility.brick.GetBrickResp\"\x00\x12P\n\x05Write\x12!.dfs.facility.brick.WriteBrickReq\x1a\".dfs.facility.brick.WriteBrickResp\"\x00\x12^\n\rFindObsStatus\x12$.dfs.facility.brick.FindObsStatusReq\x1a%.dfs.facility.brick.FindObsStatusResp\"\x00\x12U\n\nFindLevel1\x12!.dfs.facility.brick.FindLevel1Req\x1a\".dfs.facility.brick.FindLevel1Resp\"\x00\x42%Z#cnlab.net/csst/proto/facility/brickb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_BRICKRECORD = _descriptor.Descriptor(
  name='BrickRecord',
  full_name='dfs.facility.brick.BrickRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.brick.BrickRecord.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ra', full_name='dfs.facility.brick.BrickRecord.ra', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dec', full_name='dfs.facility.brick.BrickRecord.dec', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boundingbox', full_name='dfs.facility.brick.BrickRecord.boundingbox', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=70,
  serialized_end=141,
)


_BRICKOBSSTATUSRECORD = _descriptor.Descriptor(
  name='BrickObsStatusRecord',
  full_name='dfs.facility.brick.BrickObsStatusRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brick_id', full_name='dfs.facility.brick.BrickObsStatusRecord.brick_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='band', full_name='dfs.facility.brick.BrickObsStatusRecord.band', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cover_num', full_name='dfs.facility.brick.BrickObsStatusRecord.cover_num', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='dfs.facility.brick.BrickObsStatusRecord.update_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=143,
  serialized_end=237,
)


_BRICKLEVEL1RECORD = _descriptor.Descriptor(
  name='BrickLevel1Record',
  full_name='dfs.facility.brick.BrickLevel1Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brick_id', full_name='dfs.facility.brick.BrickLevel1Record.brick_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level1_id', full_name='dfs.facility.brick.BrickLevel1Record.level1_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='dfs.facility.brick.BrickLevel1Record.obs_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='dfs.facility.brick.BrickLevel1Record.module', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_time', full_name='dfs.facility.brick.BrickLevel1Record.obs_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=239,
  serialized_end=345,
)


_FINDBRICKREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.facility.brick.FindBrickReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.facility.brick.FindBrickReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.facility.brick.FindBrickReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=460,
  serialized_end=514,
)

_FINDBRICKREQ = _descriptor.Descriptor(
  name='FindBrickReq',
  full_name='dfs.facility.brick.FindBrickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.facility.brick.FindBrickReq.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.facility.brick.FindBrickReq.other_conditions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDBRICKREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=514,
)


_FINDBRICKRESP = _descriptor.Descriptor(
  name='FindBrickResp',
  full_name='dfs.facility.brick.FindBrickResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.brick.FindBrickResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.brick.FindBrickResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.brick.FindBrickResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.brick.FindBrickResp.records', index=3,
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
  serialized_start=517,
  serialized_end=649,
)


_GETBRICKREQ = _descriptor.Descriptor(
  name='GetBrickReq',
  full_name='dfs.facility.brick.GetBrickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.brick.GetBrickReq.id', index=0,
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
  serialized_start=651,
  serialized_end=676,
)


_GETBRICKRESP = _descriptor.Descriptor(
  name='GetBrickResp',
  full_name='dfs.facility.brick.GetBrickResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.brick.GetBrickResp.record', index=0,
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
  serialized_start=678,
  serialized_end=741,
)


_WRITEBRICKREQ = _descriptor.Descriptor(
  name='WriteBrickReq',
  full_name='dfs.facility.brick.WriteBrickReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.brick.WriteBrickReq.record', index=0,
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
  serialized_start=743,
  serialized_end=807,
)


_WRITEBRICKRESP = _descriptor.Descriptor(
  name='WriteBrickResp',
  full_name='dfs.facility.brick.WriteBrickResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.brick.WriteBrickResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.brick.WriteBrickResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.brick.WriteBrickResp.record', index=2,
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
  serialized_start=809,
  serialized_end=921,
)


_FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.facility.brick.FindObsStatusReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.facility.brick.FindObsStatusReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.facility.brick.FindObsStatusReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=460,
  serialized_end=514,
)

_FINDOBSSTATUSREQ = _descriptor.Descriptor(
  name='FindObsStatusReq',
  full_name='dfs.facility.brick.FindObsStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brick_id', full_name='dfs.facility.brick.FindObsStatusReq.brick_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='band', full_name='dfs.facility.brick.FindObsStatusReq.band', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.facility.brick.FindObsStatusReq.other_conditions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=924,
  serialized_end=1115,
)


_FINDOBSSTATUSRESP = _descriptor.Descriptor(
  name='FindObsStatusResp',
  full_name='dfs.facility.brick.FindObsStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.brick.FindObsStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.brick.FindObsStatusResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.brick.FindObsStatusResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.brick.FindObsStatusResp.records', index=3,
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
  serialized_start=1118,
  serialized_end=1263,
)


_FINDLEVEL1REQ = _descriptor.Descriptor(
  name='FindLevel1Req',
  full_name='dfs.facility.brick.FindLevel1Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brick_id', full_name='dfs.facility.brick.FindLevel1Req.brick_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level1_id', full_name='dfs.facility.brick.FindLevel1Req.level1_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module', full_name='dfs.facility.brick.FindLevel1Req.module', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1265,
  serialized_end=1333,
)


_FINDLEVEL1RESP = _descriptor.Descriptor(
  name='FindLevel1Resp',
  full_name='dfs.facility.brick.FindLevel1Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.brick.FindLevel1Resp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.brick.FindLevel1Resp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.brick.FindLevel1Resp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.brick.FindLevel1Resp.records', index=3,
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
  serialized_start=1336,
  serialized_end=1475,
)

_FINDBRICKREQ_OTHERCONDITIONSENTRY.containing_type = _FINDBRICKREQ
_FINDBRICKREQ.fields_by_name['other_conditions'].message_type = _FINDBRICKREQ_OTHERCONDITIONSENTRY
_FINDBRICKRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDBRICKRESP.fields_by_name['records'].message_type = _BRICKRECORD
_GETBRICKRESP.fields_by_name['record'].message_type = _BRICKRECORD
_WRITEBRICKREQ.fields_by_name['record'].message_type = _BRICKRECORD
_WRITEBRICKRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITEBRICKRESP.fields_by_name['record'].message_type = _BRICKRECORD
_FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY.containing_type = _FINDOBSSTATUSREQ
_FINDOBSSTATUSREQ.fields_by_name['other_conditions'].message_type = _FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY
_FINDOBSSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDOBSSTATUSRESP.fields_by_name['records'].message_type = _BRICKOBSSTATUSRECORD
_FINDLEVEL1RESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDLEVEL1RESP.fields_by_name['records'].message_type = _BRICKLEVEL1RECORD
DESCRIPTOR.message_types_by_name['BrickRecord'] = _BRICKRECORD
DESCRIPTOR.message_types_by_name['BrickObsStatusRecord'] = _BRICKOBSSTATUSRECORD
DESCRIPTOR.message_types_by_name['BrickLevel1Record'] = _BRICKLEVEL1RECORD
DESCRIPTOR.message_types_by_name['FindBrickReq'] = _FINDBRICKREQ
DESCRIPTOR.message_types_by_name['FindBrickResp'] = _FINDBRICKRESP
DESCRIPTOR.message_types_by_name['GetBrickReq'] = _GETBRICKREQ
DESCRIPTOR.message_types_by_name['GetBrickResp'] = _GETBRICKRESP
DESCRIPTOR.message_types_by_name['WriteBrickReq'] = _WRITEBRICKREQ
DESCRIPTOR.message_types_by_name['WriteBrickResp'] = _WRITEBRICKRESP
DESCRIPTOR.message_types_by_name['FindObsStatusReq'] = _FINDOBSSTATUSREQ
DESCRIPTOR.message_types_by_name['FindObsStatusResp'] = _FINDOBSSTATUSRESP
DESCRIPTOR.message_types_by_name['FindLevel1Req'] = _FINDLEVEL1REQ
DESCRIPTOR.message_types_by_name['FindLevel1Resp'] = _FINDLEVEL1RESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrickRecord = _reflection.GeneratedProtocolMessageType('BrickRecord', (_message.Message,), {
  'DESCRIPTOR' : _BRICKRECORD,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.BrickRecord)
  })
_sym_db.RegisterMessage(BrickRecord)

BrickObsStatusRecord = _reflection.GeneratedProtocolMessageType('BrickObsStatusRecord', (_message.Message,), {
  'DESCRIPTOR' : _BRICKOBSSTATUSRECORD,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.BrickObsStatusRecord)
  })
_sym_db.RegisterMessage(BrickObsStatusRecord)

BrickLevel1Record = _reflection.GeneratedProtocolMessageType('BrickLevel1Record', (_message.Message,), {
  'DESCRIPTOR' : _BRICKLEVEL1RECORD,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.BrickLevel1Record)
  })
_sym_db.RegisterMessage(BrickLevel1Record)

FindBrickReq = _reflection.GeneratedProtocolMessageType('FindBrickReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDBRICKREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.brick.brick_pb2'
    # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindBrickReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDBRICKREQ,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindBrickReq)
  })
_sym_db.RegisterMessage(FindBrickReq)
_sym_db.RegisterMessage(FindBrickReq.OtherConditionsEntry)

FindBrickResp = _reflection.GeneratedProtocolMessageType('FindBrickResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDBRICKRESP,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindBrickResp)
  })
_sym_db.RegisterMessage(FindBrickResp)

GetBrickReq = _reflection.GeneratedProtocolMessageType('GetBrickReq', (_message.Message,), {
  'DESCRIPTOR' : _GETBRICKREQ,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.GetBrickReq)
  })
_sym_db.RegisterMessage(GetBrickReq)

GetBrickResp = _reflection.GeneratedProtocolMessageType('GetBrickResp', (_message.Message,), {
  'DESCRIPTOR' : _GETBRICKRESP,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.GetBrickResp)
  })
_sym_db.RegisterMessage(GetBrickResp)

WriteBrickReq = _reflection.GeneratedProtocolMessageType('WriteBrickReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITEBRICKREQ,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.WriteBrickReq)
  })
_sym_db.RegisterMessage(WriteBrickReq)

WriteBrickResp = _reflection.GeneratedProtocolMessageType('WriteBrickResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITEBRICKRESP,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.WriteBrickResp)
  })
_sym_db.RegisterMessage(WriteBrickResp)

FindObsStatusReq = _reflection.GeneratedProtocolMessageType('FindObsStatusReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.brick.brick_pb2'
    # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindObsStatusReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDOBSSTATUSREQ,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindObsStatusReq)
  })
_sym_db.RegisterMessage(FindObsStatusReq)
_sym_db.RegisterMessage(FindObsStatusReq.OtherConditionsEntry)

FindObsStatusResp = _reflection.GeneratedProtocolMessageType('FindObsStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDOBSSTATUSRESP,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindObsStatusResp)
  })
_sym_db.RegisterMessage(FindObsStatusResp)

FindLevel1Req = _reflection.GeneratedProtocolMessageType('FindLevel1Req', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL1REQ,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindLevel1Req)
  })
_sym_db.RegisterMessage(FindLevel1Req)

FindLevel1Resp = _reflection.GeneratedProtocolMessageType('FindLevel1Resp', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL1RESP,
  '__module__' : 'facility.brick.brick_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.brick.FindLevel1Resp)
  })
_sym_db.RegisterMessage(FindLevel1Resp)


DESCRIPTOR._options = None
_FINDBRICKREQ_OTHERCONDITIONSENTRY._options = None
_FINDOBSSTATUSREQ_OTHERCONDITIONSENTRY._options = None

_BRICKSRV = _descriptor.ServiceDescriptor(
  name='BrickSrv',
  full_name='dfs.facility.brick.BrickSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1478,
  serialized_end=1908,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.facility.brick.BrickSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDBRICKREQ,
    output_type=_FINDBRICKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.facility.brick.BrickSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETBRICKREQ,
    output_type=_GETBRICKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.facility.brick.BrickSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITEBRICKREQ,
    output_type=_WRITEBRICKRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindObsStatus',
    full_name='dfs.facility.brick.BrickSrv.FindObsStatus',
    index=3,
    containing_service=None,
    input_type=_FINDOBSSTATUSREQ,
    output_type=_FINDOBSSTATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindLevel1',
    full_name='dfs.facility.brick.BrickSrv.FindLevel1',
    index=4,
    containing_service=None,
    input_type=_FINDLEVEL1REQ,
    output_type=_FINDLEVEL1RESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRICKSRV)

DESCRIPTOR.services_by_name['BrickSrv'] = _BRICKSRV

# @@protoc_insertion_point(module_scope)
