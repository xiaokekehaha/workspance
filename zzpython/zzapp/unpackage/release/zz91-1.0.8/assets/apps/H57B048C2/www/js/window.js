﻿// 百度地图API功能
var nowaddress;
var dwflag = true;
var oldaddress;
var redw = false;
var nowprovice;
var nowcity;
if (window.plus) {
	var netstatst = getnetstats();
	if (netstatst != "未连接网络") {
		if (BMap) {
			var myGeo = new BMap.Geocoder();
		}
	}
}
var dwtype = 1;
var nWaiting;

function login() {
		gotourl("/login/", "login");
	}
	//通用加载页面
var loadnum = 0;
//加载新数据
function loaddata(url) {

}

function gotourl(url, wintype) {
	if (wintype != "blank") {
		nowwintype = wintype;
	}
	checkUpdate();
	blankpage=2;
	var trueurl=url
	if (company_id == 0) {
		if (wintype == "laidianbao" || wintype == "myrc" || wintype == "qianbao" || wintype == "messages" || wintype == "order") {
			url = "/login/?tourl=" + url + "&wintarget=" + wintype;
			wintype = "login";
		}
	}
	url = url.replace("/companyinfo/?company_id=", "/companyinfo/?forcid=");
	if (wintype == "blank" || wintype == "reg") {
		url = url.replace("&", "TandT").replace("?", "wenhao")
		mui.openWindow({
			id: url,
			url: "blank.html?url2=" + url + "&wintype=" + wintype + "&company_id=" + company_id.toString() + "&clientid=" + clientid + "&appsystem=" + appsystem + "&visitoncode=" + visitoncode,
			preload: false //TODO 等show，hide事件，动画都完成后放开预加载
		});
		return;
	}
	if (window.plus) {
		nWaiting = plus.nativeUI.showWaiting("数据加载中......");
	}
	var backwin = 1;
	if (url.indexOf("http://app.zz91.com") < 0) {
		if (url.indexOf("?") < 0) {
			url = "http://app.zz91.com/" + url + "?t=" + (new Date()).getTime().toString() + "&company_id=" + company_id.toString() + "&win=" + win.toString() + "&clientid=" + clientid + "&appsystem=" + appsystem + "&visitoncode=" + visitoncode;
		} else {
			url = "http://app.zz91.com/" + url + "&t=" + (new Date()).getTime().toString() + "&company_id=" + company_id.toString() + "&win=" + win.toString() + "&clientid=" + clientid + "&appsystem=" + appsystem + "&visitoncode=" + visitoncode;
		}
	}
	if (indexwin){
		var backwin = indexwin[indexwin.length - 1];
		if (backwin){
			if (backwin[1]==trueurl){
				if (nWaiting) {
					nWaiting.close();
				}
				return;
			}
		}
	}
	
	if (isback == 1) {
		indexwin.push([wintype, trueurl]);
	}
	var content = document.getElementById("dcontent1");
	
	if (content) {
		content.innerHTML = "<br /><br /><center class=midload><img src=images/96R.gif><br>正在为您努力加载中......<br /></center>"
	}
	showheader(wintype);
	//plus.storage.clear();
	var backcontent = plus.storage.getItem(trueurl);
	var backcontenttime = plus.storage.getItem(trueurl+'time');
	if (backcontent && backcontenttime && trueurl!="/messagelist/"){
		var dc = parseInt(backcontenttime);
		var dn = (new Date()).getTime();
		if (dn - dc > winInterval) { // 未超过上次升级检测间隔，不需要进行升级检查
			plus.storage.removeItem(trueurl);
			plus.storage.removeItem(trueurl+'time');
		}else{
			content.innerHTML=backcontent;
			iOSclosecontent();
			if (nWaiting) {
				nWaiting.close();
			}
			window.scrollTo(0, 0);
			return;
		}
	}
	var xhr = null;
	var textvalue = "";
	var protocol = /^([\w-]+:)\/\//.test(url) ? RegExp.$1 : window.location.protocol;
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		switch (xhr.readyState) {
			case 4:
				if ((xhr.status >= 200 && xhr.status < 300) || xhr.status === 304 || (xhr.status === 0 && protocol === 'file:')) {
					textvalue = xhr.responseText;
					content.innerHTML = textvalue;
					plus.storage.setItem(trueurl, textvalue);
					plus.storage.setItem(trueurl+'time', (new Date()).getTime().toString());
					if (nWaiting) {
						nWaiting.close();
					}
					iOSclosecontent();
				} else {
					loadnum += 1;
					if (loadnum <= 3) {
						gotourl(url, wintype);
					} else {
						var btnArray = ['重试加载', '取消'];
						mui.confirm('哎呀,网络不给力，点击重试加载试试！', '提示', btnArray, function(e) {
							if (e.index == 0) {
								gotourl(url, wintype);
								if (nWaiting) {
									nWaiting.close();
								}
							} else if (e.index == 1) {
								if (nWaiting) {
									nWaiting.close();
								}
							} else {
								if (nWaiting) {
									nWaiting.close();
								}
							}
							if (nWaiting) {
								nWaiting.close();
							}
						});
					}
				}
				break;
			default:
				if (nWaiting) {
					nWaiting.close();
				}
				break;
		}
	}
	xhr.open("GET", url);
	xhr.send();
	if (nWaiting) {
		nWaiting.close();
	}
	nowurl = url;
	nowherf = url;
	window.scrollTo(0, 0);
}

