package com.ast.ast1949.trade.controller;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.security.NoSuchAlgorithmException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Date;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import java.util.Map.Entry;

import javax.annotation.Resource;
import javax.mail.MessagingException;
import javax.mail.internet.AddressException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import net.sf.json.JSONArray;

import org.apache.commons.httpclient.HttpException;
import org.jsoup.Jsoup;
import org.jsoup.safety.Whitelist;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.view.RedirectView;

import com.ast.ast1949.domain.company.CategoryCompanyPriceDO;
import com.ast.ast1949.domain.company.Company;
import com.ast.ast1949.domain.company.CompanyAccount;
import com.ast.ast1949.domain.company.CompanyPriceDO;
import com.ast.ast1949.domain.phone.Phone;
import com.ast.ast1949.domain.phone.PhoneClickLog;
import com.ast.ast1949.domain.price.PriceCategoryDO;
import com.ast.ast1949.domain.price.PriceDO;
import com.ast.ast1949.domain.products.CategoryProductsDO;
import com.ast.ast1949.domain.products.ProductAddProperties;
import com.ast.ast1949.domain.products.ProductsDO;
import com.ast.ast1949.domain.products.ProductsPicDO;
import com.ast.ast1949.domain.products.ProductsViewHistory;
import com.ast.ast1949.domain.score.ScoreChangeDetailsDo;
import com.ast.ast1949.dto.ExtResult;
import com.ast.ast1949.dto.ExtTreeDto;
import com.ast.ast1949.dto.PageDto;
import com.ast.ast1949.dto.PageHeadDTO;
import com.ast.ast1949.dto.company.CompanyPriceDTO;
import com.ast.ast1949.dto.price.ForPriceDTO;
import com.ast.ast1949.dto.price.PriceCategoryDTO;
import com.ast.ast1949.dto.products.CategoryProductsDTO;
import com.ast.ast1949.dto.products.ProductsDto;
import com.ast.ast1949.service.auth.AuthService;
import com.ast.ast1949.service.company.CategoryCompanyPriceService;
import com.ast.ast1949.service.company.CompanyAccountService;
import com.ast.ast1949.service.company.CompanyPriceService;
import com.ast.ast1949.service.company.CompanyService;
import com.ast.ast1949.service.company.CrmCompanySvrService;
import com.ast.ast1949.service.credit.CreditIntegralDetailsService;
import com.ast.ast1949.service.facade.CategoryProductsFacade;
import com.ast.ast1949.service.facade.MemberRuleFacade;
import com.ast.ast1949.service.information.ExhibitService;
import com.ast.ast1949.service.phone.PhoneClickLogService;
import com.ast.ast1949.service.phone.PhoneLogService;
import com.ast.ast1949.service.phone.PhoneService;
import com.ast.ast1949.service.price.PriceCategoryService;
import com.ast.ast1949.service.price.PriceService;
import com.ast.ast1949.service.products.ProductAddPropertiesService;
import com.ast.ast1949.service.products.ProductsPicService;
import com.ast.ast1949.service.products.ProductsService;
import com.ast.ast1949.service.products.ProductsViewHistoryService;
import com.ast.ast1949.service.score.ScoreChangeDetailsService;
import com.ast.ast1949.service.site.CategoryService;
import com.ast.ast1949.trade.util.FrontConst;
import com.ast.ast1949.util.AstConst;
import com.ast.ast1949.util.CNToHexUtil;
import com.ast.ast1949.util.NavConst;
import com.ast.ast1949.util.PageCacheUtil;
import com.zz91.util.auth.frontsso.SsoUser;
import com.zz91.util.auth.frontsso.SsoUtils;
import com.zz91.util.cache.MemcachedUtils;
import com.zz91.util.datetime.DateUtil;
import com.zz91.util.exception.AuthorizeException;
import com.zz91.util.http.HttpUtils;
import com.zz91.util.lang.StringUtils;
import com.zz91.util.seo.SeoUtil;
import com.zz91.util.tags.TagsUtils;
import com.zz91.util.velocity.AddressTool;

@Controller
public class TradeController extends BaseController {
	@Resource
	private CompanyService companyService;
	@Resource
	private ProductsService productsService;
	@Resource
	private CategoryService categoryService;
	@Resource
	private PriceCategoryService priceCategoryService;
	@Resource
	private PriceService priceService;
	@Resource
	private CompanyPriceService companyPriceService;
	@Resource
	private ProductsPicService productsPicService;
	@Resource
	private CategoryCompanyPriceService categoryCompanyPriceService;
	@Resource
	private CompanyAccountService companyAccountService;
	@Resource
	private AuthService authService;
	@Resource
	private ScoreChangeDetailsService scoreChangeDetailsService;
	@Resource
	private CreditIntegralDetailsService creditIntegralDetailsService;
	@Resource
	private CrmCompanySvrService crmCompanySvrService;
	@Resource
	private ProductsViewHistoryService productsViewHistoryService;
	@Resource
	private ExhibitService exhibitService;
	@Resource
	private PhoneService phoneService;
	@Resource
	private PhoneClickLogService phoneClickLogService;
	@Resource
	private PhoneLogService phoneLogService;
	@Resource
    private ProductAddPropertiesService productAddPropertiesService;

	private final static String DEFAULT_CITY_CODE = "10011000";
	public final static String DEFAULT_MEMBERSHIP_CODE = "10051000";
	private List<ExtTreeDto> listTree = new ArrayList<ExtTreeDto>();
	public final static String PYAPP_URL =  "http://pyapp.zz91.com";
	public final static String RELATED_PRICE = "tradedetail_price";

	/**
	 * 交易中心首页
	 */
	@RequestMapping
	public ModelAndView index(Map<String, Object> out) {
		
//		SeoUtil.getInstance().buildSeo("index", out);
		
		//供应列表
		out.put("gyProductList", productsService.queryNewestVipProducts("10331000", 14));
		//out.put("gyProductList", productsService.queryNewestVipProducts("10331000",null, 14));
		//求购列表
		out.put("qgProductList", productsService.queryNewestVipProducts("10331001", 14));
		//最新展会
		out.put("newestExhibit", exhibitService.queryNewestExhibit(null, null, 10));
		Map<String,String> map = TagsUtils.getInstance().queryTagsByCode("1000100210011000", null, 10);
		for(String key:map.keySet()){
			map.put(key, CNToHexUtil.getInstance().encode(key));
		}
		out.put("tags", map);
		
		// seo keyword description title 
		SeoUtil.getInstance().buildSeo("index",out);
		return null;
	}

	private void initCommonList(Map<String,Object>out,String code,String pricetypeId,String dayId,String weekId){
		//供应列表
		out.put("gyProductList", productsService.queryNewestVipProducts("10331000",code, 7));
		//求购列表
		out.put("qgProductList", productsService.queryNewestVipProducts("10331001",code, 7));
		//优质商家推荐
		out.put("vipCompanyList",companyService.queryRecentZst(10));
		out.put("code", code);
		out.put("pricetypeId", pricetypeId);
		out.put("dayId", dayId);
		out.put("weekId", weekId);
	}

	private List<CategoryProductsDTO> buildCategory(String parentCode) {
		Map<String, String> map = CategoryProductsFacade.getInstance()
				.getChild(parentCode);
		if (map == null) {
			return null;
		}

		List<CategoryProductsDTO> list = new ArrayList<CategoryProductsDTO>();
		for (Entry<String, String> m : map.entrySet()) {
			CategoryProductsDTO c = new CategoryProductsDTO();
			c.setCategoryProductsDO(new CategoryProductsDO(null, m.getKey(), m
					.getValue(), null, null, null, null));
			if(m.getKey().length()<9){
				c.setChild(buildCategory(m.getKey()));
			}
			list.add(c);
		}

		return list;
	}

	final static int SEARCH_EXPIRED = 20000;

