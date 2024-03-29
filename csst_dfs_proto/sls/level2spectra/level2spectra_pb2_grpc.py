# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import level2spectra_pb2 as sls_dot_level2spectra_dot_level2spectra__pb2


class Level2spectraSrvStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Find = channel.unary_unary(
                '/dfs.sls.level2spectra.Level2spectraSrv/Find',
                request_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraReq.SerializeToString,
                response_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraResp.FromString,
                )
        self.Get = channel.unary_unary(
                '/dfs.sls.level2spectra.Level2spectraSrv/Get',
                request_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraReq.SerializeToString,
                response_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraResp.FromString,
                )
        self.Write = channel.stream_unary(
                '/dfs.sls.level2spectra.Level2spectraSrv/Write',
                request_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraReq.SerializeToString,
                response_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraResp.FromString,
                )
        self.UpdateQc2Status = channel.unary_unary(
                '/dfs.sls.level2spectra.Level2spectraSrv/UpdateQc2Status',
                request_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusReq.SerializeToString,
                response_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusResp.FromString,
                )
        self.UpdateProcStatus = channel.unary_unary(
                '/dfs.sls.level2spectra.Level2spectraSrv/UpdateProcStatus',
                request_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusReq.SerializeToString,
                response_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusResp.FromString,
                )


class Level2spectraSrvServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateQc2Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProcStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Level2spectraSrvServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraReq.FromString,
                    response_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraResp.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraReq.FromString,
                    response_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraResp.SerializeToString,
            ),
            'Write': grpc.stream_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraReq.FromString,
                    response_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraResp.SerializeToString,
            ),
            'UpdateQc2Status': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateQc2Status,
                    request_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusReq.FromString,
                    response_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusResp.SerializeToString,
            ),
            'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProcStatus,
                    request_deserializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusReq.FromString,
                    response_serializer=sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.sls.level2spectra.Level2spectraSrv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Level2spectraSrv(object):
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
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level2spectra.Level2spectraSrv/Find',
            sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraReq.SerializeToString,
            sls_dot_level2spectra_dot_level2spectra__pb2.FindLevel2spectraResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level2spectra.Level2spectraSrv/Get',
            sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraReq.SerializeToString,
            sls_dot_level2spectra_dot_level2spectra__pb2.GetLevel2spectraResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.sls.level2spectra.Level2spectraSrv/Write',
            sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraReq.SerializeToString,
            sls_dot_level2spectra_dot_level2spectra__pb2.WriteLevel2spectraResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateQc2Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level2spectra.Level2spectraSrv/UpdateQc2Status',
            sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusReq.SerializeToString,
            sls_dot_level2spectra_dot_level2spectra__pb2.UpdateQc2StatusResp.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level2spectra.Level2spectraSrv/UpdateProcStatus',
            sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusReq.SerializeToString,
            sls_dot_level2spectra_dot_level2spectra__pb2.UpdateProcStatusResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
