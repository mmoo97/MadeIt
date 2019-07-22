import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('ec2-54-80-18-12.compute-1.amazonaws.com', 8080))
client.send("I am the client\n")
from_server = client.recv(4096)
client.close()

print('this is from the server')