	/**
	 * a:ptype
	 * b:province
	 * c:posttime
	 * d:priceflag
	 * e:nopiclist
	 * f:havepic
	 * p:page
	 */
	@RequestMapping
	public ModelAndView offerlist(String ptype,String province,
			String posttime, String priceflag, String nopiclist, 
			String havepic, String page, String keywords, String mainCode,
			HttpServletRequest request, HttpServletResponse response, Map<String, Object> out) throws Exception {

			PageCacheUtil.setCDNCache(response, PageCacheUtil.MAX_AGE_MIN*30);

		out.put("ptype", ptype);  //O1供应，2求购，其他全部
		out.put("province", province); //
		out.put("posttime", posttime); //整型，单位天
		out.put("priceflag", priceflag); //1：必需有价格，其他：全部
		out.put("nopiclist", nopiclist); //1：文字，其他：图文
		out.put("havepic", havepic); //1：有图片，其他：全部
		out.put("page", page);
		out.put("mainCode", mainCode);
		
//		out.put("keywordsEncode", keywords);
		/////// 
		if(StringUtils.isNotEmpty(mainCode)){
			keywords = CategoryProductsFacade.getInstance().getValue(mainCode);
			keywords = keywords.replaceAll("/", "astoxg");
			keywords = keywords.replaceAll("%", "astoxf");
			keywords = keywords.replaceAll("\\\\", "astoxl");
			keywords=keywords.replace("(","astokhl");
			keywords=keywords.replace(")","astokhr");
			 
		}else{
			keywords = URLDecoder.decode(keywords, HttpUtils.CHARSET_UTF8); 
		}
		if(keywords==null){
			keywords="";
		}
		String keywordsEncode=URLEncoder.encode(keywords,HttpUtils.CHARSET_UTF8);
		out.put("keywordsEncode", keywordsEncode);
		keywords=keywords.replaceAll("astoxg", "/");
		keywords=keywords.replaceAll("astoxl", "'\'");
		keywords = keywords.replaceAll("astoxf", "%");
		keywords=keywords.replaceAll("astohg", "-");
		keywords=keywords.replaceAll("astokhl", "(");
		keywords=keywords.replaceAll("astokhr", ")");
		out.put("keywords", keywords);
		

		// 新版列表页面
		PageCacheUtil.setStatus(response, 301);
		//http://s.zz91.com/trade/s-7070e7baa4e7bbb4.html?ptype=&province=&posttime=
		response.setHeader("Location", "http://s.zz91.com/trade/s-"+CNToHexUtil.getInstance().encode(keywords)+".html?ptype=&province=&posttime="); 
		response.setHeader("Connection", "close"); 
		return null; 
		
//		do {
//			
//			//step1 获取标王信息（只ID）
//			List<Integer> keywordsList = null;
//			if(StringUtils.isEmpty(page) || Integer.valueOf(page).intValue()==1){
//				keywordsList = productsKeywordsRankService.queryProductsId(keywords,null,6);
//				TagsUtils.getInstance().searchTags(keywords.replace("/", ""));
//			}
//			StringBuffer sb=new StringBuffer();
//			String url = ParamUtils.getInstance().getValue("baseConfig", "search_api");
//			if(StringUtils.isNotEmpty(url)){
//				sb.append(url);
//			}else{
//				sb.append("http://python.zz91.com/prolist/?"); // 默认地址
//			}
//			sb.append("ptype=").append(StringUtils.getNotNullValue(ptype)).append("&");
//			sb.append("provincecode=").append(StringUtils.getNotNullValue(province)).append("&");
//			sb.append("province=").append(URLEncoder.encode(StringUtils.getNotNullValue(CategoryFacade.getInstance().getValue(province)),HttpUtils.CHARSET_UTF8)).append("&");
//			sb.append("posttime=").append(StringUtils.getNotNullValue(posttime)).append("&");
//			sb.append("priceflag=").append(StringUtils.getNotNullValue(priceflag)).append("&");
//			sb.append("nopiclist=").append(StringUtils.getNotNullValue(nopiclist)).append("&");
//			sb.append("havepic=").append(StringUtils.getNotNullValue(havepic)).append("&");
//			sb.append("page=").append(StringUtils.getNotNullValue(page)).append("&");
//			sb.append("keywords=").append(URLEncoder.encode(keywords,HttpUtils.CHARSET_UTF8));
//			
//			
//			if(keywordsList!=null && keywordsList.size()>0){
//				String kl=keywordsList.toString();
//				sb.append("&pdtidlist=").append(kl.replace("[", "").replace("]", "").replace(" ", ""));
//			}
//
//			//step2 搜索供求信息
//			Document doc = Jsoup.parse(new URL(sb.toString()), SEARCH_EXPIRED);
//			String totalStr=doc.select("#totalrecords").val();
//			if(!StringUtils.isNumber(totalStr)){
//				totalStr = "1";
//			}
//			Integer total = Integer.valueOf(totalStr);
//			if(total==null || total.intValue()<=0){
//				break;
//			}
//			
//			out.put("totalRecords", total);
//			out.put("producsResult", doc.select("li").toString().replace("&lt;", "<").replace("&gt;", ">"));
//			//step3 获取相关类别 and 相关搜索
////			if(StringUtils.isNotEmpty(mainCode)){
////				out.put("relativeCategories", categoryProductsService.queryCategoryProductsByCode(mainCode, "0"));
////			}
//			
//			String code = "";
//			if (StringUtils.isNotEmpty(mainCode)) {
//				code = mainCode;
//			} else if (StringUtils.isNotEmpty(keywords)) {
//				//CategoryProductsDO cp=categoryProductsService.queryCategoryProductsByLabel(keywords);
//				PageDto<CategoryProductsDTO> cpPage = new PageDto<CategoryProductsDTO>();
////				List<CategorySolrDto> list=solrService.queryCategory(keywords, code);
//				List<CategoryProductsDTO> list = categoryProductsService.pageCategoryProductsBySearchEngine(keywords, cpPage).getRecords();
//				CategoryProductsDTO cp=null;
//				if(list!=null&&list.size()>0){
//					cp=list.get(0);
//				}
//				if(cp!=null){
//					code=cp.getCategoryProductsDO().getCode();
//				}else{
//					code="";
//				}
//			}
////			
//			
//			Map<String, String> relativeCategories=null;
//			if(code.length()>4){
//				relativeCategories=CategoryProductsFacade.getInstance().getChild(code.substring(0,code.length()-4));
//			}else{
//				relativeCategories=CategoryProductsFacade.getInstance().getChild(code);
//			}
//			if(relativeCategories==null){
//				relativeCategories = new HashMap<String, String>();
//			}
//			out.put("relativeCategories", relativeCategories);
//			
//			// 获取子类别
//			out.put("childCategory", CategoryProductsFacade.getInstance().getChild(mainCode));
//			
////			List<ProductsSearchAssociateKeywordsDO> relativeSearch = productsSearchAssociateKeywords.queryByCategoryProductsCode(code);
//			
////			Map<String, String> relativeMap=new HashMap<String, String>();
////			for(ProductsSearchAssociateKeywordsDO k:relativeSearch){
////				relativeMap.put(k.getKeyword(), URLEncoder.encode(k.getKeyword(), URL_ENCODE));
////			}
//			// 类别未设置标签，相关搜索无效
//			//out.put("relativeSearch", categoryProductsService.queryCategoryByTags(keywords,20));  //以后替换成按照关键字搜索相关标签
//			
//			//step4 获取相关标签
//			Map<String , String> map = TagsUtils.getInstance().queryTagsByTag(keywords.replace("/", ""), TagsUtils.ORDER_SEARCH, 20);
//			for(String key:map.keySet()){
//				map.put(key, CNToHexUtil.getInstance().encode(key));
//			}
//			out.put("tagsList", map);
//			
//			//step5 获取相关企业报价
//			showCompanyPrice(out, keywords);
//			//step6 获取相关资讯
////			out.put("newsList", newsService.queryNewsByTitle(keywords, 3));
//			//step7 获取相关报价
//			PageDto<PriceDO> pricePage = new PageDto<PriceDO>();
//			pricePage.setPageSize(5);
//			out.put("priceList",priceService.pagePriceBySearchEngine(keywords, null, pricePage).getRecords());
////			out.put("priceList", priceService.queryPriceByTitleAndTypeId(null, keywords, "5")); // 老方法
//			
//			out.put("code", keywords);
//			//step8 分析导航
//			
//			if (StringUtils.isNotEmpty(code)) {
//				// 分析类别导航
//				Map<String, String> navigationCategoryMap = new LinkedHashMap<String, String>();
//				for (int i = 4; i <= code.length(); i = i + 4) {
//					String pc = code.substring(0, i);
//					navigationCategoryMap.put(pc, CategoryProductsFacade
//							.getInstance().getValue(pc));
////					List<CategorySolrDto> list=solrService.queryCategory(keywordsEncode, code);
////					for(int i=0;i<list.size();i++){
////						navigationCategoryMap.put(pc, list.get(i).getLabel());
////					}
//				}
//				out.put("navigationCategoryMap", navigationCategoryMap);
//			}
//			
//			//step9 设置SEO头部
//			//第一次进去当前页面，page是空的
//			if(StringUtils.isEmpty(page)){
//				page ="1";
//			}
//			if(!"1".equals(ptype)&&!"2".equals(ptype)){
//				ptype = "";
//			}
//			SeoUtil.getInstance().buildSeo("offlist"+ptype, new String[]{keywords,page}, new String[]{keywords}, new String[]{keywords}, out);
//			
////			//供应列表
////			out.put("gyProductList", productsService.queryNewestVipProducts("10331000",code, 7));
////			//求购列表
////			out.put("qgProductList", productsService.queryNewestVipProducts("10331001",code, 7));
////			
////			out.put("tags", TagsUtils.getInstance().queryTagsByCode("100010021003", null, 10));
//			
//			//List<InquiryDto> list=inquiryService.queryScrollInquiry();
//			//out.put("scorllInquiry", list);
//			
//			return new ModelAndView();
//		} while (false);
//		if(StringUtils.isEmpty(mainCode)){
//			mainCode="1000";
//		}
//		out.put("productCode", mainCode);
//		out.put("keywords", keywords);
//		out.put("keywordsEncode", keywordsEncode);
//		//供应列表
//		out.put("gyProductList", productsService.queryNewestVipProducts("10331000",mainCode, 8));
//		//求购列表
//		out.put("qgProductList", productsService.queryNewestVipProducts("10331001",mainCode, 8));
//		SeoUtil.getInstance().buildSeo("soukong"+ptype, new String[]{keywords}, new String[]{keywords}, new String[]{keywords}, out);
//		return new ModelAndView("offerNothing");
	}

	public static void main(String[] args) {
		String k="abdsafsd/fsd/f";
		System.out.println(k.replaceAll("/", ""));
	}
	
//	private String getSearchUrlByCondition(String keywords, String buyOrSale,
//			String productCateCode, String assistCateCode, String areaCode,
//			String postInDays, String havePic) {
//		StringBuilder urlBuf = new StringBuilder();
//		// urlBuf.append("/trade/offerlist--");
//		urlBuf.append("--");
//		if (StringUtils.isNotEmpty(keywords))
//			urlBuf.append(EscapeUnescape.escape(keywords));
//		urlBuf.append("--bs");
//		if (StringUtils.isNotEmpty(buyOrSale))
//			urlBuf.append(buyOrSale);
//		urlBuf.append("--mc");
//		if (StringUtils.isNotEmpty(productCateCode))
//			urlBuf.append(productCateCode);
//		urlBuf.append("--ac");
//		if (StringUtils.isNotEmpty(assistCateCode))
//			urlBuf.append(assistCateCode);
//		urlBuf.append("--area");
//		if (StringUtils.isNotEmpty(areaCode))
//			urlBuf.append(areaCode);
//		urlBuf.append("--int");
//		if (StringUtils.isNumber(postInDays))
//			urlBuf.append(postInDays);
//		// urlBuf.append("--pri");
//		// if (StringUtils.isNumber(isShowPrice))
//		// urlBuf.append(isShowPrice);
//		// urlBuf.append("--pic");
//		// if (StringUtils.isNumber(isShowPic))
//		// urlBuf.append(isShowPic);
//		urlBuf.append("--havepic");
//		if (StringUtils.isNumber(havePic))
//			urlBuf.append(havePic);
//		// urlBuf.append("--p");
//		// if (StringUtils.isNumber(p))
//		// urlBuf.append(p);
//		// urlBuf.append(".htm");
//		return urlBuf.toString();
//	}

