# -*- coding: utf-8 -*-

import threading
import time
import socket
from statusDict import LOCAL_STATUS as LOCAL_STATUS
from statusDict import REMOTE_STATUS as SERVER_STATUS

class UdpRemoteThread(threading.Thread):
    def __init__(self, LocalIP = 'localhost', LocalPort = 10230, bufferSize = 102400):
        threading.Thread.__init__(self)

        self.STATUS = SERVER_STATUS.WAIT
        self.localIp = str(LocalIP)
        self.localPort = int(LocalPort)
        self.bufferSize = bufferSize
        self.beginTime = time.time()
        self.endTime = self.beginTime
        self.dataSize = 0
        self.clientAddr = None
        self.udpServer = None

        try:
            Addr = (self.localIp, self.localPort)
            self.udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # self.udpServer.settimeout(5)
            self.udpServer.bind(Addr)
        except Exception as e:
            print(e.message)
            self.STATUS = SERVER_STATUS.ERROR

    def run(self):
        print('server run@ ', self.localIp, self.localPort)
        dataPack = None
        while(self.STATUS is not SERVER_STATUS.ERROR):

            if self.STATUS is SERVER_STATUS.WAIT:
                print('server wait.')
                #开启监听
                try:
                    data, self.clientAddr = self.udpServer.recvfrom(10)
                except Exception as e:
                    if e.errno == 10054:
                        print('error: no client.')
                    else:
                        print('other error: ', e)
                    self.STATUS = SERVER_STATUS.ERROR

                #todo:超时
                if data == 'S':
                    #确认回复
                    print('status-wait,SYN data recev:', data, self.clientAddr)
                    dataPack = 'T'* 50000
                    time.sleep(6)
                    self.udpServer.sendto('A', self.clientAddr)
                    self.STATUS = SERVER_STATUS.START
                else:
                    print('status-wait, UNKNOWN data recev:', data, self.clientAddr)
                    self.STATUS = LOCAL_STATUS.ERROR

            if self.STATUS is SERVER_STATUS.START:
                print('test begin.')
                #开始发包
                #RESET
                self.udpServer.sendto('R',self.clientAddr)
                time.sleep(0.0001)
                #dataPack
                self.udpServer.sendto(dataPack, self.clientAddr)
                self.STATUS = SERVER_STATUS.END

            if self.STATUS is SERVER_STATUS.END:
                print('test end')
                time.sleep(0.5)
                self.STATUS = SERVER_STATUS.WAIT
                self.clientAddr = None
    
            if self.STATUS is LOCAL_STATUS.ERROR:
                print('server ERROR:please check params')
                break
        self.udpServer.close()
        del self.udpServer
        print('server shutdown')

if __name__ == '__main__':
    udptest = UdpRemoteThread()
    udptest.start()

    inCmd = raw_input()
    while(inCmd != 'end'):
        inCmd = raw_input()
    udptest.udpServer.close()
