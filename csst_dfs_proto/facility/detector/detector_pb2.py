# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/detector/detector.proto

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
  name='facility/detector/detector.proto',
  package='dfs.facility.detector',
  syntax='proto3',
  serialized_options=_b('Z&cnlab.net/csst/proto/facility/detector'),
  serialized_pb=_b('\n facility/detector/detector.proto\x12\x15\x64\x66s.facility.detector\x1a\x12\x63ommon/error.proto\"}\n\x08\x44\x65tector\x12\n\n\x02no\x18\x01 \x01(\t\x12\x15\n\rdetector_name\x18\x02 \x01(\t\x12\x11\n\tmodule_id\x18\x03 \x01(\t\x12\x11\n\tfilter_id\x18\x04 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\t\x12\x13\n\x0bupdate_time\x18\x06 \x01(\t\"k\n\x0e\x44\x65tectorStatus\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65tector_no\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x13\n\x0bstatus_time\x18\x04 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\t\"1\n\x0f\x46indDetectorReq\x12\x11\n\tmodule_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\"\x87\x01\n\x10\x46indDetectorResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x30\n\x07records\x18\x04 \x03(\x0b\x32\x1f.dfs.facility.detector.Detector\"\x1c\n\x0eGetDetectorReq\x12\n\n\x02no\x18\x01 \x01(\t\"B\n\x0fGetDetectorResp\x12/\n\x06record\x18\x01 \x01(\x0b\x32\x1f.dfs.facility.detector.Detector\"C\n\x10WriteDetectorReq\x12/\n\x06record\x18\x01 \x01(\x0b\x32\x1f.dfs.facility.detector.Detector\"s\n\x11WriteDetectorResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12/\n\x06record\x18\x03 \x01(\x0b\x32\x1f.dfs.facility.detector.Detector\"D\n\x11UpdateDetectorReq\x12/\n\x06record\x18\x03 \x01(\x0b\x32\x1f.dfs.facility.detector.Detector\"C\n\x12UpdateDetectorResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"\x1f\n\x11\x44\x65leteDetectorReq\x12\n\n\x02no\x18\x01 \x01(\t\"C\n\x12\x44\x65leteDetectorResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"g\n\rFindStatusReq\x12\x13\n\x0b\x64\x65tector_no\x18\x01 \x01(\t\x12\x19\n\x11status_begin_time\x18\x02 \x01(\t\x12\x17\n\x0fstatus_end_time\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\x05\"\x8b\x01\n\x0e\x46indStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x36\n\x07records\x18\x04 \x03(\x0b\x32%.dfs.facility.detector.DetectorStatus\"\x1a\n\x0cGetStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\"F\n\rGetStatusResp\x12\x35\n\x06record\x18\x01 \x01(\x0b\x32%.dfs.facility.detector.DetectorStatus\"G\n\x0eWriteStatusReq\x12\x35\n\x06record\x18\x01 \x01(\x0b\x32%.dfs.facility.detector.DetectorStatus\"w\n\x0fWriteStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x35\n\x06record\x18\x03 \x01(\x0b\x32%.dfs.facility.detector.DetectorStatus2\xf7\x05\n\x0b\x44\x65tectorSrv\x12Y\n\x04\x46ind\x12&.dfs.facility.detector.FindDetectorReq\x1a\'.dfs.facility.detector.FindDetectorResp\"\x00\x12V\n\x03Get\x12%.dfs.facility.detector.GetDetectorReq\x1a&.dfs.facility.detector.GetDetectorResp\"\x00\x12\\\n\x05Write\x12\'.dfs.facility.detector.WriteDetectorReq\x1a(.dfs.facility.detector.WriteDetectorResp\"\x00\x12_\n\x06Update\x12(.dfs.facility.detector.UpdateDetectorReq\x1a).dfs.facility.detector.UpdateDetectorResp\"\x00\x12_\n\x06\x44\x65lete\x12(.dfs.facility.detector.DeleteDetectorReq\x1a).dfs.facility.detector.DeleteDetectorResp\"\x00\x12[\n\nFindStatus\x12$.dfs.facility.detector.FindStatusReq\x1a%.dfs.facility.detector.FindStatusResp\"\x00\x12X\n\tGetStatus\x12#.dfs.facility.detector.GetStatusReq\x1a$.dfs.facility.detector.GetStatusResp\"\x00\x12^\n\x0bWriteStatus\x12%.dfs.facility.detector.WriteStatusReq\x1a&.dfs.facility.detector.WriteStatusResp\"\x00\x42(Z&cnlab.net/csst/proto/facility/detectorb\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_DETECTOR = _descriptor.Descriptor(
  name='Detector',
  full_name='dfs.facility.detector.Detector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='dfs.facility.detector.Detector.no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_name', full_name='dfs.facility.detector.Detector.detector_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='module_id', full_name='dfs.facility.detector.Detector.module_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_id', full_name='dfs.facility.detector.Detector.filter_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.facility.detector.Detector.create_time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='dfs.facility.detector.Detector.update_time', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=79,
  serialized_end=204,
)


