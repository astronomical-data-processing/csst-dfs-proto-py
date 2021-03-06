# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import observation_pb2 as facility_dot_observation_dot_observation__pb2


class ObservationSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/dfs.facility.observation.ObservationSrv/Find',
        request_serializer=facility_dot_observation_dot_observation__pb2.FindObservationReq.SerializeToString,
        response_deserializer=facility_dot_observation_dot_observation__pb2.FindObservationResp.FromString,
        )
    self.Get = channel.unary_unary(
        '/dfs.facility.observation.ObservationSrv/Get',
        request_serializer=facility_dot_observation_dot_observation__pb2.GetObservationReq.SerializeToString,
        response_deserializer=facility_dot_observation_dot_observation__pb2.GetObservationResp.FromString,
        )
    self.Write = channel.unary_unary(
        '/dfs.facility.observation.ObservationSrv/Write',
        request_serializer=facility_dot_observation_dot_observation__pb2.WriteObservationReq.SerializeToString,
        response_deserializer=facility_dot_observation_dot_observation__pb2.WriteObservationResp.FromString,
        )
    self.UpdateQc0Status = channel.unary_unary(
        '/dfs.facility.observation.ObservationSrv/UpdateQc0Status',
        request_serializer=facility_dot_observation_dot_observation__pb2.UpdateQc0StatusReq.SerializeToString,
        response_deserializer=facility_dot_observation_dot_observation__pb2.UpdateQc0StatusResp.FromString,
        )
    self.UpdateProcStatus = channel.unary_unary(
        '/dfs.facility.observation.ObservationSrv/UpdateProcStatus',
        request_serializer=facility_dot_observation_dot_observation__pb2.UpdateProcStatusReq.SerializeToString,
        response_deserializer=facility_dot_observation_dot_observation__pb2.UpdateProcStatusResp.FromString,
        )


class ObservationSrvServicer(object):
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

  def UpdateQc0Status(self, request, context):
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


def add_ObservationSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=facility_dot_observation_dot_observation__pb2.FindObservationReq.FromString,
          response_serializer=facility_dot_observation_dot_observation__pb2.FindObservationResp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=facility_dot_observation_dot_observation__pb2.GetObservationReq.FromString,
          response_serializer=facility_dot_observation_dot_observation__pb2.GetObservationResp.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=facility_dot_observation_dot_observation__pb2.WriteObservationReq.FromString,
          response_serializer=facility_dot_observation_dot_observation__pb2.WriteObservationResp.SerializeToString,
      ),
      'UpdateQc0Status': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateQc0Status,
          request_deserializer=facility_dot_observation_dot_observation__pb2.UpdateQc0StatusReq.FromString,
          response_serializer=facility_dot_observation_dot_observation__pb2.UpdateQc0StatusResp.SerializeToString,
      ),
      'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateProcStatus,
          request_deserializer=facility_dot_observation_dot_observation__pb2.UpdateProcStatusReq.FromString,
          response_serializer=facility_dot_observation_dot_observation__pb2.UpdateProcStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dfs.facility.observation.ObservationSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
