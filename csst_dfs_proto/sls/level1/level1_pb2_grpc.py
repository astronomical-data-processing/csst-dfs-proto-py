# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import level1_pb2 as sls_dot_level1_dot_level1__pb2


class Level1SrvStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Find = channel.unary_unary(
                '/dfs.sls.level1.Level1Srv/Find',
                request_serializer=sls_dot_level1_dot_level1__pb2.FindLevel1Req.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.FindLevel1Resp.FromString,
                )
        self.FindByBrickIds = channel.unary_unary(
                '/dfs.sls.level1.Level1Srv/FindByBrickIds',
                request_serializer=sls_dot_level1_dot_level1__pb2.FindByBrickIdsReq.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.FindByBrickIdsResp.FromString,
                )
        self.Get = channel.unary_unary(
                '/dfs.sls.level1.Level1Srv/Get',
                request_serializer=sls_dot_level1_dot_level1__pb2.GetLevel1Req.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.GetLevel1Resp.FromString,
                )
        self.Write = channel.stream_unary(
                '/dfs.sls.level1.Level1Srv/Write',
                request_serializer=sls_dot_level1_dot_level1__pb2.WriteLevel1Req.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.WriteLevel1Resp.FromString,
                )
        self.UpdateQc1Status = channel.unary_unary(
                '/dfs.sls.level1.Level1Srv/UpdateQc1Status',
                request_serializer=sls_dot_level1_dot_level1__pb2.UpdateQc1StatusReq.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.UpdateQc1StatusResp.FromString,
                )
        self.UpdateProcStatus = channel.unary_unary(
                '/dfs.sls.level1.Level1Srv/UpdateProcStatus',
                request_serializer=sls_dot_level1_dot_level1__pb2.UpdateProcStatusReq.SerializeToString,
                response_deserializer=sls_dot_level1_dot_level1__pb2.UpdateProcStatusResp.FromString,
                )


class Level1SrvServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Find(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindByBrickIds(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateQc1Status(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProcStatus(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Level1SrvServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Find': grpc.unary_unary_rpc_method_handler(
                    servicer.Find,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.FindLevel1Req.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.FindLevel1Resp.SerializeToString,
            ),
            'FindByBrickIds': grpc.unary_unary_rpc_method_handler(
                    servicer.FindByBrickIds,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.FindByBrickIdsReq.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.FindByBrickIdsResp.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.GetLevel1Req.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.GetLevel1Resp.SerializeToString,
            ),
            'Write': grpc.stream_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.WriteLevel1Req.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.WriteLevel1Resp.SerializeToString,
            ),
            'UpdateQc1Status': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateQc1Status,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.UpdateQc1StatusReq.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.UpdateQc1StatusResp.SerializeToString,
            ),
            'UpdateProcStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProcStatus,
                    request_deserializer=sls_dot_level1_dot_level1__pb2.UpdateProcStatusReq.FromString,
                    response_serializer=sls_dot_level1_dot_level1__pb2.UpdateProcStatusResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.sls.level1.Level1Srv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Level1Srv(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Find(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level1.Level1Srv/Find',
            sls_dot_level1_dot_level1__pb2.FindLevel1Req.SerializeToString,
            sls_dot_level1_dot_level1__pb2.FindLevel1Resp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindByBrickIds(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level1.Level1Srv/FindByBrickIds',
            sls_dot_level1_dot_level1__pb2.FindByBrickIdsReq.SerializeToString,
            sls_dot_level1_dot_level1__pb2.FindByBrickIdsResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level1.Level1Srv/Get',
            sls_dot_level1_dot_level1__pb2.GetLevel1Req.SerializeToString,
            sls_dot_level1_dot_level1__pb2.GetLevel1Resp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/dfs.sls.level1.Level1Srv/Write',
            sls_dot_level1_dot_level1__pb2.WriteLevel1Req.SerializeToString,
            sls_dot_level1_dot_level1__pb2.WriteLevel1Resp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateQc1Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level1.Level1Srv/UpdateQc1Status',
            sls_dot_level1_dot_level1__pb2.UpdateQc1StatusReq.SerializeToString,
            sls_dot_level1_dot_level1__pb2.UpdateQc1StatusResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProcStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/dfs.sls.level1.Level1Srv/UpdateProcStatus',
            sls_dot_level1_dot_level1__pb2.UpdateProcStatusReq.SerializeToString,
            sls_dot_level1_dot_level1__pb2.UpdateProcStatusResp.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