_DETECTORSTATUS = _descriptor.Descriptor(
  name='DetectorStatus',
  full_name='dfs.facility.detector.DetectorStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.detector.DetectorStatus.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.detector.DetectorStatus.detector_no', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.facility.detector.DetectorStatus.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_time', full_name='dfs.facility.detector.DetectorStatus.status_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.facility.detector.DetectorStatus.create_time', index=4,
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
  serialized_start=206,
  serialized_end=313,
)


_FINDDETECTORREQ = _descriptor.Descriptor(
  name='FindDetectorReq',
  full_name='dfs.facility.detector.FindDetectorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_id', full_name='dfs.facility.detector.FindDetectorReq.module_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.facility.detector.FindDetectorReq.key', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=364,
)


_FINDDETECTORRESP = _descriptor.Descriptor(
  name='FindDetectorResp',
  full_name='dfs.facility.detector.FindDetectorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.FindDetectorResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.detector.FindDetectorResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.FindDetectorResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.detector.FindDetectorResp.records', index=3,
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
  serialized_start=367,
  serialized_end=502,
)


_GETDETECTORREQ = _descriptor.Descriptor(
  name='GetDetectorReq',
  full_name='dfs.facility.detector.GetDetectorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='dfs.facility.detector.GetDetectorReq.no', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=504,
  serialized_end=532,
)


_GETDETECTORRESP = _descriptor.Descriptor(
  name='GetDetectorResp',
  full_name='dfs.facility.detector.GetDetectorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.GetDetectorResp.record', index=0,
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
  serialized_start=534,
  serialized_end=600,
)


_WRITEDETECTORREQ = _descriptor.Descriptor(
  name='WriteDetectorReq',
  full_name='dfs.facility.detector.WriteDetectorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.WriteDetectorReq.record', index=0,
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
  serialized_start=602,
  serialized_end=669,
)


_WRITEDETECTORRESP = _descriptor.Descriptor(
  name='WriteDetectorResp',
  full_name='dfs.facility.detector.WriteDetectorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.WriteDetectorResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.WriteDetectorResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.WriteDetectorResp.record', index=2,
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
  serialized_start=671,
  serialized_end=786,
)


_UPDATEDETECTORREQ = _descriptor.Descriptor(
  name='UpdateDetectorReq',
  full_name='dfs.facility.detector.UpdateDetectorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.UpdateDetectorReq.record', index=0,
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
  serialized_start=788,
  serialized_end=856,
)


_UPDATEDETECTORRESP = _descriptor.Descriptor(
  name='UpdateDetectorResp',
  full_name='dfs.facility.detector.UpdateDetectorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.UpdateDetectorResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.UpdateDetectorResp.error', index=1,
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
  serialized_start=858,
  serialized_end=925,
)


_DELETEDETECTORREQ = _descriptor.Descriptor(
  name='DeleteDetectorReq',
  full_name='dfs.facility.detector.DeleteDetectorReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='no', full_name='dfs.facility.detector.DeleteDetectorReq.no', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=927,
  serialized_end=958,
)


_DELETEDETECTORRESP = _descriptor.Descriptor(
  name='DeleteDetectorResp',
  full_name='dfs.facility.detector.DeleteDetectorResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.DeleteDetectorResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.DeleteDetectorResp.error', index=1,
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
  serialized_start=960,
  serialized_end=1027,
)


_FINDSTATUSREQ = _descriptor.Descriptor(
  name='FindStatusReq',
  full_name='dfs.facility.detector.FindStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detector_no', full_name='dfs.facility.detector.FindStatusReq.detector_no', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_begin_time', full_name='dfs.facility.detector.FindStatusReq.status_begin_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_end_time', full_name='dfs.facility.detector.FindStatusReq.status_end_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.facility.detector.FindStatusReq.limit', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_end=1132,
)


_FINDSTATUSRESP = _descriptor.Descriptor(
  name='FindStatusResp',
  full_name='dfs.facility.detector.FindStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.FindStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.facility.detector.FindStatusResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.FindStatusResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.facility.detector.FindStatusResp.records', index=3,
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
  serialized_start=1135,
  serialized_end=1274,
)


_GETSTATUSREQ = _descriptor.Descriptor(
  name='GetStatusReq',
  full_name='dfs.facility.detector.GetStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.facility.detector.GetStatusReq.id', index=0,
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
  serialized_start=1276,
  serialized_end=1302,
)