	/**
	 * 
	 * @param searchDTO
	 * @param out
	 * @param oldKeywords
	 */
//	private void showUrl(ProductsSearchForFrontDTO searchDTO,
//			Map<String, Object> out, String oldKeywords) {
//		String url = buildUrl(searchDTO, oldKeywords);
//		out.put("url", url);
//		String topNavUrl = buildTopNavUrl(searchDTO, oldKeywords);
//		out.put("topNavUrl", topNavUrl);
//		String noDateUrl = buildNoDateUrl(searchDTO, oldKeywords);
//		out.put("noDateUrl", noDateUrl);
//	}

	/**
	 * 
	 * @param searchDTO
	 * @param out
	 */
//	private void showRelative(ProductsSearchForFrontDTO searchDTO,
//			Map<String, Object> out) {
//		if (searchDTO.getMc() != null) {
//			String mainCode = searchDTO.getMc();
//			if (mainCode.length() > 4) {
//				String parentCode = mainCode
//						.substring(0, mainCode.length() - 4);
//				List<CategoryProductsDO> relativeCategories = categoryProductsService
//						.queryCategoryProductsByCode(parentCode, "0");
//				out.put("relativeCategories", relativeCategories);
//			}
//		}
//	}

	/**
	 * 
	 * @param searchDTO
	 * @param out
	 */
//	private void showRelativeSearch(ProductsSearchForFrontDTO searchDTO,
//			Map<String, Object> out) {
//		if (searchDTO.getAc() != null || searchDTO.getMc() != null) {
//			String code = searchDTO.getAc() != null ? searchDTO.getAc()
//					: searchDTO.getMc();
//
//			List<ProductsSearchAssociateKeywordsDO> relativeSearch = productsSearchAssociateKeywords
//					.queryByCategoryProductsCode(code);
//			List<String[]> list = new ArrayList<String[]>();
//			for (ProductsSearchAssociateKeywordsDO search : relativeSearch) {
//				String[] arr = new String[] { search.getKeyword(),
//						EscapeUnescape.escape(search.getKeyword()) };
//				list.add(arr);
//			}
//			out.put("relativeSearch", list);
//		}
//	}

	/**
	 * 
	 * @param out
	 * @param keywords
	 */
	@SuppressWarnings("unused")
    private void showCompanyPrice(Map<String, Object> out, String keywords) {
		// 用于控制字符串长度
//		out.put("stringUtils", new StringUtils());
//		CompanyPriceDTO companyPriceDTO = new CompanyPriceDTO();
//		companyPriceDTO.setTitle(keywords);
//		companyPriceDTO.getPage().setPageSize(10);
//		companyPriceDTO.getPage().setStartIndex(0);
//		List<CompanyPriceDTO> companyPriceList = companyPriceService
//				.queryCompanyPriceForFront(companyPriceDTO);
//		out.put("companyPriceList", companyPriceList);
		// 搜索引擎搜索
		PageDto<CompanyPriceDTO> page = new PageDto<CompanyPriceDTO>();
		page.setPageSize(10);
		CompanyPriceDTO companyPriceDTO = new CompanyPriceDTO();
		CompanyPriceDO companyPriceDO = new CompanyPriceDO();
		companyPriceDO.setTitle(keywords);
		companyPriceDTO.setCompanyPriceDO(companyPriceDO);
		page = companyPriceService.pageCompanyPriceBySearchEngine(companyPriceDTO, page);
		out.put("companyPriceList", page.getRecords());
	}

//	/**
//	 * 
//	 * @param out
//	 * @param keywords
//	 */
//	private void showTags(Map<String, Object> out, String keywords) {
//		TagsInfoDTO tagsInfoDto = new TagsInfoDTO();
//		TagsInfoDO tagsInfoDO = new TagsInfoDO();
//		tagsInfoDO.setName(keywords);
//		tagsInfoDto.setTagsInfoDO(tagsInfoDO);
//		PageDto page = new PageDto();
//		page.setPageSize(20);
//		page.setStartIndex(0);
//		tagsInfoDto.setPage(page);
//		List<TagsInfoDO> tagsList = tagsInfoService
//				.queryTagsInfoByConditionFromCache(tagsInfoDto);
//		out.put("tagsList", tagsList);
//	}

	/**
	 * 组成用于分页的url
	 * 
	 * @param searchDTO
	 * @param oldKeywords
	 * @return
	 */
//	private String buildUrl(ProductsSearchForFrontDTO searchDTO,
//			String oldKeywords) {
//		String bs = "";
//		if (searchDTO.getBuyOrSale() != null) {
//			bs = searchDTO.getBuyOrSale();
//		}
//		String url = "offerlist---bs" + bs;
//		return url + buildTopNavUrl(searchDTO, oldKeywords);
//	}

	/**
	 * 列表头部导航链接地址，供求类型为固定
	 * 
	 * @param searchDTO
	 * @param oldKeywords
	 * @param url
	 * @return
	 */
//	private String buildTopNavUrl(ProductsSearchForFrontDTO searchDTO,
//			String oldKeywords) {
//		String url = buildNoDateUrl(searchDTO, oldKeywords);
//		url += "---d"
//				+ (searchDTO.getPostInDays() == null ? "" : searchDTO
//						.getPostInDays());
//		return url;
//	}

	/**
	 * 
	 * @param searchDTO
	 * @param oldKeywords
	 * @return
	 */
//	private String buildNoDateUrl(ProductsSearchForFrontDTO searchDTO,
//			String oldKeywords) {
//		String url = "---" + oldKeywords;
//		if (searchDTO.getMid() != null || searchDTO.getAid() != null) {
//			if (searchDTO.getMid() != null) {
//				url += "---m" + searchDTO.getMid();
//			}
//			if (searchDTO.getAid() != null) {
//				url += "---a" + searchDTO.getAid();
//			}
//		} else {
//			url += "---m";
//		}
//		url += "---area"
//				+ (searchDTO.getProvinceCode() == null ? "" : searchDTO
//						.getProvinceCode());
//		return url;
//	}

	@RequestMapping
	public void offerNothing(Map<String, Object> out,String productCode, String keywords,String keywordsEncode) {
		if(StringUtils.isEmpty(productCode)){
			productCode="1000";
		}
		try {
			keywords = new String(keywords.getBytes("iso-8859-1"),"utf-8");
		} catch (UnsupportedEncodingException e) {
		}
		out.put("productCode", productCode);
		out.put("keywords", keywords);
		out.put("keywordsEncode", keywordsEncode);
		//供应列表
		out.put("gyProductList", productsService.queryNewestVipProducts("10331000",productCode, 8));
		//求购列表
		out.put("qgProductList", productsService.queryNewestVipProducts("10331001",productCode, 8));
	}

	/**
	 * 根据类别id获取类别code,并设置关键字。
	 * 
	 * @param searchDTO
	 */
//	private String setCategoryCodeAndkeywords(
//			ProductsSearchForFrontDTO searchDTO) {
//		String keywords = null;
//		if (searchDTO.getAid() != null) {
//			CategoryProductsDO categoryProducts = categoryProductsService
//					.queryCategoryProductsById(searchDTO.getAid());
//			searchDTO.setAc(categoryProducts.getCode());
//			keywords = categoryProducts.getLabel();
//		}
//		if (searchDTO.getMid() != null) {
//			CategoryProductsDO categoryProducts = categoryProductsService
//					.queryCategoryProductsById(searchDTO.getMid());
//			if (categoryProducts != null) {
//				searchDTO.setMc(categoryProducts.getCode());
//				keywords = categoryProducts.getLabel();
//			}
//		}
//		if (searchDTO.getKeywords() != null
//				&& !searchDTO.getKeywords().equals("null")) {
//			keywords = searchDTO.getKeywords();
//		}
//		return keywords;
//	}

	/**
	 * 供求类别大类下详细页面
	 * 
	 * @param out
	 * @param mainCode
	 */

