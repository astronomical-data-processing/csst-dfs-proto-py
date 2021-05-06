# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import detector_pb2 as facility_dot_detector__pb2


class DetectorSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Find = channel.unary_unary(
        '/facility.DetectorSrv/Find',
        request_serializer=facility_dot_detector__pb2.FindDetectorReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.FindDetectorResp.FromString,
        )
    self.Get = channel.unary_unary(
        '/facility.DetectorSrv/Get',
        request_serializer=facility_dot_detector__pb2.GetDetectorReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.GetDetectorResp.FromString,
        )
    self.Write = channel.unary_unary(
        '/facility.DetectorSrv/Write',
        request_serializer=facility_dot_detector__pb2.WriteDetectorReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.WriteDetectorResp.FromString,
        )
    self.Update = channel.unary_unary(
        '/facility.DetectorSrv/Update',
        request_serializer=facility_dot_detector__pb2.UpdateDetectorReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.UpdateDetectorResp.FromString,
        )
    self.FindStatus = channel.unary_unary(
        '/facility.DetectorSrv/FindStatus',
        request_serializer=facility_dot_detector__pb2.FindStatusReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.FindStatusResp.FromString,
        )
    self.GetStatus = channel.unary_unary(
        '/facility.DetectorSrv/GetStatus',
        request_serializer=facility_dot_detector__pb2.GetStatusReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.GetStatusResp.FromString,
        )
    self.WriteStatus = channel.unary_unary(
        '/facility.DetectorSrv/WriteStatus',
        request_serializer=facility_dot_detector__pb2.WriteStatusReq.SerializeToString,
        response_deserializer=facility_dot_detector__pb2.WriteStatusResp.FromString,
        )


class DetectorSrvServicer(object):
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

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DetectorSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=facility_dot_detector__pb2.FindDetectorReq.FromString,
          response_serializer=facility_dot_detector__pb2.FindDetectorResp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=facility_dot_detector__pb2.GetDetectorReq.FromString,
          response_serializer=facility_dot_detector__pb2.GetDetectorResp.SerializeToString,
      ),
      'Write': grpc.unary_unary_rpc_method_handler(
          servicer.Write,
          request_deserializer=facility_dot_detector__pb2.WriteDetectorReq.FromString,
          response_serializer=facility_dot_detector__pb2.WriteDetectorResp.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=facility_dot_detector__pb2.UpdateDetectorReq.FromString,
          response_serializer=facility_dot_detector__pb2.UpdateDetectorResp.SerializeToString,
      ),
      'FindStatus': grpc.unary_unary_rpc_method_handler(
          servicer.FindStatus,
          request_deserializer=facility_dot_detector__pb2.FindStatusReq.FromString,
          response_serializer=facility_dot_detector__pb2.FindStatusResp.SerializeToString,
      ),
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=facility_dot_detector__pb2.GetStatusReq.FromString,
          response_serializer=facility_dot_detector__pb2.GetStatusResp.SerializeToString,
      ),
      'WriteStatus': grpc.unary_unary_rpc_method_handler(
          servicer.WriteStatus,
          request_deserializer=facility_dot_detector__pb2.WriteStatusReq.FromString,
          response_serializer=facility_dot_detector__pb2.WriteStatusResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'facility.DetectorSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
