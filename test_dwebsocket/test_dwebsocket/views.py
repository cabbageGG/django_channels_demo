#-*- coding: utf-8 -*-

__author__ = 'liyangjin'
__time__ = '2018/1/24 16:43'

		
from dwebsocket import require_websocket

@require_websocket
def channels_example(request):
    message = request.websocket.wait()
    request.websocket.send(message)
