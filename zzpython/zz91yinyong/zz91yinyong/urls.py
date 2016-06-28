﻿from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT

#----首页
urlpatterns=patterns('zz91yinyong.main',
	(r'^$', 'index'),
	#----广告页
	(r'^guanggao.html$', 'guanggao'),
	(r'^app.html', 'app'),
	(r'^pay/index.html', 'pay'),
	(r'^invite/invite.html', 'invite'),
	(r'^invite/i(?P<mcode>\w+).html', 'invite'),
	(r'^invite/help.html', 'invitehelp'),
	(r'^invite/help(?P<code>\w+).html', 'invitehelp'),
	(r'^invite/s(?P<mcode>\w+).html', 'invitesee'),
	(r'^showppccomplist_float.html$', 'showppccomplist_float'),
	(r'^messages.html$', 'messages'),
	(r'^messages_save.html$', 'messages_save'),
	(r'^log/getloginfo.html$', 'getloginfo'),
	(r'^log/saveloginfo.html$', 'saveloginfo'),
	(r'^test.html$', 'test'),
	(r'^ad/show.html$', 'adshow'),
)

#----再生钱包
urlpatterns+=patterns('zz91yinyong.qianbao',
	(r'^qianbao/$', 'index'),
	(r'^qianbao/zhangdan.html$', 'zhangdan'),
	(r'^qianbao/zhangdannore.html$', 'zhangdannore'),
	(r'^qianbao/chongzhi.html$', 'chongzhi'),
	(r'^qb.h(?P<id>\w+)$', 'chongzhi'),
	(r'^qianbao/intxt.html$', 'intxt'),
	(r'^qianbao/outtxt.html$', 'outtxt'),
	(r'^qianbao/shop.html$', 'shop'),
	(r'^qianbao/simptxt.html$', 'simptxt'),
	(r'^qianbao/oflist.html$', 'oflist'),
	(r'^qianbao/offmore.html$', 'offmore'),
	(r'^qianbao/qianbaopay.html$', 'qianbaopay'),
)
#----生意管家
urlpatterns+=patterns('zz91yinyong.myrc',
	(r'^myrc_index/$', 'myrc_index'),
	(r'^myrc_products/$', 'myrc_products'),
)
#----pingxx 支付
urlpatterns+=patterns('zz91yinyong.pingxx',
	(r'^pingxx/pay.html$', 'pay'),
	(r'^pingxx/pay_save.html$', 'pay_save'),
)
#----来电宝
urlpatterns+=patterns('zz91yinyong.ldb_weixin',
	#----来电宝首页
	(r'^laidianbao/$', 'laidianbao'),
	(r'^laidianbao/list-(?P<page>\d+).html$', 'laidianbao'),
	#----来电宝微信
	(r'^ldb_weixin/product_introduction.html$', 'product_introduction'),
	(r'^ldb_weixin/about.html$', 'about'),
	(r'^ldb_weixin/contact.html$', 'contact'),
	(r'^ldb_weixin/callanalysis.html$', 'callanalysis'),
	(r'^ldb_weixin/businessearch.html$', 'businessearch'),
	(r'^ldb_weixin/businessearchmore.html$', 'businessearchmore'),
	(r'^ldb_weixin/balance.html$', 'balance'),
	(r'^ldb_weixin/phonerecords.html$', 'phonerecords'),
	(r'^ldb_weixin/phonerecords-(?P<datearg>\d+).html$', 'phonerecords'),
	(r'^ldb_weixin/phonerecordsmore.html$', 'phonerecordsmore'),
	(r'^ldb_weixin/phoneclick.html$', 'phoneclick'),
	(r'^ldb_weixin/phoneclickmore.html$', 'phoneclickmore'),
	(r'^ldb_weixin/lookcontact.html$', 'lookcontact'),
	#---来电宝钱包首页
	(r'^ldb_weixin/index.html$', 'index'),
)

