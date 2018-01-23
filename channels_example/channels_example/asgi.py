#-*- coding: utf-8 -*-

__author__ = 'liyangjin'
__time__ = '2018/1/21 20:41'

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channels_example.settings")    #这里填的是你的配置文件settings.py的位置
channel_layer = channels.asgi.get_channel_layer()