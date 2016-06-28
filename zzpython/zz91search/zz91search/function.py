﻿#@param htmlstr HTML字符串.
def filter_tags(htmlstr):
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    s=replaceCharEntity(s)#替换实体
    return s
##替换常用HTML字符实体.
#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':' ','160':' ',
                'lt':'<','60':'<',
                'gt':'>','62':'>',
                'amp':'&','38':'&',
                'quot':'"','34':'"',}
   
    re_charEntity=re.compile(r'&#?(?P<name>\w+);')
    sz=re_charEntity.search(htmlstr)
    while sz:
        entity=sz.group()#entity全称，如&gt;
        key=sz.group('name')#去除&;后entity,如&gt;为gt
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1)
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            #以空串代替
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr
def subString(string,length):   
    if length >= len(string):   
        return string   
    result = ''  
    i = 0  
    p = 0  
    while True:   
        ch = ord(string[i])   
        #1111110x   
        if ch >= 252:   
            p = p + 6  
        #111110xx   
        elif ch >= 248:   
            p = p + 5  
        #11110xxx   
        elif ch >= 240:   
            p = p + 4  
        #1110xxxx   
        elif ch >= 224:   
            p = p + 3  
        #110xxxxx   
        elif ch >= 192:
            p = p + 2  
        else:   
            p = p + 1      
               
        if p >= length:   
            break;
        else:   
            i = p   
    return string[0:i]
    pass
#获得明感字符
def getmingganword(s):
    if not s:
        return 1
    file = open(limitpath)
    list=[]
    lines = file.readlines(100000)
    if lines:
        for line in lines:
            line=line.strip('\n').strip()
            if line in s:
                return 1
                break
            list.append(line)
    if s in list:
        return 2
    if "激情" in s:
        return 2
    if "乱伦" in s:
        return 2
    
    return None
#----判断是否样品
def getyangflag(products_id):
    sql="select a.sample_id from sample_relate_product as a left join sample as b on a.sample_id=b.id where product_id=%s and b.is_del=0"
    cursor.execute(sql,[products_id])
    productlist = cursor.fetchone()
    if productlist:
        return productlist[0]
#----获得拿样价
def gettakeprice(sample_id):
    sql='select take_price from sample where id=%s'
    cursor.execute(sql,sample_id)
    result = cursor.fetchone()
    if result:
        return result[0]
#加密
def getjiami(strword):
    return strword.encode('utf8','ignore').encode("hex")
def getjiemi(strword):
    return strword.decode("hex").decode('utf8','ignore')
#静态文件保存
def _key_to_file(pth):
    pth = str(pth)
    return '/usr/data/offerlist/'+pth+'/'
def getstaticValue(pth,key):
    fname = _key_to_file(pth)
    if not (os.path.exists(fname+str(key)+'.pkl')):
        return None
    else:
        pkl_file = open(fname+str(key)+'.pkl','rb')
        return pickle.load(pkl_file)
        pkl_file.close()
def updatetaticValue(pth,key,list):
    fname = _key_to_file(pth)
    if not os.path.exists(fname):
        os.makedirs(fname)
    output = open(fname+str(key)+".pkl", 'wb')
    pick = pickle.Pickler(output)
    pick.dump(list)
    output.close()
    
def getproid(id):
    fname = _key_to_file(id)
    if not (os.path.exists(fname+str(id)+'.pkl')):
        return None
    else:
        pkl_file = open(fname+str(id)+'.pkl','rb')
        return pickle.load(pkl_file)
        pkl_file.close()
def updateproid(id,list):
    fname = _key_to_file(id)
    if not os.path.exists(fname):
        os.makedirs(fname)
    output = open(fname+str(id)+".pkl", 'wb')
    pick = pickle.Pickler(output)
    pick.dump(list)
    output.close()
#判断是否为中文
def is_cn_char(i): 
    return 0x4e00<=ord(i)<0x9fa6
def getsearcher():
    purl = '/usr/data/offerlist/'
    if not (os.path.exists(purl+"searcher.txt")):
        f = open(purl+"searcher.txt",'w')
        f.write('offersearch_new')
    f = open(purl+"searcher.txt",'r')
    return f.read()
    f.close()
def updatesearcher(value):
    purl = '/usr/data/offerlist/'
    f = open(purl+"searcher.txt",'w')
    f.write(value)
    f = open(purl+"searcher.txt",'r')
    f.close()
def englishlist():
    pinyin=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return pinyin
#获得中文首拼音
def single_get_first(unicode1):
    str1 = unicode1.encode('gbk')
    try:        
        ord(str1)
        return str1
    except:
        asc = ord(str1[0]) * 256 + ord(str1[1]) - 65536
        if asc >= -20319 and asc <= -20284:
            return 'a'
        if asc >= -20283 and asc <= -19776:
            return 'b'
        if asc >= -19775 and asc <= -19219:
            return 'c'
        if asc >= -19218 and asc <= -18711:
            return 'd'
        if asc >= -18710 and asc <= -18527:
            return 'e'
        if asc >= -18526 and asc <= -18240:
            return 'f'
        if asc >= -18239 and asc <= -17923:
            return 'g'
        if asc >= -17922 and asc <= -17418:
            return 'h'
        if asc >= -17417 and asc <= -16475:
            return 'j'
        if asc >= -16474 and asc <= -16213:
            return 'k'
        if asc >= -16212 and asc <= -15641:
            return 'l'
        if asc >= -15640 and asc <= -15166:
            return 'm'
        if asc >= -15165 and asc <= -14923:
            return 'n'
        if asc >= -14922 and asc <= -14915:
            return 'o'
        if asc >= -14914 and asc <= -14631:
            return 'p'
        if asc >= -14630 and asc <= -14150:
            return 'q'
        if asc >= -14149 and asc <= -14091:
            return 'r'
        if asc >= -14090 and asc <= -13119:
            return 's'
        if asc >= -13118 and asc <= -12839:
            return 't'
        if asc >= -12838 and asc <= -12557:
            return 'w'
        if asc >= -12556 and asc <= -11848:
            return 'x'
        if asc >= -11847 and asc <= -11056:
            return 'y'
        if asc >= -11055 and asc <= -10247:
            return 'z'
        return ''
#获得城市信息
def getnavareavalue(code):
    sql="select label,code from category where code='"+code+"'"
    cursor.execute(sql)
    result=cursor.fetchone()
    if result:
        area2=result[0]
        return result
def getcategorylabel(code):
    if code:
        sql="select label from category where code='"+code+"'"
        cursor.execute(sql)
        result=cursor.fetchone()
        if result:
            return result[0]
def getnextareavalue(code):
    sql="select code,label from category where code like '"+str(code)+"____'"
    cursor.execute(sql)
    listall=[]
    result=cursor.fetchall()
    if result:
        for list in result:
            list={'code':list[0],'label':list[1],'firstpinyin':single_get_first(list[1])}
            listall.append(list)
    return listall

#获得城市
def getareavalue(code):
    codelen=len(code)
    provincevalue=mc.get("pro_provincevalue"+str(code))
    if provincevalue:
        listall=provincevalue
    else:
        sql="select code,label from category where left(code,"+str(codelen)+")=%s and length(code)="+str(codelen+4)+" order by show_index asc"
        cursor.execute(sql,code)
        result=cursor.fetchall()
        listall=[]
        if (result):
            for list in result:
                nextprovincelist=getnextareavalue(list[0])
                list2={'code':list[0],'label':list[1],'firstpinyin':single_get_first(list[1]),'nextprovincelist':nextprovincelist}
                listall.append(list2)
        mc.set("pro_provincevalue"+str(code),listall,0)
    return listall


