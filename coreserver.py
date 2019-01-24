#Author     :LuciferMorningStar
#-*- coding:utf8 -*
#@Time      :19-1-24 
#@Author    :LuciferMorningStar
#@Site      :
#@file      :coreserver.py
#@Software  :PyCharm
from parkprojecttest import car as c
from parkprojecttest import parkingRecord as pr
from parkprojecttest import customer as cu
from parkprojecttest import parking as p
from parkprojecttest import parkingLot as pl
import time
import math


#计算应缴费用
def need_pay(time1, time2):
    #正常按小时算的方式，此处采用按秒方便测试
    #return math.ceil((time2 - time1) / 60 / 60) * 5
    return (time2 - time1) * 5


#提取订单
def get_record(car, park):
    if car.cid == park.cid:
        i = park.in_time
        s = park.stop_time
        m = park.move_time
        le = park.leave_time
        if s != 0 and m != 0:
            st = s
            en = m
        else:
            st = i
            en = le
        ne = need_pay(st, en)
    else:
        print("获取订单错误")
    st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(st))
    en = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(en))
    record = {'车牌号：': park.cid, '开始计费时间：': st, '结束计费时间：': en, '需要缴纳费用：': ne}
    return record


#获取时间
def get_time():
    return int(time.time())


#运算缴费
def pay(ne):
    money = int(input("交费："))
    if ne == money:
        print('谢谢')
    elif ne > money:
        ne = ne - money
        print('还需缴费' + str(ne) + '元')
        pay(ne)
    elif ne < money:
        money = money - ne
        print('找零' + str(money) + '元,谢谢')


num = 0


#模拟
def test():
    # 1. 车主开车进入停车场，产生停车记录
    car = c.Car('辽A88888', '#00ffff', '法拉利')
    cus = cu.Customer(car.cid, '13012340000', '21010410000101xxxx')
    global num
    num += 1
    par = p.Parking('xx停车场', num)
    park_re = pr.ParkingRecord(car.cid)
    park_re.get_in_time(get_time())
    # 2. 车主开车继续向前，将车停到车位上，修改前面的停车记录
    time.sleep(2)
    pl.ParkLot("1-12-1", par.pid, car.cid)
    park_re.get_stop_time(get_time())
    # 3. 车主停车完成
    # 一段时间(购物、吃饭...)之后，车主驾车准备离开停车场
    time.sleep(5)
    # 4. 车主开车离开车位，修改停车记录
    park_re.get_move_time(get_time())
    # 5. 车主开车到达出口，系统根据停车的时间生成订单
    park_re.get_leave_time(get_time())
    record = get_record(car, park_re)
    print(str(record))
    # 6. 车主缴纳停车费
    ne = record['需要缴纳费用：']
    pay(ne)
    # 7. 车主离开停车场


