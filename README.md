# DS-assignment1
Programming assignment 1 for Distributed Systems class - Spring 2020 at University of Colorado at Boulder

# Steps to setup the project

* Clone this repository
* Go to the grpc_meta folder and do a ```pip3 install -r requirements.txt```. This installs all the grpc tools and libraries.
* Run the grpc server file using ```python3 grpc_server.py```
* Run the grpc client stating the host ip and a filename to store the metrics. An example command ```python3 grpc_client.py --host 127.0.0.1 --filename metrics.pickle```
* Follow the same steps for the UDP folder.

