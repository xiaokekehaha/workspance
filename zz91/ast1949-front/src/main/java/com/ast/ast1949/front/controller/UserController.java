/**
 * Copyright 2010 ASTO.
 * All right reserved.
 * Created on 2010-7-15
 */
package com.ast.ast1949.front.controller;

import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.Date;
import java.util.Map;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import com.ast.ast1949.domain.auth.AuthForgotPassword;
import com.ast.ast1949.domain.auth.AuthUser;
import com.ast.ast1949.domain.company.CompanyAccount;
import com.ast.ast1949.domain.company.GetPasswordLog;
import com.ast.ast1949.dto.ExtResult;
import com.ast.ast1949.dto.PageHeadDTO;
import com.ast.ast1949.service.auth.AuthService;
import com.ast.ast1949.service.company.CompanyAccountService;
import com.ast.ast1949.service.company.GetPasswordLogService;
import com.ast.ast1949.util.DateUtil;
import com.zz91.util.seo.SeoUtil;
import com.zz91.util.sms.SmsUtil;

/**
 * @author Mays (x03570227@gmail.com)
 *
 */
@Controller
public class UserController extends BaseController {

	@Resource
	private AuthService authService;
	@Resource
    private CompanyAccountService companyAccountService;
	@Resource
	private GetPasswordLogService getPasswordLogService;
	
