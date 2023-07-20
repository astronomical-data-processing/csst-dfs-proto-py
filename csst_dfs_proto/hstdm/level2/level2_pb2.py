# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hstdm/level2/level2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19hstdm/level2/level2.proto\x12\x10\x64\x66s.hstdm.level2\x1a\x12\x63ommon/error.proto\"\x82\x02\n\x0cLevel2Record\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tlevel1_id\x18\x03 \x01(\x03\x12\x12\n\nproject_id\x18\x04 \x01(\x03\x12\x11\n\tfile_type\x18\x05 \x01(\t\x12\x10\n\x08\x66ilename\x18\x06 \x01(\t\x12\x11\n\tfile_path\x18\x07 \x01(\t\x12\x12\n\nqc2_status\x18\x08 \x01(\x05\x12\x10\n\x08qc2_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\x05\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x13\n\x0bpipeline_id\x18\r \x01(\t\"\xe1\x02\n\rFindLevel2Req\x12\x11\n\tlevel0_id\x18\x01 \x01(\t\x12\x11\n\tlevel1_id\x18\x02 \x01(\x03\x12\x12\n\nproject_id\x18\x03 \x01(\x03\x12\x11\n\tfile_type\x18\x04 \x01(\x03\x12\x19\n\x11\x63reate_time_start\x18\x05 \x01(\t\x12\x17\n\x0f\x63reate_time_end\x18\x06 \x01(\t\x12\x12\n\nqc2_status\x18\x07 \x01(\x05\x12\x12\n\nprc_status\x18\x08 \x01(\x05\x12\x10\n\x08\x66ilename\x18\t \x01(\t\x12\r\n\x05limit\x18\n \x01(\x05\x12N\n\x10other_conditions\x18\x0b \x03(\x0b\x32\x34.dfs.hstdm.level2.FindLevel2Req.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x84\x01\n\x0e\x46indLevel2Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12/\n\x07records\x18\x04 \x03(\x0b\x32\x1e.dfs.hstdm.level2.Level2Record\"\x1a\n\x0cGetLevel2Req\x12\n\n\x02id\x18\x01 \x01(\x03\"?\n\rGetLevel2Resp\x12.\n\x06record\x18\x01 \x01(\x0b\x32\x1e.dfs.hstdm.level2.Level2Record\"N\n\x0eWriteLevel2Req\x12.\n\x06record\x18\x01 \x01(\x0b\x32\x1e.dfs.hstdm.level2.Level2Record\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"p\n\x0fWriteLevel2Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12.\n\x06record\x18\x03 \x01(\x0b\x32\x1e.dfs.hstdm.level2.Level2Record\"0\n\x12UpdateQc2StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc2StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xbb\x03\n\tLevel2Srv\x12K\n\x04\x46ind\x12\x1f.dfs.hstdm.level2.FindLevel2Req\x1a .dfs.hstdm.level2.FindLevel2Resp\"\x00\x12H\n\x03Get\x12\x1e.dfs.hstdm.level2.GetLevel2Req\x1a\x1f.dfs.hstdm.level2.GetLevel2Resp\"\x00\x12P\n\x05Write\x12 .dfs.hstdm.level2.WriteLevel2Req\x1a!.dfs.hstdm.level2.WriteLevel2Resp\"\x00(\x01\x12`\n\x0fUpdateQc2Status\x12$.dfs.hstdm.level2.UpdateQc2StatusReq\x1a%.dfs.hstdm.level2.UpdateQc2StatusResp\"\x00\x12\x63\n\x10UpdateProcStatus\x12%.dfs.hstdm.level2.UpdateProcStatusReq\x1a&.dfs.hstdm.level2.UpdateProcStatusResp\"\x00\x42#Z!cnlab.net/csst/proto/hstdm/level2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hstdm.level2.level2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z!cnlab.net/csst/proto/hstdm/level2'
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._options = None
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_options = b'8\001'
  _LEVEL2RECORD._serialized_start=68
  _LEVEL2RECORD._serialized_end=326
  _FINDLEVEL2REQ._serialized_start=329
  _FINDLEVEL2REQ._serialized_end=682
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_start=628
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_end=682
  _FINDLEVEL2RESP._serialized_start=685
  _FINDLEVEL2RESP._serialized_end=817
  _GETLEVEL2REQ._serialized_start=819
  _GETLEVEL2REQ._serialized_end=845
  _GETLEVEL2RESP._serialized_start=847
  _GETLEVEL2RESP._serialized_end=910
  _WRITELEVEL2REQ._serialized_start=912
  _WRITELEVEL2REQ._serialized_end=990
  _WRITELEVEL2RESP._serialized_start=992
  _WRITELEVEL2RESP._serialized_end=1104
  _UPDATEQC2STATUSREQ._serialized_start=1106
  _UPDATEQC2STATUSREQ._serialized_end=1154
  _UPDATEQC2STATUSRESP._serialized_start=1156
  _UPDATEQC2STATUSRESP._serialized_end=1224
  _UPDATEPROCSTATUSREQ._serialized_start=1226
  _UPDATEPROCSTATUSREQ._serialized_end=1275
  _UPDATEPROCSTATUSRESP._serialized_start=1277
  _UPDATEPROCSTATUSRESP._serialized_end=1346
  _LEVEL2SRV._serialized_start=1349
  _LEVEL2SRV._serialized_end=1792
# @@protoc_insertion_point(module_scope)