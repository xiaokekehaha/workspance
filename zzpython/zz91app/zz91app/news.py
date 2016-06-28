#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponsePermanentRedirect
import MySQLdb,sys,os,memcache,settings,urllib,re,time
import simplejson
from django.core.cache import cache
from zz91db_2_news import newsdb
from zz91db_ast import companydb
from zz91tools import int_to_strall
from settings import spconfig,appurl
spconfig=settings.SPHINXCONFIG
from sphinxapi import *
from zz91page import *

dbn=newsdb()
dbc=companydb()
reload(sys)
sys.setdefaultencoding('UTF-8')
nowpath=os.path.dirname(__file__)
execfile(nowpath+"/func/public_function.py")
execfile(nowpath+"/func/news_function.py")

zzn=zznews()

#----资讯首页(一期)
def newsindex(request):
    newscolumn=zzn.getnewscolumn()
    datatype=request.GET.get("datatype")
    if datatype=="json":
        return HttpResponse(simplejson.dumps(newscolumn, ensure_ascii=False))
    return render_to_response('news/index.html',locals())
def newscolumnlist(request):
    datatype=request.GET.get("datatype")
    list=zzn.getcolumnlist()
    if datatype=="json":
        return HttpResponse(simplejson.dumps(list, ensure_ascii=False))
#----资讯搜索
def news_search(request,page=''):
    cursor_news = conn_news.cursor()
    keywords=request.GET.get("keywords")
#    page=request.GET.get("page")
    if (keywords!=None):
        keywords=keywords.replace("资讯","")
        keywords=keywords.replace("价格","")
        webtitle=keywords
    if (str(keywords)=='None'):    
        keywords=None
        webtitle="资讯中心"
    if (page=='' or page==0 or page==None):
        page=1
    nowlanmu="<a href='/news/'>资讯中心</a>"
    funpage=zz91page()
    limitNum=funpage.limitNum(10)
    nowpage=funpage.nowpage(int(page))
    frompageCount=funpage.frompageCount()
    after_range_num = funpage.after_range_num(5)
    before_range_num = funpage.before_range_num(4)
    newslist=zzn.getnewslist(keywords=keywords,frompageCount=frompageCount,limitNum=limitNum)
    listcount=0
    if (newslist):
        listall=newslist['list']
        listcount=newslist['count']
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
    cursor_news.close()
    return render_to_response('news/list.html',locals())
#资讯列表页(一期)
def news_list(request):
    host=getnowurl(request)
    typeid=request.GET.get("typeid")
    page=request.GET.get("page")
    if typeid=='':
        typeid=185
    #columnid=getcolumnid(cursor_news)
    typename=zzn.get_typename(typeid)
#    webtitle="资讯中心"
#    nowlanmu="<a href='newslist.html'>资讯中心</a>"
    keywords=request.GET.get("keywords")
    username=request.session.get("username",None)
    nowlanmu="<a href='/news/'>资讯中心</a>"
#    page=request.GET.get("page")
    if (keywords!=None):
        keywords=keywords.replace("资讯","")
        keywords=keywords.replace("价格","")
        webtitle=keywords
    if (str(keywords)=='None'):    
        keywords=None
        webtitle="资讯中心"
        
    if (page=='' or page==0 or page==None):
        page=1
    funpage=zz91page()
    limitNum=funpage.limitNum(20)
    nowpage=funpage.nowpage(int(page))
    frompageCount=funpage.frompageCount()
    after_range_num = funpage.after_range_num(5)
    before_range_num = funpage.before_range_num(4)
    if typeid=='196':
        newslist=zzn.getnewslist(keywords="p",frompageCount=frompageCount,limitNum=limitNum,typeid='',allnum='',typeid2="")
    elif typeid=='195':
        newslist=zzn.getcompanynews(frompageCount,limitNum)
    else:
        if typeid and typeid!="None":
            typeidarr=[int(typeid)]
        else:
            typeidarr=None
        newslist=zzn.getnewslist(keywords=keywords,frompageCount=frompageCount,limitNum=limitNum,allnum='',typeid=typeidarr,typeid2="")
    listcount=0
    if (newslist):
        listall=newslist['list']
        listcount=newslist['count']
        if (int(listcount)>1000000):
            listcount=1000000-1
    listcount = funpage.listcount(listcount)
    page_listcount=funpage.page_listcount()
    firstpage = funpage.firstpage()
    lastpage = funpage.lastpage()
    page_range  = funpage.page_range()
    nextpage = funpage.nextpage()
    prvpage = funpage.prvpage()
#    newsnav=getnewsnav()
#    listall=listalla['list']
#    newslistcount=listalla['count']
    
    if (listcount==1):
        morebutton='style=display:none'
    else:
        morebutton=''
    #置顶资讯
    topnewslist=zzn.get_topnews(typeid=typeid)
    newslist['topnewslist']=topnewslist
    datatype=request.GET.get("datatype")
    if datatype=="json":
        return HttpResponse(simplejson.dumps(newslist, ensure_ascii=False))
    if page>1:
        return render_to_response('news/listmore.html',locals())
    return render_to_response('news/list.html',locals())

#----资讯最终页(一期)
def newsdetail(request,id=''):
    host=getnowurl(request)
    typeid=request.GET.get("typeid")
    company_id=request.GET.get("company_id")
    webtitle="资讯中心"
    nowlanmu="<a href='/news/'>资讯中心</a>"
    username=request.session.get("username",None)
    datatype=request.GET.get("datatype")
    typenews=None
    if typeid=='195':
        content=zzn.getshowcompanynews(id)
        typename='企业新闻'
        articalup=zzn.getcompanyup(id)
        articalnx=zzn.getcompanynx(id)
    else:
        zzn.newsclick_add(id)
        content=zzn.getnewscontent(id)
        detail=content['content'].replace('/uploads/uploads','http://pyapp.zz91.com/app/changepic.html?width=300&height=300&url=http://imgnews.zz91.com')
        content['content']=detail
        webtitle=content['title']
        favoriteflag=0
        if company_id:
            favoriteflag=isfavorite(id,'10091012',company_id)
        content['favoriteflag']=favoriteflag
        #获得当前新闻栏目
        newstype=dbn.get_newstype(id)
        if newstype:
            typename=newstype['typename']
            typeid=newstype['typeid']
            typeid2=newstype['typeid2']
            #相关阅读
            typenews=zzn.get_typenews(typeid,typeid2)
            #上一篇文章
            #articalup=zzn.getarticalup(id,typeid)
            #下一篇文章
            #articalnx=zzn.getarticalnx(id,typeid)
    if datatype=="json":
        content['othernewslist']=typenews
        return HttpResponse(simplejson.dumps(content, ensure_ascii=False))
    return render_to_response('news/detail.html',locals())