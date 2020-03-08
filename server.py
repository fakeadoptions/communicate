import socket
import os
import sys
import struct

def socket_service_image():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', 8080))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    count=0
    print("Wait for Connection.....................")

    while True:
        sock, addr = s.accept()
        deal_image(sock, addr,count)
        count=count+1
def deal_image(sock, addr,count):
    print("Accept connection from {0}".format(addr))
    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
          #  new_filename = os.path.join('./', 'new_' + fn)
            new_filename = os.path.join('./', str(count) + '.jpg')
            recvd_size = 0
            fp = open(new_filename, 'wb')
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
        sock.close()
        break

if __name__ == '__main__':
    socket_service_image()