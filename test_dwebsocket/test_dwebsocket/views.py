#-*- coding: utf-8 -*-

__author__ = 'liyangjin'
__time__ = '2018/1/24 16:43'

		
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from django.http import HttpResponse


@accept_websocket
def echo(request):
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render("hello")
    else:
        for message in request.websocket:
            request.websocket.send(message)#发送消息到客户端