	final static public String EMAIL_TYPE = "0";
	final static public String MOBILE_TYPE = "1";
	final static public String QQ_EMAIL_TYPE = "2";

	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView passwordReminder(Map<String, Object> model){
		
	    // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"登录时遇到问题了？"},
                new String[]{""},
                new String[]{""},model);
		/*setSiteInfo(new PageHeadDTO(), model);*/
	    return new ModelAndView();
	}

	@RequestMapping(value = "forgetPasswd.htm" , method = RequestMethod.GET)
    public ModelAndView forgetPasswd(Map<String, Object> out, 
            String errorMsg, HttpServletRequest request){
	    // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
	    out.put("errorMsg", errorMsg);
	    return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView forgetAuth(Map<String, Object> out , HttpServletRequest request){
        // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了登录名"},
                new String[]{""},
                new String[]{""},out);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView getPasswd(Map<String, Object> out , HttpServletRequest request,String username){
       // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
        AuthUser authUser = authService.queryAuthUserByUsername(username);
        if (authUser == null) {
            out.put("errorMsg", "您输入的账号有误！");
            return new ModelAndView("/user/forgetPasswd");
        }
        out.put("username", username);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView mobileForPasswd(Map<String, Object> out , HttpServletRequest request , String username){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
        
        CompanyAccount companyAccount = companyAccountService.queryAccountByAccount(username);
        String mobile = "********" + companyAccount.getMobile().substring(companyAccount.getMobile().length()-3,companyAccount.getMobile().length());
        out.put("mobile", mobile);
        out.put("allMobile", companyAccount.getMobile());
        out.put("username", username);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView resetPasswordForPasswd(Map<String, Object> model,String password, String username)
        throws IOException, NoSuchAlgorithmException{
      // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},model);
        if (authService.resetPasswordByMobileKey(username,password)) {
            return new ModelAndView("/user/resetPwSuccess");
        }
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView mailForPasswd(Map<String, Object> out , HttpServletRequest request , String username)
            throws IOException, NoSuchAlgorithmException{
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
        CompanyAccount companyAccount = companyAccountService.queryAccountByAccount(username);
        GetPasswordLog getPasswordLog = new GetPasswordLog();
        getPasswordLog.setCompanyId(companyAccount.getCompanyId());
        getPasswordLog.setType(EMAIL_TYPE);
        if (getPasswordLogService.numOfType(companyAccount.getCompanyId(), EMAIL_TYPE) < 5) {
            String email = companyAccount.getEmail();
            if (companyAccount.getIsUseBackEmail() != null && companyAccount.getIsUseBackEmail().equals("1")) {
                email = companyAccount.getBackEmail();
            }
            String key = authService.generateForgotPasswordKey(email);
            if(key!=null){
                String url="#";
                if(request.getServerPort()==80){
                    url=request.getServerName()+request.getContextPath();
                }else{
                    url=request.getServerName()+":"+request.getServerPort()+request.getContextPath();
                }
                authService.sendResetPasswordMail(key,email,url);
                getPasswordLogService.insertPasswordLog(getPasswordLog);
            }
            int index = email.indexOf("@");
            String hiddenEmail = email.replace(email.substring(4, index), "**");
            String goEmail = "http://mail."+email.substring(index+1,email.length());
            out.put("username", username);
            out.put("email", email);
            out.put("hiddenEmail", hiddenEmail);
            out.put("goEmail", goEmail);
            return new ModelAndView();
        } else {
            out.put("username", username);
            out.put("error", "1");
            return new ModelAndView("/user/getPasswd");
        }
        
    }
    @RequestMapping
    public ModelAndView qqForPasswd(Map<String, Object> out , HttpServletRequest request , String username){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
        out.put("username", username);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView qqForPasswdNext(Map<String, Object> out , HttpServletRequest request , CompanyAccount companyAccount)
            throws IOException, NoSuchAlgorithmException{
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},out);
        String qq = companyAccount.getQq();
        companyAccount = companyAccountService.queryAccountByAccount(companyAccount.getAccount());
        GetPasswordLog getPasswordLog = new GetPasswordLog();
        getPasswordLog.setCompanyId(companyAccount.getCompanyId());
        getPasswordLog.setType(QQ_EMAIL_TYPE);
        if (qq.equals(companyAccount.getQq())) {
            String email = qq + "@qq.com";
            if (getPasswordLogService.numOfType(companyAccount.getCompanyId(), QQ_EMAIL_TYPE) < 5) {
                String key = authService.generateForgotPasswordKey(email);
                if(key!=null){
                    String url="#";
                    if(request.getServerPort()==80){
                        url=request.getServerName()+request.getContextPath();
                    }else{
                        url=request.getServerName()+":"+request.getServerPort()+request.getContextPath();
                    }
                    authService.sendResetPasswordMail(key,email,url);
                    getPasswordLogService.insertPasswordLog(getPasswordLog);
                }
            } else {
                out.put("error", "1");
                out.put("username", companyAccount.getAccount());
                return new ModelAndView("/user/qqForPasswd");
            }
        } else {
            out.put("username", companyAccount.getAccount());
            out.put("errorMsg", "您输入的不是注册时的qq！");
            return new ModelAndView("/user/qqForPasswd");
        }
        out.put("username", companyAccount.getAccount());
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView mobileForAuth(Map<String, Object> out , HttpServletRequest request ){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了登录名"},
                new String[]{""},
                new String[]{""},out);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView mobileForAuthNext(Map<String, Object> out , HttpServletRequest request , CompanyAccount companyAccount){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了登录名"},
                new String[]{""},
                new String[]{""},out);
        /*String mobile = companyAccount.getMobile();*/
        Integer companyId = companyAccountService.queryComapnyIdByMobile(companyAccount.getMobile());
        if (companyId != null && companyId >0) {
            companyAccount = companyAccountService.queryAccountByCompanyId(companyId);
            /*mobile = "********" + companyAccount.getMobile().substring(companyAccount.getMobile().length()-3,companyAccount.getMobile().length());
            out.put("mobile", mobile);
            out.put("allMobile", companyAccount.getMobile());*/
            out.put("username", companyAccount.getAccount());
            return new ModelAndView();
        } else {
            out.put("errorMsg", "您输入的不是注册时的手机号码！");
            return new ModelAndView("/user/mobileForAuth");
        }
        
        
    }
    @RequestMapping
    public ModelAndView mailForAuth(Map<String, Object> out , HttpServletRequest request ){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了登录名"},
                new String[]{""},
                new String[]{""},out);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView mailForAuthNext(Map<String, Object> out , HttpServletRequest request , CompanyAccount companyAccount)
            throws IOException, NoSuchAlgorithmException{
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了登录名"},
                new String[]{""},
                new String[]{""},out);
        String email = companyAccount.getEmail();
        Integer companyId = companyAccountService.queryCompanyIdByEmail(email);
        companyAccount = companyAccountService.queryAccountByCompanyId(companyId);
        //是否是注册的邮箱！
        Integer i=authService.countUserByEmail(email);
        if (i!= null && i.intValue()>0) {
            if (getPasswordLogService.numOfType(companyAccount.getCompanyId(), EMAIL_TYPE) < 5) {
                GetPasswordLog getPasswordLog = new GetPasswordLog();
                getPasswordLog.setCompanyId(companyAccount.getCompanyId());
                getPasswordLog.setType(EMAIL_TYPE);
                String key = authService.generateForgotPasswordKey(email);
                if(key!=null){
                    String url="#";
                    if(request.getServerPort()==80){
                        url=request.getServerName()+request.getContextPath();
                    }else{
                        url=request.getServerName()+":"+request.getServerPort()+request.getContextPath();
                    }
                    authService.sendResetPasswordMail(key,email,url);
                    getPasswordLogService.insertPasswordLog(getPasswordLog);
                }
                int index = email.indexOf("@");
                String hiddenEmail = email.replace(email.substring(4, index), "**");
                String goEmail = "http://mail."+email.substring(index+1,email.length());
                out.put("email", email);
                out.put("hiddenEmail", hiddenEmail);
                out.put("goEmail", goEmail);
                return new ModelAndView();
            } else {
                out.put("error", "1");
                return new ModelAndView("/user/mailForAuth");
            }
        } else {
            out.put("errorMsg", "您输入的不是注册时的邮箱！");
            return new ModelAndView("/user/mailForAuth");
        }
    }
    @RequestMapping
    public ModelAndView repeatSendEmail(Map<String, Object> model, String email, HttpServletRequest request)
        throws IOException, NoSuchAlgorithmException{
        Integer companyId = companyAccountService.queryCompanyIdByEmail(email);
        ExtResult result = new ExtResult();
        if (companyId != null) {
            if (getPasswordLogService.numOfType(companyId, EMAIL_TYPE) < 5) {
                GetPasswordLog getPasswordLog = new GetPasswordLog();
                getPasswordLog.setCompanyId(companyId);
                getPasswordLog.setType(EMAIL_TYPE);
                String key = authService.generateForgotPasswordKey(email);
                if(key!=null){
                    String url="#";
                    if(request.getServerPort()==80){
                        url=request.getServerName()+request.getContextPath();
                    }else{
                        url=request.getServerName()+":"+request.getServerPort()+request.getContextPath();
                    }
                    authService.sendResetPasswordMail(key,email,url);
                    getPasswordLogService.insertPasswordLog(getPasswordLog);
                    result.setSuccess(true);
                }
            } else {
                result.setData("num");
            }
        }
        return printJson(result, model);
    }
    @RequestMapping
    public ModelAndView SendCheckCode(Map<String, Object> model, String mobile, HttpServletRequest request)
        throws IOException, NoSuchAlgorithmException{
        Integer companyId = companyAccountService.queryComapnyIdByMobile(mobile);
        CompanyAccount companyAccount = companyAccountService.queryAccountByCompanyId(companyId);
        String email = companyAccount.getEmail();
        ExtResult result = new ExtResult();
        if (companyId != null) {
            if (getPasswordLogService.numOfType(companyId, MOBILE_TYPE) < 5) {
                GetPasswordLog getPasswordLog = new GetPasswordLog();
                getPasswordLog.setCompanyId(companyId);
                getPasswordLog.setType(MOBILE_TYPE);
                String key = authService.generateForgotPasswordMobileKey(email);
                String content  ="您正在取回密码，验证码：" + key + "，该验证码1小时内有效。工作人员不会向您索取验证码，切勿泄露给他人【ZZ91再生网】";
                if(key!=null){
                    SmsUtil.getInstance().sendSms(mobile, content);
                    getPasswordLogService.insertPasswordLog(getPasswordLog);
                    result.setSuccess(true);
                }
            } else {
                result.setData("num");
            }
        }
        return printJson(result, model);
    }
    /*
     * 手机验证：当客户发送了手机验证后，接着客户又发送email验证，则手机验证的key会失效
     * 原因： email的key和手机的key是放在auth_forgot_password这同一张表中，而手机key查找是按用户最新的key。
     */
    @RequestMapping
    public ModelAndView verifyCheckCode(Map<String, Object> out, HttpServletRequest request, String smscomfirmcode) 
            throws IOException, NoSuchAlgorithmException{
        ExtResult result = new ExtResult();
        do {
                AuthForgotPassword o= authService.listAuthForgotPasswordByKey(smscomfirmcode);
                if(o==null){
                    break;
                }
                long start=DateUtil.getMillis(o.getGmtCreated());
                long now=DateUtil.getMillis(new Date());
                long twoday=60*60*1000;
                if((now-start)>twoday){
                    result.setData("验证码已过期！");
                } else if (smscomfirmcode.equals(o.getAuthKey())){
                    result.setSuccess(true);
                } else {
                    result.setSuccess(false);
                }
        } while (false);
        
        return printJson(result, out);
    }
    @RequestMapping
    public ModelAndView emailExpired(Map<String, Object> out , HttpServletRequest request){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"邮箱已过期"},
                new String[]{""},
                new String[]{""},out);
        return new ModelAndView();
    }
    @RequestMapping
    public ModelAndView resetPwSuccess(Map<String, Object> out , HttpServletRequest request){
     // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"密码成功找回"},
                new String[]{""},
                new String[]{""},out);
        return new ModelAndView();
    }
	/*@RequestMapping(method = RequestMethod.POST)
	public ModelAndView passwordReminder2(Map<String, Object> model, String email, HttpServletRequest request)
		throws IOException, NoSuchAlgorithmException{
		ExtResult result = new ExtResult();
		String key = authService.generateForgotPasswordKey(email);
		if(key!=null){
			String url="#";
			if(request.getServerPort()==80){
				url=request.getServerName()+request.getContextPath();
			}else{
				url=request.getServerName()+":"+request.getServerPort()+request.getContextPath();
			}
			authService.sendResetPasswordMail(key,email,url);
			result.setSuccess(true);
		}
		return printJson(result, model);
	}*/

	/*@RequestMapping(method = RequestMethod.POST)
	public ModelAndView isemailregist(Map<String, Object> model, String email) throws IOException{
		ExtResult result = new ExtResult();
		Integer i=authService.countUserByEmail(email);
		if (i!= null && i.intValue()>0) {
			result.setSuccess(true);
//			result.setData(u.getId());
		}
		return printJson(result, model);
	}*/

	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView resetPassword(Map<String, Object> model, String k, String am) throws NoSuchAlgorithmException, UnsupportedEncodingException {
	 // seo keyword description title 
        SeoUtil.getInstance().buildSeo("resetPassword",
                new String[]{"我忘记了密码"},
                new String[]{""},
                new String[]{""},model);
		do {
			if(am==null || "".equals(am)){
				break;
			}
			if(k==null || "".equals(k)){
				break;
			}
			AuthForgotPassword o= authService.listAuthForgotPasswordByKey(k);
			if(o==null){
			    return new ModelAndView("/user/emailExpired");
			}
			long start=DateUtil.getMillis(o.getGmtCreated());
			long now=DateUtil.getMillis(new Date());
			long twoday=2*60*60*24*1000;
			if((now-start)>twoday){
			    return new ModelAndView("/user/emailExpired");
			}
			model.put("k", k); //key
	        model.put("am", am);
	        model.put("username", o.getUsername());
		} while (false);
		 return new ModelAndView();
	}

	@RequestMapping
	public ModelAndView resetPassword(Map<String, Object> model, String k, String am, String pwd1, String pwd2)
		throws IOException, NoSuchAlgorithmException{
		if(authService.resetPasswordFromForgotPasswordKey(am, k, pwd1)) {
		    return new ModelAndView("/user/resetPwSuccess");
		}
		 return new ModelAndView();
	}
}
