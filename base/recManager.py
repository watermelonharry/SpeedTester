# -*- coding: utf-8 -*-

import threading
import time
import socket
from statusDict import LOCAL_STATUS as LOCAL_STATUS

class UdpClientThread(threading.Thread):
    def __init__(self, remoteIP='localhost', remotePort = 10230, bufferSize = 102400):
        threading.Thread.__init__(self)

        self.STATUS = LOCAL_STATUS.WAIT
        self.remoteIp = str(remoteIP)
        self.remotePort = int(remotePort)
        self.bufferSize = bufferSize
        self.beginTime = time.time()
        self.endTime = self.beginTime
        self.dataSize = 0
        self.costMS = 0

        try:
            self.remoteAddr = (self.remoteIp, self.remotePort)
            self.udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udpClient.settimeout(5)
        except Exception as e:
            print(e.message)
            self.STATUS = LOCAL_STATUS.ERROR
            self.remoteAddr = None

    def run(self):
        print('client RUNNNIG.')
        while(True):

            if self.STATUS is LOCAL_STATUS.READY:
                #开始测试
                #reset时间
                data, addr = self.udpClient.recvfrom(10)
                if data == 'R':
                    self.beginTime = time.time()
                    data, addr = self.udpClient.recvfrom(self.bufferSize)
                    self.endTime = time.time()
                    self.dataSize = len(data)
                    self.costMS = (self.endTime-self.beginTime-0.0001)*1000

                    print('test END:', str(self.dataSize) + 'Byte', 'time-'+str(self.costMS)+' ms')
                    self.STATUS = LOCAL_STATUS.END

                else:
                    print('RESET ERROR, restart test')
                    self.STATUS = LOCAL_STATUS.ERROR
                    break


            if self.STATUS is LOCAL_STATUS.WAIT:
                #确认对方在线
                #todo:需要加try包围，在无remote在线时会报error 100054
                self.udpClient.sendto('S', self.remoteAddr)
                try:
                    data, addr = self.udpClient.recvfrom(10)
                except Exception as e:
                    if e.errno == 10054:
                        print('server unreachable, check ip&port.')
                    else:
                        print('other error:', e)
                    self.STATUS = LOCAL_STATUS.ERROR
                    break

                if data == 'A':
                    print('status-wait, recv:', data, addr)
                    self.STATUS = LOCAL_STATUS.READY
                else:
                    print('status-error: remote IP not online')
                    self.STATUS = LOCAL_STATUS.ERROR

            if self.STATUS is LOCAL_STATUS.END:
                #结束进程，清理
                print('test end.')
                break

            if self.STATUS is LOCAL_STATUS.ERROR:
                print('client ERROR, restart test')
                break
        # 结束进程，清理
        self.udpClient.close()
        time.sleep(0.5)
        del self.udpClient
        self.udpClient = None

    def getStatus(self):
        return self.STATUS

if __name__ == '__main__':
    udptest = UdpClientThread()
    udptest.start()
    udptest.join()
    print('main thread end')