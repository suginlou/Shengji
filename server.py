import socket
from _thread import *


## Server IPv4 address, use a port that is not typically used for anything else
## Server is always running, receiving and sending data to clients
## The clients send 'move' data, which gives the characteristics of that player's game (e.g. size, position etc.)
## The client receive information on the other player's characteristics, in the form of lists (no. of players, position, time left in game etc.)
server = "192.168.1.6"
port = 5555

## Define s as the socket, the socket is the endpoint that is used to connect to the server, AF_INET is the connection type
## SOCK_STREAM is the way we are receiving information
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## We bind the server and port to the socket to set up an endpoint for that server
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

## The socket only listens for 2 players
s.listen(2)
print("Waiting for a connection, Server Started")

## Threading allows for multiple functions to run at one time. So in the case where we have a threaded function
## in the server script that looks for a connection from other clients, once it finds a connection from another client,
## it can create another thread to run the function for that client while scanning and creating new threads for new client connections
def threaded_client(conn):
    ## If a connection is made, then the server sends a string to confirm
    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            ## The server receives 2048 bits of information and decodes it to get the data in human readable format
            ## by decoding it. In this case we are just sending the data we receive back to the client
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            ## If we stop receiving data, then we tell that it is disconnected abd breaks the connection
            if not data:
                print("Disconnected")
                break
            ## If we do have data, we print the received data and that we are sending it back
            else:
                print("Received ", reply)
                print("Sending : ", reply)

            ## We encode the reply and send it back to the client
            conn.sendall(str.encode(reply))
        except:
            break

    ## If threaded clients close then we lose connection
    print("Lost Connection")
    conn.close()

## When the script runs, it looks for a connection and if it finds one, starts a threaded client using the function
while True:
    conn, addr = s.accept()
    print(conn)
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))