package com.zz91.ep.dao.mblog;

import java.util.List;

import com.zz91.ep.domain.mblog.MBlogInfo;
import com.zz91.ep.dto.PageDto;
import com.zz91.ep.dto.mblog.MBlogInfoDto;
import com.zz91.ep.dto.search.SearchSupplyDto;
import com.zz91.ep.dto.trade.TradeSupplyNormDto;

/**
 * author:fangchao 
 * date: 2013-10-23
 */
public interface MBlogInfoDao {
	/**
	 * 函数名称：insert
	 * 功能描述：添加账户信息
	 * 输入参数：
	 * 		   @param MBlogInfoDao mBlogInfo 账户信息
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/22　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public Integer insert(MBlogInfo mBlogInfo);
	 /**
	 * 函数名称：update
	 * 功能描述：修改账户信息
	 * 输入参数：
	 * 		   @param MBlogInfoDao mBlogInfo 账户信息
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/22　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public Integer update(MBlogInfo mBlogInfo);
	 /**
	 * 函数名称：queryInfoById
	 * 功能描述：根据账户信息查询用户信息
	 * 输入参数：
	 * 		   @param Integer id 账户信息id
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/23　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public MBlogInfo queryInfoById(Integer id);
	 /**
	 * 函数名称：queryInfoByName
	 * 功能描述：根据昵称信息查询用户信息
	 * 输入参数：
	 * 		   @param String name 昵称
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/23　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public List<MBlogInfo> queryInfoByName(String name,PageDto<MBlogInfo> page);
	 /**
	 * 函数名称：queryInfoCountByName
	 * 功能描述：统计根据昵称信息查询用户信息
	 * 输入参数：
	 * 		   @param String name 昵称
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/23　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public Integer queryInfoCountByName(String name);
	 /**
	 * 函数名称：updateIsDeleteStatus
	 * 功能描述：修改账户信息
	 * 输入参数：
	 * 		   @param Integer id 账户信息
	 *         @param String isDelete 账户状态
	 * 		   
	 * 异　　常：无
	 * 变更履历：修改日期　　　　　修改者　　　　　　　版本号　　　　　 修改内容
	 * 　　　　　2013/10/23　　 fangchao 　　 　　 1.0.0　　 　　 创建方法函数
	 */
	 public Integer updateIsDeleteStatus(String account,String isDelete);
	 
	 public List<MBlogInfo> queryInfobyAreaCode(String areaCode,String provinceCode);
	 
	 public MBlogInfo queryInfoByInfoIdorCid(Integer infoId,Integer cid);
	 
	 public MBlogInfo queryInfoByInfoByName(String name);
	 
	 public MBlogInfo queryInfoByCid(Integer cid);
}