	@RequestMapping
	public void offerindex(Map<String, Object> out, String mainCode) {

		if (StringUtils.isEmpty(mainCode)) {
			mainCode = "1000";
		}

		CategoryProductsDO c = new CategoryProductsDO();
		c.setCode(mainCode);
		c.setLabel(CategoryProductsFacade.getInstance().getValue(mainCode));
		out.put("currentCategoryProducts", c);
		out.put("categoryProductsList", buildCategory(mainCode));

		/**
		 * 推荐再生通企业
		 */
		//List<Company> companyList = companyService.queryGoodCompany(20);
//				.queryCompanyNameByRegtime();
		//out.put("companyList", companyList);
		// 再生技术
		// 行情综述
		// 商务热点
//		String type[] = { "index_below_right_02", "review_quotes",
//				"index_below_right_05" };
//		List<BbsPostDTO> bList = bbsService
//				.batchQueryBbsPostByTagsSignTypes(type);
//		for (int i = 0; i < type.length; i++) {
//			out.put("bList" + type[i], bList);
//		}

//		List<TagsInfoDO> tagsList = tagsInfoService.queryTagsInfoByType("4", 30);
//		Map<String, String> encodeTagsMap=new HashMap<String, String>();
//		for(TagsInfoDO tags:tagsList){
//			try {
//				encodeTagsMap.put(tags.getName(), URLEncoder.encode(tags.getName(), "utf-8"));
//			} catch (UnsupportedEncodingException e) {
//				e.printStackTrace();
//			}
//		}
//		out.put("hotTags", tagsList);
//		out.put("encodeTagsMap", encodeTagsMap);
		out.put("hotTags", TagsUtils.getInstance().queryTagsByCode("100010021000", 0, 30));
		
		/**
		 * 查询大类别下的行情价格
		 */
		List<PriceCategoryDO> priceList;
		List<ForPriceDTO> listForPrice;
//		PriceDTO priceDTO = new PriceDTO();
		String code = null;
		Integer typeId=220;
		String priceCode="paper";
		if ("1000".equals(mainCode)) {

			// 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废金属_废金属供应_废金属求购_废金属价格_废料交易中心_${site_name}");
			headDTO.setPageKeywords("废金属,废金属价格,废金属回收,废金属行情,废铜价格,废钢价格,废铁价格,废铜,废铝,废钢,废铁");
			headDTO.setPageDescription("${site_name}废金属市场为您精选了废铜、废铝、废钢、废铁、贵金属等废金属的供应信息、求购信息、行业资讯、价格行情。");
			setSiteInfo(headDTO, out);
			// 废金属
			code = "废金属";
			typeId=216;
			priceCode="metal";
			// 金属价格
			// 页面排行第一的时间

			PriceDO priceDO = priceService.queryTopGmtOrderByParentId(17);
			out.put("metalGmtOrder", priceDO.getGmtOrder());

			priceList = priceCategoryService.queryPriceCategoryByParentId(17);
			out.put("MetalList", priceList.subList(0, 9));

			// 金属新料价格
			List<PriceCategoryDO> metalNewCategory = priceCategoryService
					.queryPriceCategoryByParentId(18);
			out.put("metalNewCategory", metalNewCategory);
			Integer pageSize = 2;
			List<PriceCategoryDTO> bigList = priceService.queryPriceList(18,
					null, pageSize);
			out.put("bigList", bigList);
			
		} else if ("1001".equals(mainCode)) {
			// 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废塑料|废塑料价格行情|废塑料供求信息_再生料_交易中心_${site_name}");
			headDTO.setPageKeywords("废塑料,废塑料价格,废塑料供应,废塑料求购,废塑料回收, 再生料,PP,PVC");
			headDTO.setPageDescription("${site_name}废塑料市场是中国最大的废塑料网上贸易市场，这里有我们为您精选的PP,PET PE,ABS,PVC,HDPE,LDPE,PA,PC,PS等废塑料、再生料的供应信息、求购信息、废塑料行业资讯、废塑料价格、废塑料行情、废塑料黄页信息等");
			setSiteInfo(headDTO, out);
			// 废塑料
			code = "废塑料";
			typeId=217;
			priceCode="plastic";
			// 废塑料市场动态
			listForPrice = priceService.queryEachPriceByParentId(22);
			out.put("plasticMarketList", listForPrice);
			// 塑料新料市场价出厂价
			listForPrice = priceService.queryEachPriceByParentId(21);
			out.put("newPlasticList", listForPrice);
			
		} else if ("1002".equals(mainCode)) {
			// 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废旧轮胎与废橡胶|废旧轮胎与废橡胶供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废旧轮胎,废橡胶,废旧轮胎回收,废橡胶回收,废橡胶价格,橡胶颗粒,橡胶粉");
			headDTO.setPageDescription("${site_name}废旧轮胎与废橡胶市场是中国最大的废旧轮胎与废橡胶网上交易市场，这里有我们为您精选的废轮胎,橡胶粉,橡胶颗粒,硅胶,再生胶等废旧轮胎与废橡胶供应信息、求购信息,废旧轮胎与废橡胶行业资讯、价格行情、公司黄页、展会信息等");
			setSiteInfo(headDTO, out);
			// 废橡胶
			code = "废橡胶";
//			priceDTO.setLimitSize(10);
//			priceDTO.setParentId(15);
			listForPrice = priceService.queryPriceByParentId(15,10);
			out.put("rubberList", listForPrice);

		} else if ("1003".equals(mainCode)) {
			// 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废纺织品与废皮革|废纺织品与废皮革价格行情_交易中心_${site_name}");
			headDTO.setPageKeywords("废纺织品,废布,废布回收,废皮革,废棉料,化纤,无纺布,尼龙");
			headDTO.setPageDescription("中国再生资源交易废纺织品与废皮革市场是中国最大的废纺织品与废皮革网上交易市场，这里有我们为您精选的废棉料,废布,碎布,无纺布,涤纶,尼龙等废纺织品与废皮革供应信息、求购信息、回收信息、公司黄页、行业资讯、价格行情等");
			setSiteInfo(headDTO, out);
		} else if ("1004".equals(mainCode)) {
			// 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废纸|废纸价格行情|废纸供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废纸,废纸价格,废纸回收,求购废纸,废纸价格行情,白板纸,白卡纸,包装纸");
			headDTO.setPageDescription("${site_name}废纸市场是中国最大的废纸网上交易市场，这里有我们为您精选的美废,废报纸书刊,欧废,日废,牛皮纸,纸板箱等废纸供应信息、求购信息、回收信息、废纸公司黄页、废纸行业资讯、废纸价格行情、废纸展会信息等");
			setSiteInfo(headDTO, out);
			// 废纸
			code = "废纸";
//			priceDTO.setLimitSize(10);
//			priceDTO.setParentId(13);
			listForPrice = priceService.queryPriceByParentId(13,10);
			out.put("paperList", listForPrice);

		} else if ("1005".equals(mainCode)) {
			// 废纺织品与废皮革 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废电子电器|旧电脑供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废电子电器,旧电脑,电路板,旧电线,电池,电子元件,线路板,主板,电容");
			headDTO.setPageDescription("${site_name}废电子电器市场是中国最大的废电子电器与废电脑设备网上贸易市场，这里有我们为您精选的电路板,线路板,CPU,主板,电容,电瓶,变压器,旧电脑等废电子电器与废电脑设备供应信息、废电子电器行业资讯、废电子电器行情、废电子电器展会信息等");
			setSiteInfo(headDTO, out);
			code = "废纺织品";
		} else if ("1006".equals(mainCode)) {
			// 废玻璃 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废玻璃|废玻璃价格行情|废玻璃供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废玻璃,废玻璃回收,废玻璃价格,玻璃纤维,玻璃瓶,碎玻璃,浮法玻璃");
			headDTO.setPageDescription("${site_name}废玻璃市场是中国最大的废玻璃网上贸易市场，这里有我们为您精选的碎玻璃，玻璃纤维，有机玻璃等废玻璃供应信息、求购信息、公司黄页等");
			setSiteInfo(headDTO, out);
			code = "废玻璃";
		} else if ("1007".equals(mainCode)) {
			// 废旧二手设备设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废旧二手设备|废旧二手设备供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废旧设备,二手设备回收,废旧二手设备,废旧二手设备回收,工程设备，化工设备，制冷设备");
			headDTO.setPageDescription("${site_name}废旧二手设备市场是中国最大的废旧设备与旧交通工具网上交易市场，这里有我们为您精选的机电,废变压器,注塑机,电动机,锅炉等废旧二手设备供应信息、废旧二手设备求购信息、回收信息、行业资讯、价格行情、展会信息等");
			setSiteInfo(headDTO, out);
			code = "废旧二手设备";
		} else if ("1008".equals(mainCode)) {
			// 其他废料 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("废木|化工废料|其他废料供求信息_交易中心_${site_name}");
			headDTO.setPageKeywords("废木,废木制品,木削,木屑,化工废料,废碘,废油,刨花,木削");
			headDTO.setPageDescription("${site_name}其他废料市场是中国最大的废木、化工废料网上贸易市场，这里有我们为您精选的废木、废木制品、木削、木屑、化工废料等废料供应信息、求购信息、公司黄页等");
			setSiteInfo(headDTO, out);
			code = "其他废料";
		} else {
			// 服务 设置页面头部信息
			PageHeadDTO headDTO = new PageHeadDTO();
			headDTO.setTopNavIndex(NavConst.TRADE_CENTER);
			headDTO.setPageTitle("服务|报关/清关服务|物流服务|代理服务_交易中心_${site_name}");
			headDTO.setPageKeywords("废料服务,废料报关/清关服务,物流服务,废料进口代理服务, 报关服务,清关服务");
			headDTO.setPageDescription("${site_name}是中国最大的再生资源网上贸易市场，我们为您提供报关/清关服务,物流服务,代理服务,招聘等一系列服务");
			setSiteInfo(headDTO, out);
			code = "服务";
		}
		out.put("code", code);
		out.put("stringUtils", new StringUtils());
		String escapeCode=null;
		try {
			escapeCode = URLEncoder.encode(CategoryProductsFacade.getInstance().getValue(mainCode), "utf-8");
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
		out.put("escapeCode", escapeCode);
		
		//行情综述
		//out.put("priceList", priceService.queryPriceByTypeId(typeId, null, null, 6));
		out.put("typeId", typeId);
		out.put("priceCode", priceCode);
		out.put("mainCode", mainCode);
		/**
		 * 最新供求
		 */
		//out.put("productsList", productsService.queryProductsByMainCode(mainCode, null, 14));

	}
	
	@RequestMapping
	public ModelAndView metal(HttpServletRequest request, Map<String, Object> out){
		initCommonList(out,"1000","216","32","33");
		Map<String,String> map = TagsUtils.getInstance().queryTagsByCode("1000100210011000", null, 10);
		for(String key:map.keySet()){
			map.put(key, CNToHexUtil.getInstance().encode(key));
		}
		out.put("tags", map);
//		out.put("tags", TagsUtils.getInstance().queryTagsByCode("1000100210011001", null, 10));
		SeoUtil.getInstance().buildSeo("list",
				new String[]{"废金属"},
				new String[]{"废金属","废铜","废钢","废铁"},
				new String[]{"废金属","废铜","废铝","废钢","废铁","贵金属"},
				out);
		return null;
	}
	
	@RequestMapping
	public ModelAndView plastic(HttpServletRequest request, Map<String, Object> out){
		initCommonList(out,"1001","217","34","35");
		Map<String,String> map = TagsUtils.getInstance().queryTagsByCode("1000100210011000", null, 10);
		for(String key:map.keySet()){
			map.put(key, CNToHexUtil.getInstance().encode(key));
		}
		out.put("tags", map);
//		out.put("tags", TagsUtils.getInstance().queryTagsByCode("1000100210011002", null, 10));
		SeoUtil.getInstance().buildSeo("list",
				new String[]{"废塑料"},
				new String[]{"废塑料","再生料","PP","PV"},
				new String[]{"废塑料","PP","PET","PE","ABS","PVC"},
				out);
		return null;
	}
	
	@RequestMapping
	public ModelAndView waste(HttpServletRequest request, Map<String, Object> out){
		initCommonList(out,null,"220","36","37");
		Map<String,String> map = TagsUtils.getInstance().queryTagsByCode("1000100210011000", null, 10);
		for(String key:map.keySet()){
			map.put(key, CNToHexUtil.getInstance().encode(key));
		}
		out.put("tags", map);
//		out.put("tags", TagsUtils.getInstance().queryTagsByCode("1000100210011003", null, 10));
		SeoUtil.getInstance().buildSeo("list",
				new String[]{"综合废料"},
				new String[]{"综合废料","废纸","废橡胶","废旧二手设备"},
				new String[]{"综合废料","废纸","废橡胶","废旧二手设备","废玻璃","废纺织品"},
				out);
		return null;
	}

	/**
	 * 根据productsId查询出供求信息,自动加载公司其他同类产品,产品相册，图片地址
	 * 
	 * @param productsId
	 *            传入后台的供求id主键值
	 * @throws ParseException
	 * @throws IOException 
	 * @throws HttpException 
	 */
	@SuppressWarnings("unchecked")
	@RequestMapping
	public ModelAndView productdetails(Integer productsId, String title, Integer idx, String iqerror,
			HttpServletRequest request, Map<String, Object> out, HttpServletResponse response,String from)
			throws ParseException, HttpException, IOException {
		PageCacheUtil.setNoCDNCache(response);
		do {
			// 获取供求信息 step1
			if (productsId == null) {
				out.put(AstConst.ERROR_TEXT, "您的地址有错误,请检查一下");
				break;
			}

			ProductsDto productDetails=productsService.queryProductsDetailsById(productsId);
			
			String isDel= "0";
	        List<ProductAddProperties> productAddProperties = productAddPropertiesService.queryByProductId(productsId, isDel);
	        out.put("productAddProperties", productAddProperties);
	        //获取主类别,辅助类别code
	        out.put("manufactureList", categoryService.queryCategoriesByPreCode("1011"));
			
//			ProductDetailsDTO productDetails = productDetailsService
//					.queryProductDetailsByProductsId(productsId);
			if (productDetails == null) {
				out.put(AstConst.ERROR_TEXT, "您的地址有错误,请检查一下");
				break;
			}

			// 判断信息是否正常，（审核通过，未过期，没有暂停发布）
			if (productDetails.getProducts().getCheckStatus() == null
					|| !"1".equals(productDetails.getProducts().getCheckStatus())) {
				if ("0".equals(productDetails.getProducts().getCheckStatus())) {
					out.put(AstConst.ERROR_TEXT, "您查看的供求信息还没有被审核，请耐心等待！");
				} else {
					out.put(AstConst.ERROR_TEXT, "对不起，您查看的供求信息审核没有通过！");
				}
				break;
			}

			// 检查过期情况
			int interval = DateUtil.getIntervalDays(new Date(),
					productDetails.getProducts().getExpireTime());
			if (interval > 0) {
				out.put("expiredFlag", "1");
			}

			// 检查暂停发布情况
			// XXX 数据类型不正确，数据库中是字符型
			if (productDetails.getProducts().getIsPause() != null
					&& productDetails.getProducts().getIsPause()) {
				out.put(AstConst.ERROR_TEXT, "对不起，您查看的供求信息现在已经停止发布了！");
				break;
			}
			// 检查用户是否黑名单
			if(companyService.validateIsBlack(productDetails.getProducts().getCompanyId())){
				out.put(AstConst.ERROR_TEXT, "对不起，该用户已被拉为黑名单！");
				break;
			}
			
//			String details=productDetails.getProducts().getDetails();
//			if(details==null){
//				details="";
//			}
//			details=details.replace("\n", "<br />");
//			productDetails.getProducts().setDetails(details);
			
//			productDetails.getProducts().setDetails(Jsoup.clean(productDetails.getProducts().getDetails(), Whitelist.basic()));
			//去掉属性空格
			if (productDetails.getProducts().getAppearance() != null) {
			    productDetails.getProducts().setAppearance(productDetails.getProducts().getAppearance().trim());
			}
			if (productDetails.getProducts().getColor() != null) {
			    productDetails.getProducts().setColor(productDetails.getProducts().getColor().trim());
            }
			if (productDetails.getProducts().getImpurity() != null) {
			    productDetails.getProducts().setImpurity(productDetails.getProducts().getImpurity().trim());
            }
			if (productDetails.getProducts().getManufacture() != null) {
			    if(productDetails.getProducts().getManufacture().length() == 1) {
			        productDetails.getProducts().setManufacture("");
			    } else {
			        productDetails.getProducts().setManufacture(productDetails.getProducts().getManufacture().trim());
			    }
		    }
			if (productDetails.getProducts().getOrigin() != null) {
			    productDetails.getProducts().setOrigin(productDetails.getProducts().getOrigin().trim());
		    }
			if (productDetails.getProducts().getSource() != null) {
			    productDetails.getProducts().setSource(productDetails.getProducts().getSource().trim());
            }
			if (productDetails.getProducts().getSpecification() != null) {
			    productDetails.getProducts().setSpecification(productDetails.getProducts().getSpecification().trim());
            }
			if (productDetails.getProducts().getUseful() != null) {
			    productDetails.getProducts().setUseful(productDetails.getProducts().getUseful().trim());
            }
			if (productDetails.getProducts().getLocation() != null) {
                productDetails.getProducts().setLocation(productDetails.getProducts().getLocation().trim());
            }
			//根据主类别不同显示不同的属性
			String typeCode = productDetails.getProducts().getCategoryProductsMainCode().substring(0, 4);
			out.put("typeCode", typeCode);
			out.put("productDetails", productDetails);
			// 判断是否要获取联系信息，并根据根据查看和显示的标记获取联系信息 step2
			boolean showFlag = false, viewFlag = false; boolean lifeFlag=false;

//			CompanyDO loginUserCompany = getCachedCompany(request);
			SsoUser sessionUser = getCachedUser(request);
			
			if (sessionUser != null) {
				viewFlag=crmCompanySvrService.validatePeriod(sessionUser.getCompanyId(), CrmCompanySvrService.ZST_CODE);
				if(!viewFlag){
					viewFlag=crmCompanySvrService.validatePeriod(sessionUser.getCompanyId(), CrmCompanySvrService.JBZST_CODE);
				}
				out.put("loginFlag", "1");
			}

			showFlag=crmCompanySvrService.validatePeriod(productDetails.getProducts().getCompanyId(), CrmCompanySvrService.ZST_CODE);
			if(!showFlag){
				showFlag=crmCompanySvrService.validatePeriod(productDetails.getProducts().getCompanyId(), CrmCompanySvrService.JBZST_CODE);
			}
			if(!showFlag){
				showFlag=crmCompanySvrService.validatePeriod(productDetails.getProducts().getCompanyId(), CrmCompanySvrService.ESITE_CODE);
			}
			if(!showFlag){
				showFlag=crmCompanySvrService.validatePeriod(productDetails.getProducts().getCompanyId(), CrmCompanySvrService.LDB_CODE);
			}
			
			Company company = companyService.querySimpleCompanyById(productDetails.getProducts().getCompanyId());
			if(company==null){
				//公司信息不存在
				out.put(AstConst.ERROR_TEXT, "您查看的供求信息无法显示");
				break;
			}
			out.put("companyInfo", company);
			//判断终身服务
			lifeFlag=crmCompanySvrService.validatePeriod(productDetails.getProducts().getCompanyId(), CrmCompanySvrService.LIFE_CODE);
			out.put("lifeFlag", lifeFlag);
			if (showFlag || viewFlag) {
				// 获取发布供求的用户信息和积分信息
				out.put("creditIntegral", creditIntegralDetailsService.countIntegralByCompany(company.getId()));
				
				CompanyAccount account=companyAccountService.queryAccountByAccount(productDetails.getProducts().getAccount());
				out.put("companyAccount", account);
			}else{
				// 普会来电宝客户访问普会
				if(sessionUser != null&&crmCompanySvrService.validatePeriod(sessionUser.getCompanyId(), CrmCompanySvrService.LDB_CODE)){
					Phone phone = phoneService.queryByCompanyId(sessionUser.getCompanyId());
					String balance = phoneLogService.countBalance(phone);
					PhoneClickLog phoneClickLog = phoneClickLogService.queryById(sessionUser.getCompanyId(), productDetails.getProducts().getCompanyId());
					if(phoneClickLog!=null){
						out.put("ldbFlag", 2);
					}else{
						if(StringUtils.isNotEmpty(balance)&&Double.valueOf(balance)>0){
							// 余额 大于1 
							out.put("ldbFlag", 1);
						}else{
							// 服务过期等等
							out.put("ldbFlag", 0);
						}
					}
				}
			}

			// 获取供求图片信息 step3
			List<ProductsPicDO> picList = productsPicService.queryProductPicInfoByProductsIdForFront(productsId);
			out.put("picList", picList);
			if(picList.size()>0){
				out.put("firstPic", picList.get(0));
			}

			// 获取同公司，同类其他供求信息 step4
			List<ProductsDto> similarProducts= productsService.queryProductsOfCompany(company.getId(), 5);
			out.put("similarProducts", similarProducts);

			// 获取同一个类别的企业报价 step5 (同一种类别，如果没有对应的类别，则找名称匹配的)
			CompanyPriceDTO companyPriceDTO = new CompanyPriceDTO();
			companyPriceDTO.getPage().setStartIndex(0);
			companyPriceDTO.getPage().setPageSize(12);
			companyPriceDTO.setCompanyPriceDO(new CompanyPriceDO());

			// 查找有没有对应的code
			CategoryCompanyPriceDO categoryCompanyPrice = categoryCompanyPriceService
					.queryCategoryCompanyPriceByLabel(productDetails
							.getCategoryProductsMainLabel());
			
			if (categoryCompanyPrice != null
					&& categoryCompanyPrice.getCode() != null
					&& categoryCompanyPrice.getCode().length() > 0) {
				companyPriceDTO.getCompanyPriceDO()
						.setCategoryCompanyPriceCode(
								categoryCompanyPrice.getCode());
			} else {
				companyPriceDTO.setTitle(productDetails.getProducts().getTitle());
			}
//			out.put("companyPriceList", companyPriceService.queryCompanyPriceForFront(companyPriceDTO));
			out.put("companyPriceList", companyPriceService.pageCompanyPriceBySearchEngine(companyPriceDTO, companyPriceDTO.getPage()).getRecords());

			// 获取相关的标签信息 step6
			String tags = "";
			if (productDetails.getProducts().getTags() != null) {
				tags += productDetails.getProducts().getTags();
			}
			if (productDetails.getProducts().getTagsAdmin() != null) {
				tags += "," + productDetails.getProducts().getTagsAdmin();
			}
			
			Map<String, String> map = TagsUtils.getInstance().encodeTags(tags, "utf-8");
			for(String key:map.keySet()){
				map.put(key, CNToHexUtil.getInstance().encode(key));
			}
			out.put("tagsInfoList",	map);
			
			out.put("tagList",TagsUtils.getInstance().queryTagsByTag(productDetails.getProducts().getTitle(),TagsUtils.ORDER_SEARCH, 20));
			// FIXME 获取供求类别对应的产品相册信息 step7

			// 分析类别导航 step8
			Map<String, String> navigationCategoryMap = new LinkedHashMap<String, String>();
			for (int i = 4; i <= productDetails.getProducts().getCategoryProductsMainCode()
					.length(); i = i + 4) {
				String code = productDetails.getProducts().getCategoryProductsMainCode()
						.substring(0, i);
				navigationCategoryMap.put(code, CategoryProductsFacade
						.getInstance().getValue(code));
			}
			out.put("navigationCategoryMap", navigationCategoryMap);
			if(productDetails.getProducts().getCategoryProductsMainCode()!=null 
					&& productDetails.getProducts().getCategoryProductsMainCode().length()>4){
				out.put("adkeywords", productDetails.getProducts().getCategoryProductsMainCode().substring(0, 4));
			}
			
			//没有标签，取父类别
			if(StringUtils.isEmpty(tags)){
				for(String code:navigationCategoryMap.keySet()){
					tags = navigationCategoryMap.get(code);
				}
			}
			
			// 相关报价 使用标签 作为关键字搜索
			String address = AddressTool.getAddress("pyapp");
			if(StringUtils.isEmpty(address)){
				address = PYAPP_URL;
			}
			String url = address + "/" + RELATED_PRICE + "/?tradeID=" + productsId + "&listnum=10&wordslen=20";
			String relatedPriceListStr = HttpUtils.getInstance().httpGet(url,HttpUtils.CHARSET_UTF8);
			
			if(relatedPriceListStr.startsWith("[")){
				JSONArray relatedPriceList = JSONArray.fromObject(relatedPriceListStr);
				out.put("relatedPriceList", relatedPriceList);
			}
			

			// SEO step11
			StringBuffer sb = new StringBuffer();
			sb.append(productDetails.getProductsTypeLabel());
			sb.append(productDetails.getProducts().getTitle());
			String bigCategory = null;

			if (productDetails.getProducts().getCategoryProductsMainCode() != null
					&& productDetails.getProducts().getCategoryProductsMainCode().length() > 4) {
				bigCategory = navigationCategoryMap.get(productDetails
						.getProducts().getCategoryProductsMainCode().subSequence(0, 4));
			}
			
			SeoUtil.getInstance().buildSeo("product", new String[]{sb.toString(),bigCategory}, 
					new String[]{sb.toString(),productDetails.getProducts().getTitle()}, 
					new String[]{sb.toString()}, out);

			// 是否拥有再生通或者简版再生通的权限
			if (!showFlag) {
				ProductsDO product = new ProductsDO();
				PageDto<ProductsDto> page = new PageDto<ProductsDto>();
				if(productDetails.getCategoryProductsMainLabel()!=null){
					product.setTitle(productDetails.getCategoryProductsMainLabel().replace("/"," "));
				}else{
					product.setTitle(productDetails.getProducts().getTitle());
				}
				product.setIsVip(true);
				page.setPageSize(5);
				page = productsService.pageProductsBySearchEngine(product,null,null, page);
				List<ProductsDto> list = page.getRecords();
				out.put("vipProductList", list);
			}

			// 获取访问历史痕迹
			String cookie = HttpUtils.getInstance().getCookie(request,
					ProductsViewHistoryService.HISTORY_KEY,
					ProductsViewHistoryService.DOMAIN);

			if (StringUtils.isNotEmpty(cookie)) {
				List<ProductsViewHistory> historyList = productsViewHistoryService.queryHistory(cookie, null);
				out.put("historyList", historyList);
			}
			
			try {
				out.put("keywordsEncode", URLEncoder.encode(productDetails.getProducts().getTitle(), HttpUtils.CHARSET_UTF8));
				out.put("relatedkey", productDetails.getProducts().getTags());
			} catch (UnsupportedEncodingException e) {
			}
			// put 统计来源
			if(StringUtils.isNotEmpty(from)){
				out.put("from", from);
			}
			
			return new ModelAndView();
		} while (true);
		return new ModelAndView("/common/error");
	}

	/**
	 * 初始化发布的供求信息
	 */
	@RequestMapping
	public ModelAndView postoffer_step1(Map<String, Object> out,
			HttpServletRequest request, Integer t) {
//		setSiteInfo(new PageHeadDTO(), out);
		// 判断是不是已经超过发布条数限制了
//		CompanyDO company = getCachedCompany(request);
		SsoUser sessionUser = getCachedUser(request);
		if (sessionUser != null) {
			out.put("result", String.valueOf(productsService
					.queryUserIsAddProducts(sessionUser.getCompanyId(),sessionUser.getMembershipCode())));
		}
		out.put("t", t);
		// seo 设置
		buildDefaultSeo(out);
		
		return null;
	}
	
	/**
	 * 快速发布
	 * @param out
	 * @throws ParseException 
	 */
	@RequestMapping
	public ModelAndView doPublic(Map<String,Object>out,HttpServletRequest request,ProductsDO products,Integer postlimittime,String tagsArr) throws ParseException{
		do {
			SsoUser ssoUser = getCachedUser(request);
			if(ssoUser==null){
				return new ModelAndView("postoffer_step1");
			}
			
			// 验证前一张页面是否zz91
			String preUrl = request.getHeader("referer");
			if(StringUtils.isEmpty(preUrl)||StringUtils.isContains(new String[]{"zz91.com","zz9l.com","postoffer_step1"}, preUrl)){
				return new ModelAndView("postoffer_step1");
			}
			
			//如果最后一次插入的时间与本次插入时候的系统时间之差timeTemp小于在特定时间则不允许插入:返回一个true
			if(!productsService.queryLastGmtCreateTimeByCId(ssoUser.getCompanyId())){
				out.put("reason","您发布供求的速度太快了，请稍后再试！");
				break;
			}

			if(!productsService.queryUserIsAddProducts(ssoUser.getCompanyId(),ssoUser.getMembershipCode())){
				out.put("reason","您今天发布的供求信息已经超过限制！");
				break;
			}
			products.setAccount(ssoUser.getAccount());
			products.setCompanyId(ssoUser.getCompanyId());
			products.setCategoryProductsAssistCode("");
			Date now = new Date();
			products.setRefreshTime(now);
			// 计算过期时间（本步骤应该在数据库中进行）
			if (postlimittime == -1) {
				products.setExpireTime(DateUtil.getDate("9999-12-31 23:59:59",AstConst.DATE_FORMATE_WITH_TIME));
			} else {
				products.setExpireTime(DateUtil.getDateAfterDays(now, postlimittime));
			}
			
			// 产品标签处理
			tagsArr = TagsUtils.getInstance().arrangeTags(tagsArr);
			products.setTags(tagsArr);
			// 标签系统创建新标签
			TagsUtils.getInstance().createTags(tagsArr);
			
			// 信息来源 fast_public
			products.setSourceTypeCode("fast_public");
			
			// 发布供求信息
			Integer id = productsService.publishProductsByCompany(products, ssoUser.getMembershipCode(), ssoUser.getAreaCode());
			
			// 没有发布成功
			if (id <= 0) {
				break;
			}
			
			// 发布供求信息 判断简介和主营业务是否为空 截取供求详细
			Company company = companyService.queryCompanyById(ssoUser.getCompanyId());
			if(StringUtils.isEmpty(company.getIntroduction())&&StringUtils.isEmpty(company.getBusiness())){
				company.setIntroduction(products.getDetails());
				String str = Jsoup.clean(products.getDetails(), Whitelist.none());
				if(StringUtils.isNotEmpty(str)&&str.length()>200){
					str = str.substring(0,200);
				}
				company.setBusiness(str);
				companyService.updateCompanyByUser(company);
			}
			
			return new ModelAndView("redirect:"+AddressTool.getAddress("myrc")+"/myproducts/office_post_suc.htm?from=1&productId="+id);
		} while (false);
		return new ModelAndView("postoffer_step1");
	}

	private void buildDefaultSeo(Map<String,Object> out){
		SeoUtil.getInstance().buildSeo(out);
	}
	
	@RequestMapping
	public ModelAndView postAccess(Map<String, Object> out,
			HttpServletRequest request) throws IOException {
		ExtResult result = new ExtResult();
		SsoUser sessionUser = getCachedUser(request);
		if (sessionUser != null) {
			result.setSuccess(productsService.queryUserIsAddProducts(sessionUser.getCompanyId(), sessionUser.getMembershipCode()));
		}
		return printJson(result, out);
	}

	final static String CATEGORY_MANUFACTURE = "1011";

	/**
	 * 初始化发布的供求信息,判断密码
	 * 
	 * @param productsDO为供求信息
	 * @param companyContactsDO为客户联系信息
	 * @param response请求响应
	 * @param out输出结果信息
	 * @return
	 * @return ModelAndView视图
	 * @throws IOException
	 */
	@Deprecated
	@RequestMapping
	public ModelAndView postoffer_step2(ProductsDO productsDO, String email,
			Map<String, Object> out, HttpServletRequest request)
			throws IOException {

//		CompanyDO company = getCachedCompany(request);
		SsoUser sessionUser = getCachedUser(request);

		if (sessionUser == null) {
			return new ModelAndView(new RedirectView("postoffer_step1.htm"));
		}

		if (productsDO.getProductsTypeCode() == null) {
			return new ModelAndView(new RedirectView("postoffer_step1.htm"));
		}

		if (StringUtils.isEmpty(email)) {
			email = getCachedUser(request).getEmail();
		}

		setSiteInfo(new PageHeadDTO(), out);
		// 转存productsDo和Email
		out.put("productsDO", productsDO);
		out.put("email", email);
		out.put("uploadModel", FrontConst.UPLOAD_MODEL_PRODUCTS);

		// 会员上传图片的数量
		out.put("uploadPicNum", Integer.valueOf(MemberRuleFacade.getInstance().getValue(sessionUser.getMembershipCode(),"upload_products_picture")));

		out.put("resourceUrl",
				(String) MemcachedUtils.getInstance().getClient().get(
						"baseConfig.resource_url"));

		// 初始化加工说明
		// out.put("manufactureMap",
		// CategoryFacade.getInstance().listCategoryByParentCode(
		// CATEGORY_MANUFACTURE));
		out.put("manufactureMap",
				categoryService.queryCategoriesByPreCode(CATEGORY_MANUFACTURE));

		// 判断是不是再生通会员
		
		// seo 设置
		buildDefaultSeo(out);
		return null;
	}


	@RequestMapping
	public void postProductSuccess(Map<String, Object> out, Integer productId) {
		out.put("productId", productId);
	}

	@RequestMapping
	public ModelAndView postProductsPic(Map<String, Object> out,
			ProductsPicDO picture) throws IOException {
		ExtResult result = new ExtResult();
		picture.setIsDefault("0");
		picture.setIsCover("0");
		Integer i = productsPicService.insertProductsPic(picture);
		if (i.intValue() > 0) {
			result.setSuccess(true);
			result.setData(i);
		}
		return printJson(result, out);
	}

	/**
	 * 根据密码添加供求信息
	 * 
	 * @param productsDO为供求信息
	 * @param out输出结果信息
	 * @return ModelAndView视图
	 * @throws IOException
	 */
//	@RequestMapping
//	@Deprecated
//	public ModelAndView addProducts(ProductsDO productsDO,
//			Map<String, Object> model) throws IOException {
//		ExtResult result = new ExtResult();
//		productsDO.setExpireTime(new Date());
//		Integer i = productsService.insertProduct(productsDO);
//		if (i > 0) {
//			result.setSuccess(FrontConst.SUCCESS);
//			return printJson(result, model);
//		} else {
//			model.put(AstConst.ERROR_TEXT, "error text");
//			return new ModelAndView("/common/error");
//		}
//	}

	/**
	 * 发布供求成功跳转页面
	 */
	@RequestMapping
	public void joinprocess(Map<String, Object> out) {
	}
	
	@RequestMapping
	public void ajaxUpload(Map<String, Object> out, String model,
			String filetype, String control) {
		out.put("filetype", filetype);
		out.put("model", model);
		out.put("control", control);
	}


	@RequestMapping
	public ModelAndView selectCategory(Map<String, Object> model, String code)
			throws IOException {
		JSONArray json = null;
		if (code == null) {
			listTree = categoryService.child(DEFAULT_CITY_CODE);
			json = JSONArray.fromObject(listTree);
		} else {
			listTree = categoryService.child(code);
			json = JSONArray.fromObject(listTree);
		}
		return printJson(json, model);
	}


	/**
	 * 根据供求类别ID获取对应的code
	 * 
	 * @param categoryId
	 * @return
	 */
//	private String getCodeFromCategoryProductsId(Integer categoryId) {
//		String code = "";
//		CategoryProductsDO categoryProducts = categoryProductsService
//				.queryCategoryProductsById(categoryId);
//		if (categoryProducts != null) {
//			code = categoryProductsService
//					.queryCategoryProductsById(categoryId).getCode();
//		}
//		return code;
//	}

	/**
	 * 添加标签
	 * 
	 * @param tagsName
	 * @param articleId
	 */
//	private void addTags(String tagsName, ProductsDO productsDO,
//			HttpServletRequest request) {
//		int pdtid = productsDO.getId();
//		// 获取标签列表
//		String[] tagNames = StringUtils
//				.distinctStringArray(tagsName.split(","));
//		// 获取操作员信息
////		CompanyContactsDO cc = getCachedAccount(request);
//		// 删除与文章相关的所有标签关联信息
//		List<TagsInfoDO> tagsList = tagsArticleService
//				.queryTagListFromTagsArticleRelationByArticleId("10351001",
//						pdtid);
//		List<String> tagNamesQueried = new ArrayList<String>();
//		// tagNamesQueried 存在，tagNames 不存在 删除标签关联
//		List<TagsArticleRelation> deletedTagArtRelList = new ArrayList<TagsArticleRelation>();
//		// tagNamesQueried 不存在，tagNames 存在 新新标签关联
//		List<TagsArticleRelation> newTagArtRelList = new ArrayList<TagsArticleRelation>();
//		for (TagsInfoDO tag : tagsList) {
//			tagNamesQueried.add(tag.getName());
//			if (!StringUtils.isContains(tagNames, tag.getName())) {
//				TagsArticleRelation tagArtRel = new TagsArticleRelation();
//				tagArtRel.setTagId(tag.getId());
//				tagArtRel.setTagName(tag.getName());
//				tagArtRel.setArticleId(pdtid);
//				deletedTagArtRelList.add(tagArtRel);
//			}
//		}
//		tagsArticleService.deleteTagsArticleRelationByArticleId("10351001",
//				pdtid);
//		// 设置,添加标签关联信息
//		for (String tagName : tagNames) {
//			TagsArticleRelation relation = new TagsArticleRelation();
//			relation.setArticleModuleCode("10351001");// 10351001 ,供求信息
//			relation.setArticleCategoryCode(productsDO
//					.getCategoryProductsMainCode());
//			relation.setArticleId(pdtid);
//			relation.setArticleTitle(productsDO.getTitle());
//			relation.setTagName(tagName);
//			relation.setCreator(getCachedUser(request).getAccountId());
//			try {
//				tagsArticleService.insertTagsArticleRelation(relation);
//				if (!tagNamesQueried.contains(tagName)) {
//					newTagArtRelList.add(relation);
//				}
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
//		}
//	}

	/**
	 * 供求推荐
	 */
	@RequestMapping
	public ModelAndView recommend(Integer id, Map<String, Object> out,
			HttpServletResponse response, HttpServletRequest request) {
		
		ProductsDO products = productsService.queryProductsById(id);

		if (products == null) {
			try {
				response.sendRedirect(request.getContextPath()
						+ "/root/error.htm?s=" + id);
			} catch (IOException e) {
				e.printStackTrace();
			}
			return null;
		}
		out.put("products", products);
		if (products.getAccount() != null) {
//			out.put("companyContacts", companyService
//					.selectContactsByAccount(products.getAccount()));
			out.put("companyAccount", companyAccountService.queryAccountByAccount(products.getAccount()));
		}
		out.put("id", id);
		out.put("serverName", request.getServerName());
		if (request.getServerPort() != 8080) {
			out.put("serverPort", ":" + request.getServerPort());
		}
		return new ModelAndView("/recommend");
	}

	/**
	 * 发送供求推荐
	 * 
	 * @throws MessagingException
	 * @throws IOException
	 * @throws AddressException
	 */
	@RequestMapping
	public ModelAndView sendRecommend(Map<String, Object> model) {

//		if (productsRecommend == null) {
//			model.put(AstConst.ERROR_TEXT, "error text");
//			return new ModelAndView("/common/error");
//		}
//
//		String email = productsRecommend.getReceiveEmail();
//		email = email.trim().replace(",,", "");
//		if (email.startsWith(",")) {
//			email = email.substring(1, email.length());
//		}
//		if (email.endsWith(",")) {
//			email = email.substring(0, email.length() - 1);
//		}
//
//		productsRecommend.setReceiveEmail(email);
//
//		//TODO 直接通过邮件发送推荐信息
//		Integer i =  1; // productsRecommendService.sendRecommend(productsRecommend);
//		if (i == null || i.intValue() <= 0) {
//			// go to error page
//			model.put(AstConst.ERROR_TEXT, "发送失败");
//			return new ModelAndView("/common/error");
//		} else {
//			model.put("id", productsRecommend.getProductId());
//			return new ModelAndView("/recommend_suc");
//		}
		return null;
	}

	/**
	 * 显示图片和flash
	 */
	@RequestMapping
	public ModelAndView picshow(Integer pid, Integer psort,
			Map<String, Object> out) {
		// out.put("pid", pid);
		// out.put("psort", psort);
		if (pid == null || pid.intValue() <= 0) {
			out.put(AstConst.ERROR_TEXT, "您的地址有错误,请检查一下");
			return new ModelAndView("/common/error");
		}
		// 查找对应的图片信息 必须是审核通过的
		out.put("picList",productsPicService.queryProductPicInfoByProductsIdForFront(pid));
		
		out.put("membershipCode", companyService.queryMembershipOfCompany(productsService.queryProductsWithOutDetailsById(pid).getCompanyId()));
		
		out.put("resourceUrl",(String) MemcachedUtils.getInstance().getClient().get("baseConfig.resource_url"));
		return null;
	}

	/**
	 * 供求详细图片查看
	 */
	@RequestMapping
	public void pics(Integer pid, Map<String, Object> out) {
		List<ProductsPicDO> list = productsPicService
				.queryProductPicInfoByProductsId(pid);
		out.put("list", list);
		out.put("uploadModel", FrontConst.UPLOAD_MODEL_PRODUCTS);
		out.put("resourceUrl",
				(String) MemcachedUtils.getInstance().getClient().get(
						"baseConfig.resource_url"));
	}
	
	@RequestMapping
	public ModelAndView validateProductTitle(String title, HttpServletRequest request,
			Map<String, Object> out) throws IOException {
		ExtResult result = new ExtResult();
		SsoUser sessionUser = getCachedUser(request);
		if(!productsService.isProductsAlreadyExists(title, null, sessionUser.getAccount())){
			result.setSuccess(true);
		}
		return printJson(result, out);

	}
	
	@RequestMapping
	public ModelAndView publishProducts(ProductsDO products, Integer postlimittime, String tagsArr,Integer togglePrice,
			String picIds, HttpServletRequest request, Map<String, Object> out,HttpServletResponse response,
			String verifyCode, String verifyCodeKey) 
				throws IOException,ParseException {
		ExtResult result = new ExtResult();
		
		do {
			SsoUser sessionUser = getCachedUser(request);
			if (sessionUser == null) {
				result.setData("sessionTimeOut");
				break;
			}
			
//			//验证验证码，防止机器注册
//			String vcode=String.valueOf(SsoUtils.getInstance().getValue(request, response, AstConst.VALIDATE_CODE_KEY));
//			SsoUtils.getInstance().remove(request, AstConst.VALIDATE_CODE_KEY);
//			
//			if(StringUtils.isEmpty(vcode) || StringUtils.isEmpty(verifyCode) || !verifyCode.equalsIgnoreCase(vcode)){
//				result.setData("您输入的验证码有错误！");
//				break;
//			}
			
			//验证验证码，防止机器注册
			String vcode=String.valueOf(SsoUtils.getInstance().getValue(request, response, AstConst.VALIDATE_CODE_KEY));
			SsoUtils.getInstance().remove(request, AstConst.VALIDATE_CODE_KEY);
			
			if(StringUtils.isEmpty(vcode) || StringUtils.isEmpty(verifyCode) || !verifyCode.equalsIgnoreCase(vcode)){
				result.setData("您输入的验证码有错误！");
				break;
			}
			
			if(!productsService.queryUserIsAddProducts(sessionUser.getCompanyId(),sessionUser.getMembershipCode())){
				result.setData("您今天发布的供求信息已经超过限制！");
				break;
			}
			
			// 准备数据
			products.setAccount(sessionUser.getAccount());
			products.setCompanyId(sessionUser.getCompanyId());
			Date now = new Date();
			products.setRefreshTime(now);
			// 计算过期时间（本步骤应该在数据库中进行）
			if (postlimittime == -1) {
				products.setExpireTime(DateUtil.getDate("9999-12-31 23:59:59",AstConst.DATE_FORMATE_WITH_TIME));
			} else {
				products.setExpireTime(DateUtil.getDateAfterDays(now, postlimittime));
			}
			
//			if (!StringUtils.isEmpty(products.getPrice())) {
//				products.setIsShowInPrice("1");
//			}
			
			tagsArr = TagsUtils.getInstance().arrangeTags(tagsArr);
			products.setTags(tagsArr);
			TagsUtils.getInstance().createTags(tagsArr);
			
			if(togglePrice==null){
				products.setMaxPrice(0f);
			}
			
			// 发布供求信息
			Integer productId = productsService.publishProductsByCompany(products, sessionUser.getMembershipCode(), sessionUser.getAreaCode());
			
			// 没有发布成功
			if (productId <= 0) {
				result.setData("failureInsert");
				break;
			}
			
//			if (!StringUtils.isEmpty(products.getPrice())) {
//				// 添加为报价
//				CompanyPriceDO companyPriceDO = new CompanyPriceDO();
//				companyPriceDO.setProductId(productId);
//				companyPriceDO.setAccount(sessionUser.getAccount());
//				companyPriceDO.setCompanyId(sessionUser.getCompanyId());
//				Company c = new Company();
//				c.setMembershipCode(sessionUser.getMembershipCode());
//				c.setAreaCode(sessionUser.getAreaCode());
//				companyPriceService.addProductsToCompanyPrice(companyPriceDO,
//						c, products);
//			}
			
			products.setId(productId);
			
			Set<Integer> picSet=new HashSet<Integer>();
			String[] pids=picIds.split(",");
			for(String pid: pids){
				if(!"".equals(pid)){
					picSet.add(Integer.valueOf(pid));
				}
			}
			Integer[] picIdArr=new Integer[picSet.size()];

			// 关联上传的图片
			if (StringUtils.isNotEmpty(picIds)) {
				productsService.insertProductsPicRelation(productId,
						picSet.toArray(picIdArr));
			}

			// 关联标签
//			addTags(tagsArr, products, request);

			result.setData(products);
			result.setSuccess(true);
			// 高级用户可以直接增加积分，因为直接审核通过
			if (!"10051000".equals(sessionUser.getMembershipCode())) {
				scoreChangeDetailsService
						.saveChangeDetails(new ScoreChangeDetailsDo(sessionUser.getCompanyId()
								, null, "get_post_product", null,
								productId, null));
				List<ProductsPicDO> picList = productsPicService
						.queryProductPicInfoByProductsId(productId);
				for (ProductsPicDO pic : picList) {
					scoreChangeDetailsService
							.saveChangeDetails(new ScoreChangeDetailsDo(
									sessionUser.getCompanyId(), null,
									"get_post_product_pic", null, pic.getId(),
									null));
				}
			}

		} while (false);
		
		return printJson(result, out);
	}
	
	@Deprecated
	@RequestMapping
	public ModelAndView checkuser(Map<String, Object> model, HttpServletRequest request,
			HttpServletResponse response, String username, String password, String randCode,
			String randCodeKey, String url, String cookieMaxAge) throws IOException {
		ExtResult extResult = new ExtResult();
		
		SsoUser ssoUser=null;
		try {
			ssoUser = SsoUtils.getInstance().validateUser(response, username, password, null, null);
		} catch (NoSuchAlgorithmException e) {
		} catch (AuthorizeException e) {
			extResult.setData(AuthorizeException.getMessage(e.getMessage()));
		}
		if(ssoUser!=null){
			setSessionUser(request, ssoUser);
			extResult.setSuccess(true);
		}
		
		return printJson(extResult, model);
	}
	
	@Deprecated
	@RequestMapping
	public ModelAndView checkUserEmail(Map<String, Object> model, String email)
			throws IOException {
		String result = "true";
		if (StringUtils.isNotEmpty(email)) {
			Integer i=authService.countUserByEmail(email);
			if (i!= null && i.intValue()>0) {
				result = "false";
			}
		}
		model.put("json", result);
		return new ModelAndView("json");
	}
	
	@Deprecated
	@RequestMapping
	public ModelAndView checkUserMobile(Map<String, Object> model, String mobile)
			throws IOException {
		String result = "true";
		if (StringUtils.isNotEmpty(mobile)) {
			Integer num = companyAccountService.countAccountOfMobile(mobile);
			if(num!=null && num.intValue()>0){
				result="false";
			}
		}
		model.put("json", result);
		return new ModelAndView("json");
	}
	
	@Deprecated
	@RequestMapping
	public ModelAndView checkUsername(Map<String, Object> model, String account)
			throws IOException {
		ExtResult result=new ExtResult();
		if (StringUtils.isNotEmpty(account)) {
			Integer userCount = authService
					.countUserByAccount(account);
			if (userCount == null || userCount == 0) {
				result.setSuccess(true);
			}
		}
		return printJson(result, model);
	}
	
	@RequestMapping
	public ModelAndView submitCallback(HttpServletRequest request, Map<String, Object> out, 
			String success, String data){
		if(StringUtils.isEmpty(data)){
			data="{}";
		}
		try {
//			data=URLDecoder.decode(data, HttpUtils.CHARSET_UTF8);
			data=StringUtils.decryptUrlParameter(data);
		} catch (UnsupportedEncodingException e) {
		}
		out.put("success", success);
		out.put("data", data);
		return null;
	}
	
	@RequestMapping
	public void viewHistory(HttpServletRequest request,
			HttpServletResponse response, Integer productId) {
		SsoUser sessionUser = getCachedUser(request);
		do {
			Integer companyId = null;
			if (sessionUser == null) {
				companyId = 0;
			} else {
				companyId = sessionUser.getCompanyId();
			}
			String cookieKey = null;
			if (companyId != null && companyId != 0) {
				cookieKey = productsViewHistoryService
						.queryKeyByCompanyId(companyId);
			} else {
				cookieKey = HttpUtils.getInstance().getCookie(request,
						ProductsViewHistoryService.HISTORY_KEY,
						ProductsViewHistoryService.DOMAIN);
			}

			if (cookieKey == null) {
				// 生成36位cookie
//				String base = "abcdefghijklmnopqrstuvwxyz0123456789"; // 生成字符串从此序列中取
//				Random random = new Random();
//				StringBuffer sb = new StringBuffer();
//				for (int i = 0; i < 36; i++) {
//					int number = random.nextInt(base.length());
//					sb.append(base.charAt(number));
//				}
				cookieKey = UUID.randomUUID().toString();
			}
			// 更新访问记录表中，登录用户companyId为空的数据
			if(companyId != null && companyId != 0){
				productsViewHistoryService.updateCompanyIdByCookieKey(companyId,cookieKey);
			}
			List<ProductsViewHistory> list = productsViewHistoryService
					.queryHistory(cookieKey, 10);
			boolean isInsert = true;
			for (ProductsViewHistory obj : list) {
				if (obj.getProductId().equals(productId)) {
					isInsert = false;
					productsViewHistoryService.updateGmtLastView(obj.getId());
					break;
				}
			}
			if (isInsert) {
				String productPicUrl = "";
				ProductsDto productDetails = productsService.queryProductsDetailsById(productId);
				List<ProductsPicDO> picList = productsPicService.queryProductPicInfoByProductsId(productId);
				if(picList.size()>=1){
					ProductsPicDO picObj = picList.get(0);
					productPicUrl = picObj.getPicAddress();
				}
				productsViewHistoryService.create(new ProductsViewHistory(null,
						cookieKey, companyId, productId, productDetails
								.getProducts().getTitle(), productPicUrl, null,
						null, null));
			}
			HttpUtils.getInstance().setCookie(response,
					ProductsViewHistoryService.HISTORY_KEY, cookieKey,
					ProductsViewHistoryService.DOMAIN, null);
		} while (false);
	}
	
	@RequestMapping
	public ModelAndView markToClick(HttpServletRequest request,Integer targetId,Map<String, Object>out) throws IOException{
		ExtResult result = new ExtResult();
		do {
			SsoUser ssoUser = getCachedUser(request);
			if(ssoUser==null||targetId==null){
				break;
			}
			PhoneClickLog phoneClickLog = new PhoneClickLog();
			phoneClickLog.setCompanyId(ssoUser.getCompanyId());
			phoneClickLog.setTargetId(targetId);
			// 是否 来电宝五元用户
			if(crmCompanySvrService.validatePeriod(ssoUser.getCompanyId(), CrmCompanySvrService.LDB_FIVE_CODE)){
				phoneClickLog.setClickFee(5.0f);
			}else{
				phoneClickLog.setClickFee(1.0f);
			}
			phoneClickLogService.insert(phoneClickLog);
		} while (false);
		return printJson(result, out);
	}
	
}
