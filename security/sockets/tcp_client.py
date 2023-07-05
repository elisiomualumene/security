import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("Failled Connection ")
        print("ERROR: {} ".format(e))
        sys.exit()
    print("Socket created succefully ")


    TargetHost = str(input("Write the host or IP thats will be connected "))
    TargetPort = str(input("Write the port thats will be connected "))

    try:
        s.connect((TargetHost, int(TargetPort)))
        print("TCP Client connected succefully: HOST " + TargetHost + " PORT: " + TargetPort)
        s.shutdown(2)
    except socket.error as e:
        print("ERROR Trying to connect to Socket")
        print("ERROR {}".format(e))
        sys.exit()

if __name__ == "__main__":
    main()