# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from spacemesh.v1 import tx_types_pb2 as spacemesh_dot_v1_dot_tx__types__pb2


class TransactionServiceStub(object):
    """Provides clients a way to submit a tx to the network for processing, and to
    check or follow the "journey" of a tx from mempool to block inclusion to
    mesh to STF processing. This service is separate from the Mesh and
    GlobalState services because txs move across both.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubmitTransaction = channel.unary_unary(
                '/spacemesh.v1.TransactionService/SubmitTransaction',
                request_serializer=spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionResponse.FromString,
                )
        self.TransactionsState = channel.unary_unary(
                '/spacemesh.v1.TransactionService/TransactionsState',
                request_serializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateResponse.FromString,
                )
        self.TransactionsStateStream = channel.unary_stream(
                '/spacemesh.v1.TransactionService/TransactionsStateStream',
                request_serializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamRequest.SerializeToString,
                response_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamResponse.FromString,
                )


class TransactionServiceServicer(object):
    """Provides clients a way to submit a tx to the network for processing, and to
    check or follow the "journey" of a tx from mempool to block inclusion to
    mesh to STF processing. This service is separate from the Mesh and
    GlobalState services because txs move across both.
    """

    def SubmitTransaction(self, request, context):
        """Submit a new tx to the node for processing. The response
        TransactionState message contains both the txid of the new tx, as well
        as whether or not it was admitted into the mempool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransactionsState(self, request, context):
        """Returns current tx state for one or more txs which indicates if a tx is
        on the mesh, on its way to the mesh or was rejected and will never get
        to the mesh
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransactionsStateStream(self, request, context):
        """//////// Streams
        Streams return live, new data as it becomes available to the node and
        not historical data.

        Returns tx state for one or more txs every time the tx state changes for
        one of these txs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubmitTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitTransaction,
                    request_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionResponse.SerializeToString,
            ),
            'TransactionsState': grpc.unary_unary_rpc_method_handler(
                    servicer.TransactionsState,
                    request_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateResponse.SerializeToString,
            ),
            'TransactionsStateStream': grpc.unary_stream_rpc_method_handler(
                    servicer.TransactionsStateStream,
                    request_deserializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamRequest.FromString,
                    response_serializer=spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spacemesh.v1.TransactionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TransactionService(object):
    """Provides clients a way to submit a tx to the network for processing, and to
    check or follow the "journey" of a tx from mempool to block inclusion to
    mesh to STF processing. This service is separate from the Mesh and
    GlobalState services because txs move across both.
    """

    @staticmethod
    def SubmitTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.TransactionService/SubmitTransaction',
            spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionRequest.SerializeToString,
            spacemesh_dot_v1_dot_tx__types__pb2.SubmitTransactionResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransactionsState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/spacemesh.v1.TransactionService/TransactionsState',
            spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateRequest.SerializeToString,
            spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransactionsStateStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/spacemesh.v1.TransactionService/TransactionsStateStream',
            spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamRequest.SerializeToString,
            spacemesh_dot_v1_dot_tx__types__pb2.TransactionsStateStreamResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
