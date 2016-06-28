package com.ast.ast1949.domain.bbs;

import java.util.Date;

/**
 * BbsPost generated by MyEclipse Persistence Tools
 */

public class BbsPostDO implements java.io.Serializable {

	// Fields

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private Integer id;
	private Integer companyId;
	private String account;
	private Integer bbsUserProfilerId;
	private Integer bbsPostCategoryId;
	private Integer bbsTitleStyleId;
	private Integer bbsTopicsId;
	private String title;
	private String content;
	private Integer frontCategoryId;
	private String isShow;
	private String isDel;
	private String checkPerson;
	private String checkStatus;
	private Date checkTime;
	private String uncheckedCheckStatus;
	private String unpassReason;
	private String isHotPost;
	private String postType;
	private Integer visitedCount;
	private Integer replyCount;
	private Date postTime;
	private Date replyTime;
	private Date gmtCreated;
	private Date gmtModified;
	private String url;
	private Integer integral;
	private String tags;
	private Integer bbsPostAssistId;
	private Integer noticeCount;
	private Integer recommendCount;
	private Integer collectCount;
	private String category;//类别名全称
	private String childCategory;//最底端类别名
	private String nickname;//昵称
	public String getNickname() {
		return nickname;
	}

	public void setNickname(String nickname) {
		this.nickname = nickname;
	}

	/** default constructor */
	public BbsPostDO() {
	}

	/** minimal constructor */
	public BbsPostDO(Integer id) {
		this.id = id;
	}

	/** full constructor */
	public BbsPostDO(Integer id, Integer companyId, String account,
			Integer bbsUserProfilerId, Integer bbsPostCategoryId,
			Integer bbsTitleStyleId, Integer bbsTopicsId, String title,
			String content, Integer frontCategoryId, String isShow,
			String isDel, String checkPerson, String checkStatus,
			Date checkTime, String uncheckedCheckStatus, String unpassReason,
			String isHotPost, String postType, Integer visitedCount,
			Integer replyCount, Date postTime, Date gmtCreated, Date gmtModified) {
		this.id = id;
		this.companyId = companyId;
		this.account = account;
		this.bbsUserProfilerId = bbsUserProfilerId;
		this.bbsPostCategoryId = bbsPostCategoryId;
		this.bbsTitleStyleId = bbsTitleStyleId;
		this.bbsTopicsId = bbsTopicsId;
		this.title = title;
		this.content = content;
		this.frontCategoryId = frontCategoryId;
		this.isShow = isShow;
		this.isDel = isDel;
		this.checkPerson = checkPerson;
		this.checkStatus = checkStatus;
		this.checkTime = checkTime;
		this.uncheckedCheckStatus = uncheckedCheckStatus;
		this.unpassReason = unpassReason;
		this.isHotPost = isHotPost;
		this.postType = postType;
		this.visitedCount = visitedCount;
		this.replyCount = replyCount;
		this.postTime = postTime;
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

	public Integer getBbsUserProfilerId() {
		return bbsUserProfilerId;
	}

	public void setBbsUserProfilerId(Integer bbsUserProfilerId) {
		this.bbsUserProfilerId = bbsUserProfilerId;
	}

	public Integer getBbsPostCategoryId() {
		return this.bbsPostCategoryId;
	}

	public void setBbsPostCategoryId(Integer bbsPostCategoryId) {
		this.bbsPostCategoryId = bbsPostCategoryId;
	}

	public Integer getBbsTitleStyleId() {
		return this.bbsTitleStyleId;
	}

	public void setBbsTitleStyleId(Integer bbsTitleStyleId) {
		this.bbsTitleStyleId = bbsTitleStyleId;
	}

	public Integer getBbsTopicsId() {
		return this.bbsTopicsId;
	}

	public void setBbsTopicsId(Integer bbsTopicsId) {
		this.bbsTopicsId = bbsTopicsId;
	}

	public String getTitle() {
		return this.title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getContent() {
		return this.content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	public Integer getFrontCategoryId() {
		return this.frontCategoryId;
	}

	public void setFrontCategoryId(Integer frontCategoryId) {
		this.frontCategoryId = frontCategoryId;
	}

	public String getIsShow() {
		return this.isShow;
	}

	public void setIsShow(String isShow) {
		this.isShow = isShow;
	}

	public String getIsDel() {
		return this.isDel;
	}

	public void setIsDel(String isDel) {
		this.isDel = isDel;
	}

	public String getCheckPerson() {
		return this.checkPerson;
	}

	public void setCheckPerson(String checkPerson) {
		this.checkPerson = checkPerson;
	}

	public String getCheckStatus() {
		return this.checkStatus;
	}

	public void setCheckStatus(String checkStatus) {
		this.checkStatus = checkStatus;
	}

	public Date getCheckTime() {
		return this.checkTime;
	}

	public void setCheckTime(Date checkTime) {
		this.checkTime = checkTime;
	}

	public String getUncheckedCheckStatus() {
		return this.uncheckedCheckStatus;
	}

	public void setUncheckedCheckStatus(String uncheckedCheckStatus) {
		this.uncheckedCheckStatus = uncheckedCheckStatus;
	}

	public String getUnpassReason() {
		return this.unpassReason;
	}

	public void setUnpassReason(String unpassReason) {
		this.unpassReason = unpassReason;
	}

	public String getIsHotPost() {
		return isHotPost;
	}

	public void setIsHotPost(String isHotPost) {
		this.isHotPost = isHotPost;
	}

	public String getPostType() {
		return this.postType;
	}

	public void setPostType(String postType) {
		this.postType = postType;
	}

	public Integer getVisitedCount() {
		return this.visitedCount;
	}

	public void setVisitedCount(Integer visitedCount) {
		this.visitedCount = visitedCount;
	}

	public Integer getReplyCount() {
		return this.replyCount;
	}

	public void setReplyCount(Integer replyCount) {
		this.replyCount = replyCount;
	}

	public Date getPostTime() {
		return this.postTime;
	}

	public void setPostTime(Date postTime) {
		this.postTime = postTime;
	}

	public Date getReplyTime() {
		return replyTime;
	}

	public void setReplyTime(Date replyTime) {
		this.replyTime = replyTime;
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

	public String getUrl() {
		return url;
	}

	public void setUrl(String url) {
		this.url = url;
	}

	/**
	 * @return the integral
	 */
	public Integer getIntegral() {
		return integral;
	}

	/**
	 * @param integral
	 *            the integral to set
	 */
	public void setIntegral(Integer integral) {
		this.integral = integral;
	}

	public String getTags() {
		return tags;
	}

	public void setTags(String tags) {
		this.tags = tags;
	}

	public Integer getBbsPostAssistId() {
		return bbsPostAssistId;
	}

	public void setBbsPostAssistId(Integer bbsPostAssistId) {
		this.bbsPostAssistId = bbsPostAssistId;
	}

	public Integer getNoticeCount() {
		return noticeCount;
	}

	public void setNoticeCount(Integer noticeCount) {
		this.noticeCount = noticeCount;
	}

	public Integer getRecommendCount() {
		return recommendCount;
	}

	public void setRecommendCount(Integer recommendCount) {
		this.recommendCount = recommendCount;
	}

	public Integer getCollectCount() {
		return collectCount;
	}

	public void setCollectCount(Integer collectCount) {
		this.collectCount = collectCount;
	}

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public String getChildCategory() {
		return childCategory;
	}

	public void setChildCategory(String childCategory) {
		this.childCategory = childCategory;
	}
}