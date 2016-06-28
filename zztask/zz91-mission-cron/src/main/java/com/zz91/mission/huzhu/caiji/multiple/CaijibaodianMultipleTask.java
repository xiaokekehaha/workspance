package com.zz91.mission.huzhu.caiji.multiple;

import java.io.IOException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.jsoup.Jsoup;
import org.jsoup.safety.Whitelist;

import com.zz91.mission.domain.huzhu.BbsPostCaiJi;
import com.zz91.mission.huzhu.caiji.HuZhuCaiJiCommonOperate;
import com.zz91.task.common.ZZTask;
import com.zz91.util.datetime.DateUtil;
import com.zz91.util.db.pool.DBPoolFactory;
import com.zz91.util.lang.StringUtils;
import com.zz91.util.log.LogUtil;
import com.zz91.util.mail.MailUtil;
/**
 * 互助抓取 废旧物资网 对应bbs_post 中的类别:废料学院-行业知识-综合废料 采集5个网页链接
 * 采集地址:http://baodian.feijiu.net/hybd-p-cid6.9.36-.html
 * ..... 以下是37到39省略
 * http://baodian.feijiu.net/hybd-p-cid6.9.40-.html
 * @author root
 *
 */

public class CaijibaodianMultipleTask implements ZZTask{
	final static String PRICE_OPERTION = "huzhu_caiji";
	final static String DATE_FORMAT = "yyyy-MM-dd HH:mm:ss";
	HuZhuCaiJiCommonOperate operate = new HuZhuCaiJiCommonOperate();
	final String DB = "ast";
	final static Map<String, String> QQZSS_MAP = new HashMap<String, String>();
	static {
		// httpget 使用的编码 不然会有乱码
		QQZSS_MAP.put("charset", "gb2312");

		// 采集地址 正式
		QQZSS_MAP
				.put("url", "http://baodian.feijiu.net/hybd-p-cid6.7.10-.html");
		QQZSS_MAP.put("contentUrl", "");
		QQZSS_MAP.put("listStart", "<div class=\"list-item\">"); // 列表页开头
		QQZSS_MAP.put("listEnd", "<div class=\"ad-120X600\">"); // 列表页结尾
		QQZSS_MAP.put("split", "<li>");

		QQZSS_MAP.put("contentStart", "<div class=\"cont-text\">");
		QQZSS_MAP.put("contentEnd", "<div class=\"gg-240X148\">");

	}

	@Override
	public boolean init() throws Exception {
		return false;
	}

