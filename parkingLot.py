#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :parkingLot.py
#@Software  :PyCharm


#车位对象
class ParkLot(object):
    def __init__(self, plid, pid, cid):
        self.plid = plid
        self.pid = pid
        self.cid = cid