#----price301跳转
urlpatterns += patterns('zz91yinyong.views',
#	(r'^(?P<typeid1>\w+)List_(?P<typeid>\w+)_(?P<typeid3>\w+).htm$', 'zz91yinyong.views.price301'),
#	(r'^(?P<typeid1>\w+)List(?P<typeid2>\w+)_(?P<typeid>\w+)_(?P<typeid3>\w+).htm$', 'zz91yinyong.views.price301'),
#	(r'^priceDetails_(?P<id>\w+).htm$', 'zz91yinyong.views.price301'),
	(r'^priceList_t(?P<typeid>\w+)_metal.htm$', 'price301'),
	(r'^priceList_a(?P<assist_id>\w+)_metal.htm$', 'price301'),
	(r'^priceList_t40_a(?P<assist_id>\w+)_metal.htm$', 'price301'),
	(r'^moreList_p3_t(?P<typeid>\w+)_metal.htm$', 'price301'),
	(r'^moreList_p17_a(?P<assist_id>\w+)_metal.htm$', 'price301'),
	
	(r'^priceList_t(?P<typeid>\w+)_plastic.htm$', 'price301'),
	(r'^priceList_a(?P<assist_id>\w+)_plastic.htm$', 'price301'),
	(r'^priceList_t40_a(?P<typeid>\w+)_plastic.htm$', 'price301'),
	(r'^moreList_p(?P<typeid>\w+)_plastic.htm$', 'price301'),
	
	(r'^priceDetails_(?P<id>\w+)_plastic.htm$', 'price301'),
	(r'^priceDetails_(?P<id>\w+)_paper.htm$', 'price301'),
	(r'^priceDetails_(?P<id>\w+)_metal.htm$', 'price301'),
	(r'^priceDetails_(?P<id>\w+).htm$', 'price301'),
	
	(r'^priceList_t(?P<typeid>\w+)_paper.htm$', 'price301'),
	(r'^moreList_p(?P<typeid>\w+)_paper.htm$', 'price301'),
)

