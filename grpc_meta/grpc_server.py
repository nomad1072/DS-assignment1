import time
import json
import datetime
import argparse

from grpc_files import message_pb2
from grpc_files import message_pb2_grpc
from concurrent import futures
from common.time import getFormattedTime

import grpc

class MessageServicer(message_pb2_grpc.EchoServicer):

    def __init__(self):
        pass

    def  accept(self, request, context):
        try:
            server_time = getFormattedTime()
            message = request.message
            print('Message received from client: ', message)
            time.sleep(1)
            server_request_server_time = getFormattedTime()
            response = message_pb2.Response(serveraccepttime=server_time, serversendtime=server_request_server_time)
            return response
        except Exception as e:
            print(e)


def serve():
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_EchoServicer_to_server(MessageServicer(), server)
        server.add_insecure_port("[::]:50051")
        server.start()
        print('GRPC Server is Up!')
        try:
            while True:
                time.sleep(60*60*24)
        except KeyboardInterrupt:
            server.stop(0)
    except Exception as e:
        print('Exception: ', e)

if __name__ == "__main__":
    serve()