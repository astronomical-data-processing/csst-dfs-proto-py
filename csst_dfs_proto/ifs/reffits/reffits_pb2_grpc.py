# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ifs.reffits import reffits_pb2 as ifs_dot_reffits_dot_reffits__pb2


class RefFitsSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.find = channel.unary_unary(
        '/ifs.reffits.RefFitsSrv/find',
        request_serializer=ifs_dot_reffits_dot_reffits__pb2.FindRefFitsReq.SerializeToString,
        response_deserializer=ifs_dot_reffits_dot_reffits__pb2.FindRefFitsResp.FromString,
        )
    self.get = channel.unary_unary(
        '/ifs.reffits.RefFitsSrv/get',
        request_serializer=ifs_dot_reffits_dot_reffits__pb2.GetRefFitsReq.SerializeToString,
        response_deserializer=ifs_dot_reffits_dot_reffits__pb2.GetRefFitsResp.FromString,
        )
    self.read = channel.unary_stream(
        '/ifs.reffits.RefFitsSrv/read',
        request_serializer=ifs_dot_reffits_dot_reffits__pb2.ReadRefFitsReq.SerializeToString,
        response_deserializer=ifs_dot_reffits_dot_reffits__pb2.ReadRefFitsResp.FromString,
        )
    self.write = channel.stream_unary(
        '/ifs.reffits.RefFitsSrv/write',
        request_serializer=ifs_dot_reffits_dot_reffits__pb2.WriteRefFitsReq.SerializeToString,
        response_deserializer=ifs_dot_reffits_dot_reffits__pb2.WriteRefFitsResp.FromString,
        )
    self.update_status = channel.unary_unary(
        '/ifs.reffits.RefFitsSrv/update_status',
        request_serializer=ifs_dot_reffits_dot_reffits__pb2.UpdateStatusReq.SerializeToString,
        response_deserializer=ifs_dot_reffits_dot_reffits__pb2.UpdateStatusResp.FromString,
        )


class RefFitsSrvServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def find(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def write(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update_status(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RefFitsSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'find': grpc.unary_unary_rpc_method_handler(
          servicer.find,
          request_deserializer=ifs_dot_reffits_dot_reffits__pb2.FindRefFitsReq.FromString,
          response_serializer=ifs_dot_reffits_dot_reffits__pb2.FindRefFitsResp.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=ifs_dot_reffits_dot_reffits__pb2.GetRefFitsReq.FromString,
          response_serializer=ifs_dot_reffits_dot_reffits__pb2.GetRefFitsResp.SerializeToString,
      ),
      'read': grpc.unary_stream_rpc_method_handler(
          servicer.read,
          request_deserializer=ifs_dot_reffits_dot_reffits__pb2.ReadRefFitsReq.FromString,
          response_serializer=ifs_dot_reffits_dot_reffits__pb2.ReadRefFitsResp.SerializeToString,
      ),
      'write': grpc.stream_unary_rpc_method_handler(
          servicer.write,
          request_deserializer=ifs_dot_reffits_dot_reffits__pb2.WriteRefFitsReq.FromString,
          response_serializer=ifs_dot_reffits_dot_reffits__pb2.WriteRefFitsResp.SerializeToString,
      ),
      'update_status': grpc.unary_unary_rpc_method_handler(
          servicer.update_status,
          request_deserializer=ifs_dot_reffits_dot_reffits__pb2.UpdateStatusReq.FromString,
          response_serializer=ifs_dot_reffits_dot_reffits__pb2.UpdateStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ifs.reffits.RefFitsSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