function getmessagesnum(cid) {
	if (cid) {
		mui.get("http://app.zz91.com/messagescount.html?company_id=" + cid.toString(),
			function(data) {
				var j = JSON.parse(data);
				if (isJson(j)) {
					var count = j.count;
					//count=2;
					if (count > 0) {
						var messagescount = document.getElementById("messagescount");
						if (messagescount) {
							messagescount.innerHTML = count;
							messagescount.style.display = "block";
						}
						if (appsystem=="iOS"){
							plus.runtime.setBadgeNumber( count );
						}
					}else{
						if (appsystem=="iOS"){
							plus.runtime.setBadgeNumber( 0 );
						}
					}
				}else{
					if (appsystem=="iOS"){
						plus.runtime.setBadgeNumber( 0 );
					}
				}
			});
	}
	
}

function zz91search(frm, url, wintype) {
		var keywords = frm.searchtext.value;
		gotourl(url + keywords, wintype);
}
	//地理位置定位
var searchname = "";

function geocodeSearch(latitude, longitude) {
		var i = 0;
		if (dwflag == true) {
			var pt = new BMap.Point(longitude, latitude)
			myGeo.getLocation(pt, function(rs) {
				var addComp = rs.addressComponents;
				nowprovice = addComp.province;
				nowcity = addComp.city;
				district = addComp.district;
				nowaddress = nowprovice.replace("省", "");
				nowaddress += " " + nowcity.replace("市", "");
				var oldaddress = plus.storage.getItem("nowaddress");
				if (oldaddress != nowaddress) {
					redw = true;
					plus.storage.setItem("nowaddress", nowaddress);
				}
				dwflag = false;
			});
		}
		//alert(i)
		var mylocation_status = document.getElementById("mylocation_status")
		if (mylocation_status) {
			//mylocation_status.innerHTML="GPS定位中1...";
			//mylocation_status.innerHTML=nowaddress;
			//alert(nowaddress)
		} else {
			if (i <= 8) {
				geocodeSearch();
			}
			i += 1;
		}
	}
	//附近信息

function fjsearch() {
	var url = "/offerlist/?province=" + nowaddress + "";
	gotourl(url, 'fj');
	//alert(nowaddress)
	//plus.storage.setItem("nowaddress", null);
	//plus.storage.clear()
}

function myFun(result) {
	var cityName = result.name;
	searchname = cityName;
	searchname = searchname.replace("省", "");
	searchname = searchname.replace("市", "");
	plus.storage.setItem("nowaddress", searchname);
}

function dingw() {
	if (navigator.geolocation) {
		//			navigator.geolocation.getCurrentPosition(function(position) {
		//				//dwtype=2;
		//				latitude = position.coords.latitude;
		//				longitude = position.coords.longitude;
		//				geocodeSearch(latitude, longitude);
		//			});
	} else {
		var mylocation_status = document.getElementById("mylocation_status")
		if (mylocation_status) {
			mylocation_status.innerHTML = "GPS定位失败";
		} else {
			setTimeout(dingw, 1000);
		}
	}

	if (dwtype == 1) {

		var mylocation_status = document.getElementById("mylocation_status")
		if (mylocation_status) {
			mylocation_status.innerHTML = nowaddress;
			dwtype = 2;
		} else {
			//alert(nowaddress)

			setTimeout(dingw, 1000);
		}
		if (nWaiting) {
			nWaiting.close();
		}
	} else {

	}
}

