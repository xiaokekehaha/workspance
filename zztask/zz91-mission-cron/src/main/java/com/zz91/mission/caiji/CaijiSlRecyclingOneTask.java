package com.zz91.mission.caiji;

import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.jsoup.Jsoup;
import org.jsoup.safety.Whitelist;

import com.zz91.mission.domain.subscribe.Price;
import com.zz91.task.common.ZZTask;
import com.zz91.util.datetime.DateUtil;
import com.zz91.util.db.pool.DBPoolFactory;
import com.zz91.util.http.HttpUtils;
import com.zz91.util.lang.StringUtils;
import com.zz91.util.log.LogUtil;
import com.zz91.util.mail.MailUtil;

public class CaijiSlRecyclingOneTask implements ZZTask{
    
    final static String PRICE_OPERTION = "price_caiji";
    final static String DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";
    CaiJiCommonOperate operate = new CaiJiCommonOperate();

    final static Map<String, String> RECYCLEDPLASTIC_MAP = new HashMap<String, String>();
    static{
        // httpget 使用的编码 不然会有乱码
        RECYCLEDPLASTIC_MAP.put("charset", "gbk");
        RECYCLEDPLASTIC_MAP.put("url", "http://info.1688.com");// 采集地址
        RECYCLEDPLASTIC_MAP.put("98", "http://info.1688.com/nlist/n90.html," +
                "http://info.1688.com/nlist/n79.html," + "http://info.1688.com/nlist/n84.html," + 
                "http://info.1688.com/nlist/n80.html," + "http://info.1688.com/nlist/n83.html");
        RECYCLEDPLASTIC_MAP.put("listStart", "<div class=\"content\">"); // 列表页开头
        RECYCLEDPLASTIC_MAP.put("listEnd", "<div class=\"module mod-paging\">"); // 列表页结尾

        RECYCLEDPLASTIC_MAP.put("split", "</li>");

        RECYCLEDPLASTIC_MAP.put("contentStart", "<div class=\"d-content\">");
        RECYCLEDPLASTIC_MAP.put("contentEnd", "(责任编辑：");
    }

    @Override
    public boolean init() throws Exception {
        return false;
    }

