

<%@ page import="com.nala.csd.LogisticsProblem" %>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta name="layout" content="main" />
        <g:set var="entityName" value="${message(code: 'logisticsProblem.label', default: 'LogisticsProblem')}" />
        <title><g:message code="default.create.label" args="[entityName]" /></title>
    </head>
    <body>
        <div class="nav">
            <span class="menuButton"><a class="home" href="${createLink(uri: '/')}"><g:message code="default.home.label"/></a></span>
            <span class="menuButton"><g:link class="list" action="list"><g:message code="default.list.label" args="['快递问题件']" /></g:link></span>
        </div>
        <div class="body">
            <h1><g:message code="default.create.label" args="[entityName]" /></h1>
            <g:if test="${flash.message}">
            <div class="message">${flash.message}</div>
            </g:if>
            <g:hasErrors bean="${logisticsProblemInstance}">
            <div class="errors">
                <g:renderErrors bean="${logisticsProblemInstance}" as="list" />
            </div>
            </g:hasErrors>
            <g:form action="save" >
                <div class="dialog">
                    <table>
                        <tbody>
							<tr class="prop">
                                <td valign="top" class="name">
                                    <label for="express_id">物流公司(必填)</label>
                                </td>
                                <td valign="top" class="value">
                                    <g:select name="express_id" from="${com.nala.csd.Express.list()*.name}" keys="${com.nala.csd.Express.list()*.id}" noSelection="['': '']" />
                                </td>
                            </tr>
                                                    
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="expressProblem_id">物流单号(必填)</label>
                                </td>
                                <td valign="top" class="value">
                                    <g:textField name="expressProblem_id" value="" />
                                </td>
                            </tr>
                            
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="expressProblem_type">问题类型(必填)</label>
                                </td>
                                <td valign="top" class="value">
                                    <g:textField name="expressProblem_type" value="" />
                                </td>
                            </tr>
                            
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="expressProblem_description">问题描述(必填)</label>
                                </td>
                                <td valign="top" class="value">                                 
                                    <textarea name="expressProblem_description" rows="2" cols="20"></textarea>
                                </td>
                            </tr>
                                                    
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="store"><g:message code="logisticsProblem.store.label" default="店铺" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'store', 'errors')}">
                                    <g:select name="store.id" from="${com.nala.csd.Store.list()*.name}" keys="${com.nala.csd.Store.list()*.id}" value="${logisticsProblemInstance?.store?.id }" noSelection="['':'']"  />
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="userId"><g:message code="logisticsProblem.userId.label" default="顾客ID" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'userId', 'errors')}">
                                    <g:textField name="userId" value="${logisticsProblemInstance?.userId}" />
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="remark"><g:message code="logisticsProblem.remark.label" default="备注" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'remark', 'errors')}">                                    
                                    <textarea name="remark" rows="2" cols="20"></textarea>
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="solveType"><g:message code="logisticsProblem.solveType.label" default="处理方式" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'solveType', 'errors')}">
                                    <g:textField name="solveType" value="${logisticsProblemInstance?.solveType}" />
                                </td>
                            </tr>

                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="solveCS"><g:message code="logisticsProblem.solveCS.label" default="处理人" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'solveCS', 'errors')}">
                                    <g:select name="solveCS.id" from="${com.nala.csd.Hero.list()*.name}" keys="${com.nala.csd.Hero.list()*.id}" value="${logisticsProblemInstance?.solveCS?.id }" noSelection="['': '']" />
                                    
                                </td>
                            </tr>
                            
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="results"><g:message code="logisticsProblem.results.label" default="处理结果" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'results', 'errors')}">                                    
                                    <textarea name="results" rows="2" cols="20"></textarea>
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="mobile"><g:message code="logisticsProblem.mobile.label" default="手机号" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'mobile', 'errors')}">
                                    <g:textField name="mobile" value="${logisticsProblemInstance?.mobile}" />
                                </td>
                            </tr>
                            
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="receiveInfo">收件信息</label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'receiveInfo', 'errors')}">
                                    <g:textField name="receiveInfo" value="${logisticsProblemInstance?.receiveInfo}" />
                                </td>
                            </tr>

                            <tr class="prop">
                                <td valign="top" class="name"><label for="sendGoodsDate">发货日期</label>
                                </td>
                                <td valign="top" class="value"><input id="sendGoodsDateStr"	name="sendGoodsDateStr" type="text"	onClick="WdatePicker({dateFmt:'yyyy-MM-dd'})" style="width: 160px"
                                                                      value="<g:formatDate format="yyyy-MM-dd" date="${logisticsProblemInstance?.sendGoodsDate}"/>" />
                                </td>
                            </tr>

                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="notifyMode"><g:message code="logisticsProblem.notifyMode.label" default="通知方式" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'notifyMode', 'errors')}">
                                    <g:select name="notifyMode.id" from="${com.nala.csd.NotifyMode.list()*.name}" keys="${com.nala.csd.NotifyMode.list()*.id}" value="${logisticsProblemInstance?.notifyMode?.id }" noSelection="['': '']" />
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="followUp"><g:message code="logisticsProblem.followUp.label" default="是否跟踪" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'followUp', 'errors')}">
                                    <g:checkBox name="followUp" value="${logisticsProblemInstance?.followUp}" />
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="followCS"><g:message code="logisticsProblem.followCS.label" default="跟踪人" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'followCS', 'errors')}">
                                    <g:select name="followCS.id" from="${com.nala.csd.Hero.list()*.name}" keys="${com.nala.csd.Hero.list()*.id}" value="${logisticsProblemInstance?.followCS?.id }" noSelection="['': '']" />
                                    
                                </td>
                            </tr>
                        
                            <tr class="prop">
                                <td valign="top" class="name">
                                    <label for="signUp"><g:message code="logisticsProblem.signUp.label" default="是否签收" /></label>
                                </td>
                                <td valign="top" class="value ${hasErrors(bean: logisticsProblemInstance, field: 'signUp', 'errors')}">
                                    <g:checkBox name="signUp" value="${logisticsProblemInstance?.signUp}" />
                                </td>
                            </tr>

                        </tbody>
                    </table>
                </div>
                <div class="buttons">
                    <span class="button"><g:submitButton name="create" class="save" value="${message(code: 'default.button.create.label', default: 'Create')}" /></span>
                </div>
            </g:form>
        </div>
    </body>
</html>