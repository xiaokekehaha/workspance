﻿from django.conf.urls import *
import settings

urlpatterns = patterns('zz91otherweb.views',
	#(r'^$', 'feiliao'),
	(r'^listmore(?P<typeid>\w+).html$', 'listmore'),
	(r'^verifycode/$', 'verifycode'),
	#--feiliao123改版
	(r'^$', 'index'),#首页
	(r'^feiliao123_more(?P<typeid>\w+).html$', 'feiliao123_more'),#更多
	(r'^trade/$', 'trade'),#交易
	(r'^news/$','news'),#资讯
)

#----设备信息搜索和删除，啊啊啊啊
urlpatterns += patterns('zz91otherweb.zzshebei',
    (r'^feiliao123/list/$','listl'),
    (r'^feiliao123/listl/$','listl'),
    (r'^feiliao123/doDelete.do$','doDelete'),
)
 


###
#----废料123后台
urlpatterns += patterns('zz91otherweb.admin123',
	(r'^feiliao123/visiturl.html$', 'visiturl'),
	(r'^feiliao123/admin.html$', 'default'),
	(r'^feiliao123/webtype.html$', 'webtype'),
	(r'^feiliao123/deletetype.html$', 'deletetype'),
	(r'^feiliao123/addwebtype.html$', 'addwebtype'),
	(r'^feiliao123/addwebtypeok.html$', 'addwebtypeok'),
	(r'^feiliao123/updatetype.html$', 'updatetype'),
	(r'^feiliao123/updatetypeok.html$', 'updatetypeok'),
	(r'^feiliao123/website.html$', 'website'),
	(r'^feiliao123/addwebsite.html$', 'addwebsite'),
	(r'^feiliao123/addwebsiteok.html$', 'addwebsiteok'),
	(r'^feiliao123/deleteweb.html$', 'deleteweb'),
	(r'^feiliao123/updateweb.html$', 'updateweb'),
	(r'^feiliao123/reduction.html$', 'reduction'),
	(r'^feiliao123/recommend.html$', 'recommend'),
	(r'^feiliao123/cancelrecommend.html$', 'cancelrecommend'),
	(r'^feiliao123/returnpage.html$', 'returnpage'),
	(r'^feiliao123/upload.html$', 'upload'),
	(r'^feiliao123/imgload.html$', 'imgload'),
	#---来电宝,可添加文章
	(r'^feiliao123/webartical.html$', 'webartical'),
	(r'^feiliao123/addwebartical.html$', 'addwebartical'),
	(r'^feiliao123/addwebarticalok.html$', 'addwebarticalok'),
	(r'^feiliao123/update_artical.html$', 'update_artical'),
	#----数据分析
	(r'^feiliao123/dataout.html$', 'dataout'),
	(r'^feiliao123/analyse.html$', 'analyse'),
	(r'^feiliao123/analysischart.html$', 'analysischart'),
	(r'^feiliao123/analyse_pageout.html$', 'analyse_pageout'),
	(r'^feiliao123/analyse_page.html$', 'analyse_page'),
	(r'^feiliao123/analyse_type.html$', 'analyse_type'),
	(r'^feiliao123/add_type.html$', 'add_type'),
	(r'^feiliao123/add_typeok.html$', 'add_typeok'),
	(r'^feiliao123/del_type.html$', 'del_type'),
	(r'^feiliao123/jumpout.html$', 'jumpout'),
	(r'^feiliao123/datalogin.html$', 'datalogin'),
	(r'^feiliao123/logdetail.html$', 'logdetail'),
	(r'^feiliao123/deldata.html$', 'deldata'),
	(r'^feiliao123/sendmials.html$', 'sendmials'),
	(r'^feiliao123/mailto.html$', 'mailto'),
	(r'^feiliao123/dialogs/image/image.html$', 'mailimg'),
	(r'^feiliao123/mailloadimg.html$', 'mailloadimg'),
	(r'^feiliao123/deldatasis.html$', 'deldatasis'),
	(r'^feiliao123/ipvisit.html$', 'ipvisit'),
	(r'^feiliao123/ipvisitout.html$', 'ipvisitout'),
	(r'^feiliao123/delipvisit.html$', 'delipvisit'),
	(r'^feiliao123/pagedetail.html$', 'pagedetail'),
	
	
	#----图表
	(r'^feiliao123/tongji_chart.html$', 'tongji_chart'),
	#----百度收录查询
	(r'^feiliao123/baiduincluded.html$', 'baiduincluded'),
	(r'^feiliao123/baiduincluded2.html$', 'baiduincluded2'),
	
	(r'^feiliao123/page404.html$', 'page404'),
	(r'^feiliao123/deletepage404.html$', 'deletepage404'),
	#上传文件
	(r'^feiliao123/uploadfileadmin.html$', 'uploadfileadmin'),
	(r'^feiliao123/uploadfileok.html$', 'uploadfileok'),
	#删除已上传的文件
	(r'^feiliao123/del_this_file.html$', 'del_this_file'),
	#敏感词
	(r'^feiliao123/mingang.html$', 'mingang'),
)
#----互助
urlpatterns += patterns('zz91otherweb.huzhu',
	(r'^feiliao123/huzhu_artical.html$', 'artical'),
	(r'^feiliao123/huzhu_arttype.html$', 'arttype'),
	(r'^feiliao123/huzhu_detail.html$', 'detail'),
	(r'^feiliao123/huzhu_addartical.html$', 'addartical'),
	(r'^feiliao123/huzhu_addarticalok.html$', 'addarticalok'),
	(r'^feiliao123/huzhu_updateartical.html$', 'updateartical'),
	(r'^feiliao123/huzhu_delartical.html$', 'delartical'),
)
#----资讯中心
urlpatterns += patterns('zz91otherweb.news',
	(r'^feiliao123/getquickart.html$', 'getquickart'),
	(r'^feiliao123/updatequickok.html$', 'updatequickok'),
	(r'^feiliao123/update_aqsiq.html$', 'update_aqsiq'),
	(r'^feiliao123/artical.html$', 'artical'),
	(r'^feiliao123/aqsiqdetail(?P<id>\d+).htm$', 'aqsiqdetail'),
	(r'^feiliao123/del_aqsiq.html$', 'del_aqsiq'),
	(r'^feiliao123/addartical.html$', 'addartical'),
	(r'^feiliao123/addarticalok.html$', 'addarticalok'),
	(r'^feiliao123/newsadmin.html$', 'newsadmin'),
	(r'^feiliao123/newsadmin2.html$', 'newsadmin2'),
	(r'^feiliao123/newstype.html$', 'newstype'),
	(r'^feiliao123/addnews.html$', 'addnews'),
	(r'^feiliao123/addnewsok.html$', 'addnewsok'),
	(r'^feiliao123/addnewstype.html$', 'addnewstype'),
	(r'^feiliao123/addnewstypeok.html$', 'addnewstypeok'),
	(r'^feiliao123/delete_newstype.html$', 'delete_newstype'),
	(r'^feiliao123/delete_newstype.html$', 'delete_newstype'),
	(r'^feiliao123/update_newstype.html$', 'update_newstype'),
	(r'^feiliao123/delnews.html$', 'delnews'),
	(r'^feiliao123/newsout.html$', 'newsout'),
	(r'^feiliao123/updateartical.html$', 'updateartical'),
	(r'^feiliao123/del_all_zz91.html$', 'del_all_zz91'),#zz91资讯一键删除
	(r'^feiliao123/back_newsall.html$', 'back_newsall'),
	#----报价资讯
	(r'^feiliao123/source_list.html$', 'source_list'),
	(r'^feiliao123/source_type.html$', 'source_type'),
)
#----手机站
urlpatterns += patterns('zz91otherweb.mobile',
	(r'^feiliao123/delastdbsimp.html$', 'delastdbsimp'),
	#----互助
	(r'^feiliao123/huzhu.html$', 'huzhu'),
	(r'^feiliao123/replylist.html$', 'replylist'),
	(r'^feiliao123/pushtype.html$', 'pushtype'),
	(r'^feiliao123/add_bbs_post.html$', 'add_bbs_post'),
	(r'^feiliao123/add_bbs_postok.html$', 'add_bbs_postok'),
	(r'^feiliao123/update_bbs_post.html$', 'update_bbs_post'),
	(r'^feiliao123/del_bbs_post.html$', 'del_bbs_post'),
	#---支付订单
	(r'^feiliao123/pay_order.html$', 'pay_order'),
	#----微信
	(r'^feiliao123/weixinscore.html$', 'weixinscore'),
	(r'^feiliao123/scoreexchange.html$', 'scoreexchange'),
	(r'^feiliao123/accountscore.html$', 'accountscore'),
	(r'^feiliao123/addweixinscore.html$', 'addweixinscore'),
	(r'^feiliao123/addweixinscoreok.html$', 'addweixinscoreok'),
	(r'^feiliao123/exchangetype.html$', 'exchangetype'),
	(r'^feiliao123/addexchangetype.html$', 'addexchangetype'),
	(r'^feiliao123/addexchangetypeok.html$', 'addexchangetypeok'),
	(r'^feiliao123/updatexchangetype.html$', 'updatexchangetype'),
	(r'^feiliao123/delexchangetype.html$', 'delexchangetype'),
	(r'^feiliao123/upchangetype_close.html$', 'upchangetype_close'),
	#----手机钱包
	(r'^feiliao123/paytype.html$', 'paytype'),
	(r'^feiliao123/addpaytype.html$', 'addpaytype'),
	(r'^feiliao123/addpaytypeok.html$', 'addpaytypeok'),
	(r'^feiliao123/updatepaytype.html$', 'updatepaytype'),
	(r'^feiliao123/delpaytype.html$', 'delpaytype'),
	(r'^feiliao123/addchongzhi.html$', 'addchongzhi'),
	(r'^feiliao123/addchongzhiok.html$', 'addchongzhiok'),
	(r'^feiliao123/delqbyzm.html$', 'delqbyzm'),
	(r'^feiliao123/redelqb.html$', 'redelqb'),
	#----手机钱包商城
	(r'^feiliao123/shop_product.html$', 'shop_product'),
	(r'^feiliao123/addshop_product.html$', 'addshop_product'),
	(r'^feiliao123/addshop_productok.html$', 'addshop_productok'),
	(r'^feiliao123/delshop_product.html$', 'delshop_product'),
	(r'^feiliao123/updateshop_product.html$', 'updateshop_product'),
	
	(r'^feiliao123/delshop_product.html$', 'delshop_product'),
	(r'^feiliao123/update_prorank.html$', 'update_prorank'),
	(r'^feiliao123/update_prorankok.html$', 'update_prorankok'),
	(r'^feiliao123/del_prorank.html$', 'del_prorank'),
	(r'^feiliao123/upshop_product2.html$', 'upshop_product2'),
	(r'^feiliao123/shop_baoming.html$', 'shop_baoming'),
	#钱包充值广告
	(r'^feiliao123/qianbao_gg.html$', 'qianbao_gg'),
	(r'^feiliao123/updateqbgg.html$', 'updateqbgg'),
	(r'^feiliao123/updateqbggok.html$', 'updateqbggok'),
	#----举报信息
	(r'^feiliao123/report.html$', 'report'),
	#----充值,消费金额
	(r'^feiliao123/outfee.html$', 'outfee'),
	#----充值金额走势图
	(r'^feiliao123/chongzhichart.html$', 'chongzhichart'),
	(r'^feiliao123/chongzhicharturl.html$', 'chongzhicharturl'),
	(r'^feiliao123/sunfeechart.html$', 'sunfeechart'),
	#----账户余额
	(r'^feiliao123/blance.html', 'blance'),
)
#----手机app
urlpatterns += patterns('zz91otherweb.app',
	(r'^feiliao123/messagelist.html$', 'messagelist'),
	(r'^feiliao123/addmessage.html$', 'addmessage'),
	(r'^feiliao123/addmessageok.html$', 'addmessageok'),
	(r'^feiliao123/updatemessage.html$', 'updatemessage'),
	(r'^feiliao123/delmessage.html$', 'delmessage'),
	(r'^feiliao123/appinstalluser.html$', 'appinstalluser'),
	(r'^feiliao123/telchecklist.html$', 'telchecklist'),
	(r'^feiliao123/installchart.html$', 'installchart'),
	(r'^feiliao123/installcharturl.html$', 'installcharturl'),
    
    (r'^feiliao123/installchart.html$', 'installchart'),
    (r'^feiliao123/installcharturl.html$', 'installcharturl'),
    (r'^feiliao123/activechart.html$', 'activechart'),
    (r'^feiliao123/activecharturl.html$', 'activecharturl'),
    
	(r'^feiliao123/userKeywords.html$', 'userKeywords'),
	
	#抢购首页
	(r'^feiliao123/qianggou.html$', 'qianggou'),
	#-----以下是抢购商品表(goods)
	#增加抢购商品
	(r'^feiliao123/add_goods.html$', 'add_goods'),
	(r'^feiliao123/add_goods_ok.html$','add_goods_ok'),
	#查看抢购商品表
	(r'^feiliao123/list_goods.html$', 'list_goods'),
	(r'^feiliao123/edit_goods.html$', 'edit_goods'),
	(r'^feiliao123/edit_goods_ok.html$','edit_goods_ok'),
	#上架操作
	(r'^feiliao123/turn_on.html$', 'turn_on'),
	(r'^feiliao123/delgoods.html$', 'delgoods'),
	#下架操作
	(r'^feiliao123/turn_off.html$', 'turn_off'),
	#推荐操作
	(r'^feiliao123/tuijian_on.html$', 'tuijian_on'),
	#取消推荐操作
	(r'^feiliao123/tuijian_off.html$', 'tuijian_off'),
	
	#-----以下是抢购订单表(orderForm)
	#查看订单
	(r'^feiliao123/list_order.html$', 'list_order'),
	#退回订单操作
	(r'^feiliao123/tuihui.html$', 'tuihui'),
	#成功订单操作
	(r'^feiliao123/success.html$', 'success'),
	
	#-----以下是app推送
	(r'^feiliao123/app_pushlist.html$', 'app_pushlist'),
	(r'^feiliao123/add_push.html$', 'add_push'),
	(r'^feiliao123/add_pushok.html$', 'add_pushok'),
	(r'^feiliao123/update_app_push.html$', 'update_app_push'),
	(r'^feiliao123/delthispush.html$', 'delthispush'),
	
	#---钱包优惠管理	
	(r'^feiliao123/list_qianbao_gg.html$', 'list_qianbao_gg'),
	#--添加
	(r'^feiliao123/add_qianbao_gg.html$', 'add_qianbao_gg'),
	(r'^feiliao123/add_qianbao_ggok.html$', 'add_qianbao_ggok'),
	#--编辑
	(r'^feiliao123/edit_this_gg.html$', 'edit_this_gg'),
	(r'^feiliao123/edit_this_ggok.html$', 'edit_this_ggok'),
	#--删除
	(r'^feiliao123/del_this_gg.html$', 'del_this_gg'),
	#--钱包广告开关操作
	(r'^feiliao123/flag_on.html$', 'flag_on'),#开
	(r'^feiliao123/flag_off.html$', 'flag_off'),#关
	#移动抽奖
	(r'^feiliao123/choujiang.html$', 'choujiang'),
	(r'^feiliao123/add_choujiang.html$', 'add_choujiang'),#手动添加
	(r'^feiliao123/add_choujiangok.html$', 'add_choujiangok'),#手动添加确认
	(r'^feiliao123/edit_this_cj.html$', 'edit_this_cj'),#编辑
	(r'^feiliao123/del_this_cj.html$', 'del_this_cj'),#删除
)

