#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :parkingLot.py
#@Software  :PyCharm


#车位对象
class ParkLot(object):
    def __init__(self, park_lot_id, park_id, car_id):
        self.park_lot_id = park_lot_id
        self.park_id = park_id
        self.car_id = car_id
