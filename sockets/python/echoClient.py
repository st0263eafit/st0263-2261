#!/usr/bin/env python3
import socket
import sys, getopt

def main(argv):

   try:
      opts, args = getopt.getopt(argv,"Hh:p:",["host=","port="])
   except getopt.GetoptError:
      print ('yacurl.py -h <host> -p <port>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-H':
         print ('yacurl.py -h <host> -p <port>')
         sys.exit()
      elif opt in ("-h", "--host"):
         host = str(arg)
      elif opt in ("-p", "--port"):
         port = int(arg)
   return host,port

if __name__ == "__main__":

    host,port=main(sys.argv[1:])
    print ('Host ', host)
    print ('Port ', port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))