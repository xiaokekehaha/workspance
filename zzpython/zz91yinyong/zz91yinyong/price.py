#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import MySQLdb,sys,os,memcache,settings,urllib,re,time,requests
from django.core.cache import cache

from commfunction import subString,filter_tags,replacepic,formattime
from function import getnowurl
from zz91page import *
from zz91db_ast import companydb
from zz91db_2_news import newsdb
from sphinxapi import *
from settings import spconfig

dbc=companydb()
dbn=newsdb()
reload(sys)
sys.setdefaultencoding('UTF-8')
nowpath=os.path.dirname(__file__)
execfile(nowpath+"/func/price_function.py")
zzprice=zprice()

def index(request):
    showpost=1
    alijsload=1
    host=getnowurl(request)
    webtitle="行情报价"
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    return render_to_response('price/priceindex.html',locals())

#----报价列表
def pricelist(request,category_id='',assist_id=''):
    host=getnowurl(request)
    page = request.GET.get("page")
    if (not page):
        page = 1
    showpost=1
    alijsload=1
    if '.html' in host:
        iscm=1
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    if not category_id:
        category_id=request.GET.get("category_id")
    webtitle="行情报价"
    assistvalue=None
    categoryvalue=None
    if category_id and category_id!='None':
        categoryvalue=[int(category_id)]
        category_label=zzprice.getcategory_label(category_id)
        mulu1='> <a href="/priceindex/'+str(category_id)+'.html">'+category_label+'</a>'
        webtitle+=category_label
    if not assist_id:
        assist_id=request.GET.get("assist_id")
    if assist_id:
        assist_label=zzprice.getcategory_label(assist_id)
        mulu3='> <a href="?assist_id='+assist_id+'">'+assist_label+'</a>'
        assistvalue=[int(assist_id)]
        webtitle+="-"+assist_label
    username=request.session.get("username",None)
    keywords=request.GET.get("keywords")
    if str(keywords)=="None":
        keywords=None
    if (keywords):
        mulu2='> <a href="?keywords='+keywords+'">'+keywords+'</a>'
        keywords=keywords.replace("报价","")
        keywords=keywords.replace("价格","")
        webtitle=keywords
        webtitle+="-"+keywords
    if (str(keywords)=='None'):    
        keywords=None
    if (str(category_id)=='None'):
        category_id=None
    if (category_id==None and keywords==None):
        categoryvalue=[]
    if category_id in ["40","42","41","52","44","45","47","43"]:
        showarea=1
        if category_id=="40":
            arealist="江浙沪,广东,南海 ,临沂,汨罗,北京,长葛,清远,四川,天津,安徽,河北,成都,江西,山东,辽宁,贵州,重庆,台州,陕西,福建,云南"
        if category_id=="42":
            arealist="江浙沪,山东,河南,天津,四川,湖北,江西,山西,广东,福建"
        if category_id=="41":
            arealist="废铝,江浙沪,广东,南海,长葛,汨罗,临沂,天津,福建,四川,清远,宁波,河北,台州,山东,云南,重庆,陕西"
        if category_id=="52":
            arealist="全国,山东,陕西,长葛,江浙沪,广东,四川,重庆"
        if category_id=="44":
            arealist="江浙沪,广东,南海,临沂,台州,宁波,天津,清远"
        if category_id=="45":
            arealist="江浙沪,南海,临沂,天津,广东 "
        if category_id=="47":
            arealist="江浙沪,临沂,南海"
        if category_id=="43":
            arealist="江浙沪,南海,广东,天津,河北,临沂"
        arealist=arealist.split(",")
    if not page:
        page=1
    funpage=zz91page()
    limitNum=funpage.limitNum(20)
    nowpage=funpage.nowpage(int(page))
    frompageCount=funpage.frompageCount()
    after_range_num = funpage.after_range_num(8)
    before_range_num = funpage.before_range_num(9)
    pricelistall=zzprice.getpricelist(keywords=keywords,frompageCount=frompageCount,limitNum=limitNum,category_id=categoryvalue,allnum=10000,assist_type_id=assistvalue)
    pricelist=pricelistall['list']
    listcount=pricelistall['count']
    if (int(listcount)>1000000):
        listcount=1000000-1
    listcount = funpage.listcount(listcount)
    page_listcount=funpage.page_listcount()
    firstpage = funpage.firstpage()
    lastpage = funpage.lastpage()
    page_range  = funpage.page_range()
    nextpage = funpage.nextpage()
    prvpage = funpage.prvpage()
    if (listcount==1):
        morebutton='style=display:none'
    else:
        morebutton=''
    if not keywords:
        keywords=""
    return render_to_response('price/list.html',locals())
