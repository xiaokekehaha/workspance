package com.ast.ast1949.persist.analysis.impl;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Component;

import com.ast.ast1949.domain.analysis.AnalysisProductTypeCode;
import com.ast.ast1949.persist.BaseDaoSupport;
import com.ast.ast1949.persist.analysis.AnalysisProductTypeCodeDao;

/**
 * @author kongsj
 * @date 2012-9-11
 */
@Component("analysisProductTypeCodeDao")
public class AnalysisProductTypeCodeDaoImpl extends BaseDaoSupport implements
		AnalysisProductTypeCodeDao {
	final static String SQL_PRE = "analysisProductTypeCode";

	@SuppressWarnings("unchecked")
	@Override
	public List<AnalysisProductTypeCode> queryAnalysisProductTypeCode(String account,
			String start, String end) {
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("account", account);
		map.put("start", start);
		map.put("end", end);
		return getSqlMapClientTemplate().queryForList(addSqlKeyPreFix(SQL_PRE, "queryAnalysisProductTypeCode"),	map);
	}

}
