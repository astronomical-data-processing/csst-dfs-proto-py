# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import result1_pb2 as ifs_dot_result1_dot_result1__pb2


class Result1SrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/ifs.result1.Result1Srv/Find',
        request_serializer=ifs_dot_result1_dot_result1__pb2.FindResult1Req.SerializeToString,
        response_deserializer=ifs_dot_result1_dot_result1__pb2.FindResult1Resp.FromString,
        )
    self.Get = channel.unary_unary(
        '/ifs.result1.Result1Srv/Get',
        request_serializer=ifs_dot_result1_dot_result1__pb2.GetResult1Req.SerializeToString,
        response_deserializer=ifs_dot_result1_dot_result1__pb2.GetResult1Resp.FromString,
        )
    self.Read = channel.unary_stream(
        '/ifs.result1.Result1Srv/Read',
        request_serializer=ifs_dot_result1_dot_result1__pb2.ReadResult1Req.SerializeToString,
        response_deserializer=ifs_dot_result1_dot_result1__pb2.ReadResult1Resp.FromString,
        )
    self.Write = channel.stream_unary(
        '/ifs.result1.Result1Srv/Write',
        request_serializer=ifs_dot_result1_dot_result1__pb2.WriteResult1Req.SerializeToString,
        response_deserializer=ifs_dot_result1_dot_result1__pb2.WriteResult1Resp.FromString,
        )


class Result1SrvServicer(object):
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

  def Read(self, request, context):
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


def add_Result1SrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=ifs_dot_result1_dot_result1__pb2.FindResult1Req.FromString,
          response_serializer=ifs_dot_result1_dot_result1__pb2.FindResult1Resp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=ifs_dot_result1_dot_result1__pb2.GetResult1Req.FromString,
          response_serializer=ifs_dot_result1_dot_result1__pb2.GetResult1Resp.SerializeToString,
      ),
      'Read': grpc.unary_stream_rpc_method_handler(
          servicer.Read,
          request_deserializer=ifs_dot_result1_dot_result1__pb2.ReadResult1Req.FromString,
          response_serializer=ifs_dot_result1_dot_result1__pb2.ReadResult1Resp.SerializeToString,
      ),
      'Write': grpc.stream_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=ifs_dot_result1_dot_result1__pb2.WriteResult1Req.FromString,
          response_serializer=ifs_dot_result1_dot_result1__pb2.WriteResult1Resp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ifs.result1.Result1Srv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
