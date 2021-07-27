"""Runs protoc with the gRPC plugin to generate messages and gRPC stubs."""

from grpc_tools import protoc

protoc.main((
    '',
    '-I./',
    '--python_out=.',
    '--grpc_python_out=.',
    './facility/observation/observation.proto',
))

protoc.main((
    '',
    '-I./',
    '--python_out=.',
    '--grpc_python_out=.',
    './facility/calmerge/calmerge.proto',
))

protoc.main((
    '',
    '-I./',
    '--python_out=.',
    '--grpc_python_out=.',
    './facility/level0/level0.proto',
))

protoc.main((
    '',
    '-I./',
    '--python_out=.',
    '--grpc_python_out=.',
    './facility/detector/detector.proto',
))


protoc.main((
    '',
    '-I./',
    '--python_out=.',
    '--grpc_python_out=.',
    './facility/level0prc/level0prc.proto',
))

