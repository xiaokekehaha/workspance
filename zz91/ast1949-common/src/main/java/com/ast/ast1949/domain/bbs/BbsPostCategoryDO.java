package com.ast.ast1949.domain.bbs;

import java.util.Date;

/**
 * BbsPostCategory generated by MyEclipse Persistence Tools
 */

public class BbsPostCategoryDO implements java.io.Serializable {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	// Fields

	private Integer id;
	private Integer parentId;
	private Integer l;
	private Integer r;
	private String isDel;
	private String name;
	private String remark;
	private Date gmtCreated;
	private Date gmtModified;

	// Constructors

	/** default constructor */
	public BbsPostCategoryDO() {
	}

	/** minimal constructor */
	public BbsPostCategoryDO(Integer id) {
		this.id = id;
	}

	/** full constructor */
	public BbsPostCategoryDO(Integer id, Integer parentId, Integer l, Integer r,
			String isDel, String name, String remark, Date gmtCreated,
			Date gmtModified) {
		this.id = id;
		this.parentId = parentId;
		this.l = l;
		this.r = r;
		this.isDel = isDel;
		this.name = name;
		this.remark = remark;
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

	public Integer getParentId() {
		return this.parentId;
	}

	public void setParentId(Integer parentId) {
		this.parentId = parentId;
	}

	public Integer getL() {
		return this.l;
	}

	public void setL(Integer l) {
		this.l = l;
	}

	public Integer getR() {
		return this.r;
	}

	public void setR(Integer r) {
		this.r = r;
	}

	public String getIsDel() {
		return this.isDel;
	}

	public void setIsDel(String isDel) {
		this.isDel = isDel;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getRemark() {
		return this.remark;
	}

	public void setRemark(String remark) {
		this.remark = remark;
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