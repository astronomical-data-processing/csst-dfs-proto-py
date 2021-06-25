# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/calmerge/calmerge.proto

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
  name='facility/calmerge/calmerge.proto',
  package='dfs.facility.calmerge',
  syntax='proto3',
  serialized_options=_b('Z&cnlab.net/csst/proto/facility/calmerge'),
  serialized_pb=_b('\n facility/calmerge/calmerge.proto\x12\x15\x64\x66s.facility.calmerge\x1a\x12\x63ommon/error.proto\"\x81\x02\n\x0e\x43\x61lMergeRecord\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65tector_no\x18\x02 \x01(\t\x12\x10\n\x08ref_type\x18\x03 \x01(\t\x12\x10\n\x08obs_time\x18\x04 \x01(\t\x12\x10\n\x08\x65xp_time\x18\x05 \x01(\x02\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x11\n\tfile_path\x18\x07 \x01(\t\x12\x12\n\nqc1_status\x18\x08 \x01(\x05\x12\x10\n\x08qc1_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\x05\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x12\n\nlevel0_ids\x18\r \x03(\x03\"\xbf\x02\n\x0f\x46indCalMergeReq\x12\x13\n\x0b\x64\x65tector_no\x18\x01 \x01(\t\x12\x10\n\x08ref_type\x18\x02 \x01(\t\x12\x16\n\x0e\x65xp_time_start\x18\x03 \x01(\t\x12\x14\n\x0c\x65xp_time_end\x18\x04 \x01(\t\x12\x12\n\nqc1_status\x18\x05 \x01(\x05\x12\x12\n\nprc_status\x18\x06 \x01(\x05\x12\x11\n\tfile_name\x18\x07 \x01(\t\x12\r\n\x05limit\x18\x08 \x01(\x05\x12U\n\x10other_conditions\x18\t \x03(\x0b\x32;.dfs.facility.calmerge.FindCalMergeReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8d\x01\n\x10\x46indCalMergeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x36\n\x07records\x18\x04 \x03(\x0b\x32%.dfs.facility.calmerge.CalMergeRecord\"\x1c\n\x0eGetCalMergeReq\x12\n\n\x02id\x18\x01 \x01(\x03\"H\n\x0fGetCalMergeResp\x12\x35\n\x06record\x18\x01 \x01(\x0b\x32%.dfs.facility.calmerge.CalMergeRecord\"I\n\x10WriteCalMergeReq\x12\x35\n\x06record\x18\x01 \x01(\x0b\x32%.dfs.facility.calmerge.CalMergeRecord\"y\n\x11WriteCalMergeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x35\n\x06record\x18\x03 \x01(\x0b\x32%.dfs.facility.calmerge.CalMergeRecord\"0\n\x12UpdateQc1StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc1StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xf9\x03\n\x0b\x43\x61lMergeSrv\x12Y\n\x04\x46ind\x12&.dfs.facility.calmerge.FindCalMergeReq\x1a\'.dfs.facility.calmerge.FindCalMergeResp\"\x00\x12V\n\x03Get\x12%.dfs.facility.calmerge.GetCalMergeReq\x1a&.dfs.facility.calmerge.GetCalMergeResp\"\x00\x12\\\n\x05Write\x12\'.dfs.facility.calmerge.WriteCalMergeReq\x1a(.dfs.facility.calmerge.WriteCalMergeResp\"\x00\x12j\n\x0fUpdateQc1Status\x12).dfs.facility.calmerge.UpdateQc1StatusReq\x1a*.dfs.facility.calmerge.UpdateQc1StatusResp\"\x00\x12m\n\x10UpdateProcStatus\x12*.dfs.facility.calmerge.UpdateProcStatusReq\x1a+.dfs.facility.calmerge.UpdateProcStatusResp\"\x00\x42(Z&cnlab.net/csst/proto/facility/calmergeb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_CALMERGERECORD = _descriptor.Descriptor(
  name='CalMergeRecord',
  full_name='dfs.facility.calmerge.CalMergeRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.calmerge.CalMergeRecord.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.calmerge.CalMergeRecord.detector_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_type', full_name='dfs.facility.calmerge.CalMergeRecord.ref_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_time', full_name='dfs.facility.calmerge.CalMergeRecord.obs_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time', full_name='dfs.facility.calmerge.CalMergeRecord.exp_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.facility.calmerge.CalMergeRecord.filename', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='dfs.facility.calmerge.CalMergeRecord.file_path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.facility.calmerge.CalMergeRecord.qc1_status', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_time', full_name='dfs.facility.calmerge.CalMergeRecord.qc1_time', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.facility.calmerge.CalMergeRecord.prc_status', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='dfs.facility.calmerge.CalMergeRecord.prc_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.facility.calmerge.CalMergeRecord.create_time', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level0_ids', full_name='dfs.facility.calmerge.CalMergeRecord.level0_ids', index=12,
      number=13, type=3, cpp_type=2, label=3,
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
  serialized_start=80,
  serialized_end=337,
)


_FINDCALMERGEREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.facility.calmerge.FindCalMergeReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.facility.calmerge.FindCalMergeReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.facility.calmerge.FindCalMergeReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=605,
  serialized_end=659,
)

_FINDCALMERGEREQ = _descriptor.Descriptor(
  name='FindCalMergeReq',
  full_name='dfs.facility.calmerge.FindCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.calmerge.FindCalMergeReq.detector_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_type', full_name='dfs.facility.calmerge.FindCalMergeReq.ref_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_start', full_name='dfs.facility.calmerge.FindCalMergeReq.exp_time_start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_end', full_name='dfs.facility.calmerge.FindCalMergeReq.exp_time_end', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.facility.calmerge.FindCalMergeReq.qc1_status', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.facility.calmerge.FindCalMergeReq.prc_status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='dfs.facility.calmerge.FindCalMergeReq.file_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.facility.calmerge.FindCalMergeReq.limit', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.facility.calmerge.FindCalMergeReq.other_conditions', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDCALMERGEREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=659,
)


_FINDCALMERGERESP = _descriptor.Descriptor(
  name='FindCalMergeResp',
  full_name='dfs.facility.calmerge.FindCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.calmerge.FindCalMergeResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.calmerge.FindCalMergeResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.calmerge.FindCalMergeResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.calmerge.FindCalMergeResp.records', index=3,
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
  serialized_start=662,
  serialized_end=803,
)


_GETCALMERGEREQ = _descriptor.Descriptor(
  name='GetCalMergeReq',
  full_name='dfs.facility.calmerge.GetCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.calmerge.GetCalMergeReq.id', index=0,
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
  serialized_start=805,
  serialized_end=833,
)


_GETCALMERGERESP = _descriptor.Descriptor(
  name='GetCalMergeResp',
  full_name='dfs.facility.calmerge.GetCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.calmerge.GetCalMergeResp.record', index=0,
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
  serialized_start=835,
  serialized_end=907,
)


_WRITECALMERGEREQ = _descriptor.Descriptor(
  name='WriteCalMergeReq',
  full_name='dfs.facility.calmerge.WriteCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.calmerge.WriteCalMergeReq.record', index=0,
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
  serialized_start=909,
  serialized_end=982,
)


_WRITECALMERGERESP = _descriptor.Descriptor(
  name='WriteCalMergeResp',
  full_name='dfs.facility.calmerge.WriteCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.calmerge.WriteCalMergeResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.calmerge.WriteCalMergeResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.calmerge.WriteCalMergeResp.record', index=2,
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
  serialized_start=984,
  serialized_end=1105,
)


_UPDATEQC1STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc1StatusReq',
  full_name='dfs.facility.calmerge.UpdateQc1StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.calmerge.UpdateQc1StatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.facility.calmerge.UpdateQc1StatusReq.status', index=1,
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
  serialized_start=1107,
  serialized_end=1155,
)


_UPDATEQC1STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc1StatusResp',
  full_name='dfs.facility.calmerge.UpdateQc1StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.calmerge.UpdateQc1StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.calmerge.UpdateQc1StatusResp.error', index=1,
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
  serialized_start=1157,
  serialized_end=1225,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='dfs.facility.calmerge.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.calmerge.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.facility.calmerge.UpdateProcStatusReq.status', index=1,
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
  serialized_start=1227,
  serialized_end=1276,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='dfs.facility.calmerge.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.calmerge.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.calmerge.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1278,
  serialized_end=1347,
)

