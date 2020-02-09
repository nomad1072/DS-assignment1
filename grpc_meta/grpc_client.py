import json
import time
import random
import grpc
import argparse
import io
import pickle

from grpc_files import message_pb2
from grpc_files import message_pb2_grpc
from concurrent import futures
from common.time import getFormattedTime


def main(host, filename):
    with grpc.insecure_channel(host+':50051') as channel:
        stub = message_pb2_grpc.EchoStub(channel)

        time_list = list()

        for i in range(0, 120):
            d = dict()
            client_start_time = getFormattedTime()
            response = stub.accept(message_pb2.Request(message="Request sent"))
            client_end_time = getFormattedTime()

            d["client_send_time"] = client_start_time
            d["client_end_time"] = client_end_time
            d["server_start_time"] = response.serveraccepttime
            d["server_end_time"] = response.serversendtime

            time.sleep(60)
            time_list.append(d)
        
        with open(filename, 'wb') as handle:
            pickle.dump(time_list, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--host', default='127.0.0.1', help='The IP of the host')
    parser.add_argument(
        '--filename',
        default="default_grpc_file.pickle",
        help='Name of the file')
    
    args = parser.parse_args()

    main(args.host, args.filename)