#----微门户关键词库
urlpatterns += patterns('zz91otherweb.weimenhu',
	#所有关键字
	(r'^feiliao123/key_list.html$', 'key_list'),
	(r'^feiliao123/key_tongji.html$', 'key_tongji'),
	(r'^feiliao123/key_list_del.html$', 'key_list_del'),
	(r'^feiliao123/huifu_ok_all.html$', 'huifu_ok_all'),
	(r'^feiliao123/shenhe_ok.html$', 'shenhe_ok'),
	(r'^feiliao123/shenhe_no.html$', 'shenhe_no'),
	(r'^feiliao123/delthis.html$', 'delthis'),
    (r'^feiliao123/shenhe_ok_all.html$', 'shenhe_ok_all'),#一键审核
    (r'^feiliao123/del_all1.html$', 'del_all1'),#一键删除1
	
	#未审核客户搜索关键字
	(r'^feiliao123/key_nocheck.html$', 'key_nocheck'),
	(r'^feiliao123/status_ok.html$', 'status_ok'),
	(r'^feiliao123/status_no.html$', 'status_no'),
	(r'^feiliao123/del_this.html$', 'del_this'),
	(r'^feiliao123/pushtype1.html$', 'pushtype1'),
    (r'^feiliao123/shenhe_ok_all2.html$', 'shenhe_ok_all2'),#一键审核2
    (r'^feiliao123/del_all2.html$', 'del_all2'),#一键删除2
    
    #导出数据
    (r'^feiliao123/deleted_keywords_export.html$', 'deleted_keywords_export'),#导出回收战数据（按时间）
    (r'^feiliao123/export_who_selected.html$', 'export_who_selected'),#导出回收战数据（按时间）
)
#----zz91帮助中心
urlpatterns += patterns('zz91otherweb.help',
	(r'^feiliao123/help_artical.html$', 'help_artical'),#帮助中心列表页
	(r'^feiliao123/help_column.html$', 'help_column'),#栏目页
	(r'^feiliao123/add_father_column.html$', 'add_father_column'),#添加父栏目
	(r'^feiliao123/add_father_columnok.html$', 'add_father_columnok'),#添加父栏目成功
	(r'^feiliao123/help_returnpage.html$', 'help_returnpage'),#返回列表页
	(r'^feiliao123/delete_column.html$', 'delete_column'),#删除栏目
	(r'^feiliao123/addhelpartical.html$', 'addhelpartical'),#添加或修改页面
	(r'^feiliao123/addhelparticalok.html$', 'addhelparticalok'),#添加或修改页面确认
	(r'^feiliao123/deletehelpartical.html$', 'deletehelpartical'),#删除确认
)