function fj() {
	if (appsystem!="iOS"){
		var nWaitingfj = plus.nativeUI.toast("GPS定位中...");
	}
	oldaddress = plus.storage.getItem("oldaddress");
	if (BMap){
		var myCity = new BMap.LocalCity();

		myCity.get(myFun);
		nowaddress = plus.storage.getItem("nowaddress");
	
		if (oldaddress != nowaddress) {
			plus.storage.setItem("oldaddress", nowaddress);
		} else {
			if (oldaddress != null && nowaddress != null) {
				fjsearch();
			}
			if (nWaitingfj) {
				nWaitingfj.close();
			}
			//alert(nowaddress);
			return false;
		}

	}
	
	//	if (navigator.geolocation) {
	//		navigator.geolocation.getCurrentPosition(function(position) {
	//			latitude = position.coords.latitude;
	//			longitude = position.coords.longitude;
	//			geocodeSearch(latitude, longitude);
	//		});
	//	} 
	//	
	//redw=true
	if (nowaddress == null || nowaddress == "") {
		var url = "/fj.html?keywords=" + nowaddress + "&myaddress=GPS定位中...";
	} else {
		var url = "/fj.html?keywords=" + nowaddress + "&myaddress=" + nowaddress + "";
	}
	if (nWaitingfj) {
		nWaitingfj.close();
	}
	gotourl(url, 'fj');

	if (nowprovice == "" || nowprovice == null) {
		dingw()
	} else {
		var url = "/fj.html?keywords=" + nowaddress + "&myaddress=" + nowprovice + " " + nowcity + " " + district;;
		gotourl(url, 'fj');
	}
}

function getPushInfo11() {
	var info = plus.push.getClientInfo();
	//outSet( "获取客户端推送标识信息：" );
	//outLine( "token: "+info.token );
	//outLine( "clientid: "+info.clientid );
	//outLine( "appid: "+info.appid );
	//outLine( "appkey: "+info.appkey );
	createLocalPushMsg();
}

function getPushInfo() {
		var info = plus.push.getClientInfo();
		//alert(info.clientid);
		//outSet( "获取客户端推送标识信息：" );
		//outLine( "token: "+info.token );
		//outLine( "clientid: "+info.clientid );
		//outLine( "appid: "+info.appid );
		//outLine( "appkey: "+info.appkey );
	}
	/**
	 * 本地创建一条推动消息
	 */

function createLocalPushMsg() {
		var options = {
			cover: false
		};
		var str = dateToStr(new Date());
		str += ": 欢迎使用Html5 Plus创建本地消息！";
		plus.push.createMessage(str, "LocalMSG", options);
		//outSet( "创建本地消息成功！" );
		//outLine( "请到系统消息中心查看！" );
		if (plus.os.name == "iOS") {
			//outLine('*如果无法创建消息，请到"设置"->"通知"中配置应用在通知中心显示!');
		}
	}
	/**
	 * 请求‘简单通知’推送消息
	 */

function requireNotiMsg() {
	var url = pushServer + 'notiPush.php?appid=' + encodeURIComponent(plus.runtime.appid);
	url += ('&cid=' + encodeURIComponent(plus.push.getClientInfo().clientid));
	url += ('&title=' + encodeURIComponent('Hello H5+'));
	url += ('&content=' + encodeURIComponent('欢迎回来体验HTML5 plus应用！'));
	plus.runtime.openURL(url);
}

//登陆
function zz91login(frm) {
		var username = frm.username.value;
		var passwd = frm.passwd.value;
		var tourl = frm.tourl.value;
		var wintarget = frm.wintarget.value;
		if (username == "" || passwd == "") {
			return false;
		}
//		var arg = {
//			username: username,
//			passwd: passwd,
//			appid: clientid,
//			loginflag: 1,
//			appsystem: appsystem
//		};
				var arg="username=" + username;
				arg += "&passwd=" + passwd;
				arg += "&appid=" + clientid;
				arg += "&loginflag=1";
				arg += "&appsystem=" + appsystem;
		zzajax("post","http://app.zz91.com/loginof.html", arg, function(data) {
			var j = JSON.parse(data);
			if (j && j.err) {
				if (j.err == "false") {
					company_id = j.result;
					tourl = tourl.replace("company_id=0", "company_id=" + company_id);
					if (tourl != "") {
						nowurl = tourl;
						nowwintype = "index";
						//gotourl(tourl,wintarget);
						
						regloadbody(company_id);
						if (nWaiting) {
							nWaiting.close();
						}
					} else {
						loadappbody();
					}
					plus.storage.setItem("companyid", company_id);
				} else {
					plus.ui.alert(j.errkey);
				}
				if (nWaiting) {
					nWaiting.close();
				}
			} else {
				if (nWaiting) {
					nWaiting.close();
				}
			}
		}, function(data) {

		});
		return false;
	}
	//切换账号

