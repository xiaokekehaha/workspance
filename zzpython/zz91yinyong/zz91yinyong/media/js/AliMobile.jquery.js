// JavaScript Document
(function(){AliMobile.mixWidget=function(a){var b=jQuery(a+" .option li");b.bind("click",function(d){b.removeClass("cur");var e=jQuery.inArray(this,b);var f=jQuery(this);f.addClass("cur");if(f.attr("isloaded")==1){jQuery(a+" .content").html(jQuery(a+" .J_TabContent_"+e).html())}else{jQuery(a+" .content").html('<div class="loading"><img src="/images/load.gif" /></div>');c(e,f)}});jQuery(a).append('<div class="none"></div>');jQuery.each(jQuery(a+" .option li[isloaded=1]"),function(){var d=jQuery.inArray(this,b);c(d,this)});function c(d,e){var f=jQuery(e);var g=f.attr("class");var h=f.attr("data-type")||"json";var i=f.attr("data-url")||f.attr("url");if(i!=""&&"json"==h){jQuery.getScript(i,function(){var j='<div class="J_TabContent_'+d+'">';if(json.channel&&json.channel.length>0){var k='<ul class="channel">';jQuery.each(json.channel,function(l,m){k+='<li><a class="img" href="'+m.url+'"><img alt="" src="'+m.pic+'"></a>['+m.title+']<a href="'+m.link_url+'">'+m.link_text+'</a></li>'});k+='</ul>';j+=k};if(json.shortcut&&json.shortcut.length>0){var k='<ul class="shortcut">';jQuery.each(json.shortcut,function(l,m){k+='<li><a href="'+m.url+'"><img alt="" src="'+m.pic+'"><span>'+m.title+'</span></a></li>'});k+='</ul>';j+=k};if(json.object&&json.object.length>0){var k='<div class="object">';jQuery.each(json.object,function(l,m){k+='<a href="'+m.url+'"><div class="img"><img src="'+m.pic+'" width="80" height="80" alt=""></div><div class="d"><h3>'+m.title+'</h3><p>'+m.desc+'</p></div></a>'});k+='</div>';j+=k};if(json.links&&json.links.length>0){var k='<ul class="links">';jQuery.each(json.links,function(l,m){k+='<li><span></span><a href="'+m.url+'">'+m.txt+'</a></li>'});k+='</ul>';j+=k};if(json.index&&json.index.length>0){var k='<div class="more">';jQuery.each(json.index,function(l,m){k+='<a href="'+m.url+'">'+m.cat+'</a>'});k+='</div>';j+=k};f.attr("isloaded",1);j+='</div>';jQuery(a+" .none").append(j);if("cur"==g){jQuery(a+" .content").html(jQuery(a+" .J_TabContent_"+d).html())}})};if(i!=""&&"html"==h){jQuery.ajax({url:i,type:"GET",dataType:"html",error:function(j){},success:function(j){f.attr("isloaded",1);var k='<div class="J_TabContent_'+d+'">'+j+'</div>';jQuery(a+" .none").append(k);if("cur"==g){jQuery(a+" .content").html(jQuery(a+" .J_TabContent_"+d).html())}}})}};return this};jQuery.fn.slideLayer=function(a){var b={direction:"X",slideEl:".slide",childEl:"li",wrapEl:".wrap",effect:"scroll",current:1,cycle:1,autoplay:0,delay:500,trigs:true,options:false};if(a){jQuery.extend(b,a)};return jQuery(this).each(function(c,d){var e=jQuery(d);var f=e.find(b.wrapEl);var g=e.find(b.slideEl);var h=g[0];var i=g.children(b.childEl);var j=Math.ceil(g.children(b.childEl).length);var k=b.current;var l=f.width();var m=f.height();i.css("width",l);g.css("width",j*l);if(b.trigs){n()};if(b.options){o()};if(j<2){return false};switch(b.effect){case"slide":p();break;case"scroll":q();break;case"both":p();q();break};function n(){var x='<ul>';for(var y=0;y<j;y++){x+='<li class="'+(y==0?'cur':'')+'">n</li>'};x+='</ul>';e.find(".pagination .trigs").append(x);e.find(".pagination .pg-num").html('\u7b2c<span style="color:#e10000">'+k+'</span>/'+j+'\u9875');e.find(".comment .img-text").html(e.find(" .slide>li img").eq(k-1).attr("img-text")||"")};function o(){var x=e.find(".option li");x.bind("click",function(y){var z=jQuery.inArray(this,x);g.css("left",-(l*z));k=z+1;r()})};function p(){e.find(".pagination .prev").click(function(x){if(b.cycle==1){u()}else{if(k!=1){u()}}});e.find(".pagination .next").click(function(x){if(b.cycle==1){v()}else{if(k!=j){v()}}})};function q(){g.dragwipe({wipeLeft:function(){v()},wipeRight:function(){u()}})};function r(){e.find(".option li").eq(k-1).addClass("cur").siblings().removeClass("cur");e.find(".pagination .trigs li").eq(k-1).addClass("cur").siblings().removeClass("cur");e.find(".pagination .pg-num span").html(k);e.find(".comment .img-text").html(e.find(".slide>li img").eq(k-1).attr("img-text")||"");var x=e.find(".slide>li img").eq(k-1);if(x.attr("data-src"))x.attr("src",x.attr("data-src"))};function s(){if(b.direction=="X"){g.animate({left:-(l*(k-2))},b.delay,function(){g.css("left",-(l*(k-1)));i.eq(j-1).css("left",0)})}else{g.animate({top:-(m*(k-2))},b.delay)};k==1?k=j:k--;r()};function t(){if(b.direction=="X"){g.animate({left:-(l*k)},b.delay,function(){g.css("left",-(l*(k-1)));i.eq(0).css("left",0)})}else{g.animate({top:-(m*k)},b.delay)};k==j?k=1:k++;r()};var u=function(){if(b.autoplay>1){w.process()};if(b.cycle==1){if(k!=1){s();return false}else{s();i.eq(j-1).css("left",-(l*j));i.eq(0).css("left",0);return false}}else{if(k!=1){s();return false}}};var v=function(){if(b.autoplay>1){w.process()};if(b.cycle==1){if(k!=j){t();return false}else{t();i.eq(0).css("left",l*j);i.find(b.childEl).css("left",0);return false}}else{if(k!=j){t();return false}}};var w={timeoutId:null,performProcessing:function(){v()},process:function(){clearInterval(w.timeoutId);w.timeoutId=setInterval(function(){w.performProcessing()},b.autoplay)},dispose:function(){clearInterval(w.timeoutId);return}};if(b.autoplay>1){w.process()}})};jQuery.fn.scrollLoading=function(a){var b={attr:"data-src"};var c=jQuery.extend({},b,a||{});c.cache=[];jQuery(this).each(function(){var e=this.nodeName.toLowerCase(),f=jQuery(this).attr(c["attr"]);if(!f){return};var g={obj:jQuery(this),tag:e,url:f};c.cache.push(g)});var d=function(){var e=jQuery(window).scrollTop(),f=e+jQuery(window).height();jQuery.each(c.cache,function(g,h){var i=h.obj,j=h.tag,k=h.url;if(i){post=i.position().top;if(post<10)post=i.offset().top;posb=post+i.height();if((post>e&&post<f)||(posb>e&&posb<f)){if(j==="img"){i.attr("src",k);i.removeClass("imgunloaded");i.addClass("imgloaded")}else if(j=="iframe"){i.attr("src",k)}else if(j=="span"){eval(k)}else{i.load(k)};h.obj=null}}});return false};d();jQuery(window).bind("scroll",d)};jQuery.fn.dragwipe=function(a){var b={direction:"X",wipeLeft:function(){},wipeRight:function(){},wipeUp:function(){},wipeDown:function(){},preventDefaultEvents:true};if(a){jQuery.extend(b,a)};var c=('ontouchstart'in document.documentElement);this.each(function(){var d=max=0;var e=jQuery(this);var f=e[0];f.onmousedown=f.ontouchstart=g;function g(i){var j,k,l;var m,n,l;var o=[e.position().left,e.position().top];j=h(i)[0];m=h(i)[1];f.ontouchmove=f.onmousemove=p;if(!c){return false};function p(r){k=h(r)[0];n=h(r)[1];var s=0;var t=0;if(b.direction=="X"){s=(k-j)+o[0]}else{t=(n-m)+o[1]};if(Math.abs(k-j)-Math.abs(n-m)>0){if(b.preventDefaultEvents||c){r.preventDefault()};if(b.direction=="X"){f.style.left=s+"px"}else{f.style.top=t+"px"};f.ontouchend=document.onmouseup=q}else{return}};function q(r){l=h(r)[0];yendPoint=h(r)[1];if(b.direction=="X"){var s=l-j;var t=yendPoint-m;if(s<-5){b.wipeLeft()}else if(s>5){b.wipeRight()}}else{return false};f.ontouchmove=f.ontouchend=f.onmousemove=document.onmouseup=null}};function h(i){var j=[0,0];j[0]=i.changedTouches?i.changedTouches[0].clientX:i.clientX;j[1]=i.changedTouches?i.changedTouches[0].clientY:i.clientY;return j}});return this}})();