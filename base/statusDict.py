# -*- coding: utf-8 -*-

class LocalStatus():
    def __init__(self):
        self.WAIT = 1
        self.READY = 2
        self.START = 3
        self.END = 4
        self.ERROR = 5


class RemoteStatus():
    def __init__(self):
        self.WAIT = 1
        self.START = 2
        self.END = 3
        self.ERROR = 4



LOCAL_STATUS = LocalStatus()
REMOTE_STATUS = RemoteStatus()

NOTICE_DICT = {
    0:u'无结果',
    1:u'IP验证通过，等待确认在线',
    2:u'IP验证失败，请输入正确IP'
}