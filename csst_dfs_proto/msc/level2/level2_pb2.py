# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msc/level2/level2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...common import error_pb2 as common_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17msc/level2/level2.proto\x12\x0e\x64\x66s.msc.level2\x1a\x12\x63ommon/error.proto\"\x97\x02\n\x0cLevel2Record\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tlevel0_id\x18\x02 \x01(\t\x12\x11\n\tlevel1_id\x18\x03 \x01(\x03\x12\x11\n\tdata_type\x18\x04 \x01(\t\x12\x10\n\x08\x66ilename\x18\x05 \x01(\t\x12\x11\n\tfile_path\x18\x06 \x01(\t\x12\x10\n\x08obs_time\x18\x07 \x01(\t\x12\x12\n\nqc2_status\x18\x08 \x01(\x05\x12\x10\n\x08qc2_time\x18\t \x01(\t\x12\x12\n\nprc_status\x18\n \x01(\x05\x12\x10\n\x08prc_time\x18\x0b \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x0c \x01(\t\x12\x13\n\x0bpipeline_id\x18\r \x01(\t\x12\x15\n\rimport_status\x18\x0e \x01(\x05\"\xcb\x02\n\rFindLevel2Req\x12\x11\n\tlevel0_id\x18\x01 \x01(\t\x12\x11\n\tlevel1_id\x18\x02 \x01(\x03\x12\x11\n\tdata_type\x18\x03 \x01(\t\x12\x19\n\x11\x63reate_time_start\x18\x04 \x01(\t\x12\x17\n\x0f\x63reate_time_end\x18\x05 \x01(\t\x12\x12\n\nqc2_status\x18\x06 \x01(\x05\x12\x12\n\nprc_status\x18\x07 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x08 \x01(\t\x12\r\n\x05limit\x18\t \x01(\x05\x12L\n\x10other_conditions\x18\n \x03(\x0b\x32\x32.dfs.msc.level2.FindLevel2Req.OtherConditionsEntry\x1a\x36\n\x14OtherConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x82\x01\n\x0e\x46indLevel2Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12-\n\x07records\x18\x04 \x03(\x0b\x32\x1c.dfs.msc.level2.Level2Record\"\x1a\n\x0cGetLevel2Req\x12\n\n\x02id\x18\x01 \x01(\x03\"=\n\rGetLevel2Resp\x12,\n\x06record\x18\x01 \x01(\x0b\x32\x1c.dfs.msc.level2.Level2Record\"\x16\n\x14\x46indExistedBricksReq\"Y\n\x15\x46indExistedBricksResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12\x11\n\tbrick_ids\x18\x03 \x03(\x05\"L\n\x0eWriteLevel2Req\x12,\n\x06record\x18\x01 \x01(\x0b\x32\x1c.dfs.msc.level2.Level2Record\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"n\n\x0fWriteLevel2Resp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\x12,\n\x06record\x18\x03 \x01(\x0b\x32\x1c.dfs.msc.level2.Level2Record\"0\n\x12UpdateQc2StatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"D\n\x13UpdateQc2StatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"1\n\x13UpdateProcStatusReq\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06status\x18\x02 \x01(\x05\"E\n\x14UpdateProcStatusResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error\"\xd7\x12\n\x13Level2CatalogRecord\x12\x11\n\tlevel2_id\x18\x01 \x01(\x03\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\r\n\x05\x43\x43\x44NO\x18\x03 \x01(\x05\x12\r\n\x05objID\x18\x04 \x01(\x05\x12\t\n\x01X\x18\x05 \x01(\x02\x12\x0c\n\x04XErr\x18\x06 \x01(\x01\x12\t\n\x01Y\x18\x07 \x01(\x02\x12\x0c\n\x04YErr\x18\x08 \x01(\x01\x12\n\n\x02RA\x18\t \x01(\x01\x12\r\n\x05RAErr\x18\n \x01(\x01\x12\x0b\n\x03\x44\x45\x43\x18\x0b \x01(\x01\x12\x0e\n\x06\x44\x45\x43\x45rr\x18\x0c \x01(\x01\x12\t\n\x01\x41\x18\r \x01(\x02\x12\x0c\n\x04\x41\x45rr\x18\x0e \x01(\x02\x12\t\n\x01\x42\x18\x0f \x01(\x02\x12\x0c\n\x04\x42\x45rr\x18\x10 \x01(\x02\x12\n\n\x02PA\x18\x11 \x01(\x02\x12\r\n\x05PAErr\x18\x12 \x01(\x02\x12\x0c\n\x04\x46lag\x18\x13 \x01(\x05\x12\x10\n\x08\x46lag_ISO\x18\x14 \x01(\x05\x12\x14\n\x0c\x46lag_ISO_Num\x18\x15 \x01(\x05\x12\x0c\n\x04\x46WHM\x18\x16 \x01(\x02\x12\n\n\x02\x41\x42\x18\x17 \x01(\x02\x12\t\n\x01\x45\x18\x18 \x01(\x02\x12\x11\n\tFlux_Kron\x18\x19 \x01(\x01\x12\x14\n\x0c\x46luxErr_Kron\x18\x1a \x01(\x02\x12\x10\n\x08Mag_Kron\x18\x1b \x01(\x01\x12\x13\n\x0bMagErr_Kron\x18\x1c \x01(\x01\x12\x13\n\x0bRadius_Kron\x18\x1d \x01(\x01\x12\x0b\n\x03Sky\x18\x1e \x01(\x02\x12\x12\n\nFlux_Aper1\x18\x1f \x01(\x02\x12\x15\n\rFluxErr_Aper1\x18  \x01(\x02\x12\x11\n\tMag_Aper1\x18! \x01(\x02\x12\x14\n\x0cMagErr_Aper1\x18\" \x01(\x02\x12\x12\n\nFlux_Aper2\x18# \x01(\x02\x12\x15\n\rFluxErr_Aper2\x18$ \x01(\x02\x12\x11\n\tMag_Aper2\x18% \x01(\x02\x12\x14\n\x0cMagErr_Aper2\x18& \x01(\x02\x12\x12\n\nFlux_Aper3\x18\' \x01(\x02\x12\x15\n\rFluxErr_Aper3\x18( \x01(\x02\x12\x11\n\tMag_Aper3\x18) \x01(\x02\x12\x14\n\x0cMagErr_Aper3\x18* \x01(\x02\x12\x12\n\nFlux_Aper4\x18+ \x01(\x02\x12\x15\n\rFluxErr_Aper4\x18, \x01(\x02\x12\x11\n\tMag_Aper4\x18- \x01(\x02\x12\x14\n\x0cMagErr_Aper4\x18. \x01(\x02\x12\x12\n\nFlux_Aper5\x18/ \x01(\x02\x12\x15\n\rFluxErr_Aper5\x18\x30 \x01(\x02\x12\x11\n\tMag_Aper5\x18\x31 \x01(\x02\x12\x14\n\x0cMagErr_Aper5\x18\x32 \x01(\x02\x12\x12\n\nFlux_Aper6\x18\x33 \x01(\x02\x12\x15\n\rFluxErr_Aper6\x18\x34 \x01(\x02\x12\x11\n\tMag_Aper6\x18\x35 \x01(\x02\x12\x14\n\x0cMagErr_Aper6\x18\x36 \x01(\x02\x12\x12\n\nFlux_Aper7\x18\x37 \x01(\x02\x12\x15\n\rFluxErr_Aper7\x18\x38 \x01(\x02\x12\x11\n\tMag_Aper7\x18\x39 \x01(\x02\x12\x14\n\x0cMagErr_Aper7\x18: \x01(\x02\x12\x12\n\nFlux_Aper8\x18; \x01(\x02\x12\x15\n\rFluxErr_Aper8\x18< \x01(\x02\x12\x11\n\tMag_Aper8\x18= \x01(\x02\x12\x14\n\x0cMagErr_Aper8\x18> \x01(\x02\x12\x12\n\nFlux_Aper9\x18? \x01(\x02\x12\x15\n\rFluxErr_Aper9\x18@ \x01(\x02\x12\x11\n\tMag_Aper9\x18\x41 \x01(\x02\x12\x14\n\x0cMagErr_Aper9\x18\x42 \x01(\x02\x12\x13\n\x0b\x46lux_Aper10\x18\x43 \x01(\x02\x12\x16\n\x0e\x46luxErr_Aper10\x18\x44 \x01(\x02\x12\x12\n\nMag_Aper10\x18\x45 \x01(\x02\x12\x15\n\rMagErr_Aper10\x18\x46 \x01(\x02\x12\x13\n\x0b\x46lux_Aper11\x18G \x01(\x02\x12\x16\n\x0e\x46luxErr_Aper11\x18H \x01(\x02\x12\x12\n\nMag_Aper11\x18I \x01(\x02\x12\x15\n\rMagErr_Aper11\x18J \x01(\x02\x12\x13\n\x0b\x46lux_Aper12\x18K \x01(\x02\x12\x16\n\x0e\x46luxErr_Aper12\x18L \x01(\x02\x12\x12\n\nMag_Aper12\x18M \x01(\x02\x12\x15\n\rMagErr_Aper12\x18N \x01(\x02\x12\x0c\n\x04Type\x18O \x01(\x05\x12\x0b\n\x03R20\x18P \x01(\x02\x12\x0b\n\x03R50\x18Q \x01(\x02\x12\x0b\n\x03R90\x18R \x01(\x02\x12\r\n\x05X_PSF\x18S \x01(\x01\x12\r\n\x05Y_PSF\x18T \x01(\x01\x12\x0e\n\x06RA_PSF\x18U \x01(\x01\x12\x0f\n\x07\x44\x45\x43_PSF\x18V \x01(\x01\x12\x10\n\x08\x43hi2_PSF\x18W \x01(\x02\x12\x10\n\x08\x46lux_PSF\x18X \x01(\x02\x12\x13\n\x0b\x46luxErr_PSF\x18Y \x01(\x02\x12\x0f\n\x07Mag_PSF\x18Z \x01(\x02\x12\x12\n\nMagErr_PSF\x18[ \x01(\x02\x12\x0f\n\x07X_Model\x18\\ \x01(\x01\x12\x0f\n\x07Y_Model\x18] \x01(\x01\x12\x10\n\x08RA_Model\x18^ \x01(\x01\x12\x11\n\tDEC_Model\x18_ \x01(\x01\x12\x12\n\nChi2_Model\x18` \x01(\x02\x12\x12\n\nFlag_Model\x18\x61 \x01(\x05\x12\x12\n\nFlux_Model\x18\x62 \x01(\x02\x12\x15\n\rFluxErr_Model\x18\x63 \x01(\x02\x12\x11\n\tMag_Model\x18\x64 \x01(\x02\x12\x14\n\x0cMagErr_Model\x18\x65 \x01(\x02\x12\x12\n\nFlux_Bulge\x18\x66 \x01(\x02\x12\x15\n\rFluxErr_Bulge\x18g \x01(\x02\x12\x11\n\tMag_Bulge\x18h \x01(\x02\x12\x14\n\x0cMagErr_Bulge\x18i \x01(\x02\x12\x10\n\x08Re_Bulge\x18j \x01(\x02\x12\x13\n\x0bReErr_Bulge\x18k \x01(\x02\x12\x0f\n\x07\x45_Bulge\x18l \x01(\x02\x12\x12\n\nEErr_Bulge\x18m \x01(\x02\x12\x10\n\x08PA_Bulge\x18n \x01(\x02\x12\x13\n\x0bPAErr_Bulge\x18o \x01(\x02\x12\x11\n\tFlux_Disk\x18p \x01(\x02\x12\x14\n\x0c\x46luxErr_Disk\x18q \x01(\x02\x12\x10\n\x08Mag_Disk\x18r \x01(\x02\x12\x13\n\x0bMagErr_Disk\x18s \x01(\x02\x12\x0f\n\x07Re_Disk\x18t \x01(\x02\x12\x12\n\nReErr_Disk\x18u \x01(\x02\x12\x0e\n\x06\x45_Disk\x18v \x01(\x02\x12\x11\n\tEErr_Disk\x18w \x01(\x02\x12\x0f\n\x07PA_Disk\x18x \x01(\x02\x12\x12\n\nPAErr_Disk\x18y \x01(\x02\x12\x12\n\nRatio_Disk\x18z \x01(\x02\x12\x15\n\rRatioErr_Disk\x18{ \x01(\x02\x12\x14\n\x0cSpread_Model\x18| \x01(\x02\x12\x17\n\x0fSpreadErr_Model\x18} \x01(\x02\x12\x10\n\x08\x42rick_Id\x18~ \x01(\x05\"\xf5\x01\n\x14\x46indLevel2CatalogReq\x12\x11\n\tbrick_ids\x18\x01 \x01(\t\x12\x0e\n\x06obs_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65tector_no\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\n\n\x02ra\x18\x05 \x01(\x01\x12\x0b\n\x03\x64\x65\x63\x18\x06 \x01(\x01\x12\x0e\n\x06radius\x18\x07 \x01(\x01\x12\x0e\n\x06minMag\x18\x08 \x01(\x01\x12\x0e\n\x06maxMag\x18\t \x01(\x01\x12\x16\n\x0eobs_time_start\x18\n \x01(\t\x12\x14\n\x0cobs_time_end\x18\x0b \x01(\t\x12\r\n\x05limit\x18\x0c \x01(\x05\x12\x0f\n\x07\x63olumns\x18\r \x01(\t\"k\n\x15\x46indLevel2CatalogResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12\x0f\n\x07records\x18\x04 \x01(\x0c\"\x87\x01\n\x13\x46indCatalogFileResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x12\n\ntotalCount\x18\x02 \x01(\x05\x12\x1c\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.common.Error\x12-\n\x07records\x18\x04 \x03(\x0b\x32\x1c.dfs.msc.level2.Level2Record\"/\n\x1a\x44\x65leteCatalogByLevel2IdReq\x12\x11\n\tlevel2_id\x18\x01 \x01(\x03\"L\n\x1b\x44\x65leteCatalogByLevel2IdResp\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.common.Error2\xc1\x06\n\tLevel2Srv\x12G\n\x04\x46ind\x12\x1d.dfs.msc.level2.FindLevel2Req\x1a\x1e.dfs.msc.level2.FindLevel2Resp\"\x00\x12^\n\x0b\x46indCatalog\x12$.dfs.msc.level2.FindLevel2CatalogReq\x1a%.dfs.msc.level2.FindLevel2CatalogResp\"\x00\x30\x01\x12^\n\x0f\x46indCatalogFile\x12$.dfs.msc.level2.FindLevel2CatalogReq\x1a#.dfs.msc.level2.FindCatalogFileResp\"\x00\x12\x62\n\x11\x46indExistedBricks\x12$.dfs.msc.level2.FindExistedBricksReq\x1a%.dfs.msc.level2.FindExistedBricksResp\"\x00\x12\x44\n\x03Get\x12\x1c.dfs.msc.level2.GetLevel2Req\x1a\x1d.dfs.msc.level2.GetLevel2Resp\"\x00\x12L\n\x05Write\x12\x1e.dfs.msc.level2.WriteLevel2Req\x1a\x1f.dfs.msc.level2.WriteLevel2Resp\"\x00(\x01\x12\\\n\x0fUpdateQc2Status\x12\".dfs.msc.level2.UpdateQc2StatusReq\x1a#.dfs.msc.level2.UpdateQc2StatusResp\"\x00\x12_\n\x10UpdateProcStatus\x12#.dfs.msc.level2.UpdateProcStatusReq\x1a$.dfs.msc.level2.UpdateProcStatusResp\"\x00\x12t\n\x17\x44\x65leteCatalogByLevel2Id\x12*.dfs.msc.level2.DeleteCatalogByLevel2IdReq\x1a+.dfs.msc.level2.DeleteCatalogByLevel2IdResp\"\x00\x42!Z\x1f\x63nlab.net/csst/proto/msc/level2b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'msc.level2.level2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\037cnlab.net/csst/proto/msc/level2'
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._options = None
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_options = b'8\001'
  _LEVEL2RECORD._serialized_start=64
  _LEVEL2RECORD._serialized_end=343
  _FINDLEVEL2REQ._serialized_start=346
  _FINDLEVEL2REQ._serialized_end=677
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_start=623
  _FINDLEVEL2REQ_OTHERCONDITIONSENTRY._serialized_end=677
  _FINDLEVEL2RESP._serialized_start=680
  _FINDLEVEL2RESP._serialized_end=810
  _GETLEVEL2REQ._serialized_start=812
  _GETLEVEL2REQ._serialized_end=838
  _GETLEVEL2RESP._serialized_start=840
  _GETLEVEL2RESP._serialized_end=901
  _FINDEXISTEDBRICKSREQ._serialized_start=903
  _FINDEXISTEDBRICKSREQ._serialized_end=925
  _FINDEXISTEDBRICKSRESP._serialized_start=927
  _FINDEXISTEDBRICKSRESP._serialized_end=1016
  _WRITELEVEL2REQ._serialized_start=1018
  _WRITELEVEL2REQ._serialized_end=1094
  _WRITELEVEL2RESP._serialized_start=1096
  _WRITELEVEL2RESP._serialized_end=1206
  _UPDATEQC2STATUSREQ._serialized_start=1208
  _UPDATEQC2STATUSREQ._serialized_end=1256
  _UPDATEQC2STATUSRESP._serialized_start=1258
  _UPDATEQC2STATUSRESP._serialized_end=1326
  _UPDATEPROCSTATUSREQ._serialized_start=1328
  _UPDATEPROCSTATUSREQ._serialized_end=1377
  _UPDATEPROCSTATUSRESP._serialized_start=1379
  _UPDATEPROCSTATUSRESP._serialized_end=1448
  _LEVEL2CATALOGRECORD._serialized_start=1451
  _LEVEL2CATALOGRECORD._serialized_end=3842
  _FINDLEVEL2CATALOGREQ._serialized_start=3845
  _FINDLEVEL2CATALOGREQ._serialized_end=4090
  _FINDLEVEL2CATALOGRESP._serialized_start=4092
  _FINDLEVEL2CATALOGRESP._serialized_end=4199
  _FINDCATALOGFILERESP._serialized_start=4202
  _FINDCATALOGFILERESP._serialized_end=4337
  _DELETECATALOGBYLEVEL2IDREQ._serialized_start=4339
  _DELETECATALOGBYLEVEL2IDREQ._serialized_end=4386
  _DELETECATALOGBYLEVEL2IDRESP._serialized_start=4388
  _DELETECATALOGBYLEVEL2IDRESP._serialized_end=4464
  _LEVEL2SRV._serialized_start=4467
  _LEVEL2SRV._serialized_end=5300
# @@protoc_insertion_point(module_scope)
