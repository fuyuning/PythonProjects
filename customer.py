#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :customer.py
#@Software  :PyCharm


#车主对象:车牌号，电话，身份证
class Customer(object):
    def __init__(self, car_id, phone, id_card_no):
        self.car_id = car_id
        self.phone = phone
        self.id_card_no = id_card_no
