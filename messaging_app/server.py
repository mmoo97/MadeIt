import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind is the ip the server creates and client connects to.
serv.bind(('ec2-54-80-18-12.compute-1.amazonaws.com', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print('this is from the client')
        conn.send("I am the SERVER\n")
    conn.close()
    print ('the client disconnected')