urlpatterns += patterns('',
	(r'^goback/$', 'zz91yinyong.views.goback'),
	(r'^slider2/js/widget/$', 'zz91yinyong.views.default2'),
	(r'^index.html$', 'zz91yinyong.views.newdefault'),
	(r'^category/$', 'zz91yinyong.views.category'),
	(r'^offerlist/$', 'zz91yinyong.views.offerlist'),
	(r'^register/$', 'zz91yinyong.views.register'),
	(r'^registerSave/$', 'zz91yinyong.views.registerSave'),
	(r'^login/$', 'zz91yinyong.views.login'),
	(r'^loginout/$', 'zz91yinyong.views.loginout'),
	(r'^loginof/$', 'zz91yinyong.views.loginof'),
	(r'^serviceterms/$', 'zz91yinyong.views.serviceterms'),
	#----供求
	(r'^trade/pro_report.html$', 'zz91yinyong.trade.pro_report'),
	(r'^detail/$', 'zz91yinyong.trade.detail'),
	(r'^trade/pricelist.html$', 'zz91yinyong.trade.pricelist'),
	(r'^trade/telclicklog.html$', 'zz91yinyong.trade.telclicklog'),
	

	#----互助
	(r'^huzhu/$', 'zz91yinyong.views.huzhu'),
	(r'^huzhumore/$', 'zz91yinyong.views.huzhumore'),
	(r'^huzhupost/$', 'zz91yinyong.views.huzhupost'),
	(r'^huzhu_imgload/$', 'zz91yinyong.views.huzhu_imgload'),
	(r'^huzhu_upload/$', 'zz91yinyong.views.huzhu_upload'),
	(r'^huzhupostsave/$', 'zz91yinyong.views.huzhupostsave'),
	(r'^huzhuview/(?P<id>\d+).htm$', 'zz91yinyong.views.huzhuview'),
	(r'^huzhuview/viewReply(?P<id>\d+).htm$', 'zz91yinyong.views.huzhuview'),
	(r'^huzhureplymore/$', 'zz91yinyong.views.replymore'),
	(r'^huzhu_replay/$', 'zz91yinyong.views.huzhu_replay'),
	(r'^huzhu_replayshow/$', 'zz91yinyong.views.huzhu_replayshow'),
	(r'^reply_reply/$', 'zz91yinyong.views.reply_reply'),
	
	#----行情报价
	(r'^priceindex/$', 'zz91yinyong.price.index'),
	(r'^price/$', 'zz91yinyong.price.pricelist'),
	(r'^priceindex/(?P<category_id>\d+).html$', 'zz91yinyong.price.pricelist'),
	(r'^priceindex/p(?P<assist_id>\d+).html$', 'zz91yinyong.price.pricelist'),
	(r'^pricemore/(?P<category_id>\d+).html$', 'zz91yinyong.price.pricemore'),
	(r'^pricemore/p(?P<assist_id>\d+).html$', 'zz91yinyong.price.pricemore'),
	(r'^priceindex/jinshuarea/$', 'zz91yinyong.price.jinshuarea'),
	(r'^priceindex/suliaoarea/$', 'zz91yinyong.price.suliaoarea'),
	(r'^priceindex/suliaoxinliao/$', 'zz91yinyong.price.suliaoxinliao'),
	(r'^priceindex/areasuliao/$', 'zz91yinyong.price.areasuliao'),
	(r'^priceindex/suliaoqihuo/$', 'zz91yinyong.price.suliaoqihuo'),
	(r'^priceindex/suliaozaishengliao/$', 'zz91yinyong.price.suliaozaishengliao'),
	(r'^priceindex/meiguosuliao/$', 'zz91yinyong.price.meiguosuliao'),
	(r'^priceindex/ouzhousuliao/$', 'zz91yinyong.price.ouzhousuliao'),
	(r'^priceindex/suliaozaishengliao/$', 'zz91yinyong.price.suliaozaishengliao'),
	(r'^priceindex/feizhidongtai/$', 'zz91yinyong.price.feizhidongtai'),
	(r'^priceindex/feizhiarea/$', 'zz91yinyong.price.feizhiarea'),
	(r'^priceindex/feizhiriping/$', 'zz91yinyong.price.feizhiriping'),
	(r'^pricemore/$', 'zz91yinyong.price.pricemore'),
	(r'^priceviews/$', 'zz91yinyong.price.details'),
	(r'^priceviews/(?P<id>\d+).htm$', 'zz91yinyong.views.priceviews1'),
	(r'^pricemore/$', 'zz91yinyong.views.pricemore'),
	#----企业报价最终页
	(r'^compriceviews/$', 'zz91yinyong.price.compdetails'),
	
	(r'^company/$', 'zz91yinyong.views.company'),
	(r'^companydetail/$', 'zz91yinyong.views.companydetail'),
	(r'^companyinfo/$', 'zz91yinyong.company.companyinfo'),
	#----公司供求列表
	(r'^companyproducts/$', 'zz91yinyong.views.companyproducts'),
	(r'^feedback/$', 'zz91yinyong.views.feedback'),
	(r'^feedbacksave/$', 'zz91yinyong.views.feedbacksave'),
	(r'^huzhucate/$', 'zz91yinyong.views.huzhucate'),
	(r'^verifycode/$', 'zz91yinyong.views.verifycode'),
	(r'^upload/$', 'zz91yinyong.views.upload'),
	
	(r'^categoryinfo.html$', 'zz91yinyong.views.categoryinfo'),
	
	#---支付宝支付
	(r'^zz91pay.html$', 'zz91yinyong.views.zz91pay'),
	(r'^pay/callback_get.html$', 'zz91yinyong.views.callback_get'),
	(r'^zz91payverify_notify.html$', 'zz91yinyong.views.zz91payverify_notify'),
	(r'^zz91paypingxx_notify.html$', 'zz91yinyong.views.zz91paypingxx_notify'),
	(r'^zz91payreturn_url.html$', 'zz91yinyong.views.zz91payreturn_url'),
	
	#----资讯中心
	(r'^newslist.html$', 'zz91yinyong.views.newslist'),
	(r'^newsmore.html$', 'zz91yinyong.views.newsmore'),
	(r'^newsviews.html$', 'zz91yinyong.views.newsviews'),

	#----微信
	(r'^weixin/order.html$', 'zz91yinyong.weixin.order'),
	(r'^weixin/tradesearch.html$', 'zz91yinyong.weixin.tradesearch'),
	(r'^weixin/pricesearch.html$', 'zz91yinyong.weixin.pricesearch'),
	(r'^weixin/login.html$', 'zz91yinyong.weixin.login'),
	(r'^weixin/loginsave.html$', 'zz91yinyong.weixin.loginsave'),
	(r'^weixin/reg.html$', 'zz91yinyong.weixin.reg'),
	(r'^weixin/regsave.html$', 'zz91yinyong.weixin.regsave'),
	(r'^weixin/qqlogin.html$', 'zz91yinyong.weixin.qqlogin'),
	(r'^weixin/forgetpasswd.html$', 'zz91yinyong.weixin.forgetpasswd'),
	(r'^weixin/doget.html$', 'zz91yinyong.weixin.doget'),
	(r'^weixin/ldbdoget.html$', 'zz91yinyong.weixin.ldbdoget'),
	(r'^weixin/priceday.html$', 'zz91yinyong.weixin.priceday'),
	(r'^weixin/weixintest.html$', 'zz91yinyong.weixin.weixintest'),
	
	
	(r'^weixin/zz91weixin_yz.html$', 'zz91yinyong.weixin.zz91weixin_yz'),
	(r'^weixin/zz91weixin_yzsave.html$', 'zz91yinyong.weixin.zz91weixin_yzsave'),
	(r'^weixin/zz91weixin_yzfront.html$', 'zz91yinyong.weixin.zz91weixin_yzfront'),
	
	(r'^weixin/huanbaowxget.html$', 'zz91yinyong.weixin.huanbaowxget'),
	(r'^weixin/huanbaoweixin_yz.html$', 'zz91yinyong.weixin.huanbaoweixin_yz'),
	(r'^weixin/huanbaoweixin_yzsave.html$', 'zz91yinyong.weixin.huanbaoweixin_yzsave'),
	(r'^weixin/huanbaoweixin_yzfront.html$', 'zz91yinyong.weixin.huanbaoweixin_yzfront'),
	
	#优质客户
	(r'^weixin/company/$', 'zz91yinyong.weixin.categoryindex'),
	(r'^weixin/company/(?P<code>\w+)/$', 'zz91yinyong.weixin.categorylist'),
	
	#----定制页面(一期)
	(r'^order/$', 'zz91yinyong.views.orderindex'),
	(r'^order/business.html$', 'zz91yinyong.views.orderbusiness'),
	(r'^order/price.html$', 'zz91yinyong.views.orderprice'),
	(r'^order/save_collect.html$', 'zz91yinyong.views.save_collect'),
	
	#----看资讯(一期)
	(r'^news/$', 'zz91yinyong.views.newsindex'),
	(r'^news/list-(?P<typeid>\w+).html$', 'zz91yinyong.views.news_list'),
	(r'^news/search.html$', 'zz91yinyong.views.news_search'),
	(r'^news/search-(?P<page>\d+).html$', 'zz91yinyong.views.news_search'),
	(r'^news/list-(?P<typeid>\w+)-(?P<page>\d+).html$', 'zz91yinyong.views.news_list'),
	(r'^news/newsdetail(?P<id>\d+).htm$', 'zz91yinyong.views.newsdetail'),
	#----企业微站,来电宝(一期)
	(r'^smallsite/$', 'zz91yinyong.views.smallsite'),
	(r'^smallsite/list-(?P<page>\d+).html$', 'zz91yinyong.views.smallsite'),
		
	(r'^ajaxTopbbs/$', 'zz91yinyong.views.ajaxTopbbs'),
	(r'^ajaxTopprice/$', 'zz91yinyong.views.ajaxTopprice'),
	
	(r'^getzwpic/$', 'zz91yinyong.views.getzwpic'),
	(r'^searchfirst/$', 'zz91yinyong.views.searchfirst'),
	(r'^leavewords/$', 'zz91yinyong.views.leavewords'),
	(r'^leavewords_save/$', 'zz91yinyong.views.leavewords_save'),
	(r'^favorite/$', 'zz91yinyong.views.favorite'),
	(r'^openfavorite/$', 'zz91yinyong.views.openfavorite'),
	(r'^service/$', 'zz91yinyong.views.service'),
	(r'^about/$', 'zz91yinyong.views.about'),
	
	(r'^myrc_mycommunity/$', 'zz91yinyong.views.myrc_mycommunity'),
	(r'^myrc_mycommunitymore/$', 'zz91yinyong.views.myrc_mycommunitymore'),
	(r'^myrc_mycommunitydel/$', 'zz91yinyong.views.myrc_mycommunitydel'),
	(r'^myrc_mypost/$', 'zz91yinyong.views.myrc_mypost'),
	(r'^myrc_mypostsave/$', 'zz91yinyong.views.myrc_mypostsave'),
	(r'^myrc_mypostmore/$', 'zz91yinyong.views.myrc_mypostmore'),
	(r'^myrc_myreply/$', 'zz91yinyong.views.myrc_myreply'),
	(r'^myrc_myreplysave/$', 'zz91yinyong.views.myrc_myreplysave'),
	(r'^myrc_myreplymore/$', 'zz91yinyong.views.myrc_myreplymore'),
	(r'^openmessages/$', 'zz91yinyong.views.openmessages'),
	
	(r'^myrc_backquestion/$', 'zz91yinyong.views.myrc_backquestion'),
	(r'^myrc_backquestionsave/$', 'zz91yinyong.views.myrc_backquestionsave'),
	#----我的收藏(一期)
	(r'^myrc_collect/$', 'zz91yinyong.views.myrc_collect'),
	(r'^myrc_collectmain/$', 'zz91yinyong.views.myrc_collectmain'),
	(r'^myrc_collectprice/$', 'zz91yinyong.views.myrc_collectprice'),
	(r'^redelfavorite.html$', 'zz91yinyong.views.redelfavorite'),
	
	(r'^myrc_leavewords/$', 'zz91yinyong.views.myrc_leavewords'),
	(r'^myrc_favorite/$', 'zz91yinyong.views.myrc_favorite'),
#	(r'^myrc_products/$', 'zz91yinyong.views.myrc_products'),
	#----供求发布保存修改
	(r'^products_publish/$', 'zz91yinyong.views.products_publish'),
	(r'^products_save/$', 'zz91yinyong.views.products_save'),
	(r'^products_update/$', 'zz91yinyong.views.products_update'),
	(r'^products_updatesave/$', 'zz91yinyong.views.products_updatesave'),
	(r'^products_refresh/$', 'zz91yinyong.views.products_refresh'),
	#----记录客户浏览页面
	(r'^addrecordeddata/$', 'zz91yinyong.views.addrecordeddata'),
	#标准版
	
	(r'^standard/$', 'zz91yinyong.view_s.default'),
	(r'^standard/reg/$', 'zz91yinyong.view_s.reg'),
	(r'^standard/reg_save/$', 'zz91yinyong.view_s.reg_save'),
	(r'^standard/login/$', 'zz91yinyong.view_s.login'),
	(r'^standard/loginof/$', 'zz91yinyong.view_s.loginof'),
	(r'^standard/loginout/$', 'zz91yinyong.view_s.loginout'),
	(r'^standard/priceviews/$', 'zz91yinyong.view_s.priceviews'),
	(r'^standard/priceviews/(?P<id>\d+).htm$', 'zz91yinyong.view_s.priceviews1'),
	(r'^standard/priceindex/$', 'zz91yinyong.view_s.priceindex'),
	(r'^standard/huzhuviews/(?P<id>\d+).htm$', 'zz91yinyong.view_s.huzhuviews'),
	(r'^standard/huzhuviews/viewReply(?P<id>\d+).htm$', 'zz91yinyong.view_s.huzhuviews'),
	(r'^standard/price/$', 'zz91yinyong.view_s.price'),
	(r'^standard/huzhu/$', 'zz91yinyong.view_s.huzhu'),
	(r'^standard/huzhu_replay/$', 'zz91yinyong.view_s.huzhu_replay'),
	(r'^standard/productslist/$', 'zz91yinyong.view_s.productslist'),
	(r'^standard/searchindex/$', 'zz91yinyong.view_s.searchindex'),
	(r'^standard/productscategory/$', 'zz91yinyong.view_s.productscategory'),
	(r'^standard/provincecategory/$', 'zz91yinyong.view_s.provincecategory'),
	(r'^standard/companylist/$', 'zz91yinyong.view_s.companylist'),
	(r'^standard/productdetail/$', 'zz91yinyong.view_s.productdetail'),
	(r'^standard/companydetail/$', 'zz91yinyong.view_s.companydetail'),
	(r'^standard/companyinfo/$', 'zz91yinyong.view_s.companyinfo'),
	(r'^standard/companyproducts/$', 'zz91yinyong.view_s.companyproducts'),
	(r'^standard/favorite/$', 'zz91yinyong.view_s.favorite'),
	(r'^standard/myrc_index/$', 'zz91yinyong.view_s.myrc_index'),
	(r'^standard/myrc_leavewords/$', 'zz91yinyong.view_s.myrc_leavewords'),
	(r'^standard/myrc_favorite/$', 'zz91yinyong.view_s.myrc_favorite'),
	
	#----网站索引
	(r'^zz91index/$', 'zz91yinyong.views_sy.default'),
	(r'^zz91index/p(?P<id>\d+)-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.plist'),
	(r'^zz91index/p-p(?P<pinyin>\w+)-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.plist_pinyin'),
	(r'^zz91index/c(?P<id>\d+)-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.clist'),
	(r'^zz91index/c-p(?P<pinyin>\w+)-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.clist_pinyin'),
	(r'^zz91index/tags-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.tagslist'),
	(r'^zz91index/tags-(?P<pinyin>\w+)-(?P<page>\d+).htm$', 'zz91yinyong.views_sy.tagslist_pinyin'),
	(r'^zz91index/p_date.htm$', 'zz91yinyong.views_sy.plist_date'),
	
	(r'^zz91register/$', 'zz91yinyong.views.zz91register'),
	(r'^zz91registerSucceed/$', 'zz91yinyong.views.zz91registerSucceed'),
	(r'^zz91registerSave/$', 'zz91yinyong.views.zz91registerSave'),
	(r'^zz91regGetemail/$', 'zz91yinyong.views.zz91regGetemail'),
	(r'^zz91regGetusername/$', 'zz91yinyong.views.zz91regGetusername'),
	(r'^zz91regGetzz91yinyong/$', 'zz91yinyong.views.zz91regGetzz91yinyong'),
	(r'^zz91verifycode/$', 'zz91yinyong.views.zz91verifycode'),
	(r'^getkl91baojia/$', 'zz91yinyong.views.getkl91baojia'),
#	(r'^kl91price/$', 'zz91yinyong.views.kl91price'),
#	(r'^kl91pricedetail/$', 'zz91yinyong.views.kl91pricedetail'),
	(r'^tradedetail_price/$', 'zz91yinyong.views.tradedetail_price'),
	(r'^province.html$', 'zz91yinyong.views.jsprovince'),
	(r'^provincejs.js$', 'zz91yinyong.views.provincejs'),
	(r'^areahtml/$', 'zz91yinyong.views.areahtml'),
	(r'^keywordsearch/$', 'zz91yinyong.views.keywordsearch'),
	
	#其他应用
	
	(r'^showadscript/$', 'zz91yinyong.views.showadscript'),
	(r'^showcommadscript/$', 'zz91yinyong.views.showcommadscript'),
	(r'^showcompanyadscript/$', 'zz91yinyong.views.showcompanyadscript'),
	(r'^showppctxtadscript/$', 'zz91yinyong.views.showppctxtadscript'),
	(r'^showppctxtadscript2/$', 'zz91yinyong.views.showppctxtadscript2'),
	(r'^showppccomplist/$', 'zz91yinyong.views.showppccomplist'),
	(r'^showppccomplist2/$', 'zz91yinyong.views.showppccomplist2'),
	(r'^showppccomplist_pic/$', 'zz91yinyong.views.showppccomplist_pic'),
	
	
	
	(r'^app/areyouknow.html$', 'zz91yinyong.views.areyouknow'),
	(r'^app/areyouknowmore.html$', 'zz91yinyong.views.areyouknowmore'),
	(r'^app/ppchit.html$', 'zz91yinyong.views.ppchit'),
	(r'^app/yangad.html$', 'zz91yinyong.yang.yangad'),
	(r'^app/yangad_long.html$', 'zz91yinyong.yang.yangad_long'),
	
	#----改变图片大小
	(r'^app/changepic.html$', 'zz91yinyong.views.changepic'),
	#(r'^app/i/(?P<width>\d+)x(?P<height>\d+)/(?P<imgurl>\w+).jpg$', 'zz91yinyong.views.showimg'),
	(r'^img/(?P<width>\d+)x(?P<height>\d+)/(?P<path>.*)$', 'zz91yinyong.views.showimg'),
	
	#----二维码
	(r'^app/qrcodeimg.html$', 'zz91yinyong.views.qrcodeimg'),
	(r'^app/getzhidahtml.html$', 'zz91yinyong.views.getzhidahtml'),
	(r'^app/useragent.html$', 'zz91yinyong.views.useragent'),
	
	
	#----获得资讯列表
	(r'^news/javagetnewslist.html$', 'zz91yinyong.views.javagetnewslist'),
	(r'^news/javagetnewslist_json.html$', 'zz91yinyong.views.javagetnewslist_json'),
	#----调用企业报价json
	(r'^price/javagetcompanyprice_json.html$', 'zz91yinyong.views.javagetcompanyprice_json'),
	(r'^calllogin/$', 'zz91yinyong.views.calllogin'),
	(r'^companyindexnewproducts/$', 'zz91yinyong.views.companyindexnewproducts'),
	(r'^companyindexnewcomplist/$', 'zz91yinyong.views.companyindexnewcomplist'),
	(r'^showhuanbaoindexpic/$', 'zz91yinyong.views.showhuanbaoindexpic'),
	#二维码
	(r'^getdomainpic(?P<company_id>\d+).html$', 'zz91yinyong.views.getdomainpic'),
	(r'^getvcardpic(?P<company_id>\d+).html$', 'zz91yinyong.views.getvcardpic'),
	(r'^getqiyexiupic(?P<company_id>\d+).html$', 'zz91yinyong.views.getqiyexiupic'),
	(r'^getdomainhtml(?P<company_id>\d+).html$', 'zz91yinyong.views.getdomainhtml'),
	
	
#	(r'^jobjoke/$', 'zz91yinyong.jobjoke.jobjoke'),
#	(r'^otherdetail(?P<id>\d+).htm$', 'zz91yinyong.jobjoke.otherdetail'),
	
	(r'^loginredirect.htm$', 'zz91yinyong.views.loginredirect'),
	
	#----积分
	(r'^score/index.html$', 'zz91yinyong.views.weixin_qiandao'),
	(r'^score/helptxt.html$', 'zz91yinyong.views.weixin_helptxt'),
	(r'^score/scorelist.html$', 'zz91yinyong.views.weixin_scorelist'),
	(r'^score/scorelistmore.html$', 'zz91yinyong.views.weixin_scorelistmore'),
	(r'^score/savemoble.html$', 'zz91yinyong.views.weixin_savemoble'),
	(r'^score/prizelist.html$', 'zz91yinyong.views.weixin_prizelist'),
	(r'^score/prizelog.html$', 'zz91yinyong.views.weixin_prizelog'),
	(r'^score/saveprize.html$', 'zz91yinyong.views.weixin_saveprize'),
	
	#----tags手机站转化
	(r'^a/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsPriceList'),
	(r'^b/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsHuzhuList'),
	(r'^d/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsnewsList'),
	(r'^a/(?P<keywords>\w+)-(?P<page>\d+)$', 'zz91yinyong.tagsurl.tagsPriceList'),
	(r'^b/(?P<keywords>\w+)-(?P<page>\d+)$', 'zz91yinyong.tagsurl.tagsHuzhuList'),
	(r'^d/(?P<keywords>\w+)-(?P<page>\d+)$', 'zz91yinyong.tagsurl.tagsnewsList'),
	(r'^c/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsPriceCompanyList'),
	(r'^c/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsPriceCompanyList'),
	(r'^s/(?P<keywords>\w+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagssearchList_hex'),
	(r'^s/(?P<keywords>\w+)-(?P<page>\d+)$', 'zz91yinyong.tagsurl.tagssearchList_hex'),	
	(r'^s/(?P<keywords>\w+)-(?P<kind>\d+)-(?P<page>\d+)/$', 'zz91yinyong.tagsurl.tagsTradeList'),
	(r'^s/(?P<keywords>\w+)-(?P<kind>\d+)-(?P<page>\d+)$', 'zz91yinyong.tagsurl.tagsTradeList'),
	(r'^s/(?P<keywords>\w+)/$', 'zz91yinyong.tagsurl.tagsmain'),
	(r'^s/(?P<keywords>\w+)$', 'zz91yinyong.tagsurl.tagsmain'),
	
	(r'^webapp/$', 'zz91yinyong.webapp.index'),
	(r'^closefloatapp.html$', 'zz91yinyong.views.closefloatapp'),
	#抽奖获得2015
	(r'^choujiangstaus.html$', 'zz91yinyong.views.choujiangstaus'),
	(r'^choujiangcount.html$', 'zz91yinyong.views.choujiangcount'),
	#2016砸金蛋活动
	(r'^zajindanstaus.html$', 'zz91yinyong.views.zajindanstaus'),
	(r'^zajindancount.html$', 'zz91yinyong.views.zajindancount'),
	#2016刮刮乐活动
	(r'^guagualecount.html$', 'zz91yinyong.views.guagualecount'),
	(r'^guagualestaus.html$', 'zz91yinyong.views.guagualestaus'),
	

	(r'^(?!admin)(?P<path>.*)$','django.views.static.serve',{'document_root':STATIC_ROOT}),
	
)

handler404 = 'zz91yinyong.views.viewer_404'
handler500 = 'zz91yinyong.views.viewer_500'


