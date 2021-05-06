# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/exposure.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='facility/exposure.proto',
  package='facility',
  syntax='proto3',
  serialized_options=_b('Z\035cnlab.net/csst/proto/facility'),
  serialized_pb=_b('\n\x17\x66\x61\x63ility/exposure.proto\x12\x08\x66\x61\x63ility\x1a\x12\x63ommon/error.proto\"\x80\x02\n\x08\x45xposure\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x16\n\x0e\x65xp_begin_time\x18\x02 \x01(\x03\x12\x14\n\x0c\x65xp_end_time\x18\x03 \x01(\x03\x12\x11\n\tmodule_id\x18\x04 \x01(\t\x12\x10\n\x08obs_type\x18\x05 \x01(\t\x12\x1a\n\x12\x66\x61\x63ility_status_id\x18\x06 \x01(\x03\x12\x18\n\x10module_status_id\x18\x07 \x01(\x03\x12\x12\n\nqc0_status\x18\x08 \x01(\r\x12\x10\n\x08qc0_time\x18\t \x01(\x03\x12\x12\n\nprc_status\x18\n \x01(\r\x12\x10\n\x08prc_time\x18\x0b \x01(\x03\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\x03\"\xa1\x02\n\x0f\x46indExposureReq\x12\x11\n\tmodule_id\x18\x01 \x01(\t\x12\x10\n\x08obs_type\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x16\n\x0e\x65xp_time_start\x18\x04 \x01(\t\x12\x14\n\x0c\x65xp_time_end\x18\x05 \x01(\t\x12\x12\n\nqc0_status\x18\x06 \x01(\r\x12\x12\n\nprc_status\x18\x07 \x01(\r\x12H\n\x10other_conditions\x18\x08 \x03(\x0b\x32..facility.FindExposureReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"{\n\x10\x46indExposureResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12$\n\x08\x45xposure\x18\x04 \x03(\x0b\x32\x12.facility.Exposure\" \n\x0eGetExposureReq\x12\x0e\n\x06obs_id\x18\x01 \x01(\x03\"7\n\x0fGetExposureResp\x12$\n\x08\x45xposure\x18\x01 \x01(\x0b\x32\x12.facility.Exposure\"\xa7\x01\n\x10WriteExposureReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x16\n\x0e\x65xp_begin_time\x18\x02 \x01(\x03\x12\x14\n\x0c\x65xp_end_time\x18\x03 \x01(\x03\x12\x11\n\tmodule_id\x18\x04 \x01(\t\x12\x10\n\x08obs_type\x18\x05 \x01(\t\x12\x1a\n\x12\x66\x61\x63ility_status_id\x18\x06 \x01(\x03\x12\x18\n\x10module_status_id\x18\x07 \x01(\x03\"h\n\x11WriteExposureResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12$\n\x08\x65xposure\x18\x03 \x01(\x0b\x32\x12.facility.Exposure\"4\n\x12UpdateQc0StatusReq\x12\x0e\n\x06obs_id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"D\n\x13UpdateQc0StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"5\n\x13UpdateProcStatusReq\x12\x0e\n\x06obs_id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\r\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xf9\x02\n\x0b\x45xposureSrv\x12?\n\x04\x46ind\x12\x19.facility.FindExposureReq\x1a\x1a.facility.FindExposureResp\"\x00\x12<\n\x03Get\x12\x18.facility.GetExposureReq\x1a\x19.facility.GetExposureResp\"\x00\x12\x44\n\x05Write\x12\x1a.facility.WriteExposureReq\x1a\x1b.facility.WriteExposureResp\"\x00(\x01\x12P\n\x0fUpdateQc0Status\x12\x1c.facility.UpdateQc0StatusReq\x1a\x1d.facility.UpdateQc0StatusResp\"\x00\x12S\n\x10UpdateProcStatus\x12\x1d.facility.UpdateProcStatusReq\x1a\x1e.facility.UpdateProcStatusResp\"\x00\x42\x1fZ\x1d\x63nlab.net/csst/proto/facilityb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_EXPOSURE = _descriptor.Descriptor(
  name='Exposure',
  full_name='facility.Exposure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='facility.Exposure.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_begin_time', full_name='facility.Exposure.exp_begin_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_end_time', full_name='facility.Exposure.exp_end_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_id', full_name='facility.Exposure.module_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_type', full_name='facility.Exposure.obs_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='facility_status_id', full_name='facility.Exposure.facility_status_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_status_id', full_name='facility.Exposure.module_status_id', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_status', full_name='facility.Exposure.qc0_status', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_time', full_name='facility.Exposure.qc0_time', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='facility.Exposure.prc_status', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='facility.Exposure.prc_time', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='facility.Exposure.create_time', index=11,
      number=12, type=3, cpp_type=2, label=1,
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
  serialized_start=58,
  serialized_end=314,
)


_FINDEXPOSUREREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='facility.FindExposureReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='facility.FindExposureReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='facility.FindExposureReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=552,
  serialized_end=606,
)

_FINDEXPOSUREREQ = _descriptor.Descriptor(
  name='FindExposureReq',
  full_name='facility.FindExposureReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_id', full_name='facility.FindExposureReq.module_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_type', full_name='facility.FindExposureReq.obs_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='facility.FindExposureReq.file_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_start', full_name='facility.FindExposureReq.exp_time_start', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_time_end', full_name='facility.FindExposureReq.exp_time_end', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc0_status', full_name='facility.FindExposureReq.qc0_status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='facility.FindExposureReq.prc_status', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='facility.FindExposureReq.other_conditions', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDEXPOSUREREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=317,
  serialized_end=606,
)


_FINDEXPOSURERESP = _descriptor.Descriptor(
  name='FindExposureResp',
  full_name='facility.FindExposureResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='facility.FindExposureResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='facility.FindExposureResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='facility.FindExposureResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Exposure', full_name='facility.FindExposureResp.Exposure', index=3,
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
  serialized_start=608,
  serialized_end=731,
)


_GETEXPOSUREREQ = _descriptor.Descriptor(
  name='GetExposureReq',
  full_name='facility.GetExposureReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='facility.GetExposureReq.obs_id', index=0,
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
  serialized_start=733,
  serialized_end=765,
)


_GETEXPOSURERESP = _descriptor.Descriptor(
  name='GetExposureResp',
  full_name='facility.GetExposureResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Exposure', full_name='facility.GetExposureResp.Exposure', index=0,
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
  serialized_start=767,
  serialized_end=822,
)


_WRITEEXPOSUREREQ = _descriptor.Descriptor(
  name='WriteExposureReq',
  full_name='facility.WriteExposureReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='facility.WriteExposureReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_begin_time', full_name='facility.WriteExposureReq.exp_begin_time', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_end_time', full_name='facility.WriteExposureReq.exp_end_time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_id', full_name='facility.WriteExposureReq.module_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obs_type', full_name='facility.WriteExposureReq.obs_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='facility_status_id', full_name='facility.WriteExposureReq.facility_status_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_status_id', full_name='facility.WriteExposureReq.module_status_id', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=825,
  serialized_end=992,
)


_WRITEEXPOSURERESP = _descriptor.Descriptor(
  name='WriteExposureResp',
  full_name='facility.WriteExposureResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='facility.WriteExposureResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='facility.WriteExposureResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exposure', full_name='facility.WriteExposureResp.exposure', index=2,
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
  serialized_start=994,
  serialized_end=1098,
)


_UPDATEQC0STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc0StatusReq',
  full_name='facility.UpdateQc0StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='facility.UpdateQc0StatusReq.obs_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='facility.UpdateQc0StatusReq.status', index=1,
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
  serialized_start=1100,
  serialized_end=1152,
)


_UPDATEQC0STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc0StatusResp',
  full_name='facility.UpdateQc0StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='facility.UpdateQc0StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='facility.UpdateQc0StatusResp.error', index=1,
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
  serialized_start=1154,
  serialized_end=1222,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='facility.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='obs_id', full_name='facility.UpdateProcStatusReq.obs_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='facility.UpdateProcStatusReq.status', index=1,
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
  serialized_start=1224,
  serialized_end=1277,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='facility.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='facility.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='facility.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1279,
  serialized_end=1348,
)