#----报价列表 更多
def pricemore(request,category_id='',assist_id=''):
    username=request.session.get("username",None)
    if not category_id:
        category_id=request.GET.get("category_id")
    keywords=request.GET.get("keywords")
    if not assist_id:
        assist_id=request.GET.get("assist_id")
    assistvalue=None
    if assist_id:
        assistvalue=[int(assist_id)]
    if (str(keywords)=='None'):
        keywords=None
    beginPage=request.GET.get("beginPage")
    if beginPage==None:
        beginPage=0
    if (str(category_id)=='None'):
        category_id=None
    if category_id:
        category_id=int(category_id)
    categoryvalue=[category_id]
    if category_id==None:
        categoryvalue=None
    pricelistall=zzprice.getpricelist(keywords=keywords,frompageCount=int(beginPage)*20,limitNum=20,category_id=categoryvalue,allnum=1000,assist_type_id=assistvalue)
    pricelist=pricelistall['list']
    return render_to_response('price/listmore.html',locals())
#----行情报价最终页
def details(request):
    host=getnowurl(request)
    #alijsload="1"
    showpost=1
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    id=request.GET.get("id")
    category_id=request.GET.get("category_id")
    keywords=request.GET.get("keywords")
    assist_id=request.GET.get("assist_id")
    searchkeyword=''
    category_id2=[]
    assist_id2=[]
    priceabout=[]
    arg=''
    if category_id:
        category_label=zzprice.getcategory_label(category_id)
        parent_id=zzprice.parent_id(category_id)
        parent_id2=zzprice.parent_id(parent_id)
        parent_id3=zzprice.parent_id(parent_id2)
        category_id2=[int(category_id)]
        if parent_id==5 or parent_id2==5 or parent_id3==5:
            searchkeyword='废金属'
            arg=1
        elif parent_id==6 or parent_id2==6 or parent_id3==6:
            searchkeyword='废塑料'
            arg=2
        elif parent_id==7 or parent_id2==7 or parent_id3==7:
            searchkeyword='废纸'
        elif parent_id==8 or parent_id2==8 or parent_id3==8:
            searchkeyword='废橡胶'
        elif parent_id==213 or parent_id2==213 or parent_id3==213:
            searchkeyword='原油'
        mulu1='> <a href="/priceindex/'+str(category_id)+'.html">'+category_label+'</a>'
    if keywords:
        webtitle=keywords
#        if arg==1:
#            searchkeyword=keywords
        mulu2='> <a href="/price/?keywords='+keywords+'">'+keywords+'</a>'
    if assist_id:
        assist_id2=[int(assist_id)]
        assist_label=zzprice.getcategory_label(assist_id)
        if arg==1:
#            searchkeyword=assist_label
            priceabout=zzprice.getpricelist('',0,7,category_id2,7,assist_id2,1)['list']
            searchkeyword=category_label
        elif arg==2:
            searchkeyword=assist_label
            priceabout=zzprice.getpricelist('',0,7,category_id2,7,assist_id2,2)['list']
        if assist_id!=0 and assist_label:
            mulu3='> <a href="/price/?assist_id='+str(assist_id)+'">'+str(assist_label)+'</a>'
    username=request.session.get("username",None)
    type_id=''
    sql="select title,content,gmt_created,type_id,assist_type_id from price where id=%s and is_checked=1"
    alist = dbc.fetchonedb(sql,[id])
    listall=[]
    if alist:
        title=alist[0]
        content=alist[1]
        content=content.replace("http://price.zz91.com/","http://m.zz91.com/")
        type_id=alist[3]
        assist_type_id=alist[4]
        if not category_id:
            category_id=type_id
            category_label=zzprice.getcategory_label(category_id)
            assist_type_label=zzprice.getcategory_label(assist_type_id)
            searchkeyword=category_label
            parent_id=zzprice.parent_id(category_id)
            parent_id2=zzprice.parent_id(parent_id)
            parent_id3=zzprice.parent_id(parent_id2)
            category_id2=[int(category_id)]
            if parent_id==5 or parent_id2==5 or parent_id3==5:
#                searchkeyword='废金属'
                arg=1
            elif parent_id==6 or parent_id2==6 or parent_id3==6:
#                searchkeyword='废塑料'
                searchkeyword=assist_type_label
                arg=2
            elif parent_id==7 or parent_id2==7 or parent_id3==7:
                searchkeyword='废纸'
            elif parent_id==8 or parent_id2==8 or parent_id3==8:
                searchkeyword='废橡胶'
            elif parent_id==213 or parent_id2==213 or parent_id3==213:
                searchkeyword='原油'
        webtitle=title
        content=replacepic(content)
        content=content.replace("http://price.zz91.com/priceDetails_","http://m.zz91.com/priceviews/")
        gmt_created=alist[2].strftime( '%-Y-%-m-%-d %-H:%-M:%-S')
        if str(type_id) in ("25","51","137"):
            content=zzprice.getwebprice(id)
        list={'title':title,'content':content,'gmt_created':gmt_created}
        listall.append(list)
    feizhibbsd=zzprice.getbbslist(searchkeyword,10)
    if feizhibbsd:
        feizhibbs=feizhibbsd['list']
    zhibuy=zzprice.offerlist(searchkeyword,'1',5)
    zhioffer=zzprice.offerlist(searchkeyword,'0',5)
    if searchkeyword==None:
        searchkeyword=""
    if not priceabout:
        if category_id:
            priceabout=zzprice.getpricelist(searchkeyword,0,7,[int(category_id)],7)['list']
    return render_to_response('price/details.html',locals())

#----企业报价
def compdetails(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    id=request.GET.get("id")
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    webtitle="商家报价"
    sql='select title,details,category_company_price_code,refresh_time from company_price where id=%s'
    alist = dbc.fetchonedb(sql,[id])
    if alist:
        title=alist[0]
        webtitle=title
        content=alist[1]
        category_cprice_code=alist[2]
        gmt_created=formattime(alist[3],3)
        sql2='select label from category_company_price where code=%s'
        alist2 = dbc.fetchonedb(sql2,[category_cprice_code])
        if alist2:
            clabel=alist2[0]
            priceabout=zzprice.getpricelist(clabel,0,7,'',7)['list']
            zhioffer=zzprice.offerlist(clabel,'0',5)
            feizhibbsd=zzprice.getbbslist(clabel,10)
            if feizhibbsd:
                feizhibbs=feizhibbsd['list']
    return render_to_response('price/compdetails.html',locals())


def jinshuarea(request):
    host=getnowurl(request)
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    webtitle="废金属全国各地价格"
#    jinshulist=zzprice.getprice_clist(3)
    return render_to_response('price/jinshuarea.html',locals())
def suliaoarea(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    webtitle="废塑料全国各地价格"
    host=getnowurl(request)
    return render_to_response('price/suliaoarea.html',locals())
def suliaoxinliao(request):
    webtitle="废塑料新料"
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    return render_to_response('price/suliaoxinliao.html',locals())
def areasuliao(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="各地废塑料行情"
    return render_to_response('price/areasuliao.html',locals())
def suliaoqihuo(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="塑料期货"
    return render_to_response('price/suliaoqihuo.html',locals())
def suliaozaishengliao(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="塑料再生料价格"
    return render_to_response('price/suliaozaishengliao.html',locals())
def meiguosuliao(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="美国废塑料价格"
    return render_to_response('price/meiguosuliao.html',locals())
def ouzhousuliao(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="欧洲废塑料价格"
    return render_to_response('price/ouzhousuliao.html',locals())
def feizhidongtai(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    host=getnowurl(request)
    webtitle="废纸行情动态"
    return render_to_response('price/feizhidongtai.html',locals())
def feizhiarea(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    webtitle="废纸各地价格"
    host=getnowurl(request)
    return render_to_response('price/feizhiarea.html',locals())
def feizhiriping(request):
    nowlanmu="<a href='/priceindex/'>行情报价</a>"
    webtitle="废纸日评"
    host=getnowurl(request)
    return render_to_response('price/feizhiriping.html',locals())