#----数据分析
urlpatterns += patterns('zz91otherweb.data',
	(r'^feiliao123/delcompro.html$', 'delcompro'),
	(r'^feiliao123/delkwdsearch.html$', 'delkwdsearch'),
	(r'^feiliao123/compro_check.html$', 'compro_check'),
	(r'^feiliao123/upcompro_check.html$', 'upcompro_check'),
	(r'^feiliao123/search_keywords.html$', 'search_keywords'),
	(r'^feiliao123/loadfile.html$', 'loadfile'),
	(r'^feiliao123/logindata.html$', 'logindata'),
	(r'^feiliao123/getpublishdata.html$', 'getpublishdata'),
	(r'^feiliao123/publishdata.html$', 'publishdata'),
	(r'^feiliao123/publishdetaildata.html$', 'publishdetaildata'),
	(r'^feiliao123/keywordssearchdata.html$', 'keywordssearchdata'),
	(r'^feiliao123/keywordsscreening.html$', 'keywordsscreening'),
	(r'^feiliao123/huanbaolist.html$', 'huanbaolist'),
	(r'^feiliao123/del_all_huanbaolist.html$', 'del_all_huanbaolist'),#环保资讯一键删除
	(r'^feiliao123/huanbaodetail(?P<id>\d+).htm$', 'huanbaodetail'),
)
#----抓取日志
urlpatterns += patterns('zz91otherweb.log',
	(r'^feiliao123/log_type.html$', 'log_type'),
	(r'^feiliao123/log_list.html$', 'log_list'),
	(r'^feiliao123/del_log.html$', 'del_log'),
	(r'^feiliao123/addlogtype.html$', 'addlogtype'),
	(r'^feiliao123/addlogtypeok.html$', 'addlogtypeok'),
	(r'^feiliao123/updatelogtype.html$', 'updatelogtype'),
	(r'^feiliao123/lognews.html$', 'lognews'),
	(r'^feiliao123/addlognews.html$', 'addlognews'),
	(r'^feiliao123/addlognewsok.html$', 'addlognewsok'),
	(r'^feiliao123/updatelognews.html$', 'updatelognews'),
	(r'^feiliao123/updlog_isok.html$', 'updlog_isok'),
	(r'^feiliao123/updlog_isok2.html$', 'updlog_isok2'),
	#来电宝日志
	(r'^feiliao123/ppc/log.html$', 'ppc_log'),
	
	(r'^feiliao123/appUserlog.html$', 'appUserlog'),
	(r'^feiliao123/zz91logall.html$', 'zz91logall'),
	(r'^feiliao123/errlog.html$', 'errlog'),
)

