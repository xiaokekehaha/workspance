/*
 * 文件名称：CrmSvrRight.java
 * 创建者　：涂灵峰
 * 创建时间：2012-4-18 下午3:46:56
 * 版本号　：1.0.0
 */
package com.zz91.ep.domain.crm;

import java.util.Date;

/**
 * 项目名称：中国环保网
 * 模块编号：数据持久层
 * 模块描述：服务对应权限表。
 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　修改内容
 *　　　　　 2012-04-18　　　涂灵峰　　　　　　　1.0.0　　　　　创建类文件
 */
public class CrmSvrRight implements java.io.Serializable {

	private static final long serialVersionUID = 1L;

	private Integer id;
	private Integer crmSvrId;
	private Integer crmRightId;
	private Date gmtCreated;
	private Date gmtModified;

	public Integer getId() {
		return this.id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Integer getCrmSvrId() {
		return this.crmSvrId;
	}

	public void setCrmSvrId(Integer crmSvrId) {
		this.crmSvrId = crmSvrId;
	}

	public Integer getCrmRightId() {
		return this.crmRightId;
	}

	public void setCrmRightId(Integer crmRightId) {
		this.crmRightId = crmRightId;
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