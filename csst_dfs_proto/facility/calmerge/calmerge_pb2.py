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
  package='calmerge',
  syntax='proto3',
  serialized_options=_b('Z&cnlab.net/csst/proto/facility/calmerge'),
  serialized_pb=_b('\n facility/calmerge/calmerge.proto\x12\x08\x63\x61lmerge\x1a\x12\x63ommon/error.proto\"\x81\x02\n\x0e\x43\x61lMergeRecord\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65tector_no\x18\x02 \x01(\t\x12\x10\n\x08ref_type\x18\x03 \x01(\t\x12\x10\n\x08obs_time\x18\x04 \x01(\t\x12\x10\n\x08\x65xp_time\x18\x05 \x01(\x02\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x11\n\tfile_path\x18\x07 \x01(\t\x12\x12\n\nqc1_status\x18\x08 \x01(\r\x12\x10\n\x08qc1_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\r\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x12\n\nlevel0_ids\x18\r \x03(\x03\"\xb2\x02\n\x0f\x46indCalMergeReq\x12\x13\n\x0b\x64\x65tector_no\x18\x01 \x01(\t\x12\x10\n\x08ref_type\x18\x02 \x01(\t\x12\x16\n\x0e\x65xp_time_start\x18\x03 \x01(\t\x12\x14\n\x0c\x65xp_time_end\x18\x04 \x01(\t\x12\x12\n\nqc1_status\x18\x05 \x01(\r\x12\x12\n\nprc_status\x18\x06 \x01(\r\x12\x11\n\tfile_name\x18\x07 \x01(\t\x12\r\n\x05limit\x18\x08 \x01(\r\x12H\n\x10other_conditions\x18\t \x03(\x0b\x32..calmerge.FindCalMergeReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x80\x01\n\x10\x46indCalMergeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12)\n\x07records\x18\x04 \x03(\x0b\x32\x18.calmerge.CalMergeRecord\"\x1c\n\x0eGetCalMergeReq\x12\n\n\x02id\x18\x01 \x01(\x03\";\n\x0fGetCalMergeResp\x12(\n\x06record\x18\x01 \x01(\x0b\x32\x18.calmerge.CalMergeRecord\"<\n\x10WriteCalMergeReq\x12(\n\x06record\x18\x01 \x01(\x0b\x32\x18.calmerge.CalMergeRecord\"l\n\x11WriteCalMergeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12(\n\x06record\x18\x03 \x01(\x0b\x32\x18.calmerge.CalMergeRecord\"0\n\x12UpdateQc1StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"D\n\x13UpdateQc1StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xf7\x02\n\x0b\x43\x61lMergeSrv\x12?\n\x04\x46ind\x12\x19.calmerge.FindCalMergeReq\x1a\x1a.calmerge.FindCalMergeResp\"\x00\x12<\n\x03Get\x12\x18.calmerge.GetCalMergeReq\x1a\x19.calmerge.GetCalMergeResp\"\x00\x12\x42\n\x05Write\x12\x1a.calmerge.WriteCalMergeReq\x1a\x1b.calmerge.WriteCalMergeResp\"\x00\x12P\n\x0fUpdateQc1Status\x12\x1c.calmerge.UpdateQc1StatusReq\x1a\x1d.calmerge.UpdateQc1StatusResp\"\x00\x12S\n\x10UpdateProcStatus\x12\x1d.calmerge.UpdateProcStatusReq\x1a\x1e.calmerge.UpdateProcStatusResp\"\x00\x42(Z&cnlab.net/csst/proto/facility/calmergeb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_CALMERGERECORD = _descriptor.Descriptor(
  name='CalMergeRecord',
  full_name='calmerge.CalMergeRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='calmerge.CalMergeRecord.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='calmerge.CalMergeRecord.detector_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_type', full_name='calmerge.CalMergeRecord.ref_type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_time', full_name='calmerge.CalMergeRecord.obs_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time', full_name='calmerge.CalMergeRecord.exp_time', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='calmerge.CalMergeRecord.filename', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='calmerge.CalMergeRecord.file_path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='calmerge.CalMergeRecord.qc1_status', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_time', full_name='calmerge.CalMergeRecord.qc1_time', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='calmerge.CalMergeRecord.prc_status', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='calmerge.CalMergeRecord.prc_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='calmerge.CalMergeRecord.create_time', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level0_ids', full_name='calmerge.CalMergeRecord.level0_ids', index=12,
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
  serialized_start=67,
  serialized_end=324,
)


_FINDCALMERGEREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='calmerge.FindCalMergeReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='calmerge.FindCalMergeReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='calmerge.FindCalMergeReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=579,
  serialized_end=633,
)

_FINDCALMERGEREQ = _descriptor.Descriptor(
  name='FindCalMergeReq',
  full_name='calmerge.FindCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='calmerge.FindCalMergeReq.detector_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ref_type', full_name='calmerge.FindCalMergeReq.ref_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_start', full_name='calmerge.FindCalMergeReq.exp_time_start', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_end', full_name='calmerge.FindCalMergeReq.exp_time_end', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='calmerge.FindCalMergeReq.qc1_status', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='calmerge.FindCalMergeReq.prc_status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='calmerge.FindCalMergeReq.file_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='calmerge.FindCalMergeReq.limit', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='calmerge.FindCalMergeReq.other_conditions', index=8,
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
  serialized_start=327,
  serialized_end=633,
)


