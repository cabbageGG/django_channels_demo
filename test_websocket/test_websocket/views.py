#-*- coding: utf-8 -*-

__author__ = 'liyangjin'
__time__ = '2018/1/24 16:43'

def channels_example(request):
    import uwsgi
    uwsgi.websocket_handshake()   #与客户端建立连接 ，在uwsgi2.0中，这个函数不需要参数
    while True:
        msg = uwsgi.websocket_recv()  #阻塞，等待客户端发来的消息
        uwsgi.websocket_send(msg)     #发送消息到客服端