def getcompinfo(pdtid,cursor,keywords):
    #获得缓存
    zz91search_getcompinfo=cache.get("zz91search_getcompinfo"+str(pdtid))
    if zz91search_getcompinfo:
        return zz91search_getcompinfo
    keywords=keywords.replace('\\','')
    keywords=keywords.replace('/','')
    keywords=keywords.replace('/','')
    keywords=keywords.replace('(','')
    keywords=keywords.replace(')','')
    keywords=keywords.replace('+','')
    keywords=keywords.upper()
    sql="SELECT c.id AS com_id, c.name AS com_name, p.id AS pdt_id, RIGHT( p.products_type_code, 1 ) AS pdt_kind, p.title AS pdt_name, p.details AS pdt_detail, DATE_FORMAT(p.refresh_time,'%Y/%m/%d'), c.domain_zz91 AS com_subname, p.price AS pdt_price,c.membership_code,e.label as city,p.min_price,p.max_price,p.price_unit,p.total_quantity,DATE_FORMAT(p.expire_time,'%Y-%m-%d'),DATEDIFF(p.expire_time,CURDATE()) as yxtime,p.quantity_unit,f.label,c.address,DATE_FORMAT(c.regtime,'%Y-%m-%d'),c.area_code,p.check_status FROM products AS p LEFT OUTER JOIN company AS c ON p.company_id = c.id LEFT OUTER JOIN category as e ON c.area_code=e.code left outer join category_products as f on p.category_products_main_code=f.code where p.id="+str(pdtid)+""
    cursor.execute(sql)
    productlist = cursor.fetchone()
    if productlist:
        arrpdt_kind={'kindtxt':'','kindclass':''}
        pdt_kind=productlist[3]
        viptype=str(productlist[9])
        if (str(pdt_kind) == '1'):
            arrpdt_kind['kindtxt']='求购'
            arrpdt_kind['kindclass']='buy'
        else:
            arrpdt_kind['kindtxt']='供应'
            arrpdt_kind['kindclass']='sell'
        arrviptype={'vippic':'','vipname':'','vipsubname':'','vipcheck':'','com_fqr':'','zstNum':'','ldb':''}
        if (viptype == '10051000'):
            arrviptype['vippic']=None
            arrviptype['vipname']='普通会员'
        if (viptype == '10051001'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/recycle.gif'
            arrviptype['vipname']='再生通'
        if (viptype == '100510021000'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptSilver.gif'
            arrviptype['vipname']='银牌品牌通'
        if (viptype == '100510021001'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptGold.gif'
            arrviptype['vipname']='金牌品牌通'
        if (viptype == '100510021002'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptDiamond.gif'
            arrviptype['vipname']='钻石品牌通'
        if (viptype == '10051000'):
            arrviptype['vipcheck']=None
        else:
            arrviptype['vipcheck']=1
        #来电宝客户
        sqll="select id from crm_company_service where company_id="+str(productlist[0])+" and crm_service_code in ('1007','1008','1009','1010') and apply_status=1"
        cursor.execute(sqll)
        ldbresult=cursor.fetchone()
        if ldbresult:
            sqlg="select front_tel from phone where company_id="+str(productlist[0])+""
            cursor.execute(sqlg)
            phoneresult=cursor.fetchone()
            if phoneresult:
                arrviptype['ldb']={'ldbphone':phoneresult[0]}
            else:
                arrviptype['ldb']=None
        else:
            arrviptype['ldb']=None
        arrviptype['vipsubname'] = productlist[7]
        arrviptype['com_fqr']=''
        com_province=productlist[10]
        if (com_province==None):
            com_province=''
        pdt_images=""
        area_code=productlist[21]
        #地区信息
        if (area_code):
            sqld="select label from category where code='"+str(area_code[:-4])+"'"
            cursor.execute(sqld)
            arealabel = cursor.fetchone()
            if arealabel:
                if arealabel[0]:
                    com_province=arealabel[0]+' '+com_province
        #公司信息
        if (arrviptype['vipcheck'] or arrviptype['ldb']):
            address=productlist[19]
            regtime=productlist[20]
            if (productlist[0]):
                sqlp="select count(0) from products where company_id="+str(productlist[0])+""
                cursor.execute(sqlp)
                pcopt = cursor.fetchone()
                if pcopt:
                    offercount=pcopt[0]
                else:
                    offercount=0
            
                sqlc="select tel_country_code,tel_area_code,tel,mobile,qq,contact from company_account where company_id="+str(productlist[0])+" "
                cursor.execute(sqlc)
                compinfolist = cursor.fetchone()
                if compinfolist:
                    if (compinfolist[0]):
                        tel_country_code=compinfolist[0]
                    else:
                        tel_country_code=''
                    if (compinfolist[1]):
                        tel_area_code=compinfolist[1]
                    else:
                        tel_area_code=''
                    if (compinfolist[2]):
                        tel=compinfolist[2]
                    else:
                        tel=''
                    tel=tel_country_code+'-'+tel_area_code+'-'+tel
                    mobile=compinfolist[3]
                    qq=compinfolist[4]
                    contact=compinfolist[5]
                    if (qq):
                        qq=qq.strip()
                        if (qq==""):
                            qq=None
                    arrcompinfo={'tel':tel,'mobile':mobile,'address':address,'regtime':regtime,'offercount':offercount,'qq':qq,'contact':contact}
                else:
                    arrcompinfo=None
            else:
                arrcompinfo=None
        else:
            arrcompinfo=None
        #价格范围判断
        allprice=""
        min_price=productlist[11]
        if (min_price==None):
            min_price=''
        else:
            min_price=str(min_price)
            if (min_price!='0.0'):
                allprice=allprice+min_price
        max_price=productlist[12]
        if (max_price==None):
            max_price=''
        else:
            max_price=str(max_price)
            if (max_price!='0.0' and max_price!=min_price):
                allprice=allprice+'-'+max_price
        price_unit=productlist[13]
        total_quantity=productlist[14]
        quantity_unit=productlist[17]
        if (quantity_unit==None):
            quantity_unit=''
        if (total_quantity=='' or total_quantity==' ' or total_quantity==None):
            total_quantity=None
        else:
            total_quantity=total_quantity+quantity_unit
        expire_time=productlist[15]
        yxtime=productlist[16]
        procatetype=productlist[18]
        if (procatetype!=None):
            procatetype=procatetype.replace('|',' ')
            procatetype=procatetype.replace('\\',' ')
            procatetype=procatetype.replace('/',' ')
            procatetype=procatetype.replace('(',' ')
            procatetype=procatetype.replace(')',' ')

        if (str(expire_time)=='9999-12-31'):
            yxtimevalue='长期有效'
        else:
            if (yxtime<0):
                yxtimevalue='已经过期'
            else:
                yxtimevalue='截止：'+str(expire_time)
        #
        if (price_unit==None):
            price_unit=''
        else:
            if (allprice!=''):
                allprice=allprice+price_unit
        #----
        sql1="select pic_address from products_pic where product_id="+str(productlist[2])+" and check_status=1 order by is_default desc,id desc"
        cursor.execute(sql1)
        productspic = cursor.fetchone()
        if productspic:
            pdt_images=productspic[0]
        else:
            pdt_images=""
        if (pdt_images == '' or pdt_images == '0'):
            pdt_images='../cn/img/noimage.gif'
        else:
            pdt_images='http://img3.zz91.com/100x75/'+pdt_images+''
        #发起人标志
        company_id=productlist[0]
        zs=None
        if (company_id!=None):
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001001' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            fqrflag = cursor.fetchone()
            if fqrflag:
                fqr=1
            else:
                fqr=None
            
            #诚信会员
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001005' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            cxflag = cursor.fetchone()
            if cxflag:
                cxcompany=1
            else:
                cxcompany=None

            #终生会员
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001003' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            zsflag = cursor.fetchone()
            if zsflag:
                zs=1
            else:
                zs=None
            zst_year=0
            #年限
            sql2="select sum(zst_year) from crm_company_service where company_id="+str(company_id)+" and apply_status=1"
            cursor.execute(sql2)
            zstNumvalue = cursor.fetchone()
            if zstNumvalue:
                zst_year=zstNumvalue[0]
            arrviptype['zstNum']=zst_year
        else:
            fqr=None
        #春季推荐
        if (company_id!=None):
            sql1="select a.email from auth_user as a,company_account as b where a.username=b.account and b.company_id="+str(company_id)+""
            cursor.execute(sql1)
            returnemail=cursor.fetchone()
            if (returnemail):
                email=returnemail[0]
                if email:
                    sql2="select a.id from ad as a,ad_position as b where a.position_id=b.id and b.parent_id=232 and a.ad_description='"+email+"' and gmt_plan_end>'"+str(date.today()+timedelta(days=1))+"' and review_status='Y'"
                    cursor_ads.execute(sql2)
                    returnads=cursor_ads.fetchone()
                    if returnads:
                        cjtj=1
                    else:
                        cjtj=None
                else:
                    cjtj=None
            else:
                cjtj=None
        else:
            cjtj=None
        
        
        
        list1={'com_id':productlist[0],'com_name':productlist[1],'pdt_id':productlist[2],'pdt_kind':arrpdt_kind
        ,'pdt_name':productlist[4],'com_province':com_province,'pdt_detail':productlist[5]
        ,'pdt_time_en':productlist[6],'com_subname':productlist[7],'vipflag':arrviptype,'check_status':productlist[22]
        ,'pdt_images':pdt_images,'pdt_price':allprice
        ,'vippaibian':'','pdt_name1':productlist[4],'wordsrandom':1,'fqr':fqr,'cxcompany':cxcompany,'cjtj':cjtj,'total_quantity':total_quantity,'expire_time':expire_time,'yxtimevalue':yxtimevalue,'procatetype':procatetype,'arrcompinfo':arrcompinfo,'zs':zs,'xianhuoid':''}
    else:
        list1=None
        
    #list1=getproid(pdtid)
    if (list1 == None):
        return None
    else:
        pdt_images=list1['pdt_images']
        if (pdt_images=='../cn/img/noimage.gif'):
            list1['pdt_images']='http://img0.zz91.com/front/images/global/noimage.gif'
        pdt_detail=filter_tags(list1['pdt_detail'])
        pdt_detail=pdt_detail.replace('<br>','').replace('&nbsp;',' ')
        docs=[pdt_detail]
        list1['pdt_detail']=subString(pdt_detail,50)+'...'
        
        sqlxx="select id from products_spot where product_id=%s"
        cursor.execute(sqlxx,[pdtid])
        result=cursor.fetchone()
        if result:
            list1['xianhuoid']=result[0]
        else:
            list1['xianhuoid']=None
            
        pdt_name=list1['pdt_name'].upper()
        docs=[pdt_name]
        pdt_name=pdt_name.replace(keywords,'<em>'+keywords+'</em>')
        #for list in keywords:
            #pdt_name=pdt_name.replace(list,'<em>'+list+'</em>')
        list1['pdt_name']=pdt_name    
    #设置缓存
    cache.set("zz91search_getcompinfo"+str(pdtid),list1,60*10)
    return list1

def getproductsinfo(pdtid,cursor,keywords):
    #获得缓存
    zz91search_getproductsinfo=cache.get("zz91search_getproductsinfo"+str(pdtid))
    if zz91search_getproductsinfo:
        return zz91search_getproductsinfo
    keywords=keywords.replace('\\','')
    keywords=keywords.replace('/','')
    keywords=keywords.replace('/','')
    keywords=keywords.replace('(','')
    keywords=keywords.replace(')','')
    keywords=keywords.replace('+','')
    sql="SELECT c.id AS com_id, c.name AS com_name, p.id AS pdt_id, RIGHT( p.products_type_code, 1 ) AS pdt_kind, p.title AS pdt_name, p.details AS pdt_detail, DATE_FORMAT(p.refresh_time,'%Y/%m/%d'), c.domain_zz91 AS com_subname, p.price AS pdt_price,c.membership_code,e.label as city,p.min_price,p.max_price,p.price_unit,p.quantity,DATE_FORMAT(p.expire_time,'%Y-%m-%d'),DATEDIFF(p.expire_time,CURDATE()) as yxtime,p.quantity_unit,f.label,c.address,DATE_FORMAT(c.regtime,'%Y-%m-%d'),c.area_code,p.check_status,p.tags,p.source,p.specification,p.impurity,p.color,p.useful,p.appearance,p.manufacture,p.origin,p.tags FROM products AS p LEFT OUTER JOIN company AS c ON p.company_id = c.id LEFT OUTER JOIN category as e ON c.area_code=e.code left outer join category_products as f on p.category_products_main_code=f.code where p.check_status = '1' and p.id="+str(pdtid)+""
    cursor.execute(sql)
    productlist = cursor.fetchone()
    if productlist:
        arrpdt_kind={'kindtxt':'','kindclass':''}
        pdt_kind=productlist[3]
        viptype=str(productlist[9])
        if (str(pdt_kind) == '1'):
            arrpdt_kind['kindtxt']='求购'
            arrpdt_kind['kindclass']='buy'
        else:
            arrpdt_kind['kindtxt']='供应'
            arrpdt_kind['kindclass']='sell'
        arrviptype={'vippic':'','vipname':'','vipclass':'','vipsubname':'','vipcheck':'','com_fqr':'','zstNum':'','ldb':''}
        if (viptype == '10051000'):
            arrviptype['vippic']=None
            arrviptype['vipname']='普通会员'
        if (viptype == '10051001'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/recycle.gif'
            arrviptype['vipname']='再生通'
            arrviptype['vipclass']='zst_logo'
        if (viptype == '100510021000'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptSilver.gif'
            arrviptype['vipname']='银牌品牌通'
            arrviptype['vipclass']='ypppt_logo'
        if (viptype == '100510021001'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptGold.gif'
            arrviptype['vipname']='金牌品牌通'
            arrviptype['vipclass']='jpppt_logo'
        if (viptype == '100510021002'):
            arrviptype['vippic']='http://img.zz91.com/zz91images/pptDiamond.gif'
            arrviptype['vipname']='钻石品牌通'
            arrviptype['vipclass']='zsppt_logo'
        if (viptype == '10051003'):
            arrviptype['vippic']=''
            arrviptype['vipname']='来电宝客户'
            arrviptype['vipclass']='ldb_logo'
        if (viptype == '10051000'):
            cid=productlist[0]
            if cid:
                # 1.判断是否为 百度优化会员
                sql="select count(*) from crm_company_service where company_id=%s and crm_service_code='10001002' and apply_status='1' and gmt_end>now() and now()>=gmt_start"
                cursor.execute(sql,[cid])
                baiduResult = cursor.fetchone()
                if baiduResult and baiduResult[0]>0:
                    arrviptype['vipcheck']=1
                else :
                    # 2.是否通过认证
                    sql = "SELECT count(0) FROM  company_attest where company_id = %s and check_status = '1' "
                    cursor.execute(sql,[cid])
                    attestResult = cursor.fetchone()
                    if attestResult and attestResult[0]>0:
                        arrviptype['vipcheck']=1
                    else :
                        arrviptype['vipcheck']=None
            else:
                arrviptype['vipcheck']=None
        else:
            arrviptype['vipcheck']=1
        #来电宝客户
        company_id=productlist[0]
        if company_id:
            sqll="select id from crm_company_service where company_id=%s and crm_service_code in(1007,1008,1009,1010) and apply_status=1"
            cursor.execute(sqll,[company_id])
            ldbresult=cursor.fetchone()
            if ldbresult:
                #来电宝号码
                sqlg="select front_tel from phone where company_id="+str(company_id)+" and expire_flag=0"
                cursor.execute(sqlg)
                phoneresult=cursor.fetchone()
                if phoneresult:
                    #arrviptype['ldb']={'ldbphone':phoneresult[0]}
                    ldbphone = phoneresult[0]
                else:
                    ldbphone = None
                    #arrviptype['ldb']=None
                if ldbphone:
                    # 来电宝积分参数
                    sqlg="select level,phone_cost,phone_rate from ldb_level where company_id="+str(company_id)+""
                    cursor.execute(sqlg)
                    scoreresult=cursor.fetchone()
                    if scoreresult :
                        ldbscore = scoreresult[1]
                        ldblevel = scoreresult[0]
                        if scoreresult[0] > 0:
                            ldbmax = 2**(scoreresult[0]-1) * 1000
                        else :
                            ldbmax = 2**0 * 1000
                        if scoreresult[2] > 0:
                            ldbrate =  str(int(scoreresult[2]))+"%"
                        else :
                            ldbrate = "--"
                    else:
                        ldbscore = 0
                        ldblevel = 1
                        ldbmax = 2**0 * 1000
                        ldbrate = "--"
                    # 电话量 注：电话量计算为总计拨打次数（含未接）
                    sqlg="SELECT count(0) FROM phone_log where company_id ="+str(company_id)+" AND call_sn !=  '0'"
                    cursor.execute(sqlg)
                    countresult=cursor.fetchone()
                    if countresult :
                        ldbanswer = countresult[0]
                    else :
                        ldbanswer = 0
                        
                    arrviptype['ldb']={'ldbphone':ldbphone,'ldbscore':ldbscore,'ldblevel':ldblevel,'ldbmax':ldbmax,'ldbrate':ldbrate,'ldbanswer':ldbanswer}
                else:
                    arrviptype['ldb']=None
            else:
                arrviptype['ldb']=None
        arrviptype['vipsubname'] = productlist[7]
        arrviptype['com_fqr']=''
        com_province=productlist[10]
        if (com_province==None):
            com_province=''
        pdt_images=""
        area_code=productlist[21]
        #地区信息
        if (area_code):
            sqld="select label from category where code='"+str(area_code[:-4])+"'"
            cursor.execute(sqld)
            arealabel = cursor.fetchone()
            if arealabel:
                if arealabel[0]:
                    com_province=arealabel[0]+' '+com_province
                    
        arrcompinfo=None
        bindweixin=None
        sqld="select qq,account from company_account where company_id=%s"
        cursor.execute(sqld,[productlist[0]])
        compqq = cursor.fetchone()
        if compqq:
            qq=compqq[0]
            if qq:
                qq=qq.strip()
            if (qq==""):
                qq=None
            if (qq):
                arrcompinfo={'qq':qq}
            account=compqq[1]
            bindweixin=isbindweixin(account)
        #价格范围判断
        allprice=""
        min_price=productlist[11]
        if (min_price==None):
            min_price=''
        else:
            min_price=str(min_price)
            if (min_price!='0.0'):
                allprice=allprice+min_price
        max_price=productlist[12]
        if (max_price==None):
            max_price=''
        else:
            max_price=str(max_price)
            if (max_price!='0.0' and max_price!=min_price):
                allprice=allprice+'-'+max_price
        price_unit=productlist[13]
        #
        if (price_unit==None):
            price_unit=''
        else:
            if (allprice!=''):
                allprice=allprice+price_unit
                
        total_quantity=productlist[14]
        quantity_unit=productlist[17]
        if (quantity_unit==None):
            quantity_unit=''
        if (total_quantity=='' or total_quantity==' ' or total_quantity==None):
            total_quantity=None
        else:
            total_quantity=total_quantity+quantity_unit

        procatetype=productlist[18]
        if (procatetype!=None):
            procatetype=procatetype.replace('|',' ')
            procatetype=procatetype.replace('\\',' ')
            procatetype=procatetype.replace('/',' ')
            procatetype=procatetype.replace('(',' ')
            procatetype=procatetype.replace(')',' ')

        
        
        #----
        sql1="select pic_address from products_pic where product_id="+str(productlist[2])+" and check_status=1 order by is_default desc,id desc"
        cursor.execute(sql1)
        productspic = cursor.fetchone()
        if productspic:
            pdt_images=productspic[0]
        else:
            pdt_images=""
        if (pdt_images == '' or pdt_images == '0'):
            pdt_images='../cn/img/noimage.gif'
        else:
            pdt_images='http://img3.zz91.com/122x93/'+pdt_images+''
        #发起人标志
        zs=None
        cxcompany=None
        if (company_id!=None):
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001001' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            fqrflag = cursor.fetchone()
            if fqrflag:
                fqr=1
            else:
                fqr=None
            
            #诚信会员
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001005' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            cxflag = cursor.fetchone()
            if cxflag:
                cxcompany=1
            else:
                cxcompany=None

            #终生会员
            sql1="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code='10001003' and apply_status=1 and gmt_end>='"+str(date.today())+"'"
            cursor.execute(sql1)
            zsflag = cursor.fetchone()
            if zsflag:
                zs=1
            else:
                zs=None
            zst_year=0
            #年限
            sql2="select sum(zst_year) from crm_company_service where company_id="+str(company_id)+" and apply_status=1"
            cursor.execute(sql2)
            zstNumvalue = cursor.fetchone()
            if zstNumvalue and zstNumvalue[0]>0:
                zst_year=zstNumvalue[0]
                arrviptype['zstNum']=zst_year
        else:
            fqr=None
        #供求更多属性
        sqlm="select property,content from product_addproperties where pid=%s"
        cursor.execute(sqlm,[productlist[2]])
        resultmore=cursor.fetchall()
        listmore=[]
        if resultmore:
            for ll in resultmore:
                if (ll[1]!=None):
                    contentp=ll[1].strip()
                    if (contentp==""):
                        contentp=None
                else:
                    contentp=None
                list={'property':ll[0],'content':contentp}
                listmore.append(list)
        source=productlist[24]
        listmore=getmoreproperty(listmore,'货源地',source)
        origin=productlist[31]
        listmore=getmoreproperty(listmore,'来源产品',origin)
        specification=productlist[25]
        listmore=getmoreproperty(listmore,'产品规格',specification)
        impurity=productlist[26]
        listmore=getmoreproperty(listmore,'杂质含量',impurity)
        color=productlist[27]
        listmore=getmoreproperty(listmore,'颜色',color)
        useful=productlist[28]
        listmore=getmoreproperty(listmore,'用途',useful)
        appearance=productlist[29]
        listmore=getmoreproperty(listmore,'外观',appearance)
        manufacture=productlist[30]
        listmore=getmoreproperty(listmore,'加工说明',getcategorylabel(manufacture))
        
        #询盘量
        questioncount=None
        if company_id:
            questioncount=getquestioncount(company_id)
        tagslist=[]
        tags=productlist[32]
        if tags:
            tagsarray=tags.split(",")
            for i in tagsarray:
                l={'label':i,'label_hex':getjiami(i)}
                tagslist.append(l)
        yangflag=getyangflag(pdtid)
        #拿样价
        takeprice=''
        if yangflag:
            takeprice=gettakeprice(yangflag)
        
        #入住产业带
        if company_id:
            companymarket=getcompanymarket(company_id)
        else:
            companymarket=None
        
        
        pdt_name=productlist[4]
        list1={'com_id':productlist[0],'com_name':productlist[1],'pdt_id':productlist[2],'pdt_kind':arrpdt_kind
        ,'pdt_name':productlist[4],'com_province':com_province,'pdt_detail':productlist[5],'pdt_detailfull':productlist[5]
        ,'pdt_time_en':productlist[6],'com_subname':productlist[7],'vipflag':arrviptype,'check_status':productlist[22]
        ,'pdt_images':pdt_images,'pdt_price':allprice
        ,'vippaibian':'','pdt_name1':productlist[4],'wordsrandom':1,'fqr':fqr
        ,'cxcompany':cxcompany,'total_quantity':total_quantity,'procatetype':procatetype
        ,'zs':zs,'xianhuoid':'','questioncount':questioncount,'tagslist':tagslist
        ,'arrcompinfo':arrcompinfo,'listmore':listmore,'bindweixin':bindweixin,'yangflag':yangflag,'takeprice':takeprice,'companymarket':companymarket}
    else:
        list1=None
        
    #list1=getproid(pdtid)
    if (list1 == None):
        return None
    else:
        pdt_images=list1['pdt_images']
        if (pdt_images=='../cn/img/noimage.gif'):
            list1['pdt_images']='http://img0.zz91.com/front/images/global/noimage.gif'
        pdt_detail=filter_tags(list1['pdt_detail'])
        pdt_detail=pdt_detail.replace('<br>','').replace('&nbsp;',' ')
        docs=[pdt_detail]
        list1['pdt_detail']=subString(pdt_detail,30)+'...'
        """
        sqlxx="select id from products_spot where product_id=%s"
        cursor.execute(sqlxx,[pdtid])
        result=cursor.fetchone()
        if result:
            list1['xianhuoid']=result[0]
        else:
            list1['xianhuoid']=None
        """
        pdt_name=list1['pdt_name']
        docs=[pdt_name]
        pdt_name=pdt_name.replace(keywords,'<em>'+keywords+'</em>')
        #for k in keywords:
            #pdt_name=pdt_name.replace(k,'<em>'+k+'</em>')
        list1['pdt_name']=pdt_name    
    #设置缓存
    cache.set("zz91search_getproductsinfo"+str(pdtid),list1,60*10)    
    return list1
#----获得产品图片列表
def gettradepiclist(id):
    sql1="select pic_address from products_pic where product_id=%s and check_status=1"
    cursor.execute(sql1,id)
    productspic = cursor.fetchall()
    piclist=[]
    if productspic:
        i=1
        for p in productspic:
            
            pimages=p[0]
            if (pimages == '' or pimages == '0' or pimages==None):
                pdt_images='../cn/img/noimage.gif'
                pdt_images_big='../cn/img/noimage.gif'
            else:
                pdt_images="http://img3.zz91.com/155x82/"+pimages+""
                pdt_images_big="http://img3.zz91.com/625x600/"+pimages+""
            picurl={'images':pdt_images,'images_big':pdt_images_big,'num':i}
            piclist.append(picurl)
            i+=1
    return piclist
#公司供求信息 翻页
def getcompanyproductslist(frompageCount,limitNum,company_id,pdt_type):
        cl = SphinxClient()
        servername=settings.SPHINXCONFIG["serverid"]
        serverport=settings.SPHINXCONFIG["port"]
        cl.SetServer ( servername, serverport )
        cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
        if (company_id):
            cl.SetFilter('company_id',[int(company_id)])
        if (pdt_type !='' and pdt_type!=None):
            cl.SetFilter('pdt_kind',[int(pdt_type)])
        cl.SetFilterRange('havepic',1,100)
        cl.SetSortMode( SPH_SORT_EXTENDED,"refresh_time desc" )
        cl.SetLimits (frompageCount,limitNum,limitNum)
        res = cl.Query ('','offersearch_new,offersearch_new_vip')
        listall=[]
        listcount=0
        if res:
            if res.has_key('matches'):
                tagslist=res['matches']
                for match in tagslist:
                    id=match['id']
                    list=getproductsinfo(id,cursor,'')
                    pdtimgs=list['pdt_images']
                    #pdtimgs=pdtimgs.replace('width=150&height=150','width=100&height=75')
                    list['pdt_images']=pdtimgs
                    listall.append(list)
                listcount=res['total_found']
        return {'list':listall,'count':listcount}
def getmoreproperty(listmore,text,value):
    if (value!="" and value!=None):
        value=value.strip()
        listmore.append({'property':text,'content':value})
    return listmore
def getcompanydetail(email,company_id):
    #获得缓存
    zz91search_getcompanydetail=cache.get("zz91search_getcompanydetail"+str(company_id))
    if zz91search_getcompanydetail:
        return zz91search_getcompanydetail
    if (email):
        list=mc.get("goldad"+str(company_id))
    else:
        list=mc.get("companyinfo"+str(company_id))
    #list=None
    if (list==None):
        if company_id:
            sqlp="select count(0) from products where company_id=%s"
            cursor.execute(sqlp,[company_id])
            pcopt = cursor.fetchone()
            if pcopt:
                offercount=pcopt[0]
            else:
                offercount=0
        else:
            offercount=None
        sqlc="select c.name,c.business,a.contact,a.tel_country_code,a.tel_area_code,"
        sqlc=sqlc+"a.tel,mobile,a.fax_country_code,a.fax_area_code,a.fax,a.email,a.sex,"
        sqlc=sqlc+"a.position,a.qq,c.id,c.address,DATE_FORMAT(c.regtime,'%%Y-%%m-%%d'),"
        sqlc=sqlc+"c.domain_zz91,c.membership_code,a.weixin from company as c left join company_account as a on a.company_id=c.id where "
        if (email):
            sqlc=sqlc+"a.email=%s"
            cursor.execute(sqlc,[email])
        else:
            sqlc=sqlc+"c.id=%s"
            cursor.execute(sqlc,[company_id])
        alist=cursor.fetchone()
        if alist:
            compname=alist[0]
            business=alist[1]
            contact=alist[2]
            tel_country_code=alist[3]
            if (str(tel_country_code)=='None'):
                tel_country_code=""
            tel_area_code=alist[4]
            if (str(tel_area_code)=='None'):
                tel_area_code=""
            tel=alist[5]
            
            
            #telephone=tel_country_code+'-'+tel_area_code+'-'+tel
                    
            mobile=alist[6][0:26]
            fax_country_code=alist[7]
            fax_area_code=alist[8]
            fax=alist[9]
            email=alist[10]
            sex=alist[11]
            position=alist[12]
            if (position==None):
                position=""
            position=position.strip()
            qq=alist[13]
            company_id=alist[14]
            address=alist[15]
            regtime=alist[16]
            domain_zz91=alist[17]
            viptype=alist[18]
            # 微信ID
            weixin=alist[19]
            if(weixin!=None and weixin!=""):
                weixin="微信ID："+weixin+"<br/>"
            else:
                weixin=""
                
            #会员判断
            arrviptype={'vippic':'','vipname':'','vipclass':'','vipsubname':'','vipcheck':'','com_fqr':'','zstNum':'','ldb':''}
            if (viptype == '10051000'):
                arrviptype['vippic']=None
                arrviptype['vipname']='普通会员'
            if (viptype == '10051001'):
                arrviptype['vippic']='http://img.zz91.com/zz91images/recycle.gif'
                arrviptype['vipname']='再生通'
                arrviptype['vipclass']='zst_logo'
            if (viptype == '100510021000'):
                arrviptype['vippic']='http://img.zz91.com/zz91images/pptSilver.gif'
                arrviptype['vipname']='银牌品牌通'
                arrviptype['vipclass']='ypppt_logo'
            if (viptype == '100510021001'):
                arrviptype['vippic']='http://img.zz91.com/zz91images/pptGold.gif'
                arrviptype['vipname']='金牌品牌通'
                arrviptype['vipclass']='jpppt_logo'
            if (viptype == '100510021002'):
                arrviptype['vippic']='http://img.zz91.com/zz91images/pptDiamond.gif'
                arrviptype['vipname']='钻石品牌通'
                arrviptype['vipclass']='zsppt_logo'
            if (viptype == '10051000'):
                arrviptype['vipcheck']=None
            else:
                arrviptype['vipcheck']=1
            #年限
            sql2="select sum(zst_year) from crm_company_service where company_id="+str(company_id)+" and apply_status=1"
            cursor.execute(sql2)
            zstNumvalue = cursor.fetchone()
            if zstNumvalue:
                zst_year=zstNumvalue[0]
            arrviptype['zstNum']=zst_year
            #来电宝客户
            sqll="select id from crm_company_service where company_id="+str(company_id)+" and crm_service_code in(1007,1008) and apply_status=1"
            cursor.execute(sqll)
            ldbresult=cursor.fetchone()
            if ldbresult:
                sqlg="select front_tel from phone where company_id="+str(company_id)+""
                cursor.execute(sqlg)
                phoneresult=cursor.fetchone()
                if phoneresult:
                    ldbphone=phoneresult[0]
                else:
                    ldbphone=None
            else:
                ldbphone=None
            #入住产业带
            companymarket=getcompanymarket(company_id)

            list={'name':compname,'businesstop':subString(business,100),'business':business,
            'contact':contact,'tel_country_code':tel_country_code,'tel_area_code':tel_area_code,
            'tel':tel,'mobile':mobile,'fax_country_code':fax_country_code,
            'fax_area_code':fax_area_code,'fax':fax,'email':email,'sex':sex,
            'position':position,'qq':qq,'ldbphone':ldbphone,'address':address,
            'regtime':regtime,'offercount':offercount,'domain_zz91':domain_zz91,'arrviptype':arrviptype,'companymarket':companymarket,'weixin':weixin}
            if arrviptype['vipcheck']==None:
                list = None
            if (email):
                mc.set("goldad"+str(company_id),list,60*60)
            else:
                mc.set("companyinfo"+str(company_id),list,1)
    #设置缓存
    cache.set("zz91search_getcompanydetail"+str(company_id),list,60*10)
    return list

#关键字排名
def keywordsTop(keywords):
    #获得缓存
    #zz91serach_keywordsTop=cache.get("zz91serach_keywordsTop"+str(keywords))
    #if zz91serach_keywordsTop:
        #return zz91serach_keywordsTop
    sql="select product_id from products_keywords_rank where name='"+keywords+"' and start_time<='"+str(date.today()+timedelta(days=1))+"' and end_time>='"+str(date.today())+"' and is_checked=1 and type not in('10431003','10431004')  order by start_time asc"
    cursor.execute(sql)
    results = cursor.fetchall()
    #设置缓存
    #cache.set("zz91serach_keywordsTop"+str(keywords),results,60*10)
    return results
#热门推荐
def keywordstuijian(keywords):
    #获得缓存
    #zz91serach_keywordstuijian=cache.get("zz91serach_keywordstuijian"+str(keywords))
    #if zz91serach_keywordstuijian:
        #return zz91serach_keywordstuijian
    sql="select product_id,url from products_keywords_rank where name='"+keywords+"' and type='10431003' and start_time<='"+str(date.today()+timedelta(days=1))+"' and end_time>='"+str(date.today())+"' and is_checked=1 order by start_time asc"
    cursor.execute(sql)
    results = cursor.fetchall()
    #设置缓存
    #cache.set("zz91serach_keywordstuijian"+str(keywords),results,60*10)
    return results
def keywords_fix(keywords):
    #获得缓存
    #zz91serach_keywords_fix=cache.get("zz91serach_keywords_fix"+str(keywords))
    #if zz91serach_keywords_fix:
        #return zz91serach_keywords_fix
    sql="select product_id from products_keywords_fix where keywords='"+keywords+"' and start_time<='"+str(date.today()+timedelta(days=1))+"' and end_time>='"+str(date.today())+"' and is_checked=1"
    cursor.execute(sql)
    results = cursor.fetchall()
    #设置缓存
    #cache.set("zz91serach_keywords_fix"+str(keywords),results,60*5)
    return results
def updateindexcontent(indexcl,index,zd,docid,values):
    resq = indexcl.UpdateAttributes ( index, [ zd ], { docid:[values]} )
#根据关键字判断导航
def getnavlist(keywords='',limitcount=''):
    #获得缓存
    #zz91serach_getnavlist=cache.get("zz91serach_getnavlist"+str(keywords)+str(limitcount))
    #if zz91serach_getnavlist:
        #return zz91serach_getnavlist
    navlist=""
    sql="select search_label from category_products where label=%s limit 0,1"
    cursor.execute(sql,[keywords])
    results = cursor.fetchone()
    if results:
        if results[0]:
            list=results[0].split("--")
            for p in list:
                if (p!=None and p!="" and p!=keywords and p!="null"):
                    navlist=navlist+"<a href='/trade/s-"+getjiami(p)+".html'>"+p+"</a> > "
            navlist=navlist+" <a href='/trade/s-"+getjiami(keywords)+".html'>"+keywords+"</a>"
    else:
        navlist=keywords
    #设置缓存
    #cache.set("zz91serach_getnavlist"+str(keywords)+str(limitcount),navlist,60*10)
    return navlist

def getnavlist_tj(keywords='',limitcount=''):
    #获得缓存
    #zz91serach_getnavlist_tj=cache.get("zz91serach_getnavlist_tj"+str(keywords)+str(limitcount))
    #if zz91serach_getnavlist_tj:
        #return zz91serach_getnavlist_tj
    navlist=""
    sql="select search_label from category_products where label=%s limit 0,1"
    cursor.execute(sql,[keywords])
    results = cursor.fetchone()
    if results:
        if results[0]:
            list=results[0].split("--")
            for p in list:
                if (p!=None and p!="" and p!=keywords and p!="null"):
                    navlist=navlist+"<a href='c-"+getjiami(p)+"-1.html'>"+p+"</a> > "
            navlist=navlist+" <a href='c-"+getjiami(keywords)+"-1.html'>"+keywords+"</a>"
    else:
        navlist=keywords
    #设置缓存
    #cache.set("zz91serach_getnavlist_tj"+str(keywords)+str(limitcount),navlist,60*10)
    return navlist
#判断是否为HEX码
def gethextype(keywords):
    zwtype=0
    zwflag=0
    strvalue="abcdef0123456789"
    for a in keywords:
        if (a >= u'\u4e00' and a<=u'\u9fa5'):
            zwflag=zwflag+1
    if zwflag>0:
        zwtype=1
    zwflag=0
    if zwtype==0:
        for a in keywords:
            if (strvalue.find(a)==-1):
                zwflag=zwflag+1
        if zwflag>0:
            zwtype=1
    if zwtype==1:
        return False
    else:
        return True
#相关供求类别
def getcategorylist(kname='',limitcount=''):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_ANY )
    #cl.SetSortMode( SPH_SORT_EXTENDED,"sort desc" )
    if (limitcount!=''):
        cl.SetLimits (0,limitcount,limitcount)
    if (kname!=""):
        res = cl.Query (''+kname,'category_products')
    else:
        res = cl.Query ('','category_products')
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                label=attrs['plabel']
                code=attrs['pcode']
                list1={'id':id,'code':code,'label':label,'label_hex':label.encode("hex")}
                listall.append(list1)
            return listall
#类别列表
def getindexcategorylist(code,showflag):
    #获得缓存
    zz91serach_getindexcategorylist=cache.get("zz91serach_getindexcategorylist"+str(code)+str(showflag))
    if zz91serach_getindexcategorylist:
        return zz91serach_getindexcategorylist
    l=len(code)
    sql="select label,code from category_products where code like '"+str(code)+"____' order by sort asc"
    cursor.execute(sql)
    listall_cate=[]
    catelist=cursor.fetchall()
    for a in catelist:
        if (showflag==1):
            sql1="select label from category_products where code like '"+str(a[1])+"____' order by sort asc"
            cursor.execute(sql1)
            listall_cate1=[]
            catelist1=cursor.fetchall()
            for b in catelist1:
                list1={'label':b[0],'label_hex':getjiami(b[0])}
                listall_cate1.append(list1)
        else:
            listall_cate1=None
        list={'label':a[0],'label_hex':getjiami(a[0]),'code':a[1],'catelist':listall_cate1}
        listall_cate.append(list)
        
    
    #设置缓存
    cache.set("zz91serach_getindexcategorylist"+str(code)+str(showflag),listall_cate,60*10)
    return listall_cate
#类别列表
def getindexcategorylist_yl(code,showflag):
    #获得缓存
    zz91serach_getindexcategorylist=cache.get("zz91serach_getindexcategorylist_yl"+str(code)+str(showflag))
    if zz91serach_getindexcategorylist:
        return zz91serach_getindexcategorylist
    l=len(code)
    sql="select label,code,pinyin from category_yuanliao where is_del=0 and code like '"+str(code)+"____' "
    cursor.execute(sql)
    listall_cate=[]
    catelist=cursor.fetchall()
    for a in catelist:
        if (showflag==1):
            sql1="select label,pinyin from category_yuanliao where is_del=0 and code like '"+str(a[1])+"____'"
            cursor.execute(sql1)
            listall_cate1=[]
            catelist1=cursor.fetchall()
            for b in catelist1:
                list1={'label':b[0],'label_hex':getjiami(b[0]),'yl':1,'pinyin':b[1]}
                listall_cate1.append(list1)
        else:
            listall_cate1=None
        list={'label':a[0],'label_hex':getjiami(a[0]),'code':a[1],'catelist':listall_cate1,'pinyin':a[2],'yl':1}
        listall_cate.append(list)
        
    
    #设置缓存
    cache.set("zz91serach_getindexcategorylist_yl"+str(code)+str(showflag),listall_cate,60*10)
    return listall_cate
def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    b=0
    for i in uchar:
        if ord(i) >255:
            b=b+1
        else:
            a=1
    if (b>0):
        return 1
    else:
        return None
#----黄金展位
def getgoldadlist(keywords,code):
    keywords=keywords.replace("%","%%")
    sql="select ad_content,ad_target_url,id,ad_description from ad where position_id=%s and gmt_plan_end>='"+str(date.today()+timedelta(days=1))+"' and search_exact='|1:"+keywords+"|' and review_status='Y' and online_status='Y' order by gmt_start asc,sequence asc"
    cursor_ads.execute(sql,[code])
    alist = cursor_ads.fetchall()
    listall=[]
    if alist:
        for list in alist:
            compinfo=None
            if (is_chinese(list[3])==None):
                compinfo=getcompanydetail(list[3],None)
            list={'url':'http://gg.zz91.com/hit?a='+str(list[2]),'picaddress':list[0],'compinfo':compinfo}
            listall.append(list)
    return listall
    
#----索引标签库列表
def gettagslist(frompageCount,limitNum,keywords):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED,"search_count desc" )
    cl.SetLimits (frompageCount,limitNum,60)
    res = cl.Query ('@(tname) '+keywords,'tagslist')
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall=[]
            for match in tagslist:
                ii=random.randint(1, 4)
                id=match['id']
                attrs=match['attrs']
                tags=attrs['tags']
                list={'id':id,'tags':tags,'tags_hex':tags.encode("hex"),'ii':ii}
                listall.append(list)
            listcount=res['total_found']
            return listall
            
#------最新报价信息
def getindexpricelist(kname="",assist_type_id="",limitcount="",titlelen=""):
    if (titlelen=="" or titlelen==None):
        titlelen=100
    price=SPHINXCONFIG['name']['price']['name']
    serverid=SPHINXCONFIG['name']['price']['serverid']
    port=SPHINXCONFIG['name']['price']['port']
    cl = SphinxClient()
    cl.SetServer ( serverid, port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED,"gmt_order desc" )
    cl.SetLimits (0,limitcount,limitcount)
    if(assist_type_id!=None and assist_type_id!=""):
        cl.SetFilter('assist_type_id',[assist_type_id])
    if (kname):
        res = cl.Query ('@(title,tags) '+kname,price)
    else:
        res = cl.Query ('',price)
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall_baojia=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                title=subString(attrs['ptitle'],titlelen)
                gmt_time=attrs['gmt_time']
                #td_time=gmt_time.strftime('%Y-%m-%d')
                list1={'title':title,'id':id,'gmt_time':gmt_time,'fulltitle':attrs['ptitle'],'url':'http://jiage.zz91.com/detail/'+str(id)+'.html'}
                listall_baojia.append(list1)
            listcount_baojia=res['total_found']
            return listall_baojia
#----最新互助信息
def getindexbbslist(kname='',limitcount='',bbs_post_category_id=''):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED,"post_time desc" )
    cl.SetLimits (0,limitcount,limitcount)
    if(bbs_post_category_id!=None and bbs_post_category_id!=""):
        cl.SetFilter('bbs_post_category_id',[bbs_post_category_id])
    if (kname):
        res = cl.Query ('@(title,tags) '+kname,'huzhu')
    else:
        res = cl.Query ('','huzhu')
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall_news=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                title=attrs['ptitle']
                gmt_time=attrs['ppost_time']
                list1={'title':title,'id':id,'gmt_time':gmt_time,'url':'http://huzhu.zz91.com/viewReply'+str(id)+'.htm'}
                listall_news.append(list1)
            return listall_news
            
#------最新企业报价信息
def getcompanypricelist(kname="",limitcount="",titlelen=""):
    
    if (titlelen=="" or titlelen==None):
        titlelen=100
    company_price=SPHINXCONFIG['name']['company_price']['name']
    serverid=SPHINXCONFIG['name']['price']['serverid']
    port=SPHINXCONFIG['name']['price']['port']
    cl = SphinxClient()
    cl.SetServer ( serverid, port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED,"post_time desc" )
    cl.SetLimits (0,limitcount,limitcount)
    if (kname):
        res = cl.Query ('@title '+kname,company_price)
    else:
        res = cl.Query ('',company_price)
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall_baojia=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                title=subString(attrs['ptitle'],titlelen)
                title=title.replace("\\","-")
                gmt_time=attrs['ppost_time']
                min_price=attrs['min_price']
                max_price=attrs['max_price']
                price_unit=attrs['price_unit']
                list1={'title':title,'id':id,'gmt_time':gmt_time,'min_price':min_price,'max_price':max_price,'price_unit':price_unit,'fulltitle':attrs['ptitle'],'url':'http://jiage.zz91.com/cdetail/'+str(id)+'.html'}
                listall_baojia.append(list1)
            listcount_baojia=res['total_found']
            return listall_baojia
#---供求列表
def getindexofferlist(kname,pdt_type,limitcount):
    
    listall_offerlist=[]
    tuijianlist=keywordstuijian(kname)
    tuijiannum=len(tuijianlist)
    if (tuijianlist!=None and tuijianlist!=''):
        for p in tuijianlist:
            if (p!=''):
                list1=getproductsinfo(p[0],cursor,kname)
                url=p[1]
                if (url=="" or url=="Null"):
                    url=None
                if (list1!=None):
                    list2={'id':list1['pdt_id'],'title':list1['pdt_name1'],'gmt_time':list1['pdt_time_en'],'kindtxt':list1['pdt_kind']['kindtxt'],'fulltitle':list1['pdt_name1'],'pdt_images':list1['pdt_images'],'url':url,'hot':1,'vipflag':list1['vipflag']}
                    listall_offerlist.append(list2)
    if tuijiannum>=limitcount:
        return listall_offerlist
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," refresh_time desc" )
    cl.SetLimits (0,limitcount-tuijiannum,limitcount-tuijiannum)
    if (pdt_type!=None and pdt_type!=""):
        cl.SetFilter('pdt_kind',[int(pdt_type)])
    cl.SetFilterRange('havepic',1,100)
    #cl.SetFilter('apply_status',[1])
    cl.SetGroupBy("company_id",SPH_GROUPBY_ATTR)
    
    if (kname==None):
        res = cl.Query ('','offersearch_new,offersearch_new_vip')
    else:
        try:
            res = cl.Query ('@(title,label0,label1,label2,label3,label4,city,province,tags) '+kname,'offersearch_new,offersearch_new_vip')
        except EOFError:
            pass
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            
            for match in itemlist:
                pid=match['id']
                attrs=match['attrs']
                pdt_date=attrs['pdt_date']
                pdt_kind=attrs['pdt_kind']
                kindtxt=''
                if (pdt_kind=='1'):
                    kindtxt="求购"
                else:
                    kindtxt="供应"
                title=subString(attrs['ptitle'],40)
                sql1="select pic_address from products_pic where product_id=%s and check_status=1 order by is_default desc,id desc"
                cursor.execute(sql1,[pid])
                productspic = cursor.fetchone()
                if productspic:
                    pdt_images=productspic[0]
                else:
                    pdt_images=""
                if (pdt_images == '' or pdt_images == '0'):
                    pdt_images='http://img0.zz91.com/front/images/global/noimage.gif'
                else:
                    pdt_images='http://img3.zz91.com/138x110/'+pdt_images+''
                list={'id':pid,'title':title,'gmt_time':pdt_date,'kindtxt':kindtxt,'fulltitle':attrs['ptitle'],'pdt_images':pdt_images,'hot':None}
                listall_offerlist.append(list)
            return listall_offerlist
#---获得供求报价
def getofferprice(id):
    sql="select p.min_price,p.max_price,p.price_unit from products as p where p.id=%s"
    cursor.execute(sql,[id])
    plist = cursor.fetchone()
    if plist:
        #价格范围判断
        allprice=""
        min_price=plist[0]
        if (min_price==None):
            min_price=''
        else:
            min_price=str(min_price)
            if (min_price!='0.0'):
                allprice=allprice+min_price
        max_price=plist[1]
        if (max_price==None):
            max_price=''
        else:
            max_price=str(max_price)
            if (max_price!='0.0' and max_price!=min_price):
                allprice=allprice+'-'+max_price
        price_unit=plist[2]
        #
        if (price_unit==None):
            price_unit=''
        else:
            if (allprice!=''):
                allprice=allprice+price_unit
        if (allprice==""):
            allprice="电议或面议"
        return allprice
    
#---公司库首页有图片的最新供求列表
def getindexofferlist_pic(kname="",pdt_type="",limitcount="",membertype=""):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," refresh_time desc" )
    cl.SetGroupBy("company_id",SPH_GROUPBY_ATTR)
    
    cl.SetLimits (0,limitcount,limitcount)
    if (pdt_type!=None and pdt_type!=""):
        cl.SetFilter('pdt_kind',[int(pdt_type)])
    cl.SetFilterRange('havepic',1,100)
    cl.SetFilterRange('haveprice',2,1000)
    if membertype:
        searchindex="offersearch_new_vip"
        cl.SetFilterRange('length_price',1,100000)
    else:
        searchindex="offersearch_new,offersearch_new_vip"
    if (kname==None):
        res = cl.Query ('',searchindex)
    else:
        res = cl.Query ('@(title,label0,label1,label2,label3,label4,city,province,tags) '+kname,searchindex)
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            listall_offerlist=[]
            for match in itemlist:
                pid=match['id']
                price=getofferprice(pid)
                attrs=match['attrs']
                pdt_date=attrs['pdt_date']
                pdt_kind=attrs['pdt_kind']
                kindtxt=''
                if (pdt_kind=='1'):
                    kindtxt="供应"
                else:
                    kindtxt="求购"
                title=subString(attrs['ptitle'],40)
                sql1="select pic_address from products_pic where product_id=%s and check_status=1 order by is_default desc,id desc"
                cursor.execute(sql1,[pid])
                productspic = cursor.fetchone()
                if productspic:
                    pdt_images=productspic[0]
                else:
                    pdt_images=""
                if (pdt_images == '' or pdt_images == '0'):
                    pdt_images='http://img0.zz91.com/front/images/global/noimage.gif'
                else:
                    pdt_images='http://img3.zz91.com/125x100/'+pdt_images+''
                list={'id':pid,'title':title,'gmt_time':pdt_date,'kindtxt':kindtxt,'fulltitle':attrs['ptitle'],'pdt_images':pdt_images,'price':price}
                listall_offerlist.append(list)
            return listall_offerlist

#----最新加入高会            
def getcompanyindexcomplist(kname,num):
    #-------------供求列表
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," gmt_start desc" )
    cl.SetLimits (0,num,num)
    cl.SetFilter('apply_status',[1])

    nowdate=date.today()-timedelta(days=900)
    nextday=date.today()+timedelta(days=1)
    formatnowdate=time.mktime(nowdate.timetuple())
    formatnextday=time.mktime(nextday.timetuple())
    cl.SetFilterRange('gmt_start',int(formatnowdate),int(formatnextday))
    
    if (kname):
        res = cl.Query ('@(name,business,address,sale_details,buy_details,tags,area_name,area_province) '+kname,'company')
    else:
        res = cl.Query ('','company')
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            listall_company=[]
            for match in itemlist:
                id=match['id']
                attrs=match['attrs']
                comname=attrs['compname']
                business=filter_tags(attrs['pbusiness'])
                
                area_province=attrs['parea_province']
                domain_zz91=attrs['domain_zz91']
                list={'id':id,'comname':comname,'business':business,'area_province':area_province,'domain_zz91':domain_zz91}
                listall_company.append(list)
            return listall_company
def getvipcompanycount():
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," gmt_start desc" )
    cl.SetLimits (0,1,1)
    cl.SetFilter('apply_status',[1])
    res = cl.Query ('','company')
    if res:
        listcount=res['total_found']
    return listcount

