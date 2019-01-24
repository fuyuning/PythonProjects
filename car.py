#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :car.py
#@Software  :PyCharm


class Car(object):
    #车的牌照，颜色，厂商
    def __init__(self, car_id, color, brand):
        self.car_id = car_id
        self.color = color
        self.brand = brand
