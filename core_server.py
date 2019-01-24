#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :core_server.py
#@Software  :PyCharm
from park_test import car
from park_test import parkingRecord
from park_test import customer
from park_test import parking
from park_test import parkingLot
import time
#import math


#计算应缴费用
def need_pay(begin_time, end_time):
    #正常按小时算的方式，此处采用按秒方便测试
    #return math.ceil((end_time - begin_time) / 60 / 60) * 5
    return (end_time - begin_time) * 5


#提取订单
def get_record(car_instance, park_instance):
    if car_instance.car_id == park_instance.car_id:
        if park_instance.stop_time != 0 and park_instance.move_time != 0:
            starts = park_instance.stop_time
            ends = park_instance.move_time
        else:
            starts = park_instance.in_time
            ends = park_instance.leave_time
        how_much = need_pay(starts, ends)
    else:
        print("获取订单错误")
    begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starts))
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ends))
    record = {'车牌号：': park_instance.car_id, '开始计费时间：': begin_time, '结束计费时间：': end_time, '需要缴纳费用：': how_much}
    return record


#获取时间
def get_time():
    return int(time.time())


#运算缴费
def pay(how_much):
    money = int(input("交费："))
    if how_much == money:
        print('谢谢')
    elif how_much > money:
        how_much = how_much - money
        print('还需缴费' + str(how_much) + '元')
        pay(how_much)
    elif how_much < money:
        money = money - how_much
        print('找零' + str(money) + '元,谢谢')


num = 0


#模拟
def test():
    # 1. 车主开车进入停车场，产生停车记录
    car_instance = car.Car('辽A88888', '#00ffff', '法拉利')
    customer_instance = customer.Customer(car_instance.car_id, '13012340000', '21010410000101xxxx')
    global num
    num += 1
    parking_instance = parking.Parking('xx停车场', num)
    park_record_instance = parkingRecord.ParkingRecord(car_instance.car_id)
    park_record_instance.get_in_time(get_time())
    # 2. 车主开车继续向前，将车停到车位上，修改前面的停车记录
    time.sleep(2)
    parkingLot.ParkLot("1-12-1", parking_instance.park_id, car_instance.car_id)
    park_record_instance.get_stop_time(get_time())
    # 3. 车主停车完成
    # 一段时间(购物、吃饭...)之后，车主驾车准备离开停车场
    time.sleep(5)
    # 4. 车主开车离开车位，修改停车记录
    park_record_instance.get_move_time(get_time())
    # 5. 车主开车到达出口，系统根据停车的时间生成订单
    park_record_instance.get_leave_time(get_time())
    record = get_record(car_instance, park_record_instance)
    print(str(record))
    # 6. 车主缴纳停车费
    how_much = record['需要缴纳费用：']
    pay(how_much)
    # 7. 车主离开停车场


test()