_FINDCALMERGERESP = _descriptor.Descriptor(
  name='FindCalMergeResp',
  full_name='calmerge.FindCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='calmerge.FindCalMergeResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='calmerge.FindCalMergeResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='calmerge.FindCalMergeResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='calmerge.FindCalMergeResp.records', index=3,
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
  serialized_start=636,
  serialized_end=764,
)


_GETCALMERGEREQ = _descriptor.Descriptor(
  name='GetCalMergeReq',
  full_name='calmerge.GetCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='calmerge.GetCalMergeReq.id', index=0,
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
  serialized_start=766,
  serialized_end=794,
)


_GETCALMERGERESP = _descriptor.Descriptor(
  name='GetCalMergeResp',
  full_name='calmerge.GetCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='calmerge.GetCalMergeResp.record', index=0,
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
  serialized_start=796,
  serialized_end=855,
)


_WRITECALMERGEREQ = _descriptor.Descriptor(
  name='WriteCalMergeReq',
  full_name='calmerge.WriteCalMergeReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='calmerge.WriteCalMergeReq.record', index=0,
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
  serialized_start=857,
  serialized_end=917,
)


_WRITECALMERGERESP = _descriptor.Descriptor(
  name='WriteCalMergeResp',
  full_name='calmerge.WriteCalMergeResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='calmerge.WriteCalMergeResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='calmerge.WriteCalMergeResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='calmerge.WriteCalMergeResp.record', index=2,
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
  serialized_start=919,
  serialized_end=1027,
)


_UPDATEQC1STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc1StatusReq',
  full_name='calmerge.UpdateQc1StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='calmerge.UpdateQc1StatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='calmerge.UpdateQc1StatusReq.status', index=1,
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
  serialized_start=1029,
  serialized_end=1077,
)


_UPDATEQC1STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc1StatusResp',
  full_name='calmerge.UpdateQc1StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='calmerge.UpdateQc1StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='calmerge.UpdateQc1StatusResp.error', index=1,
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
  serialized_start=1079,
  serialized_end=1147,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='calmerge.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='calmerge.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='calmerge.UpdateProcStatusReq.status', index=1,
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
  serialized_start=1149,
  serialized_end=1198,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='calmerge.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='calmerge.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='calmerge.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1200,
  serialized_end=1269,
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
  # @@protoc_insertion_point(class_scope:calmerge.CalMergeRecord)
  })
_sym_db.RegisterMessage(CalMergeRecord)

FindCalMergeReq = _reflection.GeneratedProtocolMessageType('FindCalMergeReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDCALMERGEREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.calmerge.calmerge_pb2'
    # @@protoc_insertion_point(class_scope:calmerge.FindCalMergeReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDCALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.FindCalMergeReq)
  })
_sym_db.RegisterMessage(FindCalMergeReq)
_sym_db.RegisterMessage(FindCalMergeReq.OtherConditionsEntry)

FindCalMergeResp = _reflection.GeneratedProtocolMessageType('FindCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDCALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.FindCalMergeResp)
  })
_sym_db.RegisterMessage(FindCalMergeResp)

GetCalMergeReq = _reflection.GeneratedProtocolMessageType('GetCalMergeReq', (_message.Message,), {
  'DESCRIPTOR' : _GETCALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.GetCalMergeReq)
  })
_sym_db.RegisterMessage(GetCalMergeReq)

GetCalMergeResp = _reflection.GeneratedProtocolMessageType('GetCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _GETCALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.GetCalMergeResp)
  })
_sym_db.RegisterMessage(GetCalMergeResp)

WriteCalMergeReq = _reflection.GeneratedProtocolMessageType('WriteCalMergeReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITECALMERGEREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.WriteCalMergeReq)
  })
_sym_db.RegisterMessage(WriteCalMergeReq)

WriteCalMergeResp = _reflection.GeneratedProtocolMessageType('WriteCalMergeResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITECALMERGERESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.WriteCalMergeResp)
  })
_sym_db.RegisterMessage(WriteCalMergeResp)

UpdateQc1StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.UpdateQc1StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc1StatusReq)

UpdateQc1StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSRESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.UpdateQc1StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc1StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'facility.calmerge.calmerge_pb2'
  # @@protoc_insertion_point(class_scope:calmerge.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDCALMERGEREQ_OTHERCONDITIONSENTRY._options = None

_CALMERGESRV = _descriptor.ServiceDescriptor(
  name='CalMergeSrv',
  full_name='calmerge.CalMergeSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1272,
  serialized_end=1647,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='calmerge.CalMergeSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDCALMERGEREQ,
    output_type=_FINDCALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='calmerge.CalMergeSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETCALMERGEREQ,
    output_type=_GETCALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='calmerge.CalMergeSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITECALMERGEREQ,
    output_type=_WRITECALMERGERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc1Status',
    full_name='calmerge.CalMergeSrv.UpdateQc1Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC1STATUSREQ,
    output_type=_UPDATEQC1STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='calmerge.CalMergeSrv.UpdateProcStatus',
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
