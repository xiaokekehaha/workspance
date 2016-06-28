package com.ast.ast1949.domain.bbs;

import java.util.Date;

/**
 * BbsUserProfiler generated by MyEclipse Persistence Tools
 */

public class BbsUserProfilerDO implements java.io.Serializable {

	// Fields

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Integer id;
	private Integer companyId;
	private String account;
	private String nickname;
	private String email;
	private String sex;
	private String lifeStage;
	private String marriageCase;
	private String zip;
	private String tel;
	private String mobile;
	private String qq;
	private String msn;
	private String interests;
	private String loveSports;
	private String realName;
	private Date brithday;
	private String address;
	private String workScope;
	private String remark;
	private Integer integral;
	private String pictureName;
	private String picturePath;
	private Integer postNumber;
	private Integer replyNumber;
	private Integer essenceNumber;
	private Date gmtCreated;
	private Date gmtModified;

	// Constructors

	/** default constructor */
	public BbsUserProfilerDO() {
	}

	/** minimal constructor */
	public BbsUserProfilerDO(Integer id) {
		this.id = id;
	}

	/** full constructor */
	public BbsUserProfilerDO(Integer id, Integer companyId, String account,
			String nickname, String email, String sex, String lifeStage,
			String marriageCase, String zip, String tel, String mobile,
			String qq, String msn, String interests, String loveSports,
			String realName, Date brithday, String address, String workScope,
			String remark, Integer integral, String pictureName,
			String picturePath, Integer postNumber,Integer replyNumber, Integer essenceNumber,
			Date gmtCreated, Date gmtModified) {
		this.id = id;
		this.companyId = companyId;
		this.account = account;
		this.nickname = nickname;
		this.email = email;
		this.sex = sex;
		this.lifeStage = lifeStage;
		this.marriageCase = marriageCase;
		this.zip = zip;
		this.tel = tel;
		this.mobile = mobile;
		this.qq = qq;
		this.msn = msn;
		this.interests = interests;
		this.loveSports = loveSports;
		this.realName = realName;
		this.brithday = brithday;
		this.address = address;
		this.workScope = workScope;
		this.remark = remark;
		this.integral = integral;
		this.pictureName = pictureName;
		this.picturePath = picturePath;
		this.postNumber = postNumber;
		this.replyNumber = replyNumber;
		this.essenceNumber = essenceNumber;
		this.gmtCreated = gmtCreated;
		this.gmtModified = gmtModified;
	}

	// Property accessors

	public Integer getId() {
		return this.id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Integer getCompanyId() {
		return this.companyId;
	}

	public void setCompanyId(Integer companyId) {
		this.companyId = companyId;
	}

	public String getAccount() {
		return this.account;
	}

	public void setAccount(String account) {
		this.account = account;
	}

	public String getNickname() {
		return this.nickname;
	}

	public void setNickname(String nickname) {
		this.nickname = nickname;
	}

	public String getEmail() {
		return this.email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getSex() {
		return this.sex;
	}

	public void setSex(String sex) {
		this.sex = sex;
	}

	public String getLifeStage() {
		return this.lifeStage;
	}

	public void setLifeStage(String lifeStage) {
		this.lifeStage = lifeStage;
	}

	public String getMarriageCase() {
		return this.marriageCase;
	}

	public void setMarriageCase(String marriageCase) {
		this.marriageCase = marriageCase;
	}

	public String getZip() {
		return this.zip;
	}

	public void setZip(String zip) {
		this.zip = zip;
	}

	public String getTel() {
		return this.tel;
	}

	public void setTel(String tel) {
		this.tel = tel;
	}

	public String getMobile() {
		return this.mobile;
	}

	public void setMobile(String mobile) {
		this.mobile = mobile;
	}

	public String getQq() {
		return this.qq;
	}

	public void setQq(String qq) {
		this.qq = qq;
	}

	public String getMsn() {
		return this.msn;
	}

	public void setMsn(String msn) {
		this.msn = msn;
	}

	public String getInterests() {
		return this.interests;
	}

	public void setInterests(String interests) {
		this.interests = interests;
	}

	public String getLoveSports() {
		return loveSports;
	}

	public void setLoveSports(String loveSports) {
		this.loveSports = loveSports;
	}

	public String getRealName() {
		return this.realName;
	}

	public void setRealName(String realName) {
		this.realName = realName;
	}

	public Date getBrithday() {
		return this.brithday;
	}

	public void setBrithday(Date brithday) {
		this.brithday = brithday;
	}

	public String getAddress() {
		return this.address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getWorkScope() {
		return this.workScope;
	}

	public void setWorkScope(String workScope) {
		this.workScope = workScope;
	}

	public String getRemark() {
		return this.remark;
	}

	public void setRemark(String remark) {
		this.remark = remark;
	}

	public Integer getIntegral() {
		return this.integral;
	}

	public void setIntegral(Integer integral) {
		this.integral = integral;
	}

	public String getPictureName() {
		return this.pictureName;
	}

	public void setPictureName(String pictureName) {
		this.pictureName = pictureName;
	}

	public String getPicturePath() {
		return this.picturePath;
	}

	public void setPicturePath(String picturePath) {
		this.picturePath = picturePath;
	}

	public Integer getPostNumber() {
		return this.postNumber;
	}

	public void setPostNumber(Integer postNumber) {
		this.postNumber = postNumber;
	}

	public Integer getReplyNumber() {
		return replyNumber;
	}

	public void setReplyNumber(Integer replyNumber) {
		this.replyNumber = replyNumber;
	}

	public Integer getEssenceNumber() {
		return this.essenceNumber;
	}

	public void setEssenceNumber(Integer essenceNumber) {
		this.essenceNumber = essenceNumber;
	}

	public Date getGmtCreated() {
		return this.gmtCreated;
	}

	public void setGmtCreated(Date gmtCreated) {
		this.gmtCreated = gmtCreated;
	}

	public Date getGmtModified() {
		return this.gmtModified;
	}

	public void setGmtModified(Date gmtModified) {
		this.gmtModified = gmtModified;
	}

}