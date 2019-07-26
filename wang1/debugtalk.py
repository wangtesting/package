# coding=utf-8
import uuid
import random
# import pymysql
import json
# import cx_Oracle
import string
import re
import json
import time
import hashlib
import datetime

base_url = "https://playinair.com"

def get_base_url():
    return base_url

# 获取cookie
def get_cookie(Cookie):
    A=Cookie
    b=A.split(';')[0].split('=')[1]
    print(b)
    return str(b)
# get_cookie("SESSION=94eb2f75-3b00-4def-bf1a-bb33382f049e;")

#
# # 获取cookie
# def get_cookie(cookie):
#     B =cookie.split(';')[0]
#     # C=B.split("=")[1]
#     # D="".join(B)+"".join(';')+"SESSION="+"".join(C)
#     # print(D)
#     return B
# get_cookie("ZF_COOKIE=59f551ed-dab5-4ed1-ae56-69efcaa6a39e; Domain=.anhouse.com.cn; Expires=Sat, 29-Dec-2018 12:59:56 GMT; Path=/; HttpOnly")



# accountId=$accountId
#
# def setStudentNumber(accountId):
#      global STUDENT_NUMBER
#      STUDENT_NUMBER = accountId
#      return STUDENT_NUMBER

def a(accountId):
    return accountId







# 小区名称
def new_community_name():
    name = '王文小区'
    list = [random.choice(string.digits + string.ascii_letters)]
    str = ''.join(list)
    new_name =  name + str + get_timestamp()
    print('接入方系统名称：{}'.format(new_name))
    return new_name



# 套餐名称
def new_memo():
    name = '王文新增套餐memo'
    list = [random.choice(string.digits + string.ascii_letters)]
    str = ''.join(list)
    new_name =  name + str
    print('接入方系统名称：{}'.format(new_name))
    return new_name




# 查询房源的更新时间
def update_status():
    # 1.打开数据库连接
    conn = pymysql.connect(host="st-mysql-m.a.pa.com", port=3306, user="hfqa", passwd="qn3p@bI0qg",db = "govzf_pahf_fangchan_db", charset='utf8' )
    cursor = conn.cursor()
    select_sql1 = "select updated_at from pack_secondhand_house order by created_at desc limit 1  "
    cursor.execute(select_sql1)
    data = cursor.fetchone()
    data1 = data[0]
    print(data1)
    return str(data1)


# update_status()

    # # print('房源的更新时间：{}'.format(data[0]))
    # return  data[0]

    # print(data)    # (334,)   接下来要提取出334
    # code = re.findall(r"\((.*)\,", str(data))
    # print(code)  # ['334']
    # code1 = "".join(code)
    # print(code1)
    # code2 = code1.strftime("%Y-%m-%d %H:%M:%S")
    # print(code2)    # 334

    # code3 = json.dumps(code1,ensure_ascii=False)
    # print(code3)
    # return  code3
#
# 生成时间戳
def time1():
    dt=time.time()
    print(dt)
    return dt
# time1()
# 1556588636.5806167


# 当前时间转换为时间戳 10位，一直递增走
def get_timestamp():
    return str(int(time.time()))
# print(get_timestamp())



def time_now():
# 格式化成我们想要的日期  2019-04-20 17:29:58.749459———— 2019-04-20 后面可继续加
    dt=datetime.datetime.now().strftime('%Y-%m-%d')
    return dt

# 输出明天的这个此刻
def time_tomorrowNow():
    now = datetime.datetime.now()
    # print(now)
    dt= now + datetime.timedelta(hours=23, minutes=59, seconds=59)
    dt = dt.strftime('%Y-%m-%d %H:%M:%S')
    print(dt)
    return str(dt)
# time_tomorrowNow()
#2019-04-21 17:34:21.865868--- 2019-04-21 17:32:36


def wait(t):
    time.sleep(t)


# 删除C端数据
def delete_sql():
    # 1.打开数据库连接
    conn = pymysql.connect(host = "st-mysql-m.a.pa.com", port=3306,user = "hfqa", passwd = "qn3p@bI0qg",db = 'govzf_pahf_fangchan_db', charset='utf8' )
    cursor = conn.cursor()
    select_sql3 = "delete from pack_index_secondhand_house  where community_name like '%王文%'"
    select_sql4 = "delete from pack_secondhand_house  where community_name like '%王文%'"
    select_sql5 = "delete from fcxxw_pkg_order where pkg_name = '新增个人套餐'"

    select_sql6 = "delete from pack_community where name like '%王文小区%'"
    select_sql7 = "delete from fcxxw_community_audit where remark like '%王文审核小区通过%'"
    select_sql8 = "delete from pack_index_community where name like '%王文小区%'"
    # select_sql9 = "select *  from t_company where account_id = 51"
    select_sql20 = "delete from fcxxw_pkg where memo like  '%王文新增套餐%'"
    select_sql21 = "delete from fcxxw_pkg_assign_info where customer_id = '191'"

    cursor.execute(select_sql3)
    cursor.execute(select_sql4)
    cursor.execute(select_sql5)
    cursor.execute(select_sql6)
    cursor.execute(select_sql7)
    cursor.execute(select_sql8)
    # cursor.execute(select_sql9)
    cursor.execute(select_sql20)
    cursor.execute(select_sql21)
    conn.commit()

# delete_sql()

# --log-level debug