function changeaccount() {
	if (window.plus) {
		nWaiting = plus.nativeUI.showWaiting();
	}
	var arg = "company_id=" + company_id;
	arg += "&clientid=" + clientid;
	mui.get("http://app.zz91.com/changeaccount.html?" + arg, '', function(data) {
		var j = JSON.parse(data);
		company_id = 0;
		plus.storage.setItem("companyid", company_id);
		if (j.changeflag) {

			contactperson = "<div onclick=login()>点此登录</div>";
			var welcome = document.getElementById("navwelcome");
			if (welcome) {
				if (contactperson) {
					welcome.innerHTML = contactperson;
				}
			}
			if (nWaiting) {
				nWaiting.close();
			}
			gotourl("/login/", "login");

		}
		if (nWaiting) {
			nWaiting.close();
		}
	}, function(data) {
		plus.ui.alert("系统错误！请稍后重试.")
	});
	return false;
}







window.HTMLElement.prototype.slideDown = function(speed, height) {
	var o = this;
	//clearInterval(o.slideFun);
	var h = height;
	var i = 0;
	o.style.height = h + 'px';
	//o.style.width = '150px';
	o.style.display = 'block';
	o.style.overflow = 'hidden';
	o.style.removeProperty('overflow');


	//	o.slideFun = setInterval(function(){
	//		
	//		i = i + 5;
	//		if(i>h) i=h;
	//		//o.style.height = i+'px';
	//		if(i>=h)
	//		{
	//			o.style.removeProperty('overflow');
	//			clearInterval(o.slideFun);
	//		}	
	//	},speed);
}

window.HTMLElement.prototype.slideUp = function(speed, height) {
	var o = this;
	//clearInterval(o.slideFun);
	var h = height;
	var i = h;
	//o.style.overflow = 'hidden';
	o.style.display = 'none';
	//o.style.removeProperty('overflow');

	//	o.slideFun = setInterval(function(){
	//		i -= 5;
	//		if(i<0) i=0;
	//		o.style.height = i+'px';
	//		if(i<=0)
	//		{
	//			o.style.display = 'none';
	//			o.style.removeProperty('overflow');
	//			//more.className = more.className.replace(' moreclick','');
	//			clearInterval(o.slideFun);
	//		}	
	//	
	//	},speed);
};

function openfile(url) {
	mui.openWindow({
		id: url,
		url: url,
		preload: false //TODO 等show，hide事件，动画都完成后放开预加载
	});
}

function htmldown(html) {
	var dtask = null;
	if (dtask) {
		return;
	}
	var durl = "http://app.zz91.com/app/html/index.html";
	var options = {
		method: "GET"
	};
	dtask = plus.downloader.createDownload(durl, options);
	dtask.addEventListener("statechanged", function(task, status) {
		switch (task.state) {
			case 1: // 开始
				break;
			case 2: // 已连接到服务器
				break;
			case 3: // 已接收到数据
				break;
			case 4: // 下载完成
				//plus.io.FileEntry.moveTo("_www/","index.html",'','');
				break;
		}
	});
	//dtask.start();
	plus.io.resolveLocalFileSystemURL("_www/index1.html", function(entry) {
		// 可通过entry对象操作test.html文件 
		// remove this file
		// Get the parent DirectoryEntry
		// Request the metadata object for this entry
		entry.getMetadata(function(metadata) {
			alert(metadata.modificationTime)
			plus.console.log("Last Modified: " + metadata.modificationTime);
		}, function() {
			alert(e.message);
		});
		// remove this file
		//		entry.remove(function(entry) {
		//			plus.console.log("Remove succeeded");
		//			alert(2)
		//		}, function(e) {
		//			alert(e.message);
		//		});
		// Get the parent DirectoryEntry
		entry.getParent(function(entry) {
			plus.console.log("Parent Name: " + entry.name);
			alert(entry.name)
		}, function(e) {
			alert(e.message);
		});
		// create a FileWriter to write to the file
		entry.createWriter(function(writer) {
			// Write data to file.
			writer.write("Data ");
			alert(3)
		}, function(e) {
			alert(e.message);
		});

		//		var fileURL = entry.toRemoteURL();
		//		entry.copyTo(fileURL, "newfile.txt", function(entry) {
		//			alert(1);
		//			plus.console.log("New Path: " + entry.fullPath);
		//		}, function(e) {
		//			alert(e.message);
		//		});
		entry.file(function(file) {
			var fileReader = new plus.io.FileReader();
			alert("getFile:" + JSON.stringify(file));
			fileReader.readAsText(file, 'utf-8');
			fileReader.onloadend = function(evt) {
				alert("11" + evt);
				alert("evt.target" + evt.target);
				alert(evt.target.result);
			}
			alert(file.size + '--' + file.name);
		});
	}, function(e) {
		alert("Resolve file URL failed: " + e.message);
	});
}