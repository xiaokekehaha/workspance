#-*- coding:utf-8 -*- 
from django.conf.urls import patterns,include,url
import settings

urlpatterns = patterns('zz91news.views',
    ('^$', 'index'),
    ('^zhuanti/$', 'zhuanti'),
    ('^search.htm$', 'search'),
    ('^column_list/tags-(?P<tags_hex>\w+).html$', 'newsalllist'),
    ('^column_list/tags-(?P<tags_hex>\w+)-p(?P<page>\w+).html$', 'newsalllist'),
    ('^(?P<kltype>\w+)/list/tags-(?P<tags_hex>\w+).html$', 'newsalllist'),
    ('^(?P<kltype>\w+)/list/tags-(?P<tags_hex>\w+)-p(?P<page>\w+).html$', 'newsalllist'),
    ('^tech/$', 'newsalllist'),
    ('^law/$', 'newsalllist'),
    ('^guonei/$', 'newsalllist'),
    ('^guoji/$', 'newsalllist'),
    ('^company/$', 'newsalllist'),
    ('^pic/$', 'newsalllist'),
    ('^zhuanti/$', 'zhuanti'),
    ('^verifycode/$', 'verifycode'),
    ('^tech/p(?P<page>\w+).html$', 'newsalllist'),
    ('^law/p(?P<page>\w+).html$', 'newsalllist'),
    ('^guonei/p(?P<page>\w+).html$', 'newsalllist'),
    ('^guoji/p(?P<page>\w+).html$', 'newsalllist'),
    ('^company/p(?P<page>\w+).html$', 'newsalllist'),
    ('^pic/p(?P<page>\w+).html$', 'newsalllist'),
    ('^(?P<kltype>\w+)/list/$', 'newsalllist'),
    ('^(?P<kltype>\w+)/(?P<mltype>\w+)/$', 'newsalllist'),
    ('^(?P<kltype>\w+)/(?P<mltype>\w+)/p(?P<page>\w+).html$', 'newsalllist'),
    ('^(?P<kltype>\w+)/$', 'newstype'),
    ('^(?P<kltype>\w+)/newsdetail1(?P<newsid>\d+).htm$', 'newsdetail'),
    ('^(?P<kltype>\w+)/newsdetail1(?P<newsid>\d+)-(?P<page>\w+).htm$', 'newsdetail'),
    ('^(?P<kltype>\w+)/(?P<mltype>\w+)/newsdetail1(?P<newsid>\d+).htm$', 'newsdetail'),
    ('^(?P<kltype>\w+)/(?P<mltype>\w+)/newsdetail1(?P<newsid>\d+)-(?P<page>\w+).htm$', 'newsdetail'),
)

urlpatterns += patterns('',
    (r'^(?!admin)(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)