urlpatterns += patterns('zz91otherweb.myrc',
	(r'^feiliao123/operatype.html$', 'operatype'),
	(r'^feiliao123/operadata.html$', 'operadata'),
	(r'^feiliao123/delopera.html$', 'delopera'),
)
#----行情报价
urlpatterns += patterns('zz91otherweb.price',
	(r'^feiliao123/price_category.html$', 'price_category'),
	(r'^feiliao123/price_category_attr.html$', 'price_category_attr'),
	(r'^feiliao123/add_priceattr.html$', 'add_priceattr'),
	(r'^feiliao123/add_priceattrok.html$', 'add_priceattrok'),
	(r'^feiliao123/update_priceattr.html$', 'update_priceattr'),
	(r'^feiliao123/del_priceattr.html$', 'del_priceattr'),
	(r'^feiliao123/getc_label.html$', 'getc_label'),
	(r'^feiliao123/price_category_field.html$', 'price_category_field'),
	(r'^feiliao123/add_pricefield.html$', 'add_pricefield'),
	(r'^feiliao123/add_pricefieldok.html$', 'add_pricefieldok'),
	(r'^feiliao123/update_pricefield.html$', 'update_pricefield'),
	(r'^feiliao123/del_pricefield.html$', 'del_pricefield'),
)