    @Override
    public boolean exec(Date baseDate) throws Exception {
        String defaultTime = DateUtil.toString(baseDate, DATE_FORMAT).substring(11,16);
        int flagFailure = 0 ;
        Integer typeId = 98;
        Map<String, String> urlmap = new HashMap<String, String>();
        String errContentUrl = "";
        do {
            String content = "";
            String typeValue = RECYCLEDPLASTIC_MAP.get("" + typeId);
            String[] linkArray = typeValue.split(",");
            for (String url : linkArray) {
                content = HttpUtils.getInstance().httpGet(url,
				        RECYCLEDPLASTIC_MAP.get("charset"),20000,20000);
                if(content==null){
                    errContentUrl = errContentUrl + " 抓取来源网站内容失败！请点击<a href='" +  url +"'>"
                            + "<font color='#FF0000'>阿里巴巴-塑料再生料1"+"("+typeId+")"+"</font></a>查看来源网站是否更改地址！<br />";
                    LogUtil.getInstance().log(
                            "caiji-auto", PRICE_OPERTION, null, "{'title':'塑料再生料1("+typeId+")','type':'failure','url':'<a href='" + url +"' target='_blank'>"
                                    + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");
                    flagFailure++;
                    continue;
                }
                Integer start = content.indexOf(RECYCLEDPLASTIC_MAP.get("listStart"));
                Integer end = content.indexOf(RECYCLEDPLASTIC_MAP.get("listEnd"));
                String result = operate.subContent(content, start, end);
                if (StringUtils.isEmpty(result)) {
                    continue;
                }
                // 分解list 为多个元素
                String[] str = result.split(RECYCLEDPLASTIC_MAP.get("split"));

                // 检查日期是否对应今天
                String format = DateUtil.toString(baseDate, "MM-dd");
                List<String> list = new ArrayList<String>();

                for (String s : str) {
                    if (s.indexOf(format) != -1 ) {
                        
                            if (s.indexOf("各地PE再生") != -1
                                    || s.indexOf("各地PVC再生") != -1
                                    || s.indexOf("各地PP再生") != -1
                                    || s.indexOf("各地ABS再生") != -1
                                    || s.indexOf("各地PET再生") != -1
                                    || s.indexOf("各地PS再生") != -1) {
                                list.add(s);
                            }
                    }
                }
                if(list.size()<1){
                    errContentUrl = errContentUrl + " 抓取失败，来源网站没有数据可抓取！请点击<a href='" +  url +"'>"
                            + "<font color='#FF0000'>阿里巴巴-塑料再生料1"+"("+typeId+")"+"</font></a>查看来源网站<br />";
                    LogUtil.getInstance().log(
                            "caiji-auto", PRICE_OPERTION, null, "{'title':'塑料再生料1("+typeId+")','type':'failure','url':'<a href='" + url +"' target='_blank'>"
                                    + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");
                    flagFailure++;
                    continue;
                }

                String typeName = operate.queryTypeNameByTypeId(typeId);

                for (String aStr : list) {
                    String linkStr = operate.getAlink(aStr);
                    if (StringUtils.isEmpty(linkStr)) {
                        continue;
                    } else {
                        String[] alink = linkStr.split("\"");
                        if (alink.length > 0) {
                                String resultTitle = Jsoup.clean(linkStr,Whitelist.none());
                                resultTitle = resultTitle.replace("各地", "");
                                resultTitle = resultTitle.replace("最新报价", "价格");
                            String resultContent = "";
                            /*String resultLink = alink[1];
                            out.put("resultLink", resultLink);*/
                            resultContent = operate.getContent(RECYCLEDPLASTIC_MAP, alink[1]);
                            if (StringUtils.isEmpty(resultContent)) {
                                continue;
                            }
                            // 获取内容
//                          resultContent = resultContent.toLowerCase();
                            resultContent = resultContent.replaceAll("&nbsp;", "");
                            resultContent = Jsoup.clean(
                                    resultContent,Whitelist
                                            .none()
                                            .addTags("p", "table", "th", "tr","td","b","br")
                                            .addAttributes("td", "rowspan","colspan"));
                            resultContent = resultContent.replace(" <td><b>趋势图</b></td>", "");
                            resultContent = resultContent.replace(" <td>趋势图</td>", "");

                            Price price = new Price();
                            price.setTitle(resultTitle);
                            price.setTypeId(typeId);
                            price.setTags(typeName);
                            price.setContent(resultContent);
                            price.setGmtOrder(baseDate);
                            urlmap.put(resultTitle, url);

                            Integer flg = operate.doInsert(price,false);
                           //执行插入并判断插入是否成功
                           if (flg != null && flg > 0) {
                               String catchTime = DateUtil.toString(new Date(), DATE_FORMAT).substring(11,16);
                               LogUtil.getInstance().log(
                                       "caiji-auto", PRICE_OPERTION, null, "{'title':'塑料再生料1("+typeId+")','type':'success','url':'<a href='" + url +"' target='_blank'>"
                                               + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','catchTime':'"+catchTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");
                               /*LogUtil.getInstance().log(
                                       "caiji-auto", PRICE_OPERTION, null, "{'title':'"+resultTitle.substring(5, resultTitle.length())+"("+typeId+")','type':'success','url':'<a href='" + urlmap.get(resultTitle) +"'>"
                                               + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");*/
                           } else if (flg == null){
                               errContentUrl = errContentUrl + "数据存数据库失败！请联系网页抓取开发者！<a href='" + urlmap.get(resultTitle) +"'>"
                                       + "<font color='#FF0000'>" +resultTitle+"</font></a><br />";
                               LogUtil.getInstance().log(
                                       "caiji-auto", PRICE_OPERTION, null, "{'title':'塑料再生料1("+typeId+")','type':'failure','url':'<a href='" + url +"' target='_blank'>"
                                               + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");
                               /*LogUtil.getInstance().log(
                                       "caiji-auto", PRICE_OPERTION, null, "{'title':'"+resultTitle.substring(5, resultTitle.length())+"("+typeId+")','type':'failure','url':'<a href='" + urlmap.get(resultTitle) +"'>"
                                               + "阿里巴巴</a>','defaultTime':'"+defaultTime+"','date':'"+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");*/
                               flagFailure++;
                           }
                        }
                    }
                }
            }
        } while (false);
        if (flagFailure != 0){
            String content = "塑料再生料1"+"("+typeId+")"+"未抓取"+flagFailure+"条。分别为：<br />"
                    +errContentUrl + "如果有，请<a href='http://admin1949.zz91.com/web/zz91/auto/caiji/caiji_albb_recycledPlasticOne.htm?typeId="+typeId +"'>"
                            + "<font color='#FF0000'>抓取</font></a>！";
            Map<String, Object> map = new HashMap<String, Object>();
            map.put("content", content);
            MailUtil.getInstance().sendMail(
                    "塑料再生料1自动抓取报错", 
                    "zz91.price.caiji.auto@asto.mail", null,
                    null, "zz91", "blank",
                    map, MailUtil.PRIORITY_DEFAULT);
            return false;
        } else {
            return true;
        }
    }

    @Override
    public boolean clear(Date baseDate) throws Exception {
        return false;
    }

    public static void main(String[] args) {
        DBPoolFactory.getInstance().init("file:/usr/tools/config/db/db-zztask-jdbc.properties");
        CaijiSlRecyclingOneTask js=new CaijiSlRecyclingOneTask();
        try {
            js.exec(DateUtil.getDate("2013-10-29", "yyyy-MM-dd"));
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}