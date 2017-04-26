# -*- coding: utf-8 -*-

"""
Module implementing testermain.
"""

from PyQt4.QtCore import pyqtSignature, QThread, pyqtSignal, QTimer
from PyQt4.QtGui import QDialog, QApplication
import sys
from ui.Ui_testermain import Ui_Dialog, _translate
from showdata import showDataWindow
from base.statusDict import TEST_STATUS
from func.popWindow import NoticeWindow

class testermain(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    #用于上传线程中的测试结果
    updateSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(331, 229)
        self.showWindow = showDataWindow()
        self.status = TEST_STATUS.IDLE
        self.resultList = []  #保存测试结果
        self.updateSignal.connect(self.receiveTestData)
        self.tester = None
        self.timer = None #计时器QTimer

    def Confirm(self, intArg, strArg = None):
        """
        确认窗口
        :param intArg:
        :return:确定返回True， 取消返回False
        """
        noticeWindow = NoticeWindow()
        noticeWindow.Confirm(intArg, strArg)
        return noticeWindow.status

    def verifyIp(self, ipStr):
        ip = str(ipStr).split('.')
        result =  (len(ip) == 4 and len(filter(lambda x: x >= 0 and x <= 255, map(int, filter(lambda x:x.isdigit(), ip)))) == 4 and ip[0] != '0')
        if result is True:
            return self.Confirm(1)
        else:
            self.Confirm(2)
            return False

    @pyqtSignature("")
    def on_startOneTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.status is TEST_STATUS.IDLE:
            if self.verifyIp(self.remoteIpInput.text()):
                #todo：需要输入ip和port
                self.startOneTest()
                self.status = TEST_STATUS.SINGLE_TEST
        else:
            self.Confirm(2001)

    @pyqtSignature("")
    def on_startAutoTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.status is TEST_STATUS.IDLE:
            #空闲状态，开始测试并改变UI、status
            if self.Confirm(3001):
                self.startAutoTestBtn.setText(_translate("Dialog","关闭定时测试",None))
                self.status = TEST_STATUS.PLANNED_TEST

                # print('test for html')
                # timeList = ['1:10','1:20','1:30','1:40']
                # speedList = [20,100,30,10]
                # self.updateChart(timeList, speedList)

        elif self.status is TEST_STATUS.PLANNED_TEST:
            self.startAutoTestBtn.setText(_translate("Dialog","开始定时测试",None))
            self.status = TEST_STATUS.IDLE



    @pyqtSignature("")
    def on_clearResultBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        if self.status is TEST_STATUS.IDLE:
            if self.Confirm(4001):
                self.resultList = []
        else:
            self.Confirm(2001)


    @pyqtSignature("")
    def on_showResultBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # self.showWindow.webView.reload()
        self.showWindow.show()


    @pyqtSignature("")
    def on_remoteIpInput_returnPressed(self):
        """
        Slot documentation goes here.
        """
        pass

    @pyqtSignature("")
    def on_gapTimeEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('time edit finished')
        self.Confirm(5001, u'哈')
        print(self.gapTimeEdit.time())


    @pyqtSignature("QTime")
    def on_gapTimeEdit_timeChanged(self, date):
        """
        Slot documentation goes here.

        @param date DESCRIPTION
        @type QTime
        """
        # TODO: not implemented yet
        print('time changed')
        print(self.gapTimeEdit.time())

    def startOneTest(self, ip = 'localhost', port = 10230):
        # todo：需要输入ip和port
        self.tester = UdpTestManager(updateSignal=self.updateSignal)
        self.tester.start()

    def receiveTestData(self, dataTuple):
        self.resultList.append(dataTuple)
        print('main window recv: ', dataTuple)
        self.status = TEST_STATUS.IDLE
        del self.tester
        self.tester = None

    def updateChart(self, timeList, speedList):
        """
        用于更新数据至本地图表
        :param timeList: 时间列表，eg. ['1:10','1:20','1:30','1:40']
        :param speedList: 速度列表， eg. [20,100,30,10]
        :return:
        """
        timeList = ['\''+str(c)+'\'' for c in timeList]
        timeStr = ','.join(timeList)
        speedStr = ','.join([str(c) for c in speedList])
        content = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <script src="static/echarts.js"></script>
        </head>
        <body>
            <div id="main" style="width: 690px;height:430px;"></div>
            <script type="text/javascript">
                var myChart = echarts.init(document.getElementById('main'));
                option = {
                    title: {
                        text: '网速测试结果',
                        subtext: '@heyu'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data:['网速测试']
                    },
                    toolbox: {
                        show: true,
                        feature: {
                            dataZoom: {
                                yAxisIndex: 'none'
                            },
                            dataView: {readOnly: false},
                            magicType: {type: ['line', 'bar']},
                            restore: {},
                        }
                    },
                    xAxis:  {
                        type: 'category',
                        boundaryGap: false,
                        data: [%s]
                    },
                    yAxis: {
                        type: 'value',
                        axisLabel: {
                            formatter: '{value} Kbps'
                        }
                    },
                    series: [
                        {
                            name:'网速测试',
                            type:'line',
                            data:[%s],
                            markPoint: {
                                data: [
                                    {type: 'max', name: '最大值'},
                                    {type: 'min', name: '最小值'}
                                ]
                            },
                            markLine: {
                                data: [
                                    {type: 'average', name: '平均值'}
                                ]
                            }
                        }
                    ]
                    };
                myChart.setOption(option);
            </script>
        </body>
        </html>
        """ %(timeStr,speedStr)
        with open('echart/show.html','w') as file:
            file.writelines(content)
        self.showWindow.webView.reload()
        print timeStr,speedStr

import time
import socket
from base.statusDict import LOCAL_STATUS as LOCAL_STATUS

class UdpTestManager(QThread):
    """
    测速管理员，用于管理单次测速，格式化结果
    """
    innerSignal = pyqtSignal(object)

    def __init__(self, repeatTime = 5, remoteIP='localhost', remotePort = 10230, updateSignal = None, parent = None):
        super(UdpTestManager, self).__init__(parent)
        self.updateSignal = updateSignal
        self.remoteIP = remoteIP
        self.remotePort = remotePort

        self.repeatTime = repeatTime
        self.testTime = ''
        self.avrSpeed = 0

        self.resultList =[] #用于存储上报结果

        #用于传递至单次测速类
        self.innerSignal.connect(self.processTestData)

    def run(self):
        """
        运行类，根据repeatTime，重复测速，汇总测试数据
        :return:
        """
        #todo：循环测试类
        print('test manager start.')

        ts = time.gmtime()
        self.testTime = ':'.join(str(i) for i in [(ts.tm_hour + 8) % 24, ts.tm_min, ts.tm_sec])

        for i in range(self.repeatTime):
            singleTester = UdpClientQThread(self.remoteIP, self.remotePort,updateSignal=self.innerSignal)
            singleTester.start()
            while singleTester.isRunning():
                time.sleep(0.5)
            del singleTester
            print('test finish, no.' + str(i+1))

        self.sendToParent()

    def processTestData(self, dataTuple):
        """
        处理来自UdpThread的测试结果
        :param dataTuple: （FlagBool， timeStr， speedInt）
        :return:
        """
        #todo:处理类
        print('manager rec from client:', dataTuple)
        if dataTuple[0] is True:
            self.resultList.append(dataTuple[2])

    def sendToParent(self):
        """
        将处理结果发送给上层窗口类
        :param dataTuple: （FlagBool， timeStr， speedInt）
        :return:
        """
        #todo：发送类
        if len(self.resultList) >= 3:
            self.avrSpeed = sum(self.resultList) / len(self.resultList)
            self.updateSignal.emit((True, self.testTime, self.avrSpeed))
            print('manager: test success.')
        else:
            self.updateSignal.emit((False, '-', '0'))
            print('manager: test fail.')


class UdpClientQThread(QThread):
    """
    单次测速类
    """
    def __init__(self, remoteIP='localhost', remotePort = 10230, bufferSize = 102400, updateSignal = None, parent = None):
        super(UdpClientQThread, self).__init__(parent)
        # QThread.__init__(parent)
        self.STATUS = LOCAL_STATUS.WAIT
        self.remoteIp = str(remoteIP)
        self.remotePort = int(remotePort)
        self.bufferSize = bufferSize
        self.beginTime = time.time()
        self.endTime = self.beginTime
        self.dataSize = 0
        self.costMS = 0
        self.updateSignal = updateSignal

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

                    print('test FINISH:', str(self.dataSize) + 'Byte', 'time-'+str(self.costMS)+' ms')
                    self.STATUS = LOCAL_STATUS.SUCCESS

                else:
                    print('RESET ERROR, restart test')
                    self.STATUS = LOCAL_STATUS.ERROR
                    break


            elif self.STATUS is LOCAL_STATUS.WAIT:
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

            elif self.STATUS is LOCAL_STATUS.SUCCESS:
                #结束进程，清理
                break

            if self.STATUS is LOCAL_STATUS.ERROR:
                print('client ERROR, restart test')
                self.dataSize = 0
                self.costMS = 0
                break
        # 结束进程，清理
        self.udpClient.close()
        time.sleep(0.5)
        del self.udpClient
        self.udpClient = None
        self.sendToParent()

    def sendToParent(self):
        """
        发送测试数据至parent
        :return:
        datatuple: (successFlag, time, speed)
        """
        successFlag = self.STATUS is LOCAL_STATUS.SUCCESS
        if successFlag:
            timeStruct = time.gmtime(self.beginTime)
            timeStr = ':'.join( str(i) for i in [(timeStruct.tm_hour+8)%24, timeStruct.tm_min, timeStruct.tm_sec])
            speedInt = self.dataSize * 8 / self.costMS
        else:
            timeStr = '-'
            speedInt = 0
        self.updateSignal.emit((successFlag, timeStr, speedInt))


    def getStatus(self):
        return self.STATUS


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = testermain()
    myapp.show()
    sys.exit(app.exec_())
