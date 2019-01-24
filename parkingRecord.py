#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :parkingRecord.py
#@Software  :PyCharm


#停车记录对象
class ParkingRecord(object):
    def __init__(self, car_id):
        self.car_id = car_id
        self.in_time = 0
        self.stop_time = 0
        self.move_time = 0
        self.leave_time = 0

    def get_in_time(self, times):
        self.in_time = times

    def get_stop_time(self, times):
        self.stop_time = times

    def get_move_time(self, times):
        self.move_time = times

    def get_leave_time(self, times):
        self.leave_time = times
