# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import calmerge_pb2 as facility_dot_calmerge_dot_calmerge__pb2


class CalMergeSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/calmerge.CalMergeSrv/Find',
        request_serializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeReq.SerializeToString,
        response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeResp.FromString,
        )
    self.Get = channel.unary_unary(
        '/calmerge.CalMergeSrv/Get',
        request_serializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeReq.SerializeToString,
        response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeResp.FromString,
        )
    self.Write = channel.unary_unary(
        '/calmerge.CalMergeSrv/Write',
        request_serializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeReq.SerializeToString,
        response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeResp.FromString,
        )
    self.UpdateQc1Status = channel.unary_unary(
        '/calmerge.CalMergeSrv/UpdateQc1Status',
        request_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusReq.SerializeToString,
        response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusResp.FromString,
        )
    self.UpdateProcStatus = channel.unary_unary(
        '/calmerge.CalMergeSrv/UpdateProcStatus',
        request_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusReq.SerializeToString,
        response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusResp.FromString,
        )


class CalMergeSrvServicer(object):
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

  def Write(self, request, context):
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


def add_CalMergeSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeReq.FromString,
          response_serializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeResp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeReq.FromString,
          response_serializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeResp.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeReq.FromString,
          response_serializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeResp.SerializeToString,
      ),
      'UpdateQc1Status': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateQc1Status,
          request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusReq.FromString,
          response_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusResp.SerializeToString,
      ),
      'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProcStatus,
          request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusReq.FromString,
          response_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'calmerge.CalMergeSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
