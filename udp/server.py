import socket
import sys
import time
import argparse
import pickle

from common.time import getFormattedTime

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
print('Server started on port 10000')
sock.bind(server_address)

while True:
    print('Waiting to receive messages')
    data, address = sock.recvfrom(4096)

    print('Received %s bytes from %s' % (len(data), address))
    print('Data: ', data)
    server_start_time = getFormattedTime()
    time.sleep(1)
    if data:
        server_end_time = getFormattedTime()
        transfer = { 'server_start': server_start_time, 'server_end': server_end_time}
        sent = sock.sendto(pickle.dumps(transfer), address)
        print('Sent %s bytes back to %s' % (sent, address))