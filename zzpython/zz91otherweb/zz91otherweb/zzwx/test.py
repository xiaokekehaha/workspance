﻿from client import *
import sys
import urllib
reload(sys)
sys.setdefaultencoding('UTF-8')
client = Client("wxb3a1f99915ac43ed", "6514984261ac291bfd6ef38ab150fcfb")
menujson={
     "button":[
	 {
           "name":"商机分析",
           "sub_button":[
            {	
               "type":"click",
               "name":"来电分析",
               "key":"fenxi"
            },
			{	
			   "type":"view",
               "name":"商机搜索",
               "url":"http://m.zz91.com/ldb_weixin/businessearch.html"
            }]
      },
	  {
           "name":"账户管理",
		   "sub_button":[
            {	
               "type":"view",
               "name":"账户余额",
               "url":"http://m.zz91.com/ldb_weixin/balance.html"
            },
			{	
				"type":"view",
               "name":"电话清单",
               "url":"http://m.zz91.com/ldb_weixin/phonerecords.html"
            },
			{	
				"type":"view",
               "name":"点击清单",
               "url":"http://m.zz91.com/ldb_weixin/phoneclick.html"
            }]
		   
       },
       {
           "name":"+更多",
           "sub_button":[
			{	
			   "type":"view",
               "name":"商机中心",
               "url":"http://m.zz91.com/"
            },
			{
               "type":"view",
               "name":"公司介绍",
               "url":"http://m.zz91.com/ldb_weixin/about.html"
            },
			{
               "type":"view",
               "name":"产品介绍",
               "url":"http://m.zz91.com/ldb_weixin/product_introduction.html"
            },
			{
               "type":"view",
               "name":"联系我们",
               "url":"http://m.zz91.com/ldb_weixin/contact.html"
            }]
       }]
 }
#client.get_menu()
client.create_menu(menujson)
print client.grant_token()
#client.send_text_message("okX-XjqMW7vdDUeaRZj8ebEKaJt8","afs")
#client.get_followers()