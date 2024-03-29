# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: facility/level1/level1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x61\x63ility/level1/level1.proto\x12\x13\x64\x66s.facility.level1\x1a\x12\x63ommon/error.proto\"\xb3\x03\n\x0cLevel1Record\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\x12\n\ncor_sci_id\x18\x04 \x01(\x03\x12\x11\n\tmodule_id\x18\x05 \x01(\t\x12\x12\n\nprc_params\x18\x06 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x07 \x01(\t\x12\x10\n\x08\x66ilename\x18\x08 \x01(\t\x12\x11\n\tfile_path\x18\t \x01(\t\x12\x12\n\nqc1_status\x18\n \x01(\x05\x12\x10\n\x08qc1_time\x18\x0b \x01(\t\x12\x12\n\nprc_status\x18\x0c \x01(\x05\x12\x10\n\x08prc_time\x18\r \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0e \x01(\t\x12\x13\n\x0bpipeline_id\x18\x0f \x01(\t\x12\x0e\n\x06header\x18\x10 \x01(\t\x12\x13\n\x0b\x64\x65tector_no\x18\x11 \x01(\t\x12\x39\n\x04refs\x18\x12 \x03(\x0b\x32+.dfs.facility.level1.Level1Record.RefsEntry\x1a+\n\tRefsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xaf\x03\n\rFindLevel1Req\x12\x0e\n\x06obs_id\x18\x01 \x01(\t\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\x11\n\tmodule_id\x18\x04 \x01(\t\x12\x19\n\x11\x63reate_time_start\x18\x05 \x01(\t\x12\x17\n\x0f\x63reate_time_end\x18\x06 \x01(\t\x12\x12\n\nqc1_status\x18\x07 \x01(\x05\x12\x12\n\nprc_status\x18\x08 \x01(\x05\x12\x10\n\x08\x66ilename\x18\t \x01(\t\x12\r\n\x05limit\x18\n \x01(\x05\x12\x13\n\x0bpipeline_id\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65tector_no\x18\x0c \x01(\t\x12\x0e\n\x06\x66ilter\x18\r \x01(\t\x12\x13\n\x0bobject_name\x18\x0e \x01(\t\x12Q\n\x10other_conditions\x18\x0f \x03(\x0b\x32\x37.dfs.facility.level1.FindLevel1Req.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x87\x01\n\x0e\x46indLevel1Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x32\n\x07records\x18\x04 \x03(\x0b\x32!.dfs.facility.level1.Level1Record\"&\n\x11\x46indByBrickIdsReq\x12\x11\n\tbrick_ids\x18\x01 \x03(\x05\"w\n\x12\x46indByBrickIdsResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x32\n\x07records\x18\x03 \x03(\x0b\x32!.dfs.facility.level1.Level1Record\"\x1b\n\x0c\x46indByIdsReq\x12\x0b\n\x03ids\x18\x01 \x03(\x05\"r\n\rFindByIdsResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x32\n\x07records\x18\x03 \x03(\x0b\x32!.dfs.facility.level1.Level1Record\"@\n\x0cGetLevel1Req\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tdata_type\x18\x03 \x01(\t\"B\n\rGetLevel1Resp\x12\x31\n\x06record\x18\x01 \x01(\x0b\x32!.dfs.facility.level1.Level1Record\"Q\n\x0eWriteLevel1Req\x12\x31\n\x06record\x18\x01 \x01(\x0b\x32!.dfs.facility.level1.Level1Record\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"s\n\x0fWriteLevel1Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x31\n\x06record\x18\x03 \x01(\x0b\x32!.dfs.facility.level1.Level1Record\"0\n\x12UpdateQc1StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc1StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xf2\x05\n\tLevel1Srv\x12Q\n\x04\x46ind\x12\".dfs.facility.level1.FindLevel1Req\x1a#.dfs.facility.level1.FindLevel1Resp\"\x00\x12T\n\tFindByIds\x12!.dfs.facility.level1.FindByIdsReq\x1a\".dfs.facility.level1.FindByIdsResp\"\x00\x12\x63\n\x0e\x46indByBrickIds\x12&.dfs.facility.level1.FindByBrickIdsReq\x1a\'.dfs.facility.level1.FindByBrickIdsResp\"\x00\x12\\\n\x0f\x46indByQc1Status\x12\".dfs.facility.level1.FindLevel1Req\x1a#.dfs.facility.level1.FindLevel1Resp\"\x00\x12N\n\x03Get\x12!.dfs.facility.level1.GetLevel1Req\x1a\".dfs.facility.level1.GetLevel1Resp\"\x00\x12V\n\x05Write\x12#.dfs.facility.level1.WriteLevel1Req\x1a$.dfs.facility.level1.WriteLevel1Resp\"\x00(\x01\x12\x66\n\x0fUpdateQc1Status\x12\'.dfs.facility.level1.UpdateQc1StatusReq\x1a(.dfs.facility.level1.UpdateQc1StatusResp\"\x00\x12i\n\x10UpdateProcStatus\x12(.dfs.facility.level1.UpdateProcStatusReq\x1a).dfs.facility.level1.UpdateProcStatusResp\"\x00\x42&Z$cnlab.net/csst/proto/facility/level1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'facility.level1.level1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$cnlab.net/csst/proto/facility/level1'
  _LEVEL1RECORD_REFSENTRY._options = None
  _LEVEL1RECORD_REFSENTRY._serialized_options = b'8\001'
  _FINDLEVEL1REQ_OTHERCONDITIONSENTRY._options = None
  _FINDLEVEL1REQ_OTHERCONDITIONSENTRY._serialized_options = b'8\001'
  _LEVEL1RECORD._serialized_start=74
  _LEVEL1RECORD._serialized_end=509
  _LEVEL1RECORD_REFSENTRY._serialized_start=466
  _LEVEL1RECORD_REFSENTRY._serialized_end=509
  _FINDLEVEL1REQ._serialized_start=512
  _FINDLEVEL1REQ._serialized_end=943
  _FINDLEVEL1REQ_OTHERCONDITIONSENTRY._serialized_start=889
  _FINDLEVEL1REQ_OTHERCONDITIONSENTRY._serialized_end=943
  _FINDLEVEL1RESP._serialized_start=946
  _FINDLEVEL1RESP._serialized_end=1081
  _FINDBYBRICKIDSREQ._serialized_start=1083
  _FINDBYBRICKIDSREQ._serialized_end=1121
  _FINDBYBRICKIDSRESP._serialized_start=1123
  _FINDBYBRICKIDSRESP._serialized_end=1242
  _FINDBYIDSREQ._serialized_start=1244
  _FINDBYIDSREQ._serialized_end=1271
  _FINDBYIDSRESP._serialized_start=1273
  _FINDBYIDSRESP._serialized_end=1387
  _GETLEVEL1REQ._serialized_start=1389
  _GETLEVEL1REQ._serialized_end=1453
  _GETLEVEL1RESP._serialized_start=1455
  _GETLEVEL1RESP._serialized_end=1521
  _WRITELEVEL1REQ._serialized_start=1523
  _WRITELEVEL1REQ._serialized_end=1604
  _WRITELEVEL1RESP._serialized_start=1606
  _WRITELEVEL1RESP._serialized_end=1721
  _UPDATEQC1STATUSREQ._serialized_start=1723
  _UPDATEQC1STATUSREQ._serialized_end=1771
  _UPDATEQC1STATUSRESP._serialized_start=1773
  _UPDATEQC1STATUSRESP._serialized_end=1841
  _UPDATEPROCSTATUSREQ._serialized_start=1843
  _UPDATEPROCSTATUSREQ._serialized_end=1892
  _UPDATEPROCSTATUSRESP._serialized_start=1894
  _UPDATEPROCSTATUSRESP._serialized_end=1963
  _LEVEL1SRV._serialized_start=1966
  _LEVEL1SRV._serialized_end=2720
# @@protoc_insertion_point(module_scope)