urlpatterns += patterns('zz91otherweb.automation',
	(r'^feiliao123/automation.html$', 'feisuliao'),
	(r'^feiliao123/feisuliao.html$', 'feisuliao'),
	(r'^feiliao123/suliao_price.html$', 'suliao_price'),
	(r'^feiliao123/suliao_net_price.html$', 'suliao_net_price'),
	(r'^feiliao123/suliao_zaocanwanbao.html$', 'zaocanwanbao'),
	(r'^feiliao123/net_price.html$', 'net_price'),
	(r'^feiliao123/suliao_duanxin_price.html$', 'duanxin_price'),
	(r'^feiliao123/huanbao.html$', 'huanbao'),
	(r'^feiliao123/huanbao_check.html$', 'huanbao_check'),
	(r'^feiliao123/suliao_week_price.html$', 'week_price'),
	(r'^feiliao123/chartdata.html$', 'chartdata'),
	(r'^feiliao123/area_price.html$', 'area_price'),
)

urlpatterns += patterns('zz91otherweb.useradmin',
	(r'^feiliao123/login.html$', 'login'),
	(r'^feiliao123/logout.html$', 'logout'),
	(r'^feiliao123/loginpage.html$', 'loginpage'),
)
#---css引入
urlpatterns += patterns('',
	(r'^(?!admin)(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
)