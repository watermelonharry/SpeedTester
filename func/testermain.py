# -*- coding: utf-8 -*-

"""
Module implementing testermain.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog, QApplication
import sys
from ui.Ui_testermain import Ui_Dialog
from showdata import showDataWindow
from base.statusDict import LOCAL_STATUS
from func.popWindow import NoticeWindow

class testermain(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
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
        self.status = LOCAL_STATUS.WAIT

    def Confirm(self, intArg):
        """
        确认窗口
        :param intArg:
        :return:确定返回True， 取消返回False
        """
        noticeWindow = NoticeWindow()
        noticeWindow.Confirm(intArg)
        return noticeWindow.status

    def verifyIp(self, ipStr):
        ip = str(ipStr).split('.')
        result =  len(ip) == 4 and len(filter(lambda x: x >= 0 and x <= 255, map(int, filter(lambda x:x.isdigit(), ip)))) == 4 and ip[0] != '0'
        if result is True:
            self.Confirm(1)
            return True
        else:
            self.Confirm(2)
            return False

    @pyqtSignature("")
    def on_startOneTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.verifyIp(self.remoteIpInput.text())

    @pyqtSignature("")
    def on_startAutoTestBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print('test for html')
        timeList = ['1:10','1:20','1:30','1:40']
        speedList = [20,100,30,10]
        self.updateChart(timeList, speedList)

    @pyqtSignature("")
    def on_showResultBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showWindow.webView.reload()
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
        pass

    @pyqtSignature("QTime")
    def on_gapTimeEdit_timeChanged(self, date):
        """
        Slot documentation goes here.

        @param date DESCRIPTION
        @type QTime
        """
        # TODO: not implemented yet
        pass

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
            <div id="main" style="width: 700px;height:450px;"></div>
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = testermain()
    myapp.show()
    sys.exit(app.exec_())