_GETSTATUSRESP = _descriptor.Descriptor(
  name='GetStatusResp',
  full_name='dfs.facility.detector.GetStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.GetStatusResp.record', index=0,
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
  serialized_start=1304,
  serialized_end=1374,
)


_WRITESTATUSREQ = _descriptor.Descriptor(
  name='WriteStatusReq',
  full_name='dfs.facility.detector.WriteStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.WriteStatusReq.record', index=0,
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
  serialized_start=1376,
  serialized_end=1447,
)


_WRITESTATUSRESP = _descriptor.Descriptor(
  name='WriteStatusResp',
  full_name='dfs.facility.detector.WriteStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.facility.detector.WriteStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.facility.detector.WriteStatusResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.facility.detector.WriteStatusResp.record', index=2,
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
  serialized_start=1449,
  serialized_end=1568,
)

_FINDDETECTORRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDDETECTORRESP.fields_by_name['records'].message_type = _DETECTOR
_GETDETECTORRESP.fields_by_name['record'].message_type = _DETECTOR
_WRITEDETECTORREQ.fields_by_name['record'].message_type = _DETECTOR
_WRITEDETECTORRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITEDETECTORRESP.fields_by_name['record'].message_type = _DETECTOR
_UPDATEDETECTORREQ.fields_by_name['record'].message_type = _DETECTOR
_UPDATEDETECTORRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_DELETEDETECTORRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDSTATUSRESP.fields_by_name['records'].message_type = _DETECTORSTATUS
_GETSTATUSRESP.fields_by_name['record'].message_type = _DETECTORSTATUS
_WRITESTATUSREQ.fields_by_name['record'].message_type = _DETECTORSTATUS
_WRITESTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITESTATUSRESP.fields_by_name['record'].message_type = _DETECTORSTATUS
DESCRIPTOR.message_types_by_name['Detector'] = _DETECTOR
DESCRIPTOR.message_types_by_name['DetectorStatus'] = _DETECTORSTATUS
DESCRIPTOR.message_types_by_name['FindDetectorReq'] = _FINDDETECTORREQ
DESCRIPTOR.message_types_by_name['FindDetectorResp'] = _FINDDETECTORRESP
DESCRIPTOR.message_types_by_name['GetDetectorReq'] = _GETDETECTORREQ
DESCRIPTOR.message_types_by_name['GetDetectorResp'] = _GETDETECTORRESP
DESCRIPTOR.message_types_by_name['WriteDetectorReq'] = _WRITEDETECTORREQ
DESCRIPTOR.message_types_by_name['WriteDetectorResp'] = _WRITEDETECTORRESP
DESCRIPTOR.message_types_by_name['UpdateDetectorReq'] = _UPDATEDETECTORREQ
DESCRIPTOR.message_types_by_name['UpdateDetectorResp'] = _UPDATEDETECTORRESP
DESCRIPTOR.message_types_by_name['DeleteDetectorReq'] = _DELETEDETECTORREQ
DESCRIPTOR.message_types_by_name['DeleteDetectorResp'] = _DELETEDETECTORRESP
DESCRIPTOR.message_types_by_name['FindStatusReq'] = _FINDSTATUSREQ
DESCRIPTOR.message_types_by_name['FindStatusResp'] = _FINDSTATUSRESP
DESCRIPTOR.message_types_by_name['GetStatusReq'] = _GETSTATUSREQ
DESCRIPTOR.message_types_by_name['GetStatusResp'] = _GETSTATUSRESP
DESCRIPTOR.message_types_by_name['WriteStatusReq'] = _WRITESTATUSREQ
DESCRIPTOR.message_types_by_name['WriteStatusResp'] = _WRITESTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Detector = _reflection.GeneratedProtocolMessageType('Detector', (_message.Message,), {
  'DESCRIPTOR' : _DETECTOR,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.Detector)
  })
_sym_db.RegisterMessage(Detector)

DetectorStatus = _reflection.GeneratedProtocolMessageType('DetectorStatus', (_message.Message,), {
  'DESCRIPTOR' : _DETECTORSTATUS,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.DetectorStatus)
  })
_sym_db.RegisterMessage(DetectorStatus)

FindDetectorReq = _reflection.GeneratedProtocolMessageType('FindDetectorReq', (_message.Message,), {
  'DESCRIPTOR' : _FINDDETECTORREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.FindDetectorReq)
  })
_sym_db.RegisterMessage(FindDetectorReq)

FindDetectorResp = _reflection.GeneratedProtocolMessageType('FindDetectorResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDDETECTORRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.FindDetectorResp)
  })
_sym_db.RegisterMessage(FindDetectorResp)

GetDetectorReq = _reflection.GeneratedProtocolMessageType('GetDetectorReq', (_message.Message,), {
  'DESCRIPTOR' : _GETDETECTORREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.GetDetectorReq)
  })
