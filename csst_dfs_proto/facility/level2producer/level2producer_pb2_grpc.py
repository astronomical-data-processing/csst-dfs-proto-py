# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import level2producer_pb2 as facility_dot_level2producer_dot_level2producer__pb2


class Level2ProducerSrvStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Register = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/Register',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.RegisterReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.RegisterResp.FromString,
        )
    self.Find = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/Find',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindResp.FromString,
        )
    self.FindNexts = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/FindNexts',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindNextsReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindNextsResp.FromString,
        )
    self.FindStart = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/FindStart',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindStartReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindStartResp.FromString,
        )
    self.Get = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/Get',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetResp.FromString,
        )
    self.Update = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/Update',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateResp.FromString,
        )
    self.Delete = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/Delete',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.DeleteReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.DeleteResp.FromString,
        )
    self.NewJob = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/NewJob',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.NewJobReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.NewJobResp.FromString,
        )
    self.GetJob = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/GetJob',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetJobReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetJobResp.FromString,
        )
    self.UpdateJob = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/UpdateJob',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateJobReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateJobResp.FromString,
        )
    self.WriteRunning = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/WriteRunning',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.WriteRunningReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.WriteRunningResp.FromString,
        )
    self.GetRunning = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/GetRunning',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetRunningReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetRunningResp.FromString,
        )
    self.UpdateRunning = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/UpdateRunning',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateRunningReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateRunningResp.FromString,
        )
    self.FindRunning = channel.unary_unary(
        '/dfs.facility.level2producer.Level2ProducerSrv/FindRunning',
        request_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindRunningReq.SerializeToString,
        response_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindRunningResp.FromString,
        )


class Level2ProducerSrvServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Register(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Find(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindNexts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindStart(self, request, context):
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

  def Update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NewJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteRunning(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetRunning(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateRunning(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FindRunning(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Level2ProducerSrvServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Register': grpc.unary_unary_rpc_method_handler(
          servicer.Register,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.RegisterReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.RegisterResp.SerializeToString,
      ),
      'Find': grpc.unary_unary_rpc_method_handler(
          servicer.Find,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindResp.SerializeToString,
      ),
      'FindNexts': grpc.unary_unary_rpc_method_handler(
          servicer.FindNexts,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindNextsReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindNextsResp.SerializeToString,
      ),
      'FindStart': grpc.unary_unary_rpc_method_handler(
          servicer.FindStart,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindStartReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindStartResp.SerializeToString,
      ),
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetResp.SerializeToString,
      ),
      'Update': grpc.unary_unary_rpc_method_handler(
          servicer.Update,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateResp.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.DeleteReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.DeleteResp.SerializeToString,
      ),
      'NewJob': grpc.unary_unary_rpc_method_handler(
          servicer.NewJob,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.NewJobReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.NewJobResp.SerializeToString,
      ),
      'GetJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetJobReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetJobResp.SerializeToString,
      ),
      'UpdateJob': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateJob,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateJobReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateJobResp.SerializeToString,
      ),
      'WriteRunning': grpc.unary_unary_rpc_method_handler(
          servicer.WriteRunning,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.WriteRunningReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.WriteRunningResp.SerializeToString,
      ),
      'GetRunning': grpc.unary_unary_rpc_method_handler(
          servicer.GetRunning,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.GetRunningReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.GetRunningResp.SerializeToString,
      ),
      'UpdateRunning': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateRunning,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateRunningReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.UpdateRunningResp.SerializeToString,
      ),
      'FindRunning': grpc.unary_unary_rpc_method_handler(
          servicer.FindRunning,
          request_deserializer=facility_dot_level2producer_dot_level2producer__pb2.FindRunningReq.FromString,
          response_serializer=facility_dot_level2producer_dot_level2producer__pb2.FindRunningResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dfs.facility.level2producer.Level2ProducerSrv', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