def getnomolcompanycount():
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," gmt_start desc" )
    cl.SetLimits (0,1,1)
    #cl.SetFilter('apply_status',[1])
    res = cl.Query ('','company')
    
    if res:
        listcount=res['total_found']
    return listcount
    
#---获得公司的一张供求图片信息
def getoneproductscompany(company_id):    
    sql="select a.pic_address,b.title from products_pic as a left join products as b on a.product_id=b.id where b.company_id=%s and a.check_status=1 order by a.is_default desc limit 0,1"
    cursor.execute(sql,[company_id])
    productspic = cursor.fetchone()
    pdt_title=""
    if productspic:
        pdt_images=productspic[0]
        pdt_title=productspic[1]
    else:
        pdt_images=""
    if (pdt_images == '' or pdt_images == '0'):
        pdt_images='http://img0.zz91.com/front/images/global/noimage.gif'
    else:
        pdt_images='http://img3.zz91.com/200x169/'+pdt_images+''
    return {'pdt_images':pdt_images,'pdt_title':pdt_title}
#----获得公司主营业务
def getcompanybusiness(company_id):
    sql="select business from company where id=%s"
    cursor.execute(sql,[company_id])
    comp = cursor.fetchone()
    if comp:
        return comp[0]
#----是否来电宝客户
def isldb(company_id):
    sqlg="select front_tel from phone where company_id=%s"
    cursor.execute(sqlg,company_id)
    phoneresult=cursor.fetchone()
    if phoneresult:
        return 1
    else:
        return None
