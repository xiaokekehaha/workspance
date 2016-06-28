﻿import MySQLdb
import pymongo
#在默认情况下cursor方法返回的是BaseCursor类型对象，BaseCursor类型对象在执行查询后每条记录的结果以列表(list)表示。如果要返回字典(dict)表示的记录，就要设置cursorclass参数为MySQLdb.cursors.DictCursor类。
#wget http://www.webwareforpython.org/downloads/DBUtils/DBUtils-1.1.tar.gz
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
 
#db = MySQLdb.connect(host = ´localhost´, user = ´root´, passwd = ´123456´, db = ´test´) 
#cursor = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
##返回 ({'age': 0L, 'num': 1000L}, {'age': 0L, 'num': 2000L}, {'age': 0L, 'num': 3000L})

def database_news_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuo5342fhte95enp5i.mysql.rds.aliyuncs.com' , port=3306 , user='zz91news' , passwd='4ReLhW3QLyaaECzU',
                              db='zz91news',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_news = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='zz91news', passwd='4ReLhW3QLyaaECzU',db='zz91news',charset='utf8')
    #return conn_news

def database_sex_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='127.0.0.1' , port=3306 , user='zjfriend' , passwd='PqKYuNNqW9MZFMUc',
                              db='zjfriend',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_news = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='zjfriend', passwd='PqKYuNNqW9MZFMUc',db='zjfriend',charset='utf8')
    #return conn_news

def database_huanbao_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='10.171.223.228' , port=3306 , user='ep' , passwd='4DjeuWecb3CuQWLc',
                              db='ep',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_huanbao = MySQLdb.connect(host='10.171.223.228', user='ep', passwd='4DjeuWecb3CuQWLc',db='ep',charset='utf8')
    #return conn_huanbao

def database_other_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuo5342fhte95enp5i.mysql.rds.aliyuncs.com' , port=3306 , user='zzother' , passwd='jmLt9zGdXa59vrLM',
                              db='zzother',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_other = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='zzother', passwd='jmLt9zGdXa59vrLM',db='zzother',charset='utf8')
    #return conn_other

def database_pycms_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=20 ,maxconnections=200,
                              host='10.171.223.228' , port=3306 , user='webcms' , passwd='MbBfrjGRUb27qhuT',
                              db='webcms',use_unicode=False,charset='utf8')
    return __pool.connection()

    #conn_pycms = MySQLdb.connect(host='127.0.0.1', user='webcms', passwd='MbBfrjGRUb27qhuT',db='webcms',charset='utf8')
    #return conn_pycms

def database_comp_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com' , port=3306 , user='ast' , passwd='astozz91jiubao',
                              db='ast',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_comp=MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='ast', passwd='astozz91jiubao',db='ast',charset='utf8')
    #return conn_comp

def database_tags_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com' , port=3306 , user='ast' , passwd='astozz91jiubao',
                              db='zztags',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_comp=MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='ast', passwd='astozz91jiubao',db='zztags',charset='utf8')
    #return conn_comp

def database_ads_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com' , port=3306 , user='zzads' , passwd='aJuUVbChYJ57t2SX',
                              db='zzads',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_ads = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='zzads', passwd='aJuUVbChYJ57t2SX',db='zzads',charset='utf8')
    #return conn_ads

def database_log_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='10.171.223.228' , port=3306 , user='ast' , passwd='astozz91jiubao',
                              db='zzlog',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_log = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='ast', passwd='astozz91jiubao',db='zzlog',charset='utf8')
    #return conn_log

def database_aqsiq_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='10.171.223.228' , port=3306 , user='aqsiq' , passwd='6JGnmy8mEJv7yBhd',
                              db='aqsiq',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_aqsiq = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='aqsiq', passwd='6JGnmy8mEJv7yBhd',db='aqsiq',charset='utf8')
    #return conn_aqsiq

def database_sms_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuo5342fhte95enp5i.mysql.rds.aliyuncs.com' , port=3306 , user='reborn' , passwd='vfBNMAp9VpNXAWwV',
                              db='zzsms',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_sms = MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='reborn', passwd='vfBNMAp9VpNXAWwV',db='zzsms',charset='utf8')
    #return conn_sms

def database_work_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com' , port=3306 , user='ast' , passwd='astozz91jiubao',
                              db='zzwork',use_unicode=False,charset='utf8')
    return __pool.connection()
    #conn_comp=MySQLdb.connect(host='rdsuy4s1hdg04yt0px30.mysql.rds.aliyuncs.com', user='ast', passwd='astozz91jiubao',db='ast',charset='utf8')
    #return conn_comp

def database_help_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='10.168.104.155' , port=3306 , user='zz91help' , passwd='q2zuyQAdYRSe3UFt',
                              db='zz91help',use_unicode=False,charset='utf8')
    return __pool.connection()

def database_mail_read():
    __pool = PooledDB(creator=MySQLdb, mincached=1 , maxcached=50 ,maxconnections=200,
                              host='rdsuo5342fhte95enp5i.mysql.rds.aliyuncs.com' , port=3306 , user='zzmail' , passwd='cJmzPtMN9zdQR6Yr',
                              db='zzmail',use_unicode=False,charset='utf8')
    return __pool.connection()