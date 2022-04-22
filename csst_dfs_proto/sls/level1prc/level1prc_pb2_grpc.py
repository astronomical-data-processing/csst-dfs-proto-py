# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import level1prc_pb2 as sls_dot_level1prc_dot_level1prc__pb2


class Level1PrcSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/dfs.sls.level1prc.Level1PrcSrv/Find',
        request_serializer=sls_dot_level1prc_dot_level1prc__pb2.FindLevel1PrcReq.SerializeToString,
        response_deserializer=sls_dot_level1prc_dot_level1prc__pb2.FindLevel1PrcResp.FromString,
        )
    self.Write = channel.unary_unary(
        '/dfs.sls.level1prc.Level1PrcSrv/Write',
        request_serializer=sls_dot_level1prc_dot_level1prc__pb2.WriteLevel1PrcReq.SerializeToString,
        response_deserializer=sls_dot_level1prc_dot_level1prc__pb2.WriteLevel1PrcResp.FromString,
        )
    self.UpdateProcStatus = channel.unary_unary(
        '/dfs.sls.level1prc.Level1PrcSrv/UpdateProcStatus',
        request_serializer=sls_dot_level1prc_dot_level1prc__pb2.UpdateProcStatusReq.SerializeToString,
        response_deserializer=sls_dot_level1prc_dot_level1prc__pb2.UpdateProcStatusResp.FromString,
        )


class Level1PrcSrvServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Find(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Write(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateProcStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Level1PrcSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=sls_dot_level1prc_dot_level1prc__pb2.FindLevel1PrcReq.FromString,
          response_serializer=sls_dot_level1prc_dot_level1prc__pb2.FindLevel1PrcResp.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=sls_dot_level1prc_dot_level1prc__pb2.WriteLevel1PrcReq.FromString,
          response_serializer=sls_dot_level1prc_dot_level1prc__pb2.WriteLevel1PrcResp.SerializeToString,
      ),
      'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProcStatus,
          request_deserializer=sls_dot_level1prc_dot_level1prc__pb2.UpdateProcStatusReq.FromString,
          response_serializer=sls_dot_level1prc_dot_level1prc__pb2.UpdateProcStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dfs.sls.level1prc.Level1PrcSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
