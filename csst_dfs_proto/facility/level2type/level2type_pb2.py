# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/level2type/level2type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$facility/level2type/level2type.proto\x12\x17\x64\x66s.facility.level2Type\x1a\x12\x63ommon/error.proto\"\xf6\x01\n\x10Level2TypeRecord\x12\x11\n\tdata_type\x18\x01 \x01(\t\x12\x11\n\tmodule_id\x18\x02 \x01(\t\x12\x12\n\nkey_column\x18\x03 \x01(\t\x12\x11\n\thdu_index\x18\x04 \x01(\x05\x12\x15\n\rdemo_filename\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x65mo_file_path\x18\x06 \x01(\t\x12\x11\n\tra_column\x18\x07 \x01(\t\x12\x12\n\ndec_column\x18\x08 \x01(\t\x12\x13\n\x0bupdate_time\x18\t \x01(\t\x12\x13\n\x0b\x63reate_time\x18\n \x01(\t\x12\x15\n\rimport_status\x18\x0b \x01(\x05\"m\n\x11\x46indLevel2TypeReq\x12\x11\n\tmodule_id\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\x15\n\rimport_status\x18\x03 \x01(\x05\x12\x0c\n\x04page\x18\x04 \x01(\x05\x12\r\n\x05limit\x18\x05 \x01(\x05\"\x93\x01\n\x12\x46indLevel2TypeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12:\n\x07records\x18\x04 \x03(\x0b\x32).dfs.facility.level2Type.Level2TypeRecord\"%\n\x10GetLevel2TypeReq\x12\x11\n\tdata_type\x18\x01 \x01(\t\"N\n\x11GetLevel2TypeResp\x12\x39\n\x06record\x18\x01 \x01(\x0b\x32).dfs.facility.level2Type.Level2TypeRecord\"]\n\x12WriteLevel2TypeReq\x12\x39\n\x06record\x18\x01 \x01(\x0b\x32).dfs.facility.level2Type.Level2TypeRecord\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x7f\n\x13WriteLevel2TypeResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x39\n\x06record\x18\x03 \x01(\x0b\x32).dfs.facility.level2Type.Level2TypeRecord\":\n\x15UpdateImportStatusReq\x12\x11\n\tdata_type\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\x05\"G\n\x16UpdateImportStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xb3\x03\n\rLevel2TypeSrv\x12\x61\n\x04\x46ind\x12*.dfs.facility.level2Type.FindLevel2TypeReq\x1a+.dfs.facility.level2Type.FindLevel2TypeResp\"\x00\x12^\n\x03Get\x12).dfs.facility.level2Type.GetLevel2TypeReq\x1a*.dfs.facility.level2Type.GetLevel2TypeResp\"\x00\x12\x66\n\x05Write\x12+.dfs.facility.level2Type.WriteLevel2TypeReq\x1a,.dfs.facility.level2Type.WriteLevel2TypeResp\"\x00(\x01\x12w\n\x12UpdateImportStatus\x12..dfs.facility.level2Type.UpdateImportStatusReq\x1a/.dfs.facility.level2Type.UpdateImportStatusResp\"\x00\x42*Z(cnlab.net/csst/proto/facility/level2Typeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'facility.level2type.level2type_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z(cnlab.net/csst/proto/facility/level2Type'
  _LEVEL2TYPERECORD._serialized_start=86
  _LEVEL2TYPERECORD._serialized_end=332
  _FINDLEVEL2TYPEREQ._serialized_start=334
  _FINDLEVEL2TYPEREQ._serialized_end=443
  _FINDLEVEL2TYPERESP._serialized_start=446
  _FINDLEVEL2TYPERESP._serialized_end=593
  _GETLEVEL2TYPEREQ._serialized_start=595
  _GETLEVEL2TYPEREQ._serialized_end=632
  _GETLEVEL2TYPERESP._serialized_start=634
  _GETLEVEL2TYPERESP._serialized_end=712
  _WRITELEVEL2TYPEREQ._serialized_start=714
  _WRITELEVEL2TYPEREQ._serialized_end=807
  _WRITELEVEL2TYPERESP._serialized_start=809
  _WRITELEVEL2TYPERESP._serialized_end=936
  _UPDATEIMPORTSTATUSREQ._serialized_start=938
  _UPDATEIMPORTSTATUSREQ._serialized_end=996
  _UPDATEIMPORTSTATUSRESP._serialized_start=998
  _UPDATEIMPORTSTATUSRESP._serialized_end=1069
  _LEVEL2TYPESRV._serialized_start=1072
  _LEVEL2TYPESRV._serialized_end=1507
# @@protoc_insertion_point(module_scope)