_FINDCALMERGEREQ_OTHERCONDITIONSENTRY.containing_type = _FINDCALMERGEREQ
_FINDCALMERGEREQ.fields_by_name['other_conditions'].message_type = _FINDCALMERGEREQ_OTHERCONDITIONSENTRY
_FINDCALMERGERESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDCALMERGERESP.fields_by_name['records'].message_type = _CALMERGERECORD
_GETCALMERGERESP.fields_by_name['record'].message_type = _CALMERGERECORD
_WRITECALMERGEREQ.fields_by_name['record'].message_type = _CALMERGERECORD
_WRITECALMERGERESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITECALMERGERESP.fields_by_name['record'].message_type = _CALMERGERECORD
_UPDATEQC1STATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['CalMergeRecord'] = _CALMERGERECORD
DESCRIPTOR.message_types_by_name['FindCalMergeReq'] = _FINDCALMERGEREQ
DESCRIPTOR.message_types_by_name['FindCalMergeResp'] = _FINDCALMERGERESP
DESCRIPTOR.message_types_by_name['GetCalMergeReq'] = _GETCALMERGEREQ
DESCRIPTOR.message_types_by_name['GetCalMergeResp'] = _GETCALMERGERESP
DESCRIPTOR.message_types_by_name['WriteCalMergeReq'] = _WRITECALMERGEREQ
DESCRIPTOR.message_types_by_name['WriteCalMergeResp'] = _WRITECALMERGERESP
DESCRIPTOR.message_types_by_name['UpdateQc1StatusReq'] = _UPDATEQC1STATUSREQ
DESCRIPTOR.message_types_by_name['UpdateQc1StatusResp'] = _UPDATEQC1STATUSRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalMergeRecord = _reflection.GeneratedProtocolMessageType('CalMergeRecord', (_message.Message,), {
  'DESCRIPTOR' : _CALMERGERECORD,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.CalMergeRecord)
  })
_sym_db.RegisterMessage(CalMergeRecord)

FindCalMergeReq = _reflection.GeneratedProtocolMessageType('FindCalMergeReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDCALMERGEREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.calmerge.calmerge_pb2'
    # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.FindCalMergeReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDCALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.FindCalMergeReq)
  })
_sym_db.RegisterMessage(FindCalMergeReq)
_sym_db.RegisterMessage(FindCalMergeReq.OtherConditionsEntry)

FindCalMergeResp = _reflection.GeneratedProtocolMessageType('FindCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDCALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.FindCalMergeResp)
  })
_sym_db.RegisterMessage(FindCalMergeResp)

GetCalMergeReq = _reflection.GeneratedProtocolMessageType('GetCalMergeReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.GetCalMergeReq)
  })
_sym_db.RegisterMessage(GetCalMergeReq)

GetCalMergeResp = _reflection.GeneratedProtocolMessageType('GetCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _GETCALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.GetCalMergeResp)
  })
_sym_db.RegisterMessage(GetCalMergeResp)

WriteCalMergeReq = _reflection.GeneratedProtocolMessageType('WriteCalMergeReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITECALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.WriteCalMergeReq)
  })
_sym_db.RegisterMessage(WriteCalMergeReq)

WriteCalMergeResp = _reflection.GeneratedProtocolMessageType('WriteCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITECALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.WriteCalMergeResp)
  })
_sym_db.RegisterMessage(WriteCalMergeResp)

UpdateQc1StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.UpdateQc1StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc1StatusReq)

UpdateQc1StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSRESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.UpdateQc1StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc1StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.calmerge.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDCALMERGEREQ_OTHERCONDITIONSENTRY._options = None

_CALMERGESRV = _descriptor.ServiceDescriptor(
  name='CalMergeSrv',
  full_name='dfs.facility.calmerge.CalMergeSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1350,
  serialized_end=1855,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.facility.calmerge.CalMergeSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDCALMERGEREQ,
    output_type=_FINDCALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.facility.calmerge.CalMergeSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETCALMERGEREQ,
    output_type=_GETCALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.facility.calmerge.CalMergeSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITECALMERGEREQ,
    output_type=_WRITECALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc1Status',
    full_name='dfs.facility.calmerge.CalMergeSrv.UpdateQc1Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC1STATUSREQ,
    output_type=_UPDATEQC1STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='dfs.facility.calmerge.CalMergeSrv.UpdateProcStatus',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALMERGESRV)

DESCRIPTOR.services_by_name['CalMergeSrv'] = _CALMERGESRV

# @@protoc_insertion_point(module_scope)
