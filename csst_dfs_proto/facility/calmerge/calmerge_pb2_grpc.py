# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import calmerge_pb2 as facility_dot_calmerge_dot_calmerge__pb2


class CalMergeSrvStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Find = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/Find',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeReq.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeResp.FromString,
                )
        self.GetLatestByL0 = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/GetLatestByL0',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Req.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Resp.FromString,
                )
        self.Get = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/Get',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeReq.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeResp.FromString,
                )
        self.Write = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/Write',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeReq.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeResp.FromString,
                )
        self.UpdateQc1Status = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/UpdateQc1Status',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusReq.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusResp.FromString,
                )
        self.UpdateProcStatus = channel.unary_unary(
                '/dfs.facility.calmerge.CalMergeSrv/UpdateProcStatus',
                request_serializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusReq.SerializeToString,
                response_deserializer=facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusResp.FromString,
                )


class CalMergeSrvServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLatestByL0(self, request, context):
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

    def UpdateQc1Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProcStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
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
            'GetLatestByL0': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLatestByL0,
                    request_deserializer=facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Req.FromString,
                    response_serializer=facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Resp.SerializeToString,
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
            'dfs.facility.calmerge.CalMergeSrv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CalMergeSrv(object):
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
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/Find',
            facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeReq.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.FindCalMergeResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLatestByL0(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/GetLatestByL0',
            facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Req.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.GetLatestByL0Resp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/Get',
            facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeReq.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.GetCalMergeResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/Write',
            facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeReq.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.WriteCalMergeResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateQc1Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/UpdateQc1Status',
            facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusReq.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.UpdateQc1StatusResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dfs.facility.calmerge.CalMergeSrv/UpdateProcStatus',
            facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusReq.SerializeToString,
            facility_dot_calmerge_dot_calmerge__pb2.UpdateProcStatusResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
