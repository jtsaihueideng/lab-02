"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket
HOST = "172.20.10.4"  # The server's hostname or IP address
PORT = 10000

def main():



    # TODO: Create a socket and connect it to the server at the designated IP and port
    # TODO: Get user input and send it to the server using your TCP socket
    # TODO: Receive a response from the server and close the TCP connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      inp = input("Enter your message: ")
      arr = bytes(inp,'utf-8')  
      s.sendall(arr) 
      data = s.recv(1024) 
      print(data) 
    pass


if __name__ == '__main__':
    main()
