# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sls/level2spectra/level2spectra.proto

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
  name='sls/level2spectra/level2spectra.proto',
  package='dfs.sls.level2spectra',
  syntax='proto3',
  serialized_options=_b('Z&cnlab.net/csst/proto/sls/level2spectra'),
  serialized_pb=_b('\n%sls/level2spectra/level2spectra.proto\x12\x15\x64\x66s.sls.level2spectra\x1a\x12\x63ommon/error.proto\"\x86\x02\n\x13Level2spectraRecord\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x12\n\nspectra_id\x18\x03 \x01(\t\x12\x11\n\tlevel1_id\x18\x04 \x01(\x03\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x11\n\tfile_path\x18\x07 \x01(\t\x12\x12\n\nqc1_status\x18\x08 \x01(\x05\x12\x10\n\x08qc1_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\x05\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x13\n\x0bpipeline_id\x18\r \x01(\t\"\xe1\x02\n\x14\x46indLevel2spectraReq\x12\x11\n\tlevel0_id\x18\x01 \x01(\t\x12\x11\n\tlevel1_id\x18\x02 \x01(\x03\x12\x12\n\nspectra_id\x18\x03 \x01(\t\x12\x19\n\x11\x63reate_time_start\x18\x04 \x01(\t\x12\x17\n\x0f\x63reate_time_end\x18\x05 \x01(\t\x12\x12\n\nqc1_status\x18\x06 \x01(\x05\x12\x12\n\nprc_status\x18\x07 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x08 \x01(\t\x12\r\n\x05limit\x18\t \x01(\x05\x12Z\n\x10other_conditions\x18\n \x03(\x0b\x32@.dfs.sls.level2spectra.FindLevel2spectraReq.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x97\x01\n\x15\x46indLevel2spectraResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12;\n\x07records\x18\x04 \x03(\x0b\x32*.dfs.sls.level2spectra.Level2spectraRecord\"!\n\x13GetLevel2spectraReq\x12\n\n\x02id\x18\x01 \x01(\x03\"R\n\x14GetLevel2spectraResp\x12:\n\x06record\x18\x01 \x01(\x0b\x32*.dfs.sls.level2spectra.Level2spectraRecord\"a\n\x15WriteLevel2spectraReq\x12:\n\x06record\x18\x01 \x01(\x0b\x32*.dfs.sls.level2spectra.Level2spectraRecord\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x83\x01\n\x16WriteLevel2spectraResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12:\n\x06record\x18\x03 \x01(\x0b\x32*.dfs.sls.level2spectra.Level2spectraRecord\"0\n\x12UpdateQc1StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc1StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\x9e\x04\n\x10Level2spectraSrv\x12\x63\n\x04\x46ind\x12+.dfs.sls.level2spectra.FindLevel2spectraReq\x1a,.dfs.sls.level2spectra.FindLevel2spectraResp\"\x00\x12`\n\x03Get\x12*.dfs.sls.level2spectra.GetLevel2spectraReq\x1a+.dfs.sls.level2spectra.GetLevel2spectraResp\"\x00\x12h\n\x05Write\x12,.dfs.sls.level2spectra.WriteLevel2spectraReq\x1a-.dfs.sls.level2spectra.WriteLevel2spectraResp\"\x00(\x01\x12j\n\x0fUpdateQc1Status\x12).dfs.sls.level2spectra.UpdateQc1StatusReq\x1a*.dfs.sls.level2spectra.UpdateQc1StatusResp\"\x00\x12m\n\x10UpdateProcStatus\x12*.dfs.sls.level2spectra.UpdateProcStatusReq\x1a+.dfs.sls.level2spectra.UpdateProcStatusResp\"\x00\x42(Z&cnlab.net/csst/proto/sls/level2spectrab\x06proto3')
  ,
  dependencies=[common_dot_error__pb2.DESCRIPTOR,])




