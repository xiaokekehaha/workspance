#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import MySQLdb,sys,os,memcache,settings,urllib,re,time,datetime,requests,md5,hashlib
from django.core.cache import cache
from sphinxapi import *
from zz91page import *
from zz91tools import formattime
from settings import spconfig
#from commfunction import filter_tags,formattime,havepicflag,subString
from function import getnowurl
#from zz91tools import int_to_str

from zz91db_ast import companydb
from zz91db_sms import smsdb
from zz91db_2_news import newsdb

dbc=companydb()
dbn=newsdb()

reload(sys)
sys.setdefaultencoding('UTF-8')
nowpath=os.path.dirname(__file__)
execfile(nowpath+"/func/myrc_function.py")
execfile(nowpath+"/func/qianbao_function.py")

zzm=zmyrc()
zzq=qianbao()
dbsms=smsdb()

#----生意管家首页
def myrc_index(request):
    host=getnowurl(request)
    myrc=1
    showpost=1
    showgooglead=1
    webtitle="生意管家"
    nowlanmu="<a href='/myrc_index/'>生意管家</a>"
    zzm.weixinautologin(request,request.GET.get("weixinid"))
    username=request.session.get("username",None)
    company_id=request.session.get("company_id",None)
    if username and (company_id==None or str(company_id)=="0"):
        company_id=getcompanyid(username)
        request.session['company_id']=company_id
    if (username==None or (company_id==None or str(company_id)=="0")):
        return HttpResponseRedirect("/login/?done="+host)
    
    md5companyid = hashlib.md5(username+str(company_id))
    md5companyid = md5companyid.hexdigest()[8:-8]
    #----判断是否为来电宝用户
    viptype=zzm.getviptype(company_id)
    if viptype=='10051003':
        isldb=1
    return render_to_response('myrc/myrc_index3.html',locals())
#----生意管家 我的供求信息
def myrc_products(request):
    
    webtitle="生意管家"
    nowlanmu="<a href='/myrc_index/'>生意管家</a>"
    zzm.weixinautologin(request,request.GET.get("weixinid"))
    username=request.session.get("username",None)
    company_id=request.session.get("company_id",None)
    if (username==None or (company_id==None or str(company_id)=="0")):
        return HttpResponseRedirect("/login/?done=/myrc_products/")
    page=request.GET.get("page")
    checkStatus=request.GET.get("checkStatus")
    if not checkStatus:
        checkStatus='1'
    if not page:
        page=1
    funpage = zz91page()
    limitNum=funpage.limitNum(5)
    nowpage=funpage.nowpage(int(page))
    frompageCount=funpage.frompageCount()
    after_range_num = funpage.after_range_num(2)
    before_range_num = funpage.before_range_num(9)
    qlistall=zzm.getmyproductslist(frompageCount=frompageCount,limitNum=limitNum,company_id=company_id,checkStatus=checkStatus)
    qlist=qlistall['list']
    qlistcount=qlistall['count']
    listcount=qlistcount
    if (int(listcount)>100000):
        listcount=100000
    listcount = funpage.listcount(listcount)
    page_listcount=funpage.page_listcount()
    firstpage = funpage.firstpage()
    lastpage = funpage.lastpage()
    page_range  = funpage.page_range()
    nextpage = funpage.nextpage()
    prvpage = funpage.prvpage()
    
    sql1="select count(0) from products where company_id=%s and check_status=1 and is_del=0 and refresh_time<expire_time"
    result1=dbc.fetchonedb(sql1,[company_id])
    if result1:
        alist1=result1[0]
    sql0="select count(0) from products where company_id=%s and check_status=0 and is_del=0  and refresh_time<expire_time"
    result0=dbc.fetchonedb(sql0,[company_id])
    if result0:
        alist0=result0[0]
    sql2="select count(0) from products where company_id=%s and check_status=2 and is_del=0  and refresh_time<expire_time"
    result2=dbc.fetchonedb(sql2,[company_id])
    if result2:
        alist2=result2[0]
    isnotldb=1
    viptype=zzm.getviptype(company_id)
    if viptype=='10051003':
        isnotldb=None
    #----获取用户余额
    qianbaoblance=zzq.getqianbaoblance2(company_id)
    return render_to_response('myrc/myrc_products.html',locals())