#----是否绑定微信
def isbindweixin(account):
    sql="select id from oauth_access where target_account=%s and open_type='weixin.qq.com'"
    cursor.execute(sql,[account]);
    plist=cursor.fetchone()
    if plist:
        return 1
    else:
        return None
#获得留言数
def getquestioncount(company_id):
    sqlg="select qcount from inquiry_count where company_id=%s"
    cursor.execute(sqlg,company_id)
    phoneresult=cursor.fetchone()
    if phoneresult:
        return phoneresult[0]
    else:
        return None
#----最新加入高会(含供求图片)            
def getindexcompanylist_pic(keywords="",num="",frompageCount="",limitNum=""):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," refresh_time desc" )
    cl.SetGroupBy("company_id",SPH_GROUPBY_ATTR)
    cl.SetFilterRange('havepic',1,100)
    cl.SetFilterRange('viptype',1,100)
    if (num):
        cl.SetLimits (0,num,num)
    else:
        cl.SetLimits (frompageCount,limitNum,10000)
        
    if (keywords):
        res = cl.Query ('@(title,label0,label1,label2,label3,label4,city,province,tags) '+keywords,'offersearch_new,offersearch_new_vip')
    else:
        res = cl.Query ('','offersearch_new,offersearch_new_vip')
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            listall_company=[]
            for match in itemlist:
                id=match['id']
                attrs=match['attrs']
                company_id=attrs['company_id']
                business=getcompanybusiness(company_id)
                list=getproductsinfo(id,cursor,keywords)
                list['business']=business
                pdt_images=list['pdt_images']
                pdt_images=pdt_images.replace('width=122&height=93','width=200&height=169')
                list['pdt_images']=pdt_images
                ldbflag=isldb(company_id)
                list['ldbflag']=ldbflag
                listall_company.append(list)
            listcount=res['total_found']
            return {'list':listall_company,'listcount':listcount}
