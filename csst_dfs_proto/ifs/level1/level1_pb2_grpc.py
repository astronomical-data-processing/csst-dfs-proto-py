# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import level1_pb2 as ifs_dot_level1_dot_level1__pb2


class Level1SrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/dfs.ifs.level1.Level1Srv/Find',
        request_serializer=ifs_dot_level1_dot_level1__pb2.FindLevel1Req.SerializeToString,
        response_deserializer=ifs_dot_level1_dot_level1__pb2.FindLevel1Resp.FromString,
        )
    self.Get = channel.unary_unary(
        '/dfs.ifs.level1.Level1Srv/Get',
        request_serializer=ifs_dot_level1_dot_level1__pb2.GetLevel1Req.SerializeToString,
        response_deserializer=ifs_dot_level1_dot_level1__pb2.GetLevel1Resp.FromString,
        )
    self.Write = channel.stream_unary(
        '/dfs.ifs.level1.Level1Srv/Write',
        request_serializer=ifs_dot_level1_dot_level1__pb2.WriteLevel1Req.SerializeToString,
        response_deserializer=ifs_dot_level1_dot_level1__pb2.WriteLevel1Resp.FromString,
        )
    self.UpdateQc1Status = channel.unary_unary(
        '/dfs.ifs.level1.Level1Srv/UpdateQc1Status',
        request_serializer=ifs_dot_level1_dot_level1__pb2.UpdateQc1StatusReq.SerializeToString,
        response_deserializer=ifs_dot_level1_dot_level1__pb2.UpdateQc1StatusResp.FromString,
        )
    self.UpdateProcStatus = channel.unary_unary(
        '/dfs.ifs.level1.Level1Srv/UpdateProcStatus',
        request_serializer=ifs_dot_level1_dot_level1__pb2.UpdateProcStatusReq.SerializeToString,
        response_deserializer=ifs_dot_level1_dot_level1__pb2.UpdateProcStatusResp.FromString,
        )


class Level1SrvServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Find(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Write(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateQc1Status(self, request, context):
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


def add_Level1SrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=ifs_dot_level1_dot_level1__pb2.FindLevel1Req.FromString,
          response_serializer=ifs_dot_level1_dot_level1__pb2.FindLevel1Resp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=ifs_dot_level1_dot_level1__pb2.GetLevel1Req.FromString,
          response_serializer=ifs_dot_level1_dot_level1__pb2.GetLevel1Resp.SerializeToString,
      ),
      'Write': grpc.stream_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=ifs_dot_level1_dot_level1__pb2.WriteLevel1Req.FromString,
          response_serializer=ifs_dot_level1_dot_level1__pb2.WriteLevel1Resp.SerializeToString,
      ),
      'UpdateQc1Status': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateQc1Status,
          request_deserializer=ifs_dot_level1_dot_level1__pb2.UpdateQc1StatusReq.FromString,
          response_serializer=ifs_dot_level1_dot_level1__pb2.UpdateQc1StatusResp.SerializeToString,
      ),
      'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProcStatus,
          request_deserializer=ifs_dot_level1_dot_level1__pb2.UpdateProcStatusReq.FromString,
          response_serializer=ifs_dot_level1_dot_level1__pb2.UpdateProcStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dfs.ifs.level1.Level1Srv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
