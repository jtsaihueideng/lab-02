# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Julie Deng
- Ellen Ko

## Lab Question Answers

Answer for Question 1: 

UDP reliability's decreased when we added the 50% loss to the local environment. Some of the the numbers didn't come through. 
This occurred because UDP is a "best effort" delivery protocol. It doesn't guarantee that the packets are delivered to the
destination.

Answer for Question 2:

The reliability of TCP still remained the same because all the numbers still went through. This occurred because TCP ensures
that packets are delivered to the destination. Thus, all the numbers went through.

Answer for Question 3:

The speed of TCP response reduced. This is due to the TCP taking time to recover and acknowledge the message to make sure it's not lost.


Answer for Question 1:

The variable argc is argument count. The array *argv[] is a pointer array which points to each argument passed to the program.

Answer for Question 2:

A file descriptor is a unique number that uniquely identifies an open file in a computer's operating system. A file descriptor
table is the collection of integer array indices that are file descriptors in which elements are pointers to file table entries.

Answer for Question 3:

A struct is a composite data type declaration that defines a physically grouped list of variables under one name in a block of memory.
The structure of sockaddr_in composes of a short variable, an unsigned short variable, a struct in_addr, and a char array with a size of 8
grouped in one block of memory.

Answer for Question 4:

The input parameters of socket() are three integers, which represent the domain, type, and protocol. The return type of socket() is an integer, which
is the socket file descriptor. The domain specifies the communications domain in which a socket is to be created. The type specifies the type of 
socket to be created. The protocol specifies a particular protocol to be used with the socket. 

Answer for Question 5: 

The input parameters of bind() include an integer, a struct sockaddr pointer, and a socklen_t, which represent the socket, address, and address_len,
respectively. The variable socket is the socket descriptor returned by a previous socket call. The pointer sockaddr points to a buffer containing the
name to be bound to the socket parameter. The address_len parameter is the size, in bytes, of the buffer pointed to by the address pointer.

The input parameters of listen() include two integer parameters (s and backlog). The s variable is a descriptor identifying a bound, unconnected socket.
The backlog variable is the maximum length that the queue of pending connections may grow to. If the value is SOMAXCONN, then the underlying service provider responsible for socket s sets the backlog to a maximum "reasonable" value.

Answer for Question 6:



Answer for Question 7:

The command fork() creates a new child process that runs in sync with its parent process and returns 0 if child process is created successfully. 
Whenever a new client connects to the server, a fork() call is executed making a new child process for each new client. This command can be applied 
to this assignment to create a concurrent server and handle multiple clients. 