#----最新加入普会
def getcommoncompanylist(keywords="",num="",frompageCount="",limitNum="",ptype="",price="",pic="",companyflag="",picwidth="",picheight=""):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," refresh_time desc" )
    #判断是否公司分组
    if (companyflag):
        cl.SetGroupBy("company_id",SPH_GROUPBY_ATTR)
    if pic:
        cl.SetFilterRange('havepic',1,100)
    cl.SetFilter('viptype',[0])
    cl.SetFilter('check_status',[1])
    if (ptype):
        cl.SetFilter('pdt_kind',[int(ptype)])
    if (price):
        cl.SetFilter('length_price',[0],True)
    if (num):
        cl.SetLimits (0,num,num)
    else:
        cl.SetLimits (frompageCount,limitNum,10000)
        
    if (keywords):
        res = cl.Query ('@(title,label0,label1,label2,label3,label4,tags) '+keywords,'offersearch_new')
    else:
        res = cl.Query ('','offersearch_new')
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            listall_company=[]
            for match in itemlist:
                id=match['id']
                attrs=match['attrs']
                company_id=attrs['company_id']
                #business=getcompanybusiness(company_id)
                list=getproductsinfo(id,cursor,keywords)
                #list['business']=business
                #list['business1']=business[0:100]
                if picwidth:
                    pdt_images=list['pdt_images']
                    pdt_images=pdt_images.replace('width=122&height=93','width='+str(picwidth)+'&height='+str(picheight)+'')
                    list['pdt_images']=pdt_images
                ldbflag=isldb(company_id)
                list['ldbflag']=ldbflag
                listall_company.append(list)
            listcount=res['total_found']
            return {'list':listall_company,'listcount':listcount}
