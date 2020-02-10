import socket
import sys
import pickle
import time
import argparse


from common.time import getFormattedTime

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = 'This is the message.  It will be repeated.'


def main(host, filename):
    server_address = (host, 10000)
    try:
        time_list = list()
        for i in range(0, 120):
            d = dict()
            print('Sending message! %s ' % (message))
            client_start_time = getFormattedTime()
            sent = sock.sendto(pickle.dumps(message), server_address)

            print('Receive response')
            data, server = sock.recvfrom(4096)
            transfer = pickle.loads(data)
            client_end_time = getFormattedTime()
            print('Transfer: ', transfer)
            d["client_send_time"] = client_start_time
            d["client_end_time"] = client_end_time
            d["server_start_time"] = transfer["server_start"]
            d["server_end_time"] = transfer["server_end"]
            time.sleep(60)
            time_list.append(d)
        
        with open(filename, 'wb') as handle:
            pickle.dump(time_list, handle, protocol=pickle.HIGHEST_PROTOCOL)

    finally:
        print('CLosing socket')
        sock.close()


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