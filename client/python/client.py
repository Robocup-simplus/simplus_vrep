from concurrent import futures
import logging

import grpc

import simplus_pb2
import simplus_pb2_grpc
import player


class Client(simplus_pb2_grpc.SimPlusServicer):

    def Start(self, request, context):
        response = simplus_pb2.TeamInfo()
        player.Start(request, response)
        return response

    def Action(self, request, context):
        response = simplus_pb2.Commands()
        for id, observation in enumerate(request.robots):
            cmd = simplus_pb2.Command(id=id)
            player.Play(id, request.server, observation, cmd)
            response.commands.append(cmd)
        return response

    def End(self, request, context):
        response = simplus_pb2.Result()
        player.End(request, response)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    simplus_pb2_grpc.add_SimPlusServicer_to_server(Client(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
