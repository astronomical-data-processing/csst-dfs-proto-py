# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import ephem_pb2 as common_dot_ephem_dot_ephem__pb2


class EphemSearchSrvStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Gaia3Search = channel.unary_stream(
                '/dfs.ephem.EphemSearchSrv/Gaia3Search',
                request_serializer=common_dot_ephem_dot_ephem__pb2.EphemSearchRequest.SerializeToString,
                response_deserializer=common_dot_ephem_dot_ephem__pb2.Gaia3SearchResponse.FromString,
                )


class EphemSearchSrvServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Gaia3Search(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EphemSearchSrvServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Gaia3Search': grpc.unary_stream_rpc_method_handler(
                    servicer.Gaia3Search,
                    request_deserializer=common_dot_ephem_dot_ephem__pb2.EphemSearchRequest.FromString,
                    response_serializer=common_dot_ephem_dot_ephem__pb2.Gaia3SearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'dfs.ephem.EphemSearchSrv', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EphemSearchSrv(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Gaia3Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/dfs.ephem.EphemSearchSrv/Gaia3Search',
            common_dot_ephem_dot_ephem__pb2.EphemSearchRequest.SerializeToString,
            common_dot_ephem_dot_ephem__pb2.Gaia3SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
