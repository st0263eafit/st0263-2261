CC = gcc
ARGS = -Wall -O2 -I .

all: echoserver echoclient

echoserver: echoserver.c
	$(CC) $(ARGS) -o echoserver echoserver.c

echoclient: echoclient.c
	$(CC) $(ARGS) -o echoclient echoclient.c

clean:
	rm -f *.o echoserver echoclient *~

