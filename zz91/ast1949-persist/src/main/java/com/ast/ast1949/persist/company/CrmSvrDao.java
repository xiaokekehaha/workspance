package com.ast.ast1949.persist.company;

import java.util.List;
import java.util.Map;

import com.ast.ast1949.domain.company.CrmSvr;

public interface CrmSvrDao {
 
	/**
	 *  
	 */
	public List<CrmSvr> querySvr();
	
	public List<CrmSvr> querySvrByGroup(String group);
	
	public Map<String, String> queryMembershipOfSvr(String group);
	
	public String queryApi(String svrCode, String apiName);
}
 