_LEVEL2SPECTRARECORD = _descriptor.Descriptor(
  name='Level2spectraRecord',
  full_name='dfs.sls.level2spectra.Level2spectraRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level2spectra.Level2spectraRecord.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.sls.level2spectra.Level2spectraRecord.level0_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spectra_id', full_name='dfs.sls.level2spectra.Level2spectraRecord.spectra_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level1_id', full_name='dfs.sls.level2spectra.Level2spectraRecord.level1_id', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region', full_name='dfs.sls.level2spectra.Level2spectraRecord.region', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.sls.level2spectra.Level2spectraRecord.filename', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_path', full_name='dfs.sls.level2spectra.Level2spectraRecord.file_path', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.sls.level2spectra.Level2spectraRecord.qc1_status', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_time', full_name='dfs.sls.level2spectra.Level2spectraRecord.qc1_time', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.sls.level2spectra.Level2spectraRecord.prc_status', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_time', full_name='dfs.sls.level2spectra.Level2spectraRecord.prc_time', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='dfs.sls.level2spectra.Level2spectraRecord.create_time', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pipeline_id', full_name='dfs.sls.level2spectra.Level2spectraRecord.pipeline_id', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=85,
  serialized_end=347,
)


_FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY = _descriptor.Descriptor(
  name='OtherConditionsEntry',
  full_name='dfs.sls.level2spectra.FindLevel2spectraReq.OtherConditionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.OtherConditionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.OtherConditionsEntry.value', index=1,
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
  serialized_start=649,
  serialized_end=703,
)

_FINDLEVEL2SPECTRAREQ = _descriptor.Descriptor(
  name='FindLevel2spectraReq',
  full_name='dfs.sls.level2spectra.FindLevel2spectraReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level0_id', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.level0_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level1_id', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.level1_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spectra_id', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.spectra_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time_start', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.create_time_start', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time_end', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.create_time_end', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qc1_status', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.qc1_status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prc_status', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.prc_status', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.filename', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.limit', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_conditions', full_name='dfs.sls.level2spectra.FindLevel2spectraReq.other_conditions', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=703,
)


_FINDLEVEL2SPECTRARESP = _descriptor.Descriptor(
  name='FindLevel2spectraResp',
  full_name='dfs.sls.level2spectra.FindLevel2spectraResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level2spectra.FindLevel2spectraResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='dfs.sls.level2spectra.FindLevel2spectraResp.totalCount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level2spectra.FindLevel2spectraResp.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='dfs.sls.level2spectra.FindLevel2spectraResp.records', index=3,
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
  serialized_start=706,
  serialized_end=857,
)


_GETLEVEL2SPECTRAREQ = _descriptor.Descriptor(
  name='GetLevel2spectraReq',
  full_name='dfs.sls.level2spectra.GetLevel2spectraReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level2spectra.GetLevel2spectraReq.id', index=0,
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
  serialized_start=859,
  serialized_end=892,
)


_GETLEVEL2SPECTRARESP = _descriptor.Descriptor(
  name='GetLevel2spectraResp',
  full_name='dfs.sls.level2spectra.GetLevel2spectraResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.sls.level2spectra.GetLevel2spectraResp.record', index=0,
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
  serialized_start=894,
  serialized_end=976,
)


_WRITELEVEL2SPECTRAREQ = _descriptor.Descriptor(
  name='WriteLevel2spectraReq',
  full_name='dfs.sls.level2spectra.WriteLevel2spectraReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.sls.level2spectra.WriteLevel2spectraReq.record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='dfs.sls.level2spectra.WriteLevel2spectraReq.data', index=1,
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
  serialized_start=978,
  serialized_end=1075,
)


_WRITELEVEL2SPECTRARESP = _descriptor.Descriptor(
  name='WriteLevel2spectraResp',
  full_name='dfs.sls.level2spectra.WriteLevel2spectraResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level2spectra.WriteLevel2spectraResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level2spectra.WriteLevel2spectraResp.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='record', full_name='dfs.sls.level2spectra.WriteLevel2spectraResp.record', index=2,
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
  serialized_start=1078,
  serialized_end=1209,
)


_UPDATEQC1STATUSREQ = _descriptor.Descriptor(
  name='UpdateQc1StatusReq',
  full_name='dfs.sls.level2spectra.UpdateQc1StatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level2spectra.UpdateQc1StatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.sls.level2spectra.UpdateQc1StatusReq.status', index=1,
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
  serialized_start=1211,
  serialized_end=1259,
)


_UPDATEQC1STATUSRESP = _descriptor.Descriptor(
  name='UpdateQc1StatusResp',
  full_name='dfs.sls.level2spectra.UpdateQc1StatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level2spectra.UpdateQc1StatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level2spectra.UpdateQc1StatusResp.error', index=1,
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
  serialized_start=1261,
  serialized_end=1329,
)


