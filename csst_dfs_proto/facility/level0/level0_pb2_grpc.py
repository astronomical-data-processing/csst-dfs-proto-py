# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import level0_pb2 as facility_dot_level0_dot_level0__pb2


class Level0SrvStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Find = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/Find',
                request_serializer=facility_dot_level0_dot_level0__pb2.FindLevel0DataReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.FindLevel0DataResp.FromString,
                )
        self.FindByBrickIds = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/FindByBrickIds',
                request_serializer=facility_dot_level0_dot_level0__pb2.FindByBrickIdsReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.FindByBrickIdsResp.FromString,
                )
        self.Get = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/Get',
                request_serializer=facility_dot_level0_dot_level0__pb2.GetLevel0DataReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.GetLevel0DataResp.FromString,
                )
        self.Write = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/Write',
                request_serializer=facility_dot_level0_dot_level0__pb2.WriteLevel0DataReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.WriteLevel0DataResp.FromString,
                )
        self.UpdateQc0Status = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/UpdateQc0Status',
                request_serializer=facility_dot_level0_dot_level0__pb2.UpdateQc0StatusReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.UpdateQc0StatusResp.FromString,
                )
        self.UpdateProcStatus = channel.unary_unary(
                '/dfs.facility.level0.Level0Srv/UpdateProcStatus',
                request_serializer=facility_dot_level0_dot_level0__pb2.UpdateProcStatusReq.SerializeToString,
                response_deserializer=facility_dot_level0_dot_level0__pb2.UpdateProcStatusResp.FromString,
                )


class Level0SrvServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindByBrickIds(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateQc0Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProcStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Level0SrvServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.FindLevel0DataReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.FindLevel0DataResp.SerializeToString,
            ),
            'FindByBrickIds': grpc.unary_unary_rpc_method_handler(
                    servicer.FindByBrickIds,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.FindByBrickIdsReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.FindByBrickIdsResp.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.GetLevel0DataReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.GetLevel0DataResp.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.WriteLevel0DataReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.WriteLevel0DataResp.SerializeToString,
            ),
            'UpdateQc0Status': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateQc0Status,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.UpdateQc0StatusReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.UpdateQc0StatusResp.SerializeToString,
            ),
            'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProcStatus,
                    request_deserializer=facility_dot_level0_dot_level0__pb2.UpdateProcStatusReq.FromString,
                    response_serializer=facility_dot_level0_dot_level0__pb2.UpdateProcStatusResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.facility.level0.Level0Srv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Level0Srv(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/Find',
            facility_dot_level0_dot_level0__pb2.FindLevel0DataReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.FindLevel0DataResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindByBrickIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/FindByBrickIds',
            facility_dot_level0_dot_level0__pb2.FindByBrickIdsReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.FindByBrickIdsResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/Get',
            facility_dot_level0_dot_level0__pb2.GetLevel0DataReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.GetLevel0DataResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/Write',
            facility_dot_level0_dot_level0__pb2.WriteLevel0DataReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.WriteLevel0DataResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateQc0Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/UpdateQc0Status',
            facility_dot_level0_dot_level0__pb2.UpdateQc0StatusReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.UpdateQc0StatusResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProcStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.level0.Level0Srv/UpdateProcStatus',
            facility_dot_level0_dot_level0__pb2.UpdateProcStatusReq.SerializeToString,
            facility_dot_level0_dot_level0__pb2.UpdateProcStatusResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
