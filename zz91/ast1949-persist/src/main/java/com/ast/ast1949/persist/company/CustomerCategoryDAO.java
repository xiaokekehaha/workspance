/**
 * Copyright 2010 ASTO.
 * All right reserved.
 * Created on 2010-5-31
 */
package com.ast.ast1949.persist.company;

import java.util.List;

import com.ast.ast1949.domain.company.CustomerCategoryDO;

/**
 * @author Rolyer (rolyer.live@gmail.com)
 *
 */
public interface CustomerCategoryDAO {
	/**
	 * 添加类别
	 * @param customerCategory 
	 * 		参数不可为空。
	 * @return
	 */
	public Integer insertCustomerCategory(CustomerCategoryDO customerCategory);
	/**
	 * 删除类别
	 * @param id 编号<br/>
	 * 		id不可为空。
	 * @return
	 */
	public Integer deleteCustomerCategory(Integer id);
	/**
	 * 更新类别
	 * @param customerCategory
	 * 		参数不可为空。
	 * @return
	 */
	public Integer updateCustomerCategory(CustomerCategoryDO customerCategory);
	/**
	 * 根据编号查询信息
	 * @param id 编号
	 * @return
	 */
	public CustomerCategoryDO queryCustomerCategoryById(Integer id);
	/**
	 * 根据父编号查询信息
	 * @param id 父ID
	 * @return
	 */
	public List<CustomerCategoryDO> queryCustomerCategoryByParentId(Integer id);
	/**
	 * 根据类别名称统计记录总数
	 * @param name 名称
	 * @return
	 */
//	public Integer countCustomerCategoryByName(String name);
}
