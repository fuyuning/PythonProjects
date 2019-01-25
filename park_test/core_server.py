#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :core_server.py
#@Software  :PyCharm
from park_test.car import Car
from park_test.parkingRecord import ParkingRecord
from park_test.customer import Customer
from park_test.parking import Parking
from park_test.parkingLot import ParkLot
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
    global starts
    global ends
    global how_much
    begin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(starts))
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ends))
    record = {'车牌号：': park_instance.car_id, '开始计费时间：': begin_time, '结束计费时间：': end_time,
              '需要缴纳费用：': how_much}
    return record


#获取时间
def get_time():
    return int(time.time())


#运算缴费
def pay(pay_money):
    money = int(input("交费："))
    if pay_money == money:
        print('谢谢')
    elif pay_money > money:
        pay_money -= money
        print('还需缴费' + str(pay_money) + '元')
        pay(pay_money)
    elif pay_money < money:
        money -= pay_money
        print('找零' + str(money) + '元,谢谢')


__num = 0


#模拟
def main():
    # 1. 车主开车进入停车场，产生停车记录
    car_instance = Car('辽A88888', '#00ffff', '法拉利')
    Customer(car_instance.car_id, '13012340000', '21010410000101xxxx')
    global __num
    __num += 1
    parking_instance = Parking('xx停车场', __num)
    park_record_instance = ParkingRecord(car_instance.car_id)
    park_record_instance.get_in_time(get_time())
    # 2. 车主开车继续向前，将车停到车位上，修改前面的停车记录
    time.sleep(2)
    ParkLot("1-12-1", parking_instance.park_id, car_instance.car_id)
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
    how_money = record['需要缴纳费用：']
    pay(how_money)
    # 7. 车主离开停车场


if __name__ == '__main__':
    main()