	@Override
	public boolean exec(Date baseDate) throws Exception {
		String defaultTime = DateUtil.toString(baseDate, DATE_FORMAT)
				.substring(11, 16);
		int flagFailure = 0;
		Integer typeId = 22;
		String url = "";
		Map<String, String> urlmap = new HashMap<String, String>();
		String errContentUrl = "";
		Integer max = 0;
		String tagsString = "";
		do {
			for (Integer i = 1; i < 6; i++) {
				
				switch (i) {
				case 1:
					tagsString = "基本知识";
					max=5;
					break;
				case 2:
					tagsString = "废纸标准";
					max=2;
					break;
				case 3:
					tagsString = "加工工艺";
					max=1;
					break;
				case 4:
					tagsString = "再生过程";
					max=1;
					break;
				case 5:
					tagsString = "废纸应用";
					max=1;
					break;
				default:
					break;
				}

				for (Integer j = 1; j <max+1; j++) {
					String content = "";
					try {
						if(i==5){
							url = "http://baodian.feijiu.net/hybd-p" + j
									+ "-cid6.9.40-.html";
						}else {
							url = "http://baodian.feijiu.net/hybd-p" + j
									+ "-cid6.9.3" + (i+5) + "-.html";
						}

						content = operate.httpClientHtml(url,
								QQZSS_MAP.get("charset"));
					} catch (IOException e) {
						content = null;
					}

					Integer start = content.indexOf(QQZSS_MAP.get("listStart"));
					if (start == -1) {
						sendEmail(url, typeId, defaultTime,tagsString);
						continue;
					}
					Integer end = content.indexOf(QQZSS_MAP.get("listEnd"));
					if (end == -1) {
						sendEmail(url, typeId, defaultTime,tagsString);
						continue;
					}
					String result = content.substring(start, end);
					String[] str = result.split(QQZSS_MAP.get("split"));

					// 检查日期是否对应今天
					// String formatDate = DateUtil.toString(baseDate,
					// "yyyy-MM-dd");
					List<String> list = new ArrayList<String>();

					for (String s : str) {
						if (s.indexOf(".html") != -1) {
							list.add(s);
						}
					}

					if (list.size() < 1) {
						continue;

					}
					Integer n=1;
					for (String aStr : list) {
						
						
						if (aStr != null) {
							String linkStr = "";
							linkStr = operate.getAlink(aStr);
							if (StringUtils.isEmpty(linkStr)) {
								sendEmail(url, typeId, defaultTime,tagsString);
								continue;
							} else {
								String resultTitle = Jsoup.clean(linkStr,
										Whitelist.none());
								Integer starts = aStr.indexOf("http");
								if (starts == -1) {
									sendEmail(url, typeId, defaultTime,tagsString);
									continue;
								}
								Integer ends = aStr.indexOf(".html");
								if (ends == -1) {
									sendEmail(url, typeId, defaultTime,tagsString);
									continue;
								}
								linkStr = aStr.substring(starts, (ends + 5));
								String resultContent = "";
								try {
									resultContent = operate.httpClientHtml(
											linkStr, QQZSS_MAP.get("charset"));
								} catch (IOException e) {
									resultContent = null;
								}
								Integer contentstart = resultContent
										.indexOf(QQZSS_MAP.get("contentStart"));

								if (contentstart == -1) {
									sendEmail(url, typeId, defaultTime,tagsString);
									continue;
								}

								Integer contentend = resultContent
										.indexOf(QQZSS_MAP.get("contentEnd"));

								if (contentend == -1) {
									sendEmail(url, typeId, defaultTime,tagsString);
									continue;
								}
								resultContent = resultContent.substring(
										contentstart, contentend);
								resultContent = Jsoup
										.clean(resultContent,
												Whitelist
														.none()
														.addTags("p", "ul",
																"br", "li",
																"th", "tr",
																"td")
														.addAttributes("td",
																"colspan"));

								String tags = "废纸," + tagsString;
								BbsPostCaiJi bbsPostCaiJi = new BbsPostCaiJi();
								bbsPostCaiJi.setBbsPostCategoryId(3);
								bbsPostCaiJi.setBbsPostAssistId(22);
								bbsPostCaiJi.setCategory("综合废料,行业知识,废料学院");
								bbsPostCaiJi.setContent(resultContent);
								bbsPostCaiJi.setTitle(resultTitle);
								bbsPostCaiJi.setTags(tags);

								boolean flg = operate.insert(bbsPostCaiJi);
								// 执行插入并判断插入是否成功
								if (!flg) {
									errContentUrl = errContentUrl
											+ "数据存数据库失败！请联系网页抓取开发者！<a href='"
											+ urlmap.get(resultTitle) + "'>"
											+ "<font color='#FF0000'>"
											+ resultTitle + "</font></a><br />";
									flagFailure++;
								}
							}
						}

					}
					
				}
			}

		} while (false);
		if (flagFailure != 0) {
			sendEmail(url, typeId, defaultTime,tagsString);
			return false;
		} else {
			String catchTime = DateUtil.toString(new Date(), DATE_FORMAT)
					.substring(11, 16);
			LogUtil.getInstance()
					.log("caiji-auto",
							PRICE_OPERTION,
							null,
							"{'title':'互助废料学院-废金属 废旧物资网-("
									+tagsString+ typeId
									+ ")','type':'success','url':'<a href='"
									+ url
									+ "' target='_blank'>"
									+ "废旧物资网</a>','defaultTime':'"
									+ defaultTime
									+ "','catchTime':'"
									+ catchTime
									+ "','date':'"
									+ DateUtil
											.toString(new Date(), DATE_FORMAT)
									+ "'}");
			return true;
		}
	}

	public void sendEmail(String url, Integer typeId, String defaultTime,String tagsString)
			throws ParseException {
		String errContentUrl = " 抓取失败，来源网站没有数据可抓取！请点击<a href='"
				+ url
				+ "'>"
				+ "<font color='#FF0000'>互助废料学院-废金属 废旧物资网-"
				+ "("
				+ typeId
				+ ")"
				+ "</font></a>查看来源网站<br />"
				+ "如果有，请<a href='http://apps2.zz91.com/task/job/definition/doTask.htm?jobName=CaijiQqzsslPlasticTask&start="
				+ DateUtil.getDate(new Date(), "yyyy-MM-dd") + " 00:00:00'>"
				+ "<font color='#FF0000'>抓取</font></a>！";
		LogUtil.getInstance().log(
				"caiji-auto",
				PRICE_OPERTION,
				null,
				"{'title':'综合废料-(" +tagsString + typeId
						+ ")','type':'failure','url':'<a href='" + url
						+ "' target='_blank'>" + "废旧物资网</a>','defaultTime':'"
						+ defaultTime + "','date':'"
						+ DateUtil.toString(new Date(), DATE_FORMAT) + "'}");
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("content", errContentUrl);
		MailUtil.getInstance().sendMail("互助废料学院-综合废料 废旧物资网-自动抓取报错"+tagsString,
				"zz91.price.caiji.auto@asto.mail", null, null, "zz91", "blank",
				map, MailUtil.PRIORITY_DEFAULT);

	}

	@Override
	public boolean clear(Date baseDate) throws Exception {
		return false;
	}

	public static void main(String[] args) {

		DBPoolFactory.getInstance().init(
				"file:/usr/tools/config/db/db-zztask-jdbc.properties");
		long start = System.currentTimeMillis();
		CaijibaodianMultipleTask js = new CaijibaodianMultipleTask();
		try {
			js.exec(DateUtil.getDate(new Date(), "yyyy-MM-dd"));
		} catch (Exception e) {
			e.printStackTrace();
		}
		long end = System.currentTimeMillis();
		System.out.println(end - start);
	}
}