#----第一条供求对于类别
def getfirsttradetype(kname=""):
    sqlc="select code from category_products where label=%s"
    cursor.execute(sqlc,[kname])
    rcategory = cursor.fetchone()
    if rcategory:
        return {'label':kname,'code':rcategory[0]}
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    cl.SetSortMode( SPH_SORT_EXTENDED," refresh_time desc" )
    cl.SetLimits (0,1,1)
    res = cl.Query ('@(title,label0,label1,label2,label3,label4,city,province,tags) '+kname,'offersearch_new,offersearch_new_vip')
    if res:
        if res.has_key('matches'):
            itemlist=res['matches']
            for match in itemlist:
                pid=match['id']
                sql="select category_products_main_code from products where id=%s"
                cursor.execute(sql,[pid])
                productlist = cursor.fetchone()
                if productlist:
                    category_products_main_code=productlist[0]
                    sqlc="select label from category_products where code=%s"
                    cursor.execute(sqlc,[category_products_main_code])
                    rcategory = cursor.fetchone()
                    if rcategory:
                        categorylabe=rcategory[0]
                        return {'label':categorylabe,'code':category_products_main_code}    
                    
#----新闻列表 翻页
def getnewslist(keywords="",frompageCount="",limitNum="",typeid="",allnum="",typeid2="",contentflag=""):
    cursor_news = conn_news.cursor()
    news=SPHINXCONFIG['name']['news']['name']
    serverid=SPHINXCONFIG['name']['news']['serverid']
    port=SPHINXCONFIG['name']['news']['port']
    cl = SphinxClient()
    cl.SetServer ( serverid, port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    if (typeid):
        cl.SetFilter('typeid',typeid)
    if (typeid2):
        cl.SetFilter('typeid2',[typeid2])
    cl.SetSortMode( SPH_SORT_EXTENDED,"id desc" )
    if (allnum):
        cl.SetLimits (frompageCount,limitNum,allnum)
    else:
        cl.SetLimits (frompageCount,limitNum,limitNum)
    if (keywords):
        if "p" == keywords:
            res = cl.Query ('@(flag) '+keywords,news)
        else:
            res = cl.Query ('@(title,keywords) '+keywords,news)
    else:
        res = cl.Query ('',news)
    listall_news=[]
    listcount_news=0
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            for match in tagslist:
                id=match['id']
                newsurl=get_newstype(id,cursor_news)
                attrs=match['attrs']
                title=filter_tags(attrs['ptitle'])
                pubdate=attrs['pubdate']
                pubdate2=timestamp_datetime2(pubdate)
                
                list1={'title':title,'id':id,'pubdate':pubdate2,'newsurl':newsurl}
                listall_news.append(list1)
            listcount_news=res['total_found']
    cursor_news.close()
    return {'list':listall_news,'count':listcount_news}    
#日期格式转换
def timestamp_datetime2(value):
    format = '%m-%d'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt
#----获取最终页当前新闻栏目(一期)
def get_newstype(id,cursor_news):
    sql='select typeid,typeid2 from dede_archives where id=%s'
    cursor_news.execute(sql,[id])
    result=cursor_news.fetchone()
    if result:
        typeid=result[0]
        typeid2=result[1]
        sql2='select typename,keywords from dede_arctype where id=%s'
        cursor_news.execute(sql2,[typeid])
        result2=cursor_news.fetchone()
        if result2:
            list={'typename':result2[0],'url':result2[1],'typeid':typeid,'typeid2':typeid2}
            if typeid2!='0':
                sql3='select keywords from dede_arctype where id=%s'
                cursor_news.execute(sql3,[typeid2])
                result3=cursor_news.fetchone()
                if result3:
                    list['url2']=result3[0]
            return list                
#------供求列表右边报价固定导航
def getrightpricenav(code):
    navlist1=[]
    nav1={'label':'废铜','url':'http://jiage.zz91.com/feitong/'}
    navlist1.append(nav1)
    nav1={'label':'废铁','url':'http://jiage.zz91.com/feitie/'}
    navlist1.append(nav1)
    nav1={'label':'废钢','url':'http://jiage.zz91.com/feigang1/'}
    navlist1.append(nav1)
    nav1={'label':'废铝','url':'http://jiage.zz91.com/feilv/'}
    navlist1.append(nav1)
    nav1={'label':'废镍','url':'http://jiage.zz91.com/feinie/'}
    navlist1.append(nav1)
    nav1={'label':'废不锈钢','url':'http://jiage.zz91.com/feibuxiugang/'}
    navlist1.append(nav1)
    nav1={'label':'废钼钛','url':'http://jiage.zz91.com/feimutai/'}
    navlist1.append(nav1)
    nav1={'label':'国外废金属','url':'http://jiage.zz91.com/guowaifeijinshu/'}
    navlist1.append(nav1)
    nav1={'label':'江浙沪','url':'http://jiage.zz91.com/jiangzhehu/'}
    navlist1.append(nav1)
    nav1={'label':'山东','url':'http://jiage.zz91.com/shandong/'}
    navlist1.append(nav1)
    nav1={'label':'广东','url':'http://jiage.zz91.com/guangdong/'}
    navlist1.append(nav1)
    nav1={'label':'临沂','url':'http://jiage.zz91.com/linyi1/'}
    navlist1.append(nav1)
    nav1={'label':'清远','url':'http://jiage.zz91.com/qingyuan/'}
    navlist1.append(nav1)
    
    navlist2=[]
    nav1={'label':'PP','url':'http://jiage.zz91.com/pp/'}
    navlist2.append(nav1)
    nav1={'label':'PVC','url':'http://jiage.zz91.com/pvc/'}
    navlist2.append(nav1)
    nav1={'label':'PMMA','url':'http://jiage.zz91.com/PMMA/'}
    navlist2.append(nav1)
    nav1={'label':'EVA','url':'http://jiage.zz91.com/EVA/'}
    navlist2.append(nav1)
    nav1={'label':'HDPE','url':'http://jiage.zz91.com/HDPE/'}
    navlist2.append(nav1)
    nav1={'label':'LDPE','url':'http://jiage.zz91.com/LDPE/'}
    navlist2.append(nav1)
    nav1={'label':'TPU','url':'http://jiage.zz91.com/TPU/'}
    navlist2.append(nav1)
    nav1={'label':'PET','url':'http://jiage.zz91.com/PET/'}
    navlist2.append(nav1)
    nav1={'label':'ABS','url':'http://jiage.zz91.com/ABS/'}
    navlist2.append(nav1)
    nav1={'label':'PC','url':'http://jiage.zz91.com/PC/'}
    navlist2.append(nav1)
    nav1={'label':'GPPS','url':'http://jiage.zz91.com/GPPS/'}
    navlist2.append(nav1)
    nav1={'label':'余姚','url':'http://jiage.zz91.com/yuyao/'}
    navlist2.append(nav1)
    nav1={'label':'再生料','url':'http://jiage.zz91.com/suliaozaishengliaojiagehangqing/'}
    navlist2.append(nav1)
    nav1={'label':'新料出厂','url':'http://jiage.zz91.com/chuchangjia/'}
    navlist2.append(nav1)
    nav1={'label':'新料市场','url':'http://jiage.zz91.com/shichangjia/'}
    navlist2.append(nav1)
    
    navlist3=[]
    nav1={'label':'油价快报','url':'http://jiage.zz91.com/youjia/'}
    navlist3.append(nav1)
    nav1={'label':'废纸价格','url':'http://jiage.zz91.com/feizhigedijiage/'}
    navlist3.append(nav1)
    nav1={'label':'废橡胶价格','url':'http://jiage.zz91.com/guoneixiangjiao/'}
    navlist3.append(nav1)
    nav1={'label':'综合废料','url':'http://jiage.zz91.com/hangqingzongshu/'}
    navlist3.append(nav1)
                    
    if (code=='1000' or code=='1005' or code=='1007'):
        return navlist1
    if (code=='1001' or code=='1006' or code=='1003' or code=='1010' or code=='1011'):
        return navlist2
    if (code=='1002' or code=='1004' or code=='1008' or code=='1009'):
        return navlist3
        
#微门户关键词
def getcplist(keywords,limitcount):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    #cl.SetSortMode( SPH_SORT_EXTENDED,"post_time desc" )
    cl.SetLimits (0,limitcount,limitcount)
    res = cl.Query ('@(label) '+keywords,'daohangkeywords')
    listall=[]
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall_news=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                label=attrs['plabel']
                pingyin=attrs['ppinyin']
                list={'label':label,'pingyin':pingyin}
                listall.append(list)
    """
    sql="select label,pingyin from daohang where type=1 and sid=3738 limit 0,200"
    cursor.execute(sql)
    cplist=cursor.fetchall()
    listall=[]
    if cplist:
        for list in cplist:
            list={'label':list[0],'pingyin':list[1]}
            listall.append(list)
    """
    return listall
#产业带
def getmarketlist(keywords):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
    #cl.SetSortMode( SPH_SORT_EXTENDED,"post_time desc" )
    cl.SetLimits (0,10,10)
    if keywords:
        res = cl.Query ('@(name,area,industry,business,category,introduction,address) '+keywords,'market')
    else:
        res = cl.Query (' ','market')
    listall=[]
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall_news=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                company_num=attrs['company_num']
                product_num=attrs['product_num']
                pname=attrs['pname']
                words=attrs['words']
                list={'id':id,'name':pname,'company_num':company_num,'product_num':product_num,'words':words}
                listall.append(list)
    return listall
#公司对应产业带
def getcompanymarket(company_id):
    sql="select a.name,a.words from market as a left join market_company as b on a.id=b.market_id where b.company_id=%s and b.is_quit=0 and a.is_del=0"
    cursor.execute(sql,[company_id])
    mlist=cursor.fetchone()
    if mlist:
        return {'url':'http://y.zz91.com/'+str(mlist[1])+'/','name':str(mlist[0])}
    return None
    
#----优质客户推荐栏目            
def gettjhex1():
    lb="钢铁,稀有金属,贵金属,有色金属,金属混合\复合料,废金属处理设备,金属助剂"
    lb_hex="钢铁,稀有金属,贵金属,有色金属,金属混合|复合料,废金属处理设备,金属助剂"
    alllist=[]
    lbarr=lb.split(",")
    lbarr_hex=lb_hex.split(",")
    i=0
    for a in lbarr:
        list={'name_hex':lbarr_hex[i].encode("hex"),'name':a}
        alllist.append(list)
        i=i+1
    return alllist
def gettjhex2():
    lb="通用废塑料,工程废塑料,塑料颗粒,特种废塑料,塑料混合/复合料,废塑料处理设备,塑料助剂"
    lb_hex="通用废塑料,工程废塑料,塑料颗粒,特种废塑料,塑料混合|复合料,废塑料处理设备,塑料助剂"
    alllist=[]
    lbarr=lb.split(",")
    lbarr_hex=lb_hex.split(",")
    i=0
    for a in lbarr:
        list={'name_hex':lbarr_hex[i].encode("hex"),'name':a}
        alllist.append(list)
        i=i+1
    return alllist
def gettjhex3():
    lb="废纺织品,废纸,二手设备,废电子电器,废橡胶,废轮胎,服务"
    lb_hex="纺织品,废纸,设备,电子电器,橡胶,轮胎,服务"
    alllist=[]
    lbarr=lb.split(",")
    lbarr_hex=lb_hex.split(",")
    i=0
    for a in lbarr:
        list={'name_hex':lbarr_hex[i].encode("hex"),'name':a}
        alllist.append(list)
        i=i+1
    return alllist

#获得原料列表
def getyuanliaolist(kname='',limitcount=''):
    port = settings.SPHINXCONFIG['port']
    cl = SphinxClient()
    cl.SetServer ( settings.SPHINXCONFIG['serverid'], port )
    cl.SetMatchMode ( SPH_MATCH_BOOLEAN )
#     cl.SetSortMode( SPH_SORT_EXTENDED,"@weight desc" )
    cl.SetSortMode( SPH_SORT_EXTENDED,"rrefresh_time desc" )
    cl.SetLimits (0,limitcount,limitcount)
    #有图
    cl.SetFilter('check_status',[1])
    cl.SetFilter('is_del',[0])
    #cl.SetFilterRange('havepic',1,100)
    if (kname):
        res = cl.Query ('@title '+kname,'yuanliao')
    else:
        res = cl.Query ('','yuanliao')
    if res:
        if res.has_key('matches'):
            tagslist=res['matches']
            listall=[]
            for match in tagslist:
                id=match['id']
                attrs=match['attrs']
                title=attrs['ttitle']
                #获得厂家产地
                sql0='select yl.category_main_desc,yl.category_assist_desc,cy.label,yl.price_unit,yl.trade_mark,yl.unit from yuanliao as yl left outer join category_yuanliao as cy on yl.category_main_desc=cy.code where yl.id=%s'
                cursor.execute(sql0,[id])
                result=cursor.fetchone()
                try:
                    if not result[1]:
                        factory=result[2]
                    else:
                        factory=result[1]
                except TypeError:
                    factory='其他'
                try:
                    price_unit=result[3]
                except TypeError:
                    price_unit='元'
                trade_mark=result[4]
                unit=""
                if result[5]:
                    unit="/"+result[5]
                #获得价格
                price=attrs['pprice']
                min_price=attrs['min_price']
                max_price=attrs['max_price']
                has_price='0'#价格标记，判断是否有价格，若没有则页面显示为“面议”
                if price or min_price or max_price:
                    has_price='1'
                '''
                if str(price)=="0":
                    price="面议"
                    price_unit=""
                    unit=""
                '''
                if price:
                    price=price
                elif min_price or max_price:
                    price=str(min_price)+"-"+str(max_price)
                else:
                    price="面议"
                    price_unit=""
                    unit=""
                #取出一张默认的图片
                sql1='select pic_address from yuanliao_pic where yuanliao_id=%s and is_del=0 and check_status=1 and is_default=1'
                cursor.execute(sql1,[id])
                try:
                    #图片的src
                    pic_url='http://img3.zz91.com/122x93/'+cursor.fetchone()[0]
                except TypeError:
                    pic_url='http://img0.zz91.com/front/images/global/noimage.gif'
                list1={'id':id,'title':title,'pic_address':pic_url,'factory':factory,'max_price':has_price,'price':price,'min_price':min_price,'max_price':max_price,'price_unit':price_unit,'trade_mark':trade_mark,'unit':unit}
                listall.append(list1)
            return listall