_UPDATEPROCSTATUSREQ = _descriptor.Descriptor(
  name='UpdateProcStatusReq',
  full_name='dfs.sls.level2spectra.UpdateProcStatusReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dfs.sls.level2spectra.UpdateProcStatusReq.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='dfs.sls.level2spectra.UpdateProcStatusReq.status', index=1,
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
  serialized_start=1331,
  serialized_end=1380,
)


_UPDATEPROCSTATUSRESP = _descriptor.Descriptor(
  name='UpdateProcStatusResp',
  full_name='dfs.sls.level2spectra.UpdateProcStatusResp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dfs.sls.level2spectra.UpdateProcStatusResp.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='dfs.sls.level2spectra.UpdateProcStatusResp.error', index=1,
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
  serialized_start=1382,
  serialized_end=1451,
)

_FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY.containing_type = _FINDLEVEL2SPECTRAREQ
_FINDLEVEL2SPECTRAREQ.fields_by_name['other_conditions'].message_type = _FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY
_FINDLEVEL2SPECTRARESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_FINDLEVEL2SPECTRARESP.fields_by_name['records'].message_type = _LEVEL2SPECTRARECORD
_GETLEVEL2SPECTRARESP.fields_by_name['record'].message_type = _LEVEL2SPECTRARECORD
_WRITELEVEL2SPECTRAREQ.fields_by_name['record'].message_type = _LEVEL2SPECTRARECORD
_WRITELEVEL2SPECTRARESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_WRITELEVEL2SPECTRARESP.fields_by_name['record'].message_type = _LEVEL2SPECTRARECORD
_UPDATEQC1STATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
_UPDATEPROCSTATUSRESP.fields_by_name['error'].message_type = common_dot_error__pb2._ERROR
DESCRIPTOR.message_types_by_name['Level2spectraRecord'] = _LEVEL2SPECTRARECORD
DESCRIPTOR.message_types_by_name['FindLevel2spectraReq'] = _FINDLEVEL2SPECTRAREQ
DESCRIPTOR.message_types_by_name['FindLevel2spectraResp'] = _FINDLEVEL2SPECTRARESP
DESCRIPTOR.message_types_by_name['GetLevel2spectraReq'] = _GETLEVEL2SPECTRAREQ
DESCRIPTOR.message_types_by_name['GetLevel2spectraResp'] = _GETLEVEL2SPECTRARESP
DESCRIPTOR.message_types_by_name['WriteLevel2spectraReq'] = _WRITELEVEL2SPECTRAREQ
DESCRIPTOR.message_types_by_name['WriteLevel2spectraResp'] = _WRITELEVEL2SPECTRARESP
DESCRIPTOR.message_types_by_name['UpdateQc1StatusReq'] = _UPDATEQC1STATUSREQ
DESCRIPTOR.message_types_by_name['UpdateQc1StatusResp'] = _UPDATEQC1STATUSRESP
DESCRIPTOR.message_types_by_name['UpdateProcStatusReq'] = _UPDATEPROCSTATUSREQ
DESCRIPTOR.message_types_by_name['UpdateProcStatusResp'] = _UPDATEPROCSTATUSRESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Level2spectraRecord = _reflection.GeneratedProtocolMessageType('Level2spectraRecord', (_message.Message,), {
  'DESCRIPTOR' : _LEVEL2SPECTRARECORD,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.Level2spectraRecord)
  })
_sym_db.RegisterMessage(Level2spectraRecord)

FindLevel2spectraReq = _reflection.GeneratedProtocolMessageType('FindLevel2spectraReq', (_message.Message,), {

  'OtherConditionsEntry' : _reflection.GeneratedProtocolMessageType('OtherConditionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY,
    '__module__' : 'sls.level2spectra.level2spectra_pb2'
    # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.FindLevel2spectraReq.OtherConditionsEntry)
    })
  ,
  'DESCRIPTOR' : _FINDLEVEL2SPECTRAREQ,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.FindLevel2spectraReq)
  })
_sym_db.RegisterMessage(FindLevel2spectraReq)
_sym_db.RegisterMessage(FindLevel2spectraReq.OtherConditionsEntry)

