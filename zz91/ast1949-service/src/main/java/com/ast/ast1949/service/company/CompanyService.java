/*
 * Copyright 2009 ASTO.
 * All right reserved.
 * Created on 2009 下午03:38:07
 */
package com.ast.ast1949.service.company;

import java.util.Date;
import java.util.List;

import com.ast.ast1949.domain.company.Company;
import com.ast.ast1949.domain.company.CompanyAccount;
import com.ast.ast1949.domain.products.ProductsDO;
import com.ast.ast1949.dto.PageDto;
import com.ast.ast1949.dto.company.CompanyDto;
import com.ast.ast1949.dto.products.ProductsDto;

/**
 * 公司信息服务类
 * @author Ryan
 *
 */
public interface CompanyService {
	
	/*******************
	 * 查询再生通新会员
	 * @return
	 */
	public List<Company> queryCompanyZstMember(Integer maxSize,String productsType);
	
	public Integer registerCompany(Company company) throws Exception;
	
	public Company queryCompanyById(Integer id);
	
	public Company querySimpleCompanyById(Integer id);
	
	public CompanyDto queryCompanyDetailById(Integer id);
	
	public CompanyDto querySimpleCompanyDetailById(Integer id);
	
	public String queryMembershipOfCompany(Integer id);
	
	public String queryAreaCodeOfCompany(Integer id);
	
	public Integer updateIntroduction(Integer id, String intro);
	
	public Integer updateRegFromCode(Integer id, String code);
	
	public List<Company> queryGoodCompany(Integer maxSize);
	
	public List<CompanyDto> queryCompanyByArea(String areaCode,Integer maxSize);
	
	public Integer updateCompanyByUser(Company company);
	
	public Integer updateCompanyByAdmin(Company company);
	
	public PageDto<CompanyDto> pageCompanyBySearch(Company company, PageDto<CompanyDto> page);
	
	public List<CompanyDto> queryCompanyByEmail(String email);
	
	public Integer saveCustomDomain(Integer companyId, String domain);
	
	public Company queryDomainOfCompany(Integer companyId);
	
	/**
	 * 搜索此email的账号信息，isVip判断是否搜索高会
	 * @param email
	 * @param isVip
	 * @return
	 */
	public CompanyDto queryCompanyByAccountEmail(String email,Boolean isVip);
	
	public List<Company> queryCompanyByLoginNum(Integer max);
	
	public CompanyDto queryCompanyWithAccountById(Integer id);
	
	public PageDto<CompanyDto> pageCompanyBySearchEngine(Company company, PageDto<CompanyDto> page);
	
	public String queryDetails(Integer cid);
	
	public List<Company> queryRecentZst(Integer size);
	
	public boolean validateDomainZz91(Integer companyId, String domainZz91);
	
	/**
	 * 验证访问用户是否 拉黑
	 * @return
	 */
	public boolean validateIsBlack(Integer companyId);
	
	public Integer updateMembershipCode(String membershipCode, Integer companyId);
	
	@Deprecated
	public PageDto<Company> pageCompanyByAdmin(Company company,Date gmtRegisterStart,
			Date gmtRegisterEnd,Integer cid,String email,String account,String mobile,PageDto<Company> page);

	public PageDto<CompanyDto> pageCompanyByAdmin(Company company, CompanyAccount account, 
			Date gmtRegisterStart,Date gmtRegisterEnd, String activeFlag, PageDto<CompanyDto> page);
	
	public Integer updateIsBlock(Integer companyId, String isBlock);
	
	/**
	 * 根据公司ID只查找公司名
	 * @param companyId
	 */
	public String queryCompanyNameById(Integer companyId);
	
	public void assignActiveFlag(String[] activeFlag, Integer companyId);
	
	public void reAssignActiveFlag(String activeFlag, String[] activeFlagCode, Integer companyId);
	
	public List<CompanyDto> exportCompanyByAdmin(Company company, CompanyAccount account, 
			Date gmtRegisterStart,Date gmtRegisterEnd, String activeFlag);
	//优质公司分页
	public PageDto<CompanyDto> queryCompanyVip(Company company, PageDto<CompanyDto> page,String areaCode,String keywords);
	
	/**
	 * 搜索不重复的公司以及公司供求一条，使用：1、tags新版页面2、废金属网首页
	 */
	public List<ProductsDto> queryVipNoSame(Integer size,ProductsDO products);

	public List<CompanyDto> queryCompanyZstMemberByAreacode(String industryCode,String areaCode,String keywords,PageDto<ProductsDto> page);
	
	public Integer countQueryCompanyZstMemberByAreacode(String industryCode,String areaCode,String keywords);
	
	/**
	 * 根据主营类别查询高会：用在trade 普会门市部化
	 * @param industryCode：主营编号
	 * @param size ：返回的记录条数
	 * @return
	 */
	public List<Company> queryZstMemberByIndustryCode(String industryCode,Integer size);
	
	/**
	 * 搜索黑名单客户
	 */
	public PageDto<CompanyDto> queryBlackListForAdmin(Company company,CompanyAccount companyAccount,String reason,PageDto<CompanyDto> page);

	public String getMobileLocation(String tel) throws Exception;
}