_sym_db.RegisterMessage(GetDetectorReq)

GetDetectorResp = _reflection.GeneratedProtocolMessageType('GetDetectorResp', (_message.Message,), {
  'DESCRIPTOR' : _GETDETECTORRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.GetDetectorResp)
  })
_sym_db.RegisterMessage(GetDetectorResp)

WriteDetectorReq = _reflection.GeneratedProtocolMessageType('WriteDetectorReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDETECTORREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.WriteDetectorReq)
  })
_sym_db.RegisterMessage(WriteDetectorReq)

WriteDetectorResp = _reflection.GeneratedProtocolMessageType('WriteDetectorResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITEDETECTORRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.WriteDetectorResp)
  })
_sym_db.RegisterMessage(WriteDetectorResp)

UpdateDetectorReq = _reflection.GeneratedProtocolMessageType('UpdateDetectorReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDETECTORREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.UpdateDetectorReq)
  })
_sym_db.RegisterMessage(UpdateDetectorReq)

UpdateDetectorResp = _reflection.GeneratedProtocolMessageType('UpdateDetectorResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDETECTORRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.UpdateDetectorResp)
  })
_sym_db.RegisterMessage(UpdateDetectorResp)

DeleteDetectorReq = _reflection.GeneratedProtocolMessageType('DeleteDetectorReq', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDETECTORREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.DeleteDetectorReq)
  })
_sym_db.RegisterMessage(DeleteDetectorReq)

DeleteDetectorResp = _reflection.GeneratedProtocolMessageType('DeleteDetectorResp', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDETECTORRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.DeleteDetectorResp)
  })
_sym_db.RegisterMessage(DeleteDetectorResp)

FindStatusReq = _reflection.GeneratedProtocolMessageType('FindStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _FINDSTATUSREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.FindStatusReq)
  })
_sym_db.RegisterMessage(FindStatusReq)

FindStatusResp = _reflection.GeneratedProtocolMessageType('FindStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDSTATUSRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.FindStatusResp)
  })
_sym_db.RegisterMessage(FindStatusResp)

GetStatusReq = _reflection.GeneratedProtocolMessageType('GetStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.GetStatusReq)
  })
_sym_db.RegisterMessage(GetStatusReq)

GetStatusResp = _reflection.GeneratedProtocolMessageType('GetStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATUSRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.GetStatusResp)
  })
_sym_db.RegisterMessage(GetStatusResp)

WriteStatusReq = _reflection.GeneratedProtocolMessageType('WriteStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITESTATUSREQ,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.WriteStatusReq)
  })
_sym_db.RegisterMessage(WriteStatusReq)

WriteStatusResp = _reflection.GeneratedProtocolMessageType('WriteStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITESTATUSRESP,
  '__module__' : 'facility.detector.detector_pb2'
  # @@protoc_insertion_point(class_scope:dfs.facility.detector.WriteStatusResp)
  })
_sym_db.RegisterMessage(WriteStatusResp)


DESCRIPTOR._options = None

_DETECTORSRV = _descriptor.ServiceDescriptor(
  name='DetectorSrv',
  full_name='dfs.facility.detector.DetectorSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1571,
  serialized_end=2330,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.facility.detector.DetectorSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDDETECTORREQ,
    output_type=_FINDDETECTORRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.facility.detector.DetectorSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETDETECTORREQ,
    output_type=_GETDETECTORRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.facility.detector.DetectorSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITEDETECTORREQ,
    output_type=_WRITEDETECTORRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='dfs.facility.detector.DetectorSrv.Update',
    index=3,
    containing_service=None,
    input_type=_UPDATEDETECTORREQ,
    output_type=_UPDATEDETECTORRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='dfs.facility.detector.DetectorSrv.Delete',
    index=4,
    containing_service=None,
    input_type=_DELETEDETECTORREQ,
    output_type=_DELETEDETECTORRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FindStatus',
    full_name='dfs.facility.detector.DetectorSrv.FindStatus',
    index=5,
    containing_service=None,
    input_type=_FINDSTATUSREQ,
    output_type=_FINDSTATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='dfs.facility.detector.DetectorSrv.GetStatus',
    index=6,
    containing_service=None,
    input_type=_GETSTATUSREQ,
    output_type=_GETSTATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WriteStatus',
    full_name='dfs.facility.detector.DetectorSrv.WriteStatus',
    index=7,
    containing_service=None,
    input_type=_WRITESTATUSREQ,
    output_type=_WRITESTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DETECTORSRV)

DESCRIPTOR.services_by_name['DetectorSrv'] = _DETECTORSRV

# @@protoc_insertion_point(module_scope)