FindLevel2spectraResp = _reflection.GeneratedProtocolMessageType('FindLevel2spectraResp', (_message.Message,), {
  'DESCRIPTOR' : _FINDLEVEL2SPECTRARESP,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.FindLevel2spectraResp)
  })
_sym_db.RegisterMessage(FindLevel2spectraResp)

GetLevel2spectraReq = _reflection.GeneratedProtocolMessageType('GetLevel2spectraReq', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL2SPECTRAREQ,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.GetLevel2spectraReq)
  })
_sym_db.RegisterMessage(GetLevel2spectraReq)

GetLevel2spectraResp = _reflection.GeneratedProtocolMessageType('GetLevel2spectraResp', (_message.Message,), {
  'DESCRIPTOR' : _GETLEVEL2SPECTRARESP,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.GetLevel2spectraResp)
  })
_sym_db.RegisterMessage(GetLevel2spectraResp)

WriteLevel2spectraReq = _reflection.GeneratedProtocolMessageType('WriteLevel2spectraReq', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL2SPECTRAREQ,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.WriteLevel2spectraReq)
  })
_sym_db.RegisterMessage(WriteLevel2spectraReq)

WriteLevel2spectraResp = _reflection.GeneratedProtocolMessageType('WriteLevel2spectraResp', (_message.Message,), {
  'DESCRIPTOR' : _WRITELEVEL2SPECTRARESP,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.WriteLevel2spectraResp)
  })
_sym_db.RegisterMessage(WriteLevel2spectraResp)

UpdateQc1StatusReq = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSREQ,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.UpdateQc1StatusReq)
  })
_sym_db.RegisterMessage(UpdateQc1StatusReq)

UpdateQc1StatusResp = _reflection.GeneratedProtocolMessageType('UpdateQc1StatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEQC1STATUSRESP,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.UpdateQc1StatusResp)
  })
_sym_db.RegisterMessage(UpdateQc1StatusResp)

UpdateProcStatusReq = _reflection.GeneratedProtocolMessageType('UpdateProcStatusReq', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSREQ,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.UpdateProcStatusReq)
  })
_sym_db.RegisterMessage(UpdateProcStatusReq)

UpdateProcStatusResp = _reflection.GeneratedProtocolMessageType('UpdateProcStatusResp', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROCSTATUSRESP,
  '__module__' : 'sls.level2spectra.level2spectra_pb2'
  # @@protoc_insertion_point(class_scope:dfs.sls.level2spectra.UpdateProcStatusResp)
  })
_sym_db.RegisterMessage(UpdateProcStatusResp)


DESCRIPTOR._options = None
_FINDLEVEL2SPECTRAREQ_OTHERCONDITIONSENTRY._options = None

_LEVEL2SPECTRASRV = _descriptor.ServiceDescriptor(
  name='Level2spectraSrv',
  full_name='dfs.sls.level2spectra.Level2spectraSrv',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1454,
  serialized_end=1996,
  methods=[
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='dfs.sls.level2spectra.Level2spectraSrv.Find',
    index=0,
    containing_service=None,
    input_type=_FINDLEVEL2SPECTRAREQ,
    output_type=_FINDLEVEL2SPECTRARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='dfs.sls.level2spectra.Level2spectraSrv.Get',
    index=1,
    containing_service=None,
    input_type=_GETLEVEL2SPECTRAREQ,
    output_type=_GETLEVEL2SPECTRARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='dfs.sls.level2spectra.Level2spectraSrv.Write',
    index=2,
    containing_service=None,
    input_type=_WRITELEVEL2SPECTRAREQ,
    output_type=_WRITELEVEL2SPECTRARESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateQc1Status',
    full_name='dfs.sls.level2spectra.Level2spectraSrv.UpdateQc1Status',
    index=3,
    containing_service=None,
    input_type=_UPDATEQC1STATUSREQ,
    output_type=_UPDATEQC1STATUSRESP,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProcStatus',
    full_name='dfs.sls.level2spectra.Level2spectraSrv.UpdateProcStatus',
    index=4,
    containing_service=None,
    input_type=_UPDATEPROCSTATUSREQ,
    output_type=_UPDATEPROCSTATUSRESP,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LEVEL2SPECTRASRV)

DESCRIPTOR.services_by_name['Level2spectraSrv'] = _LEVEL2SPECTRASRV

# @@protoc_insertion_point(module_scope)
