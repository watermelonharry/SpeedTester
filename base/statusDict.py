# -*- coding: utf-8 -*-

class LocalStatus():
    """
    本地client状态类
    """
    def __init__(self):
        self.WAIT = 1
        self.READY = 2
        self.START = 3
        self.SUCCESS = 4
        self.ERROR = 5


class RemoteStatus():
    """
    远程Server状态类
    """
    def __init__(self):
        self.WAIT = 1
        self.START = 2
        self.END = 3
        self.ERROR = 4
        self.STOP = 5


class TestStatus():
    """
    窗口运行状态类
    """
    def __init__(self):
        self.IDLE = 1
        self.SINGLE_TEST = 2
        self.PLANNED_TEST = 3


LOCAL_STATUS = LocalStatus()
REMOTE_STATUS = RemoteStatus()
TEST_STATUS = TestStatus()

NOTICE_DICT = {
    0:u'无结果',
    1:u'IP验证通过，确认开始测试？',
    2:u'IP验证失败，请输入正确IP.'
}