_FINDEXPOSUREREQ_OTHERCONDITIONSENTRY.containing_type = _FINDEXPOSUREREQ
_FINDEXPOSUREREQ.fields_by_name['other_conditions'].message_type = _FINDEXPOSUREREQ_OTHERCONDITIONSENTRY
_FINDEXPOSURERESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDEXPOSURERESP.fields_by_name['Exposure'].message_type = _EXPOSURE
_GETEXPOSURERESP.fields_by_name['Exposure'].message_type = _EXPOSURE
_WRITEEXPOSURERESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITEEXPOSURERESP.fields_by_name['exposure'].message_type = _EXPOSURE
_UPDATEQC0STATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['Exposure'] = _EXPOSURE
DESCRIPTOR.message_types_by_name['FindExposureReq'] = _FINDEXPOSUREREQ
DESCRIPTOR.message_types_by_name['FindExposureResp'] = _FINDEXPOSURERESP
DESCRIPTOR.message_types_by_name['GetExposureReq'] = _GETEXPOSUREREQ
DESCRIPTOR.message_types_by_name['GetExposureResp'] = _GETEXPOSURERESP
DESCRIPTOR.message_types_by_name['WriteExposureReq'] = _WRITEEXPOSUREREQ
DESCRIPTOR.message_types_by_name['WriteExposureResp'] = _WRITEEXPOSURERESP
DESCRIPTOR.message_types_by_name['UpdateQc0StatusReq'] = _UPDATEQC0STATUSREQ
DESCRIPTOR.message_types_by_name['UpdateQc0StatusResp'] = _UPDATEQC0STATUSRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Exposure = _reflection.GeneratedProtocolMessageType('Exposure', (_message.Message,), {
  'DESCRIPTOR' : _EXPOSURE,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.Exposure)
  })
_sym_db.RegisterMessage(Exposure)

FindExposureReq = _reflection.GeneratedProtocolMessageType('FindExposureReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDEXPOSUREREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'facility.exposure_pb2'
    # @@protoc_insertion_point(class_scope:facility.FindExposureReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDEXPOSUREREQ,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.FindExposureReq)
  })
_sym_db.RegisterMessage(FindExposureReq)
_sym_db.RegisterMessage(FindExposureReq.OtherConditionsEntry)

FindExposureResp = _reflection.GeneratedProtocolMessageType('FindExposureResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDEXPOSURERESP,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.FindExposureResp)
  })
_sym_db.RegisterMessage(FindExposureResp)

GetExposureReq = _reflection.GeneratedProtocolMessageType('GetExposureReq', (_message.Message,), {
  'DESCRIPTOR' : _GETEXPOSUREREQ,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.GetExposureReq)
  })
_sym_db.RegisterMessage(GetExposureReq)

GetExposureResp = _reflection.GeneratedProtocolMessageType('GetExposureResp', (_message.Message,), {
  'DESCRIPTOR' : _GETEXPOSURERESP,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.GetExposureResp)
  })
_sym_db.RegisterMessage(GetExposureResp)

WriteExposureReq = _reflection.GeneratedProtocolMessageType('WriteExposureReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITEEXPOSUREREQ,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.WriteExposureReq)
  })
_sym_db.RegisterMessage(WriteExposureReq)

WriteExposureResp = _reflection.GeneratedProtocolMessageType('WriteExposureResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITEEXPOSURERESP,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.WriteExposureResp)
  })
_sym_db.RegisterMessage(WriteExposureResp)

UpdateQc0StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc0StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC0STATUSREQ,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.UpdateQc0StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc0StatusReq)

UpdateQc0StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc0StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC0STATUSRESP,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.UpdateQc0StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc0StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'facility.exposure_pb2'
  # @@protoc_insertion_point(class_scope:facility.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDEXPOSUREREQ_OTHERCONDITIONSENTRY._options = None

_EXPOSURESRV = _descriptor.ServiceDescriptor(
  name='ExposureSrv',
  full_name='facility.ExposureSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1351,
  serialized_end=1728,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='facility.ExposureSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDEXPOSUREREQ,
    output_type=_FINDEXPOSURERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='facility.ExposureSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETEXPOSUREREQ,
    output_type=_GETEXPOSURERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='facility.ExposureSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITEEXPOSUREREQ,
    output_type=_WRITEEXPOSURERESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc0Status',
    full_name='facility.ExposureSrv.UpdateQc0Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC0STATUSREQ,
    output_type=_UPDATEQC0STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='facility.ExposureSrv.UpdateProcStatus',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXPOSURESRV)

DESCRIPTOR.services_by_name['ExposureSrv'] = _EXPOSURESRV

# @@protoc_insertion_point(module_scope)
