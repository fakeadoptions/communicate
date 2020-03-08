'''
Fuction：客户端发送图片和数据
Date：2018.9.8
Author：snowking
'''
###客户端client.py
import socket
import os
import sys
import struct
import time

def sock_client_image(filepath):
    #while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # s.connect(('服务器的ip', 6666))  #服务器和客户端在不同的系统或不同的主机下时使用的ip和端口，首先要查看服务器所在的系统网卡的ip
            s.connect(('123.56.246.118', 8080))  #服务器和客户端都在一个系统下时使用的ip和端口
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))
        #filepath = input('input the file: ')   #输入当前目录下的图片名 xxx.jpg
       # while True:
        #filepath=("input"+str(i)+".jpg")
        print(filepath)
        if os.path.exists(filepath):
       #     t=time.time()
       #     ntime=str(int(round(t*1000000)))
       #     s.send(bytes(ntime,encoding="utf-8"))
            fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(filepath).st_size)  #将xxx.jpg以128sq的格式打包
            s.send(fhead)
            fp = open(filepath, 'rb')  #打开要传输的图片
            while True:
                data = fp.read(1024) #读入图片数据
                if not data:
                    print('{0} send over...'.format(filepath))
                    break
                s.send(data)  #以二进制格式发送图片数据
            #s.close()
            #break    #循环发送
   
if __name__ == '__main__':
    for i in range(1,9964):
        sock_client_image((str(i).rjust(6,'0')+'.jpg'))