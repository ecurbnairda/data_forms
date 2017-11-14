<!DOCTYPE html>
<html>
<head profile="http://www.w3.org/2002/12/cal/hcal http://www.w3.org/2006/03/hcard">
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"61e2f91637","applicationID":"349946","transactionName":"dAxbFxYNWlpXRBxEEFUPXABLEVVeV1JGWAAYBEcKAA==","queueTime":0,"applicationTime":430,"ttGuid":"","agentToken":null,"agent":""}</script>
<script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"UAIPV15ACwcJXVVU"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{c.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(12),c={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(c.console=!0,o.indexOf("dev")!==-1&&(c.dev=!0),o.indexOf("nr_dev")!==-1&&(c.nrDev=!0))}catch(s){}c.nrDev&&i.on("internal-error",function(t){r(t.stack)}),c.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),c.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(c,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,o){try{d?d-=1:i("err",[o||new UncaughtException(t,e,n)])}catch(c){try{i("ierr",[c,(new Date).getTime(),!0])}catch(s){}}return"function"==typeof f&&f.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t){i("err",[t,(new Date).getTime()])}var i=t("handle"),a=t(13),c=t("ee"),s=t("loader"),f=window.onerror,u=!1,d=0;s.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(l){"stack"in l&&(t(5),t(4),"addEventListener"in window&&t(3),s.xhrWrappable&&t(6),u=!0)}c.on("fn-start",function(t,e,n){u&&(d+=1)}),c.on("fn-err",function(t,e,n){u&&(this.thrown=!0,o(n))}),c.on("fn-end",function(){u&&!this.thrown&&d>0&&(d-=1)}),c.on("internal-error",function(t){i("ierr",[t,(new Date).getTime(),!0])})},{}],3:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){c.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),c=t(14)(a),s=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){if(t[1]){var n=t[1];if("function"==typeof n){var r=s(n,"nr@wrapped",function(){return c(n,"fn-",null,n.name||"anonymous")});this.wrapped=t[1]=r}else"function"==typeof n.handleEvent&&c.inPlace(n,["handleEvent"],"fn-")}}),a.on(d+"-start",function(t){var e=this.wrapped;e&&(t[1]=e)})},{}],4:[function(t,e,n){var r=t("ee").get("raf"),o=t(14)(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],5:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration="number"==typeof t[1]?t[1]:0,t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t(14)(i),c="setTimeout",s="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[c,"setImmediate"],c+d),a.inPlace(window,[s],s+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(s+u,r),i.on(c+u,o)},{}],6:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",c)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,v,"fn-",c)}function i(t){y.push(t),h&&(w=-w,x.data=w)}function a(){for(var t=0;t<y.length;t++)r([],y[t]);y.length&&(y=[])}function c(t,e){return e}function s(t,e){for(var n in t)e[n]=t[n];return e}t(3);var f=t("ee"),u=f.get("xhr"),d=t(14)(u),l=NREUM.o,p=l.XHR,h=l.MO,m="readystatechange",v=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],y=[];e.exports=u;var g=window.XMLHttpRequest=function(t){var e=new p(t);try{u.emit("new-xhr",[e],e),e.addEventListener(m,o,!1)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(s(p,g),g.prototype=p.prototype,d.inPlace(g.prototype,["open","send"],"-xhr-",c),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),h){var w=1,x=document.createTextNode(w);new h(a).observe(x,{characterData:!0})}else f.on("fn-end",function(t){t[0]&&t[0].type===m||a()})},{}],7:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<d;r++)t.removeEventListener(u[r],this.listener,!1);if(!e.aborted){if(n.duration=(new Date).getTime()-this.startTime,4===t.readyState){e.status=t.status;var i=o(t,this.lastSize);if(i&&(n.rxSize=i),this.sameOrigin){var a=t.getResponseHeader("X-NewRelic-App-Data");a&&(e.cat=a.split(", ").pop())}}else e.status=0;n.cbTime=this.cbTime,f.emit("xhr-done",[t],t),c("xhr",[e,n,this.startTime])}}}function o(t,e){var n=t.responseType;if("json"===n&&null!==e)return e;var r="arraybuffer"===n||"blob"===n||"json"===n?t.response:t.responseText;return h(r)}function i(t,e){var n=s(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}var a=t("loader");if(a.xhrWrappable){var c=t("handle"),s=t(8),f=t("ee"),u=["load","error","abort","timeout"],d=u.length,l=t("id"),p=t(11),h=t(10),m=window.XMLHttpRequest;a.features.xhr=!0,t(6),f.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,p&&(p>34||p<10)||window.opera||t.addEventListener("progress",function(t){e.lastSize=t.loaded},!1)}),f.on("open-xhr-start",function(t){this.params={method:t[0]},i(this,t[1]),this.metrics={}}),f.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),f.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=h(r);i&&(n.txSize=i)}this.startTime=(new Date).getTime(),this.listener=function(t){try{"abort"===t.type&&(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{f.emit("internal-error",[n])}catch(r){}}};for(var a=0;a<d;a++)e.addEventListener(u[a],this.listener,!1)}),f.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),f.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),f.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),f.on("addEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-added",[t[1],t[2]],e)}),f.on("removeEventListener-end",function(t,e){e instanceof m&&"load"===t[0]&&f.emit("xhr-load-removed",[t[1],t[2]],e)}),f.on("fn-start",function(t,e,n){e instanceof m&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=(new Date).getTime()))}),f.on("fn-end",function(t,e){this.xhrCbStart&&f.emit("xhr-cb-time",[(new Date).getTime()-this.xhrCbStart,this.onload,e],e)})}},{}],8:[function(t,e,n){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");!r.port&&o[1]&&(r.port=o[1].split("/")[0].split("@").pop().split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,r.protocol=o[0],"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname);var i=!e.protocol||":"===e.protocol||e.protocol===n.protocol,a=e.hostname===document.domain&&e.port===n.port;return r.sameOrigin=i&&(!e.hostname||a),r}},{}],9:[function(t,e,n){function r(){}function o(t,e,n){return function(){return i(t,[(new Date).getTime()].concat(c(arguments)),e?null:this,n),e?void 0:this}}var i=t("handle"),a=t(12),c=t(13),s=t("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var u=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit"],d="api-",l=d+"ixn-";a(u,function(t,e){f[e]=o(d+e,!0,"api")}),f.addPageAction=o(d+"addPageAction",!0),e.exports=newrelic,f.interaction=function(){return(new r).get()};var p=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(l+"tracer",[Date.now(),t,n],r),function(){if(s.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return e.apply(this,arguments)}finally{s.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){p[e]=o(l+e)}),newrelic.noticeError=function(t){"string"==typeof t&&(t=new Error(t)),i("err",[t,(new Date).getTime()])}},{}],10:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],11:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],12:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],13:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],14:[function(t,e,n){function r(t){return!(t&&"function"==typeof t&&t.apply&&!t[a])}var o=t("ee"),i=t(13),a="nr@original",c=Object.prototype.hasOwnProperty,s=!1;e.exports=function(t){function e(t,e,n,o){function nrWrapper(){var r,a,c,s;try{a=this,r=i(arguments),c="function"==typeof n?n(r,a):n||{}}catch(u){d([u,"",[r,a,o],c])}f(e+"start",[r,a,o],c);try{return s=t.apply(a,r)}catch(l){throw f(e+"err",[r,a,l],c),l}finally{f(e+"end",[r,a,s],c)}}return r(t)?t:(e||(e=""),nrWrapper[a]=t,u(t,nrWrapper),nrWrapper)}function n(t,n,o,i){o||(o="");var a,c,s,f="-"===o.charAt(0);for(s=0;s<n.length;s++)c=n[s],a=t[c],r(a)||(t[c]=e(a,f?c+o:o,i,c))}function f(e,n,r){if(!s){s=!0;try{t.emit(e,n,r)}catch(o){d([o,e,n,r])}s=!1}}function u(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){d([r])}for(var o in t)c.call(t,o)&&(e[o]=t[o]);return e}function d(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=o),e.inPlace=n,e.flag=a,e}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?c(t,a,i):i()}function n(n,r,o){t&&t(n,r,o);for(var i=e(o),a=l(n),c=a.length,s=0;s<c;s++)a[s].apply(i,r);var u=f[v[n]];return u&&u.push([y,n,r,i]),i}function d(t,e){m[t]=l(t).concat(e)}function l(t){return m[t]||[]}function p(t){return u[t]=u[t]||o(n)}function h(t,e){s(t,function(t,n){e=e||"feature",v[n]=e,e in f||(f[e]=[])})}var m={},v={},y={on:d,emit:n,get:p,listeners:l,context:e,buffer:h};return y}function i(){return new r}var a="nr@context",c=t("gos"),s=t(12),f={},u={},d=e.exports=o();d.backlog=f},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!w++){var t=g.info=NREUM.info,e=u.getElementsByTagName("script")[0];if(t&&t.licenseKey&&t.applicationID&&e){s(v,function(e,n){t[e]||(t[e]=n)});var n="https"===m.split(":")[0]||t.sslForHttp;g.proto=n?"https://":"http://",c("mark",["onload",a()],null,"api");var r=u.createElement("script");r.src=g.proto+t.agent,e.parentNode.insertBefore(r,e)}}}function o(){"complete"===u.readyState&&i()}function i(){c("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var c=t("handle"),s=t(12),f=window,u=f.document,d="addEventListener",l="attachEvent",p=f.XMLHttpRequest,h=p&&p.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:p,REQ:f.Request,EV:f.Event,PR:f.Promise,MO:f.MutationObserver},t(9);var m=""+location,v={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-974.min.js"},y=p&&h&&h[d]&&!/CriOS/.test(navigator.userAgent),g=e.exports={offset:a(),origin:m,features:{},xhrWrappable:y};u[d]?(u[d]("DOMContentLoaded",i,!1),f[d]("load",r,!1)):(u[l]("onreadystatechange",o),f[l]("onload",r)),c("mark",["firstbyte",a()],null,"api");var w=0},{}]},{},["loader",2,7]);</script>
<!-- L:S content/theme/html_system_head  (0) --> <!-- load web fonts -->
<script>
  (function(d) {
    var config = {
      kitId: 'gap0qyx',
      scriptTimeout: 3000,
      async: true
    },
    h=d.documentElement,t=setTimeout(function(){h.className=h.className.replace(/\bwf-loading\b/g,"")+" wf-inactive";},config.scriptTimeout),tk=d.createElement("script"),f=false,s=d.getElementsByTagName("script")[0],a;h.className+=" wf-loading";tk.src='https://fonts.oreillystatic.com/'+config.kitId+'.js';tk.async=true;tk.onload=tk.onreadystatechange=function(){a=this.readyState;if(f||a&&a!="complete"&&a!="loaded")return;f=true;clearTimeout(t);try{Typekit.load(config)}catch(e){}};s.parentNode.insertBefore(tk,s)
  })(document);
</script>
<style>


body, p, ol, ul, td, h1, h2, h3, h4 { 
  font-family: Arial, Verdana, Helvetica, sans-serif;
}
.wf-inactive body, .wf-inactive p, .wf-inactive ol, .wf-inactive ul, .wf-inactive td, .wf-inactive h1, .wf-inactive h2, .wf-inactive h3, .wf-inactive h4 { 
  font-family: Arial, Verdana, Helvetica, sans-serif;
}
.wf-loading body, .wf-loading p, .wf-loading ol, .wf-loading ul, .wf-loading td, .wf-loading h1, .wf-loading h2, .wf-loading h3, .wf-loading h4 { 
  font-family: Arial, Verdana, Helvetica, sans-serif; 
}
.wf-active body, .wf-active p, .wf-active ol, .wf-active ul, .wf-active td, .wf-active h1, .wf-active h2, .wf-active h3, .wf-active h4 { 
  font-family: 'guardian-text-oreilly', Arial, Verdana, Helvetica, sans-serif;
}

.typewriter {
  font-family: Courier New;
  color: rgba(0, 0, 0, 0); 
}
.wf-inactive .typewriter {
  font-family: Courier New;
}
.wf-loading .typewriter {
  font-family: Courier New;
  visibility: hidden;
}
.wf-active .typewriter {
  font-family: 'oreilly-urw-typewriter-narro', Courier New;
}

</style>
<!-- controller_js -->
<script src="//cdn.oreillystatic.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
<script src="/javascripts/application.js?1473866115" type="text/javascript"></script>
<script src="//cdn.oreillystatic.com/ajax/libs/jqueryui/1.8.23/jquery-ui.min.js" type="text/javascript"></script>
<script src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/jquery_star_rating_pack.js?03" type="text/javascript"></script>
<script src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/jquery.form.min.js" type="text/javascript"></script>
<script src="/javascripts/coinbase-registration.js?1473866115" type="text/javascript"></script>
<!-- extra_external_javascript -->

<!-- extra_styles -->
<link href="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/jquery.rating-3.14.css" media="screen" rel="stylesheet" type="text/css" /><link href="http://conferences.oreilly.com/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/slot_css/386?date=2016-09-26&amp;public=true&amp;review=false&amp;" media="screen" rel="stylesheet" type="text/css" />
<!-- extra_javascript -->
<script type="text/javascript">
<!--

    var we_are_dragging = false;

    function getElementWidth(objectId) {
        x = document.getElementById(objectId);
        return x.offsetWidth;
    }

    function getElementHeight(objectId) {
        x = document.getElementById(objectId);
        return x.offsetHeight;
    }

    function getAbsoluteLeft(objectId) {
        // Get an object left position from the upper left viewport corner
        o = document.getElementById(objectId);
        oLeft = o.offsetLeft;            // Get left position from the parent object
        while(o.offsetParent!=null) {   // Parse the parent hierarchy up to the document element
            oParent = o.offsetParent;    // Get parent object reference
            oLeft += oParent.offsetLeft; // Add parent left position
            o = oParent;
        }
        return oLeft;
    }

    function getAbsoluteTop(objectId) {
        // Get an object top position from the upper left viewport corner
        o = document.getElementById(objectId);
        oTop = o.offsetTop;            // Get top position from the parent object
        while(o.offsetParent!=null) { // Parse the parent hierarchy up to the document element
            oParent = o.offsetParent;  // Get parent object reference
            oTop += oParent.offsetTop; // Add parent top position
            o = oParent;
        }
        return oTop;
    }

    function mouse_coords(e) {
      var posx = 0;
      var posy = 0;
      if (!e) var e = window.event;
      if (e.pageX || e.pageY)   {
        posx = e.pageX;
        posy = e.pageY;
      }
      else if (e.clientX || e.clientY)  {
        posx = e.clientX + document.body.scrollLeft
            + document.documentElement.scrollLeft;
        posy = e.clientY + document.body.scrollTop
            + document.documentElement.scrollTop;
      }
      return({x: posx, y: posy});
    }

    function update(e) {
      var maus = mouse_coords(e);
      px = maus.x + 6;
      py = maus.y + 6;
      $('#en_gridpop').css({left: px+"px", top: py+"px"});
    }

    function create_popup(e, linkid) {
      var pid = "#"+linkid+"_p";
      $("body").append("<div id='en_gridpop'></div>");
      $("#en_gridpop").append($(pid).children().clone());
      update(e);
      $('#en_gridpop').show();
      $("#"+linkid).addClass("slot_active");
    }

      $(document).ready(function() {
        $("div.slot").hover(function(e){
          if (!we_are_dragging) {
            if ($("#en_gridpop").length==0) {
              create_popup(e, this.id);
              $('body').bind('mousemove', update);
            }
          }
        },function(){
          var pid = "#"+$(this).attr("id")+"_p"
          $('body').unbind('mousemove', update);
          $('#en_gridpop').remove();
          $(this).removeClass("slot_active");
        });

        $("div.slot_room_title").click(function(e){
          var i = $(this).attr("id");
          i = i.substr(i.lastIndexOf('_'));
          $('#room_tools'+i).slideToggle("fast");
        }).hover(function() {
          $(this).addClass('slot_room_title_hover');
        },function(){
          $(this).removeClass('slot_room_title_hover');
        });
      });

//-->
</script>
<!-- theme_external_javascript -->

<style>
  .en_eval_link { vertical-align:top; }
  </style>
<!-- L:E content/theme/html_system_head  (0) -->
<!-- L:S content/theme/html_head  (0) -->
<title>
Schedule: O'Reilly Artificial Intelligence Conference, September 26 -
27, 2016, New York
</title>
<meta name="google-site-verification" content="uidfKEBgRM3o0f3aRFrGfEaDFmNW42xVK6BMMo6bL6Y" />

<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- content/head_extra -->
<style>
*, *:after, *:before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}

.grid {
  margin-right:-20px;
}
.grid:after {
  content: "";
  display: table;
  clear: both;
}

[class*='col-'] {
  float: left;
  padding-right: 20px;
}
[class*='col-']:last-of-type {
  float: left;
}

.col-1-2 { width: 50%; }
.col-1-3 { width: 33.33%; }
.col-2-3 { width: 66.66%; }
.col-1-4 { width: 25%; }
.col-3-4 { width: 75%; }
.col-1-5 { width: 20%; }
.col-2-5 { width: 40%; }
.col-3-5 { width: 60%; }
.col-4-5 { width: 80%; }
.col-1-6 { width: 16.66%; }
.col-5-6 { width: 83.33%; }
.col-1-8 { width: 12.5%; }
.col-3-8 { width: 37.5%; }
.col-5-8 { width: 62.5%; }
.col-7-8 { width: 87.5%; }

@media screen and (max-width:680px) {
  .mobile-stack [class*='col-'] { width: 100% !important; }
}

@media screen and (max-width:400px) {
  .mobile-stack-xs [class*='col-'] { width: 100% !important; }
}
</style>
<style>
/* global styles */
html { font-size: 62.5%; color: #222; }
h1 { font-size: 27px; font-size: 2.7rem; }
h2 { font-size: 23px; font-size: 2.3rem; }
h3 { font-size: 19px; font-size: 1.9rem; }
h1, h2, h3 { font-weight: normal; }
h4, p, li { font-size: 15px; font-size: 1.5rem; }
li { line-height: 23px; line-height: 2.3rem; }
a { text-decoration: none; }
a:hover { text-decoration: underline; }
#en_content, #en_main { width: 100%; margin: 0px; padding: 0px; }
#en_main_parts { width: 100%; }
.left { float: left; }
.right { float: right; }
/* clearfix */
.en_clearfix:after { content: "."; display: block; height: 0; clear: both; visibility: hidden; }

/* Rails error styles */
.fieldWithErrors { border: 2px solid red; display: table; }
div.en_grade_buttons .fieldWithErrors { border: 0; display: none; }
div.ErrorExplanation { width: 400px; width: 40rem; border: 2px solid red; padding: 7px 12px 7px 7px; padding: 0.7rem 1.2rem 0.7rem 0.7rem; margin-bottom: 20px; margin-bottom: 2rem; background-color: #f0f0f0; }
div.ErrorExplanation h2 { text-align: left; font-weight: bold; padding: 5px 5px 5px 15px; padding: 0.5rem 0.5rem 0.5rem 1.5rem; font-size: 12px; font-size: 1.2rem; margin: -7px 0 -7px -7px; margin: -0.7rem 0 -0.7rem -0.7rem; background-color: #c00; color: #fff; }
div.errorExplanation p { color: #333; margin-bottom: 0; padding: 5px; padding: 0.5rem; }
div.errorExplanation ul { margin-bottom: 15px; margin-bottom: 1.5rem; }
div.errorExplanation ul li { line-height: 27px; line-height: 2.7rem; list-style: square; margin-left: 2rem; }
/* flash and error reporting */
div.en_additional_notice { background-color: #efefef; border: 1px solid #f7f7f7; padding: 5px; padding: 0.5rem; margin-bottom: 15px; margin-bottom: 1.5rem; }
div.en_notice { background-color: #FFFFCC; border: 1px dotted #FFCC33; color: #ddaa33; padding: 5px; padding: 0.5rem; margin-bottom: 10px; margin-bottom: 1rem; }
div.en_error { background-color: #FFCCBF; border: 1px dotted #FF3300; color: #FF3300; padding: 5px; padding: 0.5rem; margin-bottom: 10px; margin-bottom: 1rem; }
div.en_liquid_error { border: 2px solid #484; background: #ffe; padding: 0 10px 10px 10px; padding: 0 1rem 1rem 1rem; font-family: sans-serif; }
div.en_liquid_error p, div.en_liquid_error h3 { font-family: sans-serif; }

/* For Google Remarketing Tag */
.remarketing { position:absolute; top:-9999px; left:-9999px; }
</style>
<style>
.en_notice { display: none; }
body { background-color: #FFF; color: rgb(0, 0, 0); margin: 0px; -webkit-text-size-adjust: none;  -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }

/* Clearfix */
.clearfix:before, .clearfix:after { content: " "; display: table; }
.clearfix:after { clear: both; }
.clearfix { *zoom: 1; }

  #sitenav { width:100%; background:rgba(255,255,255,.2); font-size:1.5rem; line-height:2rem; }
  #sitenav nav { padding-top:0; }
  #sitenav nav #pull { display:none; position:relative; float:right; width:100%; height:50px; padding:0; background:none; opacity:.8; }
  #sitenav nav #pull:hover {  opacity:1; }
  #sitenav nav #pull:after { content:"MENU"; display:block; float:right; line-height:50px; line-height:5rem; text-align:right; }
  #sitenav nav #pull:before { content:""; display:block; float:right; width:70px; height:50px; background:transparent url('//cdn.oreillystatic.com/en/assets/1/event/132/test_menu_icon.png') center center no-repeat; }
  #sitenav nav ul { list-style:none; text-transform:uppercase; padding:0; margin:0 -12px 0 -12px; overflow:hidden; height:auto !important; }
  #sitenav nav li { display:block; float:left; margin:0; }
  #sitenav nav li:first-child { margin-left:0; }
  #sitenav nav li a { display:block; color:#fff; text-decoration:none; padding:15px 12px; font-size:inherit !important; border:0; }
  #sitenav nav li a:hover { text-decoration:none; background:rgba(0,0,0,.5); }
  #sitenav nav li a.highlight { font-weight:bold; background:rgba(211,0,45,.5); }
  #sitenav nav li a.highlight:hover { background:rgba(211,0,45,.8); }



#reg_button { border-bottom: 1px solid eee; background-color: #d3002d; clear: left; width: 100%; }
#reg_button a { text-align: center;  font-size: 20px; font-size: 2rem; text-indent: 0; border-right: none; }
#reg_button a span { display: inline-block; vertical-align: middle; padding-bottom: 2px; }

.row { width: 100%; padding: 0px 0px 20px; }
#en_main_parts { width: 100%; }
#nav_overlay { position: absolute; z-index: 80; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); background: none\9; }
nav > a:first-child { display: none; }

/* accordion styles */
.accordion h2, .accordion h3, .accordion h4 { cursor: pointer; }
.closed::before { content: "+"; cursor: pointer; display: inline-block; padding-right: 5px; }
.open::before { content: "-"; cursor: pointer; display: inline-block; padding-right: 5px; }

#en_header { margin-left: 0px; padding-left: 0px; background-color: #000; position: relative; z-index: 100; }
.branding_bar { background-color: #d3002d; width: 100%; position: relative; z-index: 2; padding: 0; font-size:1.2rem; line-height:1.2rem; }
.content_row { max-width: 910px; width: 100%; margin: 0px auto; padding: 0 20px; }
#logo { padding: 8px 0; max-width: 129px; }

#franchise_links { padding-top: 10px; padding-bottom: 10px; font-weight: bold; font-size: 13px; font-size: 1.3rem; line-height: 18px; line-height: 1.8rem; color: #000; text-transform: uppercase; box-shadow: none; position: relative; text-align: right; }
#franchise_links a { color: #000; }
#franchise_links .current { color: #fff; }
#inside_header.row { padding-top: 20px;border-bottom: 0;  }
.event_logo { display: inline-block; vertical-align: bottom; width: 40%; max-width:33rem; }
.tagline_date_location { font-size:18px; font-size:1.8rem; line-height:22px; line-height:2.2rem; color: #fff; display: inline-block; vertical-align: top;  text-transform: uppercase; margin-top: -4px; margin-left:45px; letter-spacing: 0.5px;  }

a {text-decoration: none; color: #007eff; }
a:hover {text-decoration: underline; }
.hide { display: none; }

.btn-blue {display:block; text-decoration:none;  font-size: 2rem; line-height:2.2rem; color:#fff; padding:0.5rem 0 0.9rem 0; text-align:center; text-shadow: 0px 0px 2px #37609f; -webkit-border-radius: 10px; -moz-border-radius: 10px; border-radius: 10px; background: #284a70;  background: -moz-linear-gradient(top, #3e679d 0%, #284a70 100%); /* FF3.6+ */ background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#3e679d), color-stop(100%,#284a70)); /* Chrome,Safari4+ */ background: -webkit-linear-gradient(top, #3e679d 0%,#284a70 100%); /* Chrome10+,Safari5.1+ */ background: -o-linear-gradient(top, #3e679d 0%,#284a70 100%); /* Opera 11.10+ */ background: -ms-linear-gradient(top, #3e679d 0%,#284a70 100%); /* IE10+ */ background: linear-gradient(to bottom, #3e679d 0%,#284a70 100%); /* W3C */ -webkit-box-shadow:  0px 1px 2px 0px rgba(0, 0, 0, .4); box-shadow:  0px 1px 2px 0px rgba(0, 0, 0, .4); }
a.btn-blue:hover {text-decoration:none;}
.btn-blue.cfp { max-width: 280px; }

div.photo-cluster {margin: 2rem 0; width: 100%; float: left; clear: both;}
div.photo-cluster img {width: 32%; float: left; margin-right: 1%; text-align: center;}

.iframe { position: relative; padding-bottom: 56.25%; height: 0; }
.iframe iframe { position: absolute; }

.sold_out {   background-color: #d3002d; padding: 2px 4px 2px; font-size: 11.05px; font-weight: bold; color: #FFF; text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25); -webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px; width: 65px; float: left; margin: 2px 2px 2px; }


#en_main { width: 100%; margin: 0 auto; padding: 0 20px; max-width: 910px; }
.en_article_body { padding-bottom: 20px; }



#en_proceedings { max-width: 910px; width: 100%; margin: 0 auto 20px; margin: 0 auto 2rem; padding: 0 20px 0 0; }
h1, h2, h3 { color: #d3002d; }
h1 { margin-bottom: 20px; margin-bottom: 2rem; line-height: 30px; line-height: 3rem; }
h3 { margin-bottom: 10px; margin-bottom: 1rem; }
h4 { margin-top: 10px; margin-top: 1rem; }

h2 { margin: 15px 0; margin: 1.5rem 0; }
#en_body p, #en_body li { line-height: 22px; line-height: 2.2rem; }
.cta { margin: 0 0 1rem 1rem; padding: 1rem 2rem; min-width: 26rem; }
.cta_date { font-weight: normal; font-size: 1.5rem; }






/* for sponsor, exhibitor, and speaker banners */




@-ms-viewport {
  width: device-width;
}



  @media screen and (max-width:850px) {
    #sitenav .content_row { padding:0; }
    #sitenav nav { position:relative; }
    #sitenav nav #pull { display:block; }
    #sitenav nav ul { width:100%; display:none; position:absolute; top:100%; margin:0; background:rgba(20,20,20,.95); border-top:1px solid #8c8c8c; /*border-bottom:1px solid #8c8c8c;*/ }
    #sitenav nav ul li { width:50%; float:left; border-bottom:1px solid #8c8c8c; }
    #sitenav nav ul li:nth-child(odd) { border-right:1px solid #8c8c8c; }
    /*#sitenav nav ul li:last-child { border-bottom:0; }*/
    #sitenav nav ul a { text-align:left; text-indent:25px; line-height:20px; line-height:2rem; }
    #sitenav nav ul a.last { border-right:0; }
    #nav_overlay { background:rgba(0,0,0,.6); }
    nav a#pull { color: #fff;  text-align: left; width: 100%; text-indent: 25px; text-indent: 2.5rem; line-height: 40px; line-height: 4rem; }
  }

@media only screen and (max-width: 820px) {
   #widgets_row.row #stay_informed #photos { display: none; }
}


@media only screen and (max-width: 780px) {
    .tagline_date_location { display: block; margin-left: 0; margin-top: 10px; }  
    .event_logo { width: 100%; max-width: 33rem; } 
}

@media only screen and (max-width: 774px) {
    .cta_row.row { background: #fff; border-bottom: none; padding: 10px 0; }
    #small-reg-button { width: 50%; margin: 0 auto; }
}

@media only screen and (max-width: 760px) {
   .mobile-hide { display: none; }
   div.bio img, .right { float: none; }
   .cta { margin-top: 20px; }
}

@media only screen and (max-width: 680px) {
  #contacts>div { padding: 10px 0; }
  #en_footer .footercol ul li:first-child { font-size: 1.6rem; line-height: 2rem; }
  #en_footer ul li a {font-size: 1.6rem; line-height: 2rem; }
  ul#social li img { margin-bottom: 10px }
}

@media only screen and (max-width: 580px) {
  #franchise_links { display: none; }
}

@media only screen and (max-width: 400px) {
   #date_location_mobile { line-height: 18px; line-height: 1.8rem; }
}





</style>
              <style>

/\* grid styles \*/ \#en\_main h3 { color: \#222; display: block;
vertical-align: bottom; font-weight: bold; margin-bottom: 6px;
font-size: 15px; } \#en\_grid\_container \#slot\_grid,
\#en\_grid\_container \#slot\_grid2 { -webkit-box-sizing: content-box;
-moz-box-sizing: content-box; box-sizing: content-box; background:
-webkit-repeating-linear-gradient(135deg, \#888, \#888 6px, \#828282
6px, \#828282 12px); background: repeating-linear-gradient(135deg,
\#888, \#888 6px, \#828282 6px, \#828282 12px); } div.en\_popup\_content
{font-size: 11px; font-size: 1.1rem; } div.en\_popup\_name {font-weight:
bold; } div.en\_popup\_speaker {font-style: italic; } div.slot\_detail {
font-size: 1.1rem; line-height: 1.1rem; line-height: 1.2rem; }
div.en\_session\_psched {float: right; clear: right; }
div.slot\_room\_title {text-align: center; margin: 0; padding: 0;
border: 0; color: white; background: black; } div.slot\_room\_title div
{padding: 4px; padding: 0.4rem; font-size: 11px; font-size: 1.1rem;
line-height: 13px; line-height: 1.3rem; } div.slot\_room\_tools {margin:
0; padding: 0; color: white; background: black; display: none; }
div.slot\_room\_tools div {padding: 2px; padding: 0.2rem; background:
\#444; font-size: 11px; font-size: 1.1rem; } div.slot\_room\_tools
div.en\_field {font-size: 10px; font-size: 1rem; font-weight: normal; }
div.slot\_room\_tools input, div.slot\_room\_tools select {font-size:
10px; font-size: 1rem; }

/\*\* New Grid Date Styles \*\*/ \#en\_grid\_dates {margin-top: 5px;
margin-top: 0.5rem; margin-bottom: 1rem; } \#en\_grid\_dates ul {
list-style: none; padding-left: 0; margin-left: 0; margin-bottom:0; }
\#en\_grid\_dates ul li { display: inline-block; margin: -.5rem 1rem
.2rem 0; border: none; background-color: \#444; color: \#FFF;
-webkit-border-radius: 4px; -moz-border-radius: 4px; border-radius: 4px;
font-size: 20px; font-size: 2rem; padding: 3px 10px 5px 10px; width:
16.5rem; line-height: 24px; line-height: 2.4rem; height: 52px; height:
5.2rem; vertical-align: top; } \#en\_grid\_dates li:hover {
background-color: \#333; } \#en\_grid\_dates ul li:first-child
{margin-left: 0; } \#en\_grid\_dates ul li.active {background-color:
black; } \#en\_grid\_dates ul li.active a {color: white; }
\#en\_grid\_dates a {text-decoration: none; color: black;
padding-bottom: 2px; padding-bottom: 0.2rem; color: \#fff; }
.session\_types { font-size: 1.5rem !important; line-height: 1.7rem
!important; }

/\*\* Grid-to-list buttons \*\*/ \#list\_grid { display: inline-block;
font-size: 13px; font-size: 1.3rem; margin-bottom: 11px; } .list,
.sched\_grid { margin-bottom: 3px; margin-right: 20px; } .list:before,
.sched\_grid:before { content: ""; display: inline-block; width: 24px;
height: 15px; margin-bottom: -3px; margin-right: 4px; }
.list.inactive:before { background-position: 0 0; } .list.active:before
{ background-position: 0 -20px; } .sched\_grid.inactive:before {
background-position: -30px 0; } .sched\_grid.active:before
{background-position: -30px -20px; } \#en\_grid\_dates \#list\_grid a {
color:\#999; }

/\*\* New Track Key Styles \*\*/ \#grid\_track\_key { margin:0 0 1rem;
width:100%; font-size: 0; } \#grid\_track\_key &gt; div { font-size: 0;
} \#grid\_track\_key h3 { font-weight:normal; font-size:1.6rem;
line-height:2rem; margin:0 0 0.4rem; color:\#444; } \#grid\_track\_key
li { display: inline-block; list-style: none; } \#grid\_track\_key
li:hover a { border:0; } \#grid\_track\_key li a { display:inline-block;
margin: 0 0.2rem 0.2rem 0; padding: 0.5rem 1.5rem 0.8rem 1.5rem;
border-radius: 2px; background-color: \#444; color: \#fff; font-size:
13px; line-height: 13px; text-decoration: none; } \#grid\_track\_key li
a:hover { background-color: \#333; text-decoration: none; }
\#grid\_track\_key li a:after { content:""; display:inline-block;
width:8px; height:8px; border-right:1px solid rgba(255,255,255,.8);
border-bottom:1px solid rgba(255,255,255,.8);
-webkit-transform:rotate(-45deg); transform:rotate(-45deg);
margin-top:-2px; }

/\*\* New Topic Key Styles \*\*/ \#en\_grid\_topic\_key { margin:0 0
2rem; width:100%; font-size: 0; } \#en\_grid\_topic\_key &gt; div {
font-size: 0; } \#en\_grid\_topic\_key h3 { font-weight:normal;
font-size:1.6rem; line-height:2rem; margin:0 0 0.4rem; color:\#444; }
\#en\_grid\_topic\_key li { display: inline-block; list-style:none;
background:transparent !important; } \#en\_grid\_topic\_key li:hover a {
border:0; } \#en\_grid\_topic\_key li a { display: inline-block; margin:
0 0.2rem 0.2rem 0; padding: 0.5rem 1.5rem 0.8rem 1.5rem; border-radius:
2px; background-color: \#444; color: \#fff; font-size: 13px;
line-height: 13px; text-decoration: none; cursor: pointer; }
\#en\_grid\_topic\_key li:hover { background-color: \#d0e2f8; }
\#en\_grid\_topic\_key .featured { background: \#dedede; color:\#000; }
\#en\_grid\_topic\_key li.filter\_color\_topic a { background-color:
\#d0e2f8 !important; color:\#000; } \#en\_grid\_topic\_key
li.filter\_color\_topic\_hover a { background-color: \#d0e2f8
!important; color:\#000; } \#en\_grid\_topic\_key li a:hover {
background-color: \#333; text-decoration: none; }

/\*\* New Tag Key Styles \*\*/ \#tag\_key { margin-bottom: 1.5rem; }
\#tag\_key ul { margin: 0; padding: 0; } \#tag\_key ul li { display:
inline-block; list-style: none; background: transparent !important; }
\#tag\_key ul li a { display: inline-block; margin: 0 0.2rem 0.2rem 0;
padding: 0.5rem 1.5rem 0.8rem 1.5rem; border-radius: 2px;
background-color: \#444; color: \#fff; font-size: 13px; line-height:
13px; text-decoration: none; cursor: pointer; } \#tag\_key ul li a:hover
{ background-color: \#333; text-decoration: none; }

/\*\* New ical Styles \*\*/ .ical-offerings { font-size: 1.4rem;
font-size: 14px; color: \#555; text-align: center; width: 25rem; }
.ical-offerings a {color: \#555; text-decoration: underline; }

en\_grid\_container {width: 100%; }
===================================

en\_grid\_topic\_key ul { padding-left: 0; }
============================================

en\_gridpop {background: \#fff; border: 1px solid black; position: absolute; width: 200px; width: 20rem; padding: 2px; padding: 0.2rem; z-index: 100; }
=======================================================================================================================================================

/\*\* Print Styles \*\*/ @media print { \#sitenav,
.tagline\_date\_location, .ical-offerings, .right, p:first-child, p.pad,
\#list\_grid, \#en\_grid\_dates h3, \#sponsored\_breaks,
\#en\_grid\_dates li:last-child, \#sponsors\_contacts, footer,
\#copyright, \#en\_main \#en\_grid\_topic\_key h3, .en\_session\_psched,
h1, \#en\_footerwrap, \#en\_grid\_dates, \#en\_grid\_topic\_key,
\#franchise\_links, \#tag\_key, \#newsletter\_widget,
\#grid\_track\_key, \#strata\_links, \#grid\_track\_key div,
\#en\_grid\_topic\_key div { display:none; } }
</style>
              <style>
                  .list:before, .sched_grid:before { background: transparent url('//cdn.oreillystatic.com/en/assets/1/event/119/stratany2014_schedule_view_sprite.png'); }
                  #slot_grid { margin-bottom: 45px; }
                  #en_grid_dates  #list_grid a.active { color: #d3002d; }
                  #en_grid_dates ul li.active { background-color: #d3002d; }
                  #en_grid_dates ul li { height: 51px; height: 5.1rem; }
                  div#slot20894 { background-color: #f4f4f4; }
                  div#slot20916 { background-color: #f4f4f4; }
                  div#slot52073, div#slot52082 { background-color: #b6c2aa !important; }
              </style>





        <link href="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/2015_global_loggedin_css_v2.css"  media="screen" rel="Stylesheet" type="text/css" />
        

<style>
#reasons_row.row { background: #fff; padding:1.6em 0 3.1em 0;}
#reasons_row.row p, #reasons_row.row li, #nonprofit_row.row p { padding: 0; font-size: 17px; font-size: 1.7rem; line-height: 25px; line-height: 2.5rem; }
#reasons_row.row h1, #reasons_row.row h2, #nonprofit_row.row h2 { padding: 0; color: #d3002d; }
#reasons_row.row h2 {font-size:27px; font-size:2.7rem; }
#reasons_row.row h3 { margin-bottom: 0; }
#reasons_row.row ul li  { list-style: none; word-wrap: break-word; position: relative; }
#reasons_row.row ul li:before { content: ""; position: absolute; left: -13px;  top: 0.9rem; background-color: #d3002d; display: inline-block; width: 6px; height: 6px; border-radius: 50%; margin-bottom: 2px; }
#reasons_row.row ol li { margin: 0 0 15px 0; margin: 0 0 15px 0; padding: 0 0 0 40px; }
#rightcol { float: right; width: 300px; width: 30rem; padding: 0 0 0 12px; padding: 0 0 0 1.2rem; margin-top: -12px; margin-top: -1.2rem; }
#reasons_row.row .quote { color: #d3002d; font-size: 20px; font-size: 2rem; line-height: 25px; line-height: 2.5rem; background: white url('//cdn.oreillystatic.com/en/assets/1/eventprovider/1/background_quote.gif') left top no-repeat; margin: 0 0 20px 0; padding-top: 10px; padding-left: 10px; }
#reasons_row.row .attribution { color: #000; font-size: 14px; font-size: 1.4rem; line-height: 17px; line-height: 1.7rem; margin-top: 0; display: block; }

#nonprofit_row.row { background: #eee; padding: 40px 0; color: #222; }

#newsletter_widget, #email_signup { background: #222; width: 100%; min-height: 100px; margin: 0; overflow: auto; color: #fff; text-align: center; }
#newsletter_widget .content_row, #email_signup .content_row { padding: 40px 20px 40px 20px; }
#newsletter_widget h2, #email_signup h2 { color: #fff; font-size: 30px; font-size: 3rem; margin: 0; padding: 0; }
#newsletter_widget h2 { margin-bottom: 10px; line-height: 35px; line-height: 3.5rem; }
#newsletter_widget p, #email_signup p { font-size: 22px; font-size: 2.2rem;  margin: 0 auto; padding: 0 0 10px 0; }




#sponsors_row.row {background: #fff; border-bottom: none; padding: 0; }
#sponsors_row h2 { text-align: center; font-size: 34px; font-size: 3.4rem; margin: 0; padding: 0 0 20px 0;}
#sponsor_container {background: #fff;  margin: auto; padding-bottom: 40px; }
#sponsors_contacts.row div.big_sponsor_level {background: #b0b0b0; background: -moz-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -webkit-gradient(linear,left top,right top,color-stop(0%,#fff),color-stop(50%,#b0b0b0),color-stop(100%,#fff)); background: -webkit-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -o-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -ms-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: linear-gradient(to right,#fff 0,#b0b0b0 50%,#fff 100%); filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#b0b0b0',endColorstr='#ffffff',GradientType=1); padding: 5px; margin: 25px auto; color: #fff; text-align: center; font-weight: bold; font-size: 13px; font-size: 1.3rem; width: 100%; max-width: 830px; }
ul.sponsor_listings {list-style: none; margin: 20px 0; padding: 0; text-align: center; }
ul.sponsor_listings li {display: inline-block; vertical-align: middle; margin: 0 20px 20px 20px; }
ul.sponsor_listings li img { width: 100%;}

.spacer {height: 20px; }
#sponsors ul {overflow: hidden; }
#sponsors li:only-child {text-align: center; }
#sponsors li:last-child:nth-child(odd) {text-align: center; }
ul.sponsorList {text-align: center; margin: 0; padding: 0; }
#sponsors ul li {width: 160px; display: inline-block; margin: 10px 15px; vertical-align: middle; }
#sponsors h2 {color: #9A9A9A; text-align: center; margin-right: 0; font-weight: normal; padding-bottom: 4px; }
#sponsors .sponsor_list_heading {background: #b0b0b0; background: -moz-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -webkit-gradient(linear,left top,right top,color-stop(0%,#fff),color-stop(50%,#b0b0b0),color-stop(100%,#fff)); background: -webkit-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -o-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: -ms-linear-gradient(left,#fff 0,#b0b0b0 50%,#fff 100%); background: linear-gradient(to right,#fff 0,#b0b0b0 50%,#fff 100%); filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#b0b0b0',endColorstr='#ffffff',GradientType=1); padding: 5px; margin: 25px auto; color: #fff;  text-align: center; font-weight: bold; font-size: 13px; font-size: 1.3rem; width: 100%; max-width: 830px;}
#sponsors .heading {color: #5f5f5f; margin: 5px 0; padding: 0; font-size: 13px; font-size: 1.3rem; font-weight: bold; line-height: 1.2em; }
div.en_article_metadata {display: none; }

#contacts { /*border-top: 1px solid #BCBCBC; */padding-top: 20px; }
#contacts h3 { font-size: 14px; font-size: 1.4rem; margin: 0; padding: 0; color:#888; font-weight: bold; }
#contacts p { font-size: 14px; font-size: 1.4rem; line-height: 18px; line-height: 1.8rem; margin: 0; padding: 0 20px 10px 0; color:#888; }
#contacts a { color: #888; }

footer { background: #111; width: 100%; min-height: 150px; margin: 0; overflow: auto; padding: 15px 0 22px; font-weight: normal; font-size: 16px; font-size: 1.6rem; line-height: 1.6em; color: #fff;  margin: 0 auto; }
footer a {color: #fff; text-decoration: none; line-height: 1.4em; }
footer a:hover {text-decoration: underline; }
footer .copyright {font-size: 16px; font-size: 1.6rem; padding-top: 20px; }
footer .footercol {display: inline-block; vertical-align: top; }
footer .footercol ul li:first-child {color: #999; }
footer ul {margin: 0; padding: 20px 0; list-style: none; }
#en_body footer ul li {list-style: none; padding: 0; margin: 0; font-size: .9em; line-height: 1.3em; }

#copyright {font-size: 14px; font-size: 1.4rem; padding: 20px 0; background: #222; color: #fff; }
#copyright a { color: #fff; }

#en_body footer .social li { line-height: 45px; padding-bottom: 5px; }
#en_body footer .social li a:hover { text-decoration: none; }
#en_body footer .social li img { max-width: 32px; display: inline-block; vertical-align: middle; margin-right: 10px }

#newsletter-popup-overlay {display: none; position: absolute; z-index: 200; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); background: none\9; }
#newsletter-popup-overlay .popup {overflow: hidden; margin: 140px auto 0; margin: 14rem auto 0; background-color: #f9f9f9; text-align: center; max-width: 740px; max-width: 74rem; width: 70%; -webkit-border-radius: 8px; -moz-border-radius: 8px; border-radius: 8px; -webkit-box-shadow: 0 0 15px rgba(0,0,0,0.3); -moz-box-shadow: 0 0 15px rgba(0,0,0,0.3); box-shadow: 0 0 15px rgba(0,0,0,0.3); border: 3px solid #ddd\9; }
#newsletter-popup-overlay .popup .popup-header {background: #fff; padding: 10px 10px 15px; padding: 1rem 1rem 1.5rem; -webkit-border-radius: 8px; -moz-border-radius: 8px; border-radius: 8px; -webkit-box-shadow: 0 0 15px rgba(0,0,0,0.3); -moz-box-shadow: 0 0 15px rgba(0,0,0,0.3); box-shadow: 0 0 15px rgba(0,0,0,0.3); }
#newsletter-popup-overlay .popup .popup-header a.close {font-size: 16px; font-size: 1.6rem; line-height: 19px; line-height: 1.9rem; color: #999; display: block; padding-right: 24px; padding-right: 2.4rem; float: right; background: transparent url('http://cdn.oreilly.com/oreilly/images/close-icon-19x19.png') right 0 no-repeat; }
#newsletter-popup-overlay .popup .popup-header a.close:hover {color: #666; text-decoration: none; background: transparent url('http://cdn.oreilly.com/oreilly/images/close-icon-19x19.png') right -100px no-repeat; }
#newsletter-popup-overlay .popup .popup-header h3 {margin: 50px 13px 5px 13px; margin: 5rem 1.3rem 0.5rem 1.3rem; clear-both;padding: 0; font-size: 40px; font-size: 4rem; line-height: 44px; line-height: 4.4rem; font-weight: normal; }
#newsletter-popup-overlay .popup .popup-header p {margin: 0 40px; margin: 0 4rem; padding: 0; font-size: 20px; font-size: 2rem; line-height: 28px; line-height: 2.8rem; font-weight: normal; }
#newsletter-popup-overlay .popup-form {margin: 42px 23px 0; margin: 4.2rem 2.3rem 0; text-align: left; }
#newsletter-popup-overlay #newsletter-popup-frame {display: block; border: none; padding: 0; margin: 0 auto; width: 450px; width: 45rem; height: 90px; height: 9rem; text-align: left; }
div.banner_ad a[data-defer="random"] { display: none; }
div.banner_ad { padding-left: 2rem; max-height: 95px; text-align: center;  }

@media only screen and (max-width: 680px) {
  #widgets_row.row h2 { margin: 20px 0; }
}

#stay_informed h2 {font-size: 20px; font-size: 2rem; margin-bottom: 10px; }
#widgets_row.row { background: #000; border-bottom: none; padding: 40px 0; }
#widgets_row.row a { color: #fff; }
#widgets_row.row h2 {color: #fff; font-size: 20px; font-size: 2rem; line-height: 23px;line-height: 2.3rem; font-weight: normal; margin: 0 0 5px 0; }
#widgets_row p {color: #eee; margin: 0 0 5px 0; }
#widgets_row.row #stay_informed a {color: #fff;}
#widgets_row.row #more_coverage a { vertical-align: middle; margin-left: 10px; font-size: 2rem; }
#widgets_row.row #keynote-image { width: 100%; padding-right: 20px; }
#widgets_row.row #stay_informed h2 { margin-bottom: 0; }
#widgets_row.row #stay_informed #photos {width: 100%; margin-top: 10px; padding-top: 15px; }
#widgets_row.row #stay_informed #photos>div {width: 100%; }
#widgets_row.row #stay_informed #photos div.flickr_group {float: left; margin: 0 0 10px 6px; padding: 1px; border: 1px solid #aaa; width: 78px; }
#widgets_row.row #stay_informed #photos>div>div:first-child {margin-left: 0; }
#widgets_row.row #stay_informed #photos div.flickr_group a {text-decoration: none; }
#widgets_row.row #photos img { width: 100%; max-width: 277px; }

</style>
<style>
@media only screen and (max-width: 680px) {
   #en_footer ul li { font-size: 13px; font-size: 1.3rem; line-height: 22px; line-height: 2.2rem; }
}
</style>
<!--VWO-->
<!-- Start Visual Website Optimizer Asynchronous Code -->
<script type='text/javascript'>
var _vwo_code=(function(){
var account_id=27304,
settings_tolerance=2000,
library_tolerance=2500,
use_existing_jquery=false,
// DO NOT EDIT BELOW THIS LINE
f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);return settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();
</script>
<!-- End Visual Website Optimizer Asynchronous Code -->
<!-- Digital Grid -->
<!--metadata-->
<meta property="og:image" content="http://cdn.oreillystatic.com/en/assets/1/eventseries/41/ai_social_200x200.png" />
<meta name="twitter:image" content="http://cdn.oreillystatic.com/en/assets/1/eventseries/41/ai_social_120x120.png" />
<meta name="twitter:site" content="@oreillyAI" /> <!-- public url:  -->
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary" />

<link rel="canonical" href="http://conferences.oreilly.com/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/grid" />
<meta property="og:url" name="twitter:url" content="http://conferences.oreilly.com/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/grid" />
<meta property="og:title" name="twitter:title" content="Schedule - Artificial Intelligence 2016" />
<meta property="og:description" name="twitter:description" content="Schedule for the O&#x27;Reilly AI Conference, happening September 26-27, 2016 in New York, NY." />

<!-- Chartbeat Head -->
<script type="text/javascript">
<!--
// js/charbeat_head
var _sf_startpt=(new Date()).getTime()
-->
</script>
<!--[if lte IE 6]>
  <script type="text/javascript" src="/javascripts/supersleight-min.js"></script>
  <![endif]-->

<link rel="icon" type="image/png" href="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/ai_favicon.png">

<meta name="description" content="Schedule for the O&#x27;Reilly AI Conference, happening September 26-27, 2016 in New York, NY." />
<meta name="Category" content="Conferences" />

<meta name="search_date" content="2016-09-26" />

<meta name="search-conf-name" content="Artificial Intelligence 2016" />
<meta name="search-conf-url" content="http://conferences.oreilly.com/artificial-intelligence/ai-deep-learning-bots-ny" />

<meta name="search-content" content="other"/>

<!--for Google Webmaster Tools -->
<meta name="verify-v1" content = "ejKlkisc2aaHXLk+37fMPNCfcsC5GdJYO2qoBXRRM7g=" />

<!--
<link rel="image_src" href="http://oreilly.com/images/oreilly/oreilly_large.gif" />
-->
</head>
<body class="en_webpage en_c_schedule en_a_grid" id="en_schedule_grid">
<div id="en_content" itemscope=""
itemtype="http://data-vocabulary.org/Event">

<!-- closed in after_main-->
<meta itemprop="startDate" datetime="2016-09-26T00:00-00:00" content="September 26, 2016" />
<meta itemprop="endDate" datetime="2016-09-27T00:00-00:00" content="September 27, 2016"/>
<meta itemprop="location" content="New York" />
<meta itemprop="name" content="Artificial Intelligence 2016" />
<meta itemprop="summary" content="Schedule - Artificial Intelligence 2016" />

    <meta itemprop="photo" content="http://cdn.oreillystatic.com/en/assets/1/eventseries/41/ai_social_200x200.png" />

<meta itemprop="photo" content="http://cdn.oreillystatic.com/en/assets/1/eventseries/41/ai_social_200x200.png" />

<div id="en_main_parts">

<!-- closed in after_main -->
<div id="nav_overlay" class="hide">

</div>

<div id="en_header">

      <div class="branding_bar">
      <div class="content_row">
        <div class="grid">
        <a class="col-1-3" href="http://oreilly.com"><img id="logo" src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/oreilly_logo.svg" alt="O'Reilly Media, Inc" width="100%" border="0" style="max-width:128px;" /></a>
          <div id="franchise_links" class="col-2-3"><span class="current">New York</span>&nbsp; &bull; &nbsp;<a href="http://conferences.oreilly.com/artificial-intelligence/bot-ca">Bot Day</a></div>
          </div><!--grid-->
      </div><!-- div.content_row -->
    </div><!-- div.branding_bar -->

    <div id="inside_header" class="row">
      <div class="content_row">
        <div class="grid">
        <div class="event_logo"><a href="/artificial-intelligence/ai-deep-learning-bots-ny"><img src="//cdn.oreillystatic.com/en/assets/1/eventseries/41/ai_logo_reversed.svg" width="100%"  alt="O'Reilly Artificial Intelligence Conference" border="0" /></a></div>
        <div class="tagline_date_location">
          <div class="date_location">September 26-27, 2016</div>
          <div class="date_location">New York, NY</div>
        </div><!--div.date_location-->
        </div><!--grid-->
      </div>  <!-- div.content_row -->
    </div><!-- div#inside_header -->

<div id="sitenav">

<div class="content_row">

    <div id="navbar">
      <nav class="en_clearfix"> <a href="#" id="pull"></a>
        <ul class="clearfix">
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/grid/public">Schedule</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/speakers">Speakers</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/stype/1017">Events</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/sponsors">Sponsor Pavilion</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/hotel">Venue</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/about">About</a></li>
            <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/user/account">Account</a></li>
            


















        </ul>
      </nav>
    </div>

</div>

<!-- /content_row -->

</div>

<!-- /sitenav -->

</div>

<!-- //en_header -->
<div id="en_body">

    <div id="en_main" class="en_clearfix">






    <iframe style="visibility:hidden;display:none"
            src="/artificial-intelligence/ai-deep-learning-bots-ny/user/account/notice_login_status">
    </iframe>

<div id="en_preamble">

<div>

 

</div>

</div>

      <div id="above-topics-grid">
              



















              <h1 class="pad">Schedule</h1>
              <div class="right pad" style="clear: right;">

<div class="ical-offerings">

        iCal:
        <a href="/ai-deep-learning-bots-ny/public/schedule/ical" target="_blank">Download</a>
        <a href="webcal://conferences.oreilly.com/ai-deep-learning-bots-ny/public/schedule/ical" target="_blank">Subscribe</a>
    </div>

</div>

              <h2 data-date="2016-09-26" id="current_day" style="display:none;">Monday, September 26</h2>

              <div id="en_grid_dates" class="pad">
                 <div id="list_grid"><a href="#" class="list">List View</a>  <a href="#" class="sched_grid active">Grid View</a>&nbsp; <a style="color: #555; font-size: 14px; font-size: 1.4rem;" href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/personal" id="en_in_personal_link"><img style="color: #555; font-size: 14px; font-size: 1.4rem; vertical-align: top;" src="/images/personal-schedule-icon.png" width="17" height="18" alt="personal schedule icon"> Personal&nbsp;schedule &gt;</a></div>   

                  <ul style="margin-top: 35px;">
                  
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/grid/public/2016-09-26" data-date="2016-09-26"><li class="active">Monday<span class="hide">-</span><div class="session_types">Keynotes &amp; Sessions</div></li></a><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/grid/public/2016-09-27" data-date="2016-09-27"><li>Tuesday<span class="hide">-</span><div class="session_types">Keynotes &amp; Sessions</div></li></a>
                  </ul>
             </div>
      </div><!-- div#above-topics-grid -->

<div id="grid_track_key">

<div>

<h3>
List by type
</h3>
<li>
<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/stype/1018?schedule=public">Keynotes</a>
</li>
<li>
<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/stype/996?schedule=public">Sessions</a>
</li>

</div>

</div>

        <div id="en_grid_topic_key">
          <h3>Topics</h3>
          <div>
            <ul>
                <li id="topic_key_1911">
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/topic/1911">Impact on business and society</a>
                </li>
                <li id="topic_key_1910">
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/topic/1910">Implementing AI</a>
                </li>
                <li id="topic_key_1913">
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/topic/1913">Interacting with AI</a>
                </li>
                <li id="topic_key_2017">
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/topic/2017">Sponsored</a>
                </li>
                <li id="topic_key_1912">
                  <a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/topic/1912">Verticals and applications</a>
                </li>
            </ul>
          </div>
        </div>

    <div id="en_grid_container" class="d2016-09-26">
        <div id="slot_grid"><div class="slot_room_title" id="room_title_2439"><div>River Pavilion B</div></div><div class="room2439 slot" id="slot52029">

<div class="slot_detail">

<div id="psched54515" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54515?type=Proposal" class="en_psched_add" title="Add Monday opening remarks to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Monday opening remarks to your personal schedule" /></a>

</div>

          <span class="location">River Pavilion B</span><br />
        
    9:00am

<!-- Keynote -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54515" class="url uid">Monday opening remarks</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_9477.jpg" data-speaker-id="9477">Ben Lorica (O&#x27;Reilly Media)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_171704.jpg" data-speaker-id="171704">Roger Chen (NSFY)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54276" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54276?type=Proposal" class="en_psched_add" title="Add Software engineering of systems that learn in uncertain domains to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Software engineering of systems that learn in uncertain domains to your personal schedule" /></a>

</div>

      9:05am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54276" class="url uid">Software engineering of systems that learn in uncertain domains</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_5810.jpg" data-speaker-id="5810">Peter Norvig (Google)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54277" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54277?type=Proposal" class="en_psched_add" title="Add Why we&#x27;ll never run out of jobs to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Why we&#x27;ll never run out of jobs to your personal schedule" /></a>

</div>

      9:30am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54277" class="url uid">Why we&#x27;ll never run out of jobs</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_31917.jpg" data-speaker-id="31917">Tim O&#x27;Reilly (O&#x27;Reilly Media, Inc.)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54968" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54968?type=Proposal" class="en_psched_add" title="Add Artificial intelligence: Making a human connection to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Artificial intelligence: Making a human connection to your personal schedule" /></a>

</div>

      9:45am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54968" class="url uid">Artificial intelligence: Making a human connection</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_29945.jpg" data-speaker-id="29945">Genevieve Bell (Intel Corporation)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54238" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54238?type=Proposal" class="en_psched_add" title="Add Humanizing AI development: Lessons from China and Xiaoice at Microsoft to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Humanizing AI development: Lessons from China and Xiaoice at Microsoft to your personal schedule" /></a>

</div>

      9:55am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54238" class="url uid">Humanizing AI development: Lessons from China and Xiaoice at Microsoft</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_82951.jpg" data-speaker-id="82951">Lili Cheng (Microsoft Research)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54518" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54518?type=Proposal" class="en_psched_add" title="Add How AI is propelling driverless cars, the future of surface transport to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add How AI is propelling driverless cars, the future of surface transport to your personal schedule" /></a>

</div>

      10:10am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54518" class="url uid">How AI is propelling driverless cars, the future of surface transport</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_148359.jpg" data-speaker-id="148359">Shahin Farshchi (Lux Capital)</span>
            </span>
        

</div>

<div class="slot_detail">

<div id="psched54516" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54516?type=Proposal" class="en_psched_add" title="Add Closing remarks to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Closing remarks to your personal schedule" /></a>

</div>

      10:25am






        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54516" class="url uid">Closing remarks</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_9477.jpg" data-speaker-id="9477">Ben Lorica (O&#x27;Reilly Media)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_171704.jpg" data-speaker-id="171704">Roger Chen (NSFY)</span>
            </span>
        

</div>

</div>

<div id="slot51990" class="room2439 slot session">

<div class="slot_detail">

<div id="psched54474" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54474?type=Proposal" class="en_psched_add" title="Add Deep neural network model compression and an efficient inference engine to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Deep neural network model compression and an efficient inference engine to your personal schedule" /></a>

</div>

    11:00am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54474" class="url uid">Deep neural network model compression and an efficient inference engine</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_258221.jpg" data-speaker-id="258221">Song Han (Stanford University)</span>
            </span>
        

</div>

</div>

<div id="slot51991" class="room2439 slot session">

<div class="slot_detail">

<div id="psched54279" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54279?type=Proposal" class="en_psched_add" title="Add The future of AI to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add The future of AI to your personal schedule" /></a>

</div>

    11:50am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54279" class="url uid">The future of AI</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_253239.jpg" data-speaker-id="253239">Oren Etzioni (Allen Institute for Artificial Intelligence)</span>
            </span>
        

</div>

</div>

<div id="slot51992" class="room2439 slot topic1910 session">

<div class="slot_detail">

<div id="psched54053" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54053?type=Proposal" class="en_psched_add" title="Add How advances in deep learning and computer vision can empower the blind community to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add How advances in deep learning and computer vision can empower the blind community to your personal schedule" /></a>

</div>

    1:30pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54053" class="url uid">How advances in deep learning and computer vision can empower the blind community</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_193426.jpg" data-speaker-id="193426">Anirudh Koul (Microsoft)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_236685.jpg" data-speaker-id="236685">Saqib Shaikh (Microsoft)</span>
            </span>
        

</div>

</div>

<div id="slot51995" class="room2439 slot session">

<div class="slot_detail">

<div id="psched54218" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54218?type=Proposal" class="en_psched_add" title="Add Deep reinforcement learning for robotics to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Deep reinforcement learning for robotics to your personal schedule" /></a>

</div>

    2:20pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54218" class="url uid">Deep reinforcement learning for robotics</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252995.jpg" data-speaker-id="252995">Pieter Abbeel (OpenAI / UC Berkeley)</span>
            </span>
        

</div>

</div>

<div id="slot51998" class="room2439 slot topic1912 session">

<div class="slot_detail">

<div id="psched54109" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54109?type=Proposal" class="en_psched_add" title="Add End-to-end learning for autonomous driving to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add End-to-end learning for autonomous driving to your personal schedule" /></a>

</div>

    3:45pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54109" class="url uid">End-to-end learning for autonomous driving</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252287.jpg" data-speaker-id="252287">Urs Muller (NVIDIA)</span>
            </span>
        

</div>

</div>

<div id="slot52000" class="room2439 slot topic1910 session">

<div class="slot_detail">

<div id="psched54100" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54100?type=Proposal" class="en_psched_add" title="Add High-level APIs for scalable machine learning to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add High-level APIs for scalable machine learning to your personal schedule" /></a>

</div>

    4:35pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54100" class="url uid">High-level APIs for scalable machine learning</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_245377.jpg" data-speaker-id="245377">Martin Wicke (Google)</span>
            </span>
        

</div>

</div>

<div id="room_title_2440" class="slot_room_title">

<div>

3D08

</div>

</div>

<div id="slot51987" class="room2440 slot topic1911 session">

<div class="slot_detail">

<div id="psched53863" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/53863?type=Proposal" class="en_psched_add" title="Add Only humans need apply: Adding value to the work of very smart machines to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Only humans need apply: Adding value to the work of very smart machines to your personal schedule" /></a>

</div>

    11:00am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/53863" class="url uid">Only humans need apply: Adding value to the work of very smart machines</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_251535.jpg" data-speaker-id="251535">Tom Davenport (Babson College, MIT)</span>
            </span>
        

</div>

</div>

<div id="slot51988" class="room2440 slot topic1910 session">

<div class="slot_detail">

<div id="psched54094" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54094?type=Proposal" class="en_psched_add" title="Add Practical AI product development to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Practical AI product development to your personal schedule" /></a>

</div>

    11:50am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54094" class="url uid">Practical AI product development</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_62617.jpg" data-speaker-id="62617">Hilary Mason (Fast Forward Labs)</span>
            </span>
        

</div>

</div>

<div id="slot51993" class="room2440 slot session">

<div class="slot_detail">

<div id="psched54494" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54494?type=Proposal" class="en_psched_add" title="Add Transforming your industry with cognitive computing to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Transforming your industry with cognitive computing to your personal schedule" /></a>

</div>

    1:30pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54494" class="url uid">Transforming your industry with cognitive computing</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_254157.jpg" data-speaker-id="254157">Guruduth Banavar (Cognitive Computing, IBM)</span>
            </span>
        

</div>

</div>

<div id="slot51996" class="room2440 slot session">

<div class="slot_detail">

<div id="psched54881" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54881?type=Proposal" class="en_psched_add" title="Add Benefits of scaling machine learning to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Benefits of scaling machine learning to your personal schedule" /></a>

</div>

    2:20pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54881" class="url uid">Benefits of scaling machine learning</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_187782.jpg" data-speaker-id="187782">Reza Zadeh (Stanford | Matroid)</span>
            </span>
        

</div>

</div>

<div id="slot51999" class="room2440 slot topic1910 session">

<div class="slot_detail">

<div id="psched54067" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54067?type=Proposal" class="en_psched_add" title="Add  Unlock the power of AI: A fundamentally different approach to building intelligent systems to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add  Unlock the power of AI: A fundamentally different approach to building intelligent systems to your personal schedule" /></a>

</div>

    3:45pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54067" class="url uid"> Unlock the power of AI: A fundamentally different approach to building intelligent systems</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_236882.jpg" data-speaker-id="236882">Mark Hammond (Bonsai)</span>
            </span>
        

</div>

</div>

<div id="slot52001" class="room2440 slot session">

<div class="slot_detail">

<div id="psched55538" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/55538?type=Proposal" class="en_psched_add" title="Add The need for speed: Benchmarking deep learning workloads to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add The need for speed: Benchmarking deep learning workloads to your personal schedule" /></a>

</div>

    4:35pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/55538" class="url uid">The need for speed: Benchmarking deep learning workloads</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263019.jpg" data-speaker-id="263019">Greg Diamos (Baidu)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263097.jpg" data-speaker-id="263097">Sharan Narang (Baidu)</span>
            </span>
        

</div>

</div>

<div id="room_title_2482" class="slot_room_title">

<div>

3D09

</div>

</div>

<div id="slot52017" class="room2482 slot topic1910 session">

<div class="slot_detail">

<div id="psched54062" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54062?type=Proposal" class="en_psched_add" title="Add How to make robots empathetic to human feelings in real time to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add How to make robots empathetic to human feelings in real time to your personal schedule" /></a>

</div>

    11:00am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54062" class="url uid">How to make robots empathetic to human feelings in real time</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252222.jpg" data-speaker-id="252222">Pascale Fung (The Hong Kong University of Science and Technology)</span>
            </span>
        

</div>

</div>

<div id="slot52018" class="room2482 slot topic1910 session">

<div class="slot_detail">

<div id="psched54101" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54101?type=Proposal" class="en_psched_add" title="Add Building and applying emotion recognition to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Building and applying emotion recognition to your personal schedule" /></a>

</div>

    11:50am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54101" class="url uid">Building and applying emotion recognition</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252250.jpg" data-speaker-id="252250">Anna Roth (Microsoft)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_251905.jpg" data-speaker-id="251905">Cristian Canton (Microsoft Technology and Research)</span>
            </span>
        

</div>

</div>

<div id="slot52019" class="room2482 slot topic1913 session">

<div class="slot_detail">

<div id="psched54174" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54174?type=Proposal" class="en_psched_add" title="Add Deeply active learning: Approximating human learning with smaller datasets combined with human assistance to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Deeply active learning: Approximating human learning with smaller datasets combined with human assistance to your personal schedule" /></a>

</div>

    1:30pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54174" class="url uid">Deeply active learning: Approximating human learning with smaller datasets combined with human assistance</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_169826.jpg" data-speaker-id="169826">Christopher Nguyen (Arimo)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252622.jpg" data-speaker-id="252622">Binh Han (Arimo)</span>
            </span>
        

</div>

</div>

<div id="slot52020" class="room2482 slot topic1913 session">

<div class="slot_detail">

<div id="psched54021" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54021?type=Proposal" class="en_psched_add" title="Add Probabilistic programming for augmented intelligence to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Probabilistic programming for augmented intelligence to your personal schedule" /></a>

</div>

    2:20pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54021" class="url uid">Probabilistic programming for augmented intelligence</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_107139.jpg" data-speaker-id="107139">Vikash Mansinghka (MIT)<span class="comma">,</span> </span><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_3500.jpg" data-speaker-id="3500">Richard Tibbetts (MIT)</span>
            </span>
        

</div>

</div>

<div id="slot52021" class="room2482 slot topic1911 session">

<div class="slot_detail">

<div id="psched53930" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/53930?type=Proposal" class="en_psched_add" title="Add The future of natural language generation, 2016–2026 to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add The future of natural language generation, 2016–2026 to your personal schedule" /></a>

</div>

    3:45pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/53930" class="url uid">The future of natural language generation, 2016–2026</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_126335.jpg" data-speaker-id="126335">Robbie Allen (Automated Insights, Inc.)</span>
            </span>
        

</div>

</div>

<div id="slot52022" class="room2482 slot topic1911 session">

<div class="slot_detail">

<div id="psched54214" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54214?type=Proposal" class="en_psched_add" title="Add The new artificial intelligence frontier to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add The new artificial intelligence frontier to your personal schedule" /></a>

</div>

    4:35pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54214" class="url uid">The new artificial intelligence frontier</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252949.jpg" data-speaker-id="252949">Babak Hodjat (Sentient Technologies)</span>
            </span>
        

</div>

</div>

<div id="room_title_2483" class="slot_room_title">

<div>

3D10

</div>

</div>

<div id="slot52362" class="room2483 slot topic2017 session">

<div class="slot_detail">

<div id="psched54963" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54963?type=Proposal" class="en_psched_add" title="Add AI on IA to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add AI on IA to your personal schedule" /></a>

</div>

    11:00am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54963" class="url uid">AI on IA</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_135162.jpg" data-speaker-id="135162">Vin Sharma (Intel)</span>
            </span>
        

</div>

</div>

<div id="slot52500" class="room2483 slot topic2017 session">

<div class="slot_detail">

<div id="psched54988" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54988?type=Proposal" class="en_psched_add" title="Add Deploying AI-based services in the data center for real-time responsive experiences to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Deploying AI-based services in the data center for real-time responsive experiences to your personal schedule" /></a>

</div>

    11:50am

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54988" class="url uid">Deploying AI-based services in the data center for real-time responsive experiences</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_259924.jpg" data-speaker-id="259924">Sanford Russell (NVIDIA)</span>
            </span>
        

</div>

</div>

<div id="slot52501" class="room2483 slot topic1910 session">

<div class="slot_detail">

<div id="psched55569" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/55569?type=Proposal" class="en_psched_add" title="Add Growing up: Continuous integration for machine-learning models to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Growing up: Continuous integration for machine-learning models to your personal schedule" /></a>

</div>

    1:30pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/55569" class="url uid">Growing up: Continuous integration for machine-learning models</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263216.jpg" data-speaker-id="263216">Zachary  Hanif (Capital One)</span>
            </span>
        

</div>

</div>

<div id="slot52766" class="room2483 slot topic1911 session">

<div class="slot_detail">

<div id="psched53961" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/53961?type=Proposal" class="en_psched_add" title="Add What I learned by replacing middle-class manufacturing jobs with ML and AI to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add What I learned by replacing middle-class manufacturing jobs with ML and AI to your personal schedule" /></a>

</div>

    2:20pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/53961" class="url uid">What I learned by replacing middle-class manufacturing jobs with ML and AI</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_155541.jpg" data-speaker-id="155541">Eduardo Arino de la Rubia (Domino Data Lab)</span>
            </span>
        

</div>

</div>

<div id="slot52704" class="room2483 slot topic1910 session">

<div class="slot_detail">

<div id="psched54081" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54081?type=Proposal" class="en_psched_add" title="Add Deep learning: Modular in theory, inflexible in practice to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Deep learning: Modular in theory, inflexible in practice to your personal schedule" /></a>

</div>

    3:45pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54081" class="url uid">Deep learning: Modular in theory, inflexible in practice</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252236.jpg" data-speaker-id="252236">Diogo Almeida (Enlitic)</span>
            </span>
        

</div>

</div>

<div id="slot52708" class="room2483 slot topic1910 session">

<div class="slot_detail">

<div id="psched54002" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54002?type=Proposal" class="en_psched_add" title="Add A peek at x.ai’s data science architecture to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add A peek at x.ai’s data science architecture to your personal schedule" /></a>

</div>

    4:35pm

<!-- Session -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54002" class="url uid">A peek at x.ai’s data science architecture</a></span>
        


            <span class="description">
                <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252112.jpg" data-speaker-id="252112">Angela Zhou (x.ai)</span>
            </span>
        

</div>

</div>

<div id="slot52244" class="room2441 slot not_session">

<div class="slot_detail">

    8:00am


        Morning coffee service Sponsored by Capital One

<!--  -->
        | Room: <span class="location">River Pavilion A</span><br>

</div>

</div>

<div id="slot51994" class="room2441 slot not_session">

<div class="slot_detail">

    10:30am


        Morning Break

<!--  -->
        | Room: <span class="location">River Pavilion A</span><br>

</div>

</div>

<div id="slot51989" class="room2441 slot not_session">

<div class="slot_detail">

    12:30pm


        Lunch Sponsored by Intel

<!--  -->
        | Room: <span class="location">River Pavilion A</span><br>

</div>

</div>

<div id="slot51997" class="room2441 slot not_session">

<div class="slot_detail">

    3:00pm


        Afternoon Break

<!--  -->
        | Room: <span class="location">River Pavilion A</span><br>

</div>

</div>

<div id="slot52073" class="room2441 slot session">

<div class="slot_detail event_session">

<div id="psched54650" class="en_session_psched">

<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/add/54650?type=Proposal" class="en_psched_add" title="Add Attendee Reception to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add Attendee Reception to your personal schedule" /></a>

</div>

    5:15pm

<!-- Event -->
        <span class="summary"><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/schedule/detail/54650" class="url uid">Attendee Reception</a></span>
        
            | Room: <span class="location">River Pavilion A</span>
        


            <span class="description">
                
            </span>
        

</div>

</div>

</div>

<div id="slot_popup_store">

<div id="slot52029_p" class="slot_popup">

<div id="sched54515" class="en_popup_content">

    <div class="en_popup_time">
        9:00am-9:05am (5m)
        
        
    </div>

        
            <div class="en_popup_name">Monday opening remarks</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_9477.jpg" data-speaker-id="9477">Ben Lorica (O&#x27;Reilly Media)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_171704.jpg" data-speaker-id="171704">Roger Chen (NSFY)</span></div>
            <div class="en_popup_desc">Program chairs Ben Lorica and Roger Chen open the first day of keynotes.</div>
        

</div>

<div id="sched54276" class="en_popup_content">

    <div class="en_popup_time">
        9:05am-9:30am (25m)
        
        
    </div>

        
            <div class="en_popup_name">Software engineering of systems that learn in uncertain domains</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_5810.jpg" data-speaker-id="5810">Peter Norvig (Google)</span></div>
            <div class="en_popup_desc">Building reliable, robust software is hard. It is even harder when we move from deterministic domains (such as balancing a checkbook) to uncertain domains (such as recognizing speech or objects in an image). The field of machine learning allows us to use data to build systems in these uncertain domains. Peter Norvig looks at techniques for achieving reliability (and some of the other -ilities).</div>
        

</div>

<div id="sched54277" class="en_popup_content">

    <div class="en_popup_time">
        9:30am-9:45am (15m)
        
        
    </div>

        
            <div class="en_popup_name">Why we&#x27;ll never run out of jobs</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_31917.jpg" data-speaker-id="31917">Tim O&#x27;Reilly (O&#x27;Reilly Media, Inc.)</span></div>
            <div class="en_popup_desc">There are many who fear that in the future, AI will do more and more of the jobs done by humans, leaving us without meaningful work. To believe this is a colossal failure of the imagination. Tim O'Reilly explains why we can't just use technology to replace people; we must use it to augment them so that they can do things that were previously impossible.</div>
        

</div>

<div id="sched54968" class="en_popup_content">

    <div class="en_popup_time">
        9:45am-9:55am (10m)
        Sponsored
        
    </div>

        
            <div class="en_popup_name">Artificial intelligence: Making a human connection</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_29945.jpg" data-speaker-id="29945">Genevieve Bell (Intel Corporation)</span></div>
            <div class="en_popup_desc">Genevieve Bell explores the meaning of “intelligence” within the context of machines and its cultural impact on humans and their relationships. Genevieve interrogates AI not just as a technical agenda but as a cultural category in order to understand the ways in which the story of AI is connected to the history of human culture.</div>
        

</div>

<div id="sched54238" class="en_popup_content">

    <div class="en_popup_time">
        9:55am-10:10am (15m)
        
        
    </div>

        
            <div class="en_popup_name">Humanizing AI development: Lessons from China and Xiaoice at Microsoft</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_82951.jpg" data-speaker-id="82951">Lili Cheng (Microsoft Research)</span></div>
            <div class="en_popup_desc">Keynote by Lili Cheng</div>
        

</div>

<div id="sched54518" class="en_popup_content">

    <div class="en_popup_time">
        10:10am-10:25am (15m)
        
        
    </div>

        
            <div class="en_popup_name">How AI is propelling driverless cars, the future of surface transport</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_148359.jpg" data-speaker-id="148359">Shahin Farshchi (Lux Capital)</span></div>
            <div class="en_popup_desc">Keynote by Shahin Farshchi</div>
        

</div>

<div id="sched54516" class="en_popup_content">

    <div class="en_popup_time">
        10:25am-10:30am (5m)
        
        
    </div>

        
            <div class="en_popup_name">Closing remarks</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_9477.jpg" data-speaker-id="9477">Ben Lorica (O&#x27;Reilly Media)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_171704.jpg" data-speaker-id="171704">Roger Chen (NSFY)</span></div>
            <div class="en_popup_desc">Program chairs Ben Lorica and Roger Chen close the first day of keynotes.</div>
        

</div>

</div>

<div id="slot51990_p" class="slot_popup">

<div id="sched54474" class="en_popup_content">

    <div class="en_popup_time">
        11:00am-11:40am (40m)
        
        
    </div>

        
            <div class="en_popup_name">Deep neural network model compression and an efficient inference engine</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_258221.jpg" data-speaker-id="258221">Song Han (Stanford University)</span></div>
            <div class="en_popup_desc">Neural networks are both computationally and memory intensive, making them difficult to deploy on embedded systems with limited hardware resources. Song Han explains how deep compression addresses this limitation by reducing the storage requirement of neural networks without affecting their accuracy and proposes an energy-efficient inference engine (EIE) that works with this model.</div>
        

</div>

</div>

<div id="slot51991_p" class="slot_popup">

<div id="sched54279" class="en_popup_content">

    <div class="en_popup_time">
        11:50am-12:30pm (40m)
        
        
    </div>

        
            <div class="en_popup_name">The future of AI</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_253239.jpg" data-speaker-id="253239">Oren Etzioni (Allen Institute for Artificial Intelligence)</span></div>
            <div class="en_popup_desc">Oren Etzioni offers his perspective on the future of AI, based on cutting-edge research at the Allen Institute for AI on projects such as Aristo and Semantic Scholar. This future reflects the institute's mission: AI for the common good. </div>
        

</div>

</div>

<div id="slot51992_p" class="slot_popup">

<div id="sched54053" class="en_popup_content">

    <div class="en_popup_time">
        1:30pm-2:10pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">How advances in deep learning and computer vision can empower the blind community</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_193426.jpg" data-speaker-id="193426">Anirudh Koul (Microsoft)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_236685.jpg" data-speaker-id="236685">Saqib Shaikh (Microsoft)</span></div>
            <div class="en_popup_desc">Anirudh Koul and Saqib Shaikh explore cutting-edge advances at the intersection of computer vision, language, and deep learning that can help describe the physical world to the blind community. Anirudh and Saqib then explain how developers can utilize this state-of-the-art image description, as well as visual question answering and other computer-vision technologies, in their own applications.</div>
        

</div>

</div>

<div id="slot51995_p" class="slot_popup">

<div id="sched54218" class="en_popup_content">

    <div class="en_popup_time">
        2:20pm-3:00pm (40m)
        
        
    </div>

        
            <div class="en_popup_name">Deep reinforcement learning for robotics</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252995.jpg" data-speaker-id="252995">Pieter Abbeel (OpenAI / UC Berkeley)</span></div>
            <div class="en_popup_desc">Pieter Abbeel explores deep reinforcement learning for robotics.</div>
        

</div>

</div>

<div id="slot51998_p" class="slot_popup">

<div id="sched54109" class="en_popup_content">

    <div class="en_popup_time">
        3:45pm-4:25pm (40m)
        Verticals and applications
        
    </div>

        
            <div class="en_popup_name">End-to-end learning for autonomous driving</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252287.jpg" data-speaker-id="252287">Urs Muller (NVIDIA)</span></div>
            <div class="en_popup_desc">Urs Muller presents the architecture and training methods used to build an autonomous road-following system. A key aspect of the approach is eliminating the need for hand-programmed rules and procedures such as finding lane markings, guardrails, or other cars, thereby avoiding the creation of a large number of “if, then, else” statements.</div>
        

</div>

</div>

<div id="slot52000_p" class="slot_popup">

<div id="sched54100" class="en_popup_content">

    <div class="en_popup_time">
        4:35pm-5:15pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">High-level APIs for scalable machine learning</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_245377.jpg" data-speaker-id="245377">Martin Wicke (Google)</span></div>
            <div class="en_popup_desc">TensorFlow is a system for scalable machine learning. However, using raw TensorFlow and profiling, optimizing, and debugging large-scale models can be daunting for novice and expert users alike. Martin Wicke explores new APIs based on TensorFlow that aim to make building complex models easier and allow users to scale quickly.</div>
        

</div>

</div>

<div id="slot51987_p" class="slot_popup">

<div id="sched53863" class="en_popup_content">

    <div class="en_popup_time">
        11:00am-11:40am (40m)
        Impact on business and society
        
    </div>

        
            <div class="en_popup_name">Only humans need apply: Adding value to the work of very smart machines</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_251535.jpg" data-speaker-id="251535">Tom Davenport (Babson College, MIT)</span></div>
            <div class="en_popup_desc">The automation of decisions and actions now threatens even knowledge-worker jobs. Tom Davenport describes both the threat of automation and the promise of augmentation—combining smart machines with smart people—and explores five roles that individuals can adopt to add value to AI, as well as what these roles mean for businesses.</div>
        

</div>

</div>

<div id="slot51988_p" class="slot_popup">

<div id="sched54094" class="en_popup_content">

    <div class="en_popup_time">
        11:50am-12:30pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">Practical AI product development</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_62617.jpg" data-speaker-id="62617">Hilary Mason (Fast Forward Labs)</span></div>
            <div class="en_popup_desc">Hilary Mason explores a framework for applied AI research, with a focus on algorithmic capabilities that are useful for building real-world products today. Drawing on real-world examples, Hilary outlines a system for thinking about which AI capabilities are ready to transition from pure research to applied products and how to make the transition from research paper to a working product.</div>
        

</div>

</div>

<div id="slot51993_p" class="slot_popup">

<div id="sched54494" class="en_popup_content">

    <div class="en_popup_time">
        1:30pm-2:10pm (40m)
        
        
    </div>

        
            <div class="en_popup_name">Transforming your industry with cognitive computing</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_254157.jpg" data-speaker-id="254157">Guruduth Banavar (Cognitive Computing, IBM)</span></div>
            <div class="en_popup_desc">In the last decade, the availability of massive amounts of new data, the development of new AI techniques, and the availability of scalable computing infrastructure have given rise to a new class of machine capabilities we call cognitive computing. Guruduth Banavar offers an overview of the technological breakthroughs that are enabling this trend.</div>
        

</div>

</div>

<div id="slot51996_p" class="slot_popup">

<div id="sched54881" class="en_popup_content">

    <div class="en_popup_time">
        2:20pm-3:00pm (40m)
        
        
    </div>

        
            <div class="en_popup_name">Benefits of scaling machine learning</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_187782.jpg" data-speaker-id="187782">Reza Zadeh (Stanford | Matroid)</span></div>
            <div class="en_popup_desc">Machine learning is evolving to utilize new hardware, such as GPUs and large commodity clusters. Reza Zadeh presents two projects that have benefitted greatly through scaling: obtaining leading results on the Princeton ModelNet object recognition task and matrix computations and optimization in Apache Spark.</div>
        

</div>

</div>

<div id="slot51999_p" class="slot_popup">

<div id="sched54067" class="en_popup_content">

    <div class="en_popup_time">
        3:45pm-4:25pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name"> Unlock the power of AI: A fundamentally different approach to building intelligent systems</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_236882.jpg" data-speaker-id="236882">Mark Hammond (Bonsai)</span></div>
            <div class="en_popup_desc">Mark Hammond explains how Bonsai’s platform enables every developer to add intelligence to their software or hardware, regardless of AI expertise. Bonsai’s suite of tools—a new programming language, AI engine, and cloud service—abstracts away the lowest-level details of programming AI, allowing developers to focus on concepts they want a system to learn and how those concepts can be taught.</div>
        

</div>

</div>

<div id="slot52001_p" class="slot_popup">

<div id="sched55538" class="en_popup_content">

    <div class="en_popup_time">
        4:35pm-5:15pm (40m)
        
        
    </div>

        
            <div class="en_popup_name">The need for speed: Benchmarking deep learning workloads</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263019.jpg" data-speaker-id="263019">Greg Diamos (Baidu)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263097.jpg" data-speaker-id="263097">Sharan Narang (Baidu)</span></div>
            <div class="en_popup_desc">Greg Diamos and Sharan Narang discuss the impact of AI on applications within Baidu, including autonomous driving and speech recognition, offering a brief introduction to the challenges in training deep learning algorithms as well as the different workloads that are used in various deep learning applications.</div>
        

</div>

</div>

<div id="slot52017_p" class="slot_popup">

<div id="sched54062" class="en_popup_content">

    <div class="en_popup_time">
        11:00am-11:40am (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">How to make robots empathetic to human feelings in real time</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252222.jpg" data-speaker-id="252222">Pascale Fung (The Hong Kong University of Science and Technology)</span></div>
            <div class="en_popup_desc">Pascale Fung describes an approach to enable an interactive dialogue system to recognize user emotion and sentiment in real time and explores CNN models that recognize emotion from raw speech input without feature engineering and sentiments. These modules allow otherwise conventional dialogue systems to have “empathy” and answer users while being aware of their emotion and intent.</div>
        

</div>

</div>

<div id="slot52018_p" class="slot_popup">

<div id="sched54101" class="en_popup_content">

    <div class="en_popup_time">
        11:50am-12:30pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">Building and applying emotion recognition</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252250.jpg" data-speaker-id="252250">Anna Roth (Microsoft)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_251905.jpg" data-speaker-id="251905">Cristian Canton (Microsoft Technology and Research)</span></div>
            <div class="en_popup_desc">Anna Roth and Cristian Canton walk you through building a system to recognize emotions by inferring them from facial expressions. Cristian and Anna explain how they trained their emotion recognition CNN from noisy data and how to approach labeling subjective data like emotion with crowdsourcing before showing a demo of this work in action, as it is exposed in Microsoft’s Emotion API.</div>
        

</div>

</div>

<div id="slot52019_p" class="slot_popup">

<div id="sched54174" class="en_popup_content">

    <div class="en_popup_time">
        1:30pm-2:10pm (40m)
        Interacting with AI
        
    </div>

        
            <div class="en_popup_name">Deeply active learning: Approximating human learning with smaller datasets combined with human assistance</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_169826.jpg" data-speaker-id="169826">Christopher Nguyen (Arimo)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252622.jpg" data-speaker-id="252622">Binh Han (Arimo)</span></div>
            <div class="en_popup_desc">Natural-language assistants are the emergent killer app for AI. Getting from here to there with deep learning, however, can require enormous datasets. Christopher Nguyen and Binh Han explain how to shorten the time to effectiveness and the amount of training data that's required to achieve a given level of performance using human-in-the-loop active learning.</div>
        

</div>

</div>

<div id="slot52020_p" class="slot_popup">

<div id="sched54021" class="en_popup_content">

    <div class="en_popup_time">
        2:20pm-3:00pm (40m)
        Interacting with AI
        
    </div>

        
            <div class="en_popup_name">Probabilistic programming for augmented intelligence</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_107139.jpg" data-speaker-id="107139">Vikash Mansinghka (MIT)</span>, <span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_3500.jpg" data-speaker-id="3500">Richard Tibbetts (MIT)</span></div>
            <div class="en_popup_desc">The next generation of AI systems will provide assisted intuition and judgment for everyday people trying to collaboratively solve hard problems. Vikash Mansinghka and Richard Tibbetts explore how AI will be used on problems like malnutrition, public health, education, and governance—complex, ambiguous areas of human knowledge where data is sparse and there are no rules.</div>
        

</div>

</div>

<div id="slot52021_p" class="slot_popup">

<div id="sched53930" class="en_popup_content">

    <div class="en_popup_time">
        3:45pm-4:25pm (40m)
        Impact on business and society
        
    </div>

        
            <div class="en_popup_name">The future of natural language generation, 2016–2026</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_126335.jpg" data-speaker-id="126335">Robbie Allen (Automated Insights, Inc.)</span></div>
            <div class="en_popup_desc">Natural language generation, the branch of AI that turns raw data into human-sounding narratives, is coming into its own in 2016. Robbie Allen explores the real-world advances in NLG over the past decade and then looks ahead to the next. Computers are already writing finance, sports, ecommerce, and business intelligence stories. Find out what—and how—they’ll be writing by 2026. </div>
        

</div>

</div>

<div id="slot52022_p" class="slot_popup">

<div id="sched54214" class="en_popup_content">

    <div class="en_popup_time">
        4:35pm-5:15pm (40m)
        Impact on business and society
        
    </div>

        
            <div class="en_popup_name">The new artificial intelligence frontier</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252949.jpg" data-speaker-id="252949">Babak Hodjat (Sentient Technologies)</span></div>
            <div class="en_popup_desc">Babak Hodjat discusses the progress in AI, diving into how AI can offer unique solutions in verticals such as investment, medical diagnosis, and ecommerce. Babak details how using massively scaled distributed evolutionary computation, mimicking biological evolution, allows an AI to learn, adapt, and react faster to provide customers with the answers and decisions they need.</div>
        

</div>

</div>

<div id="slot52362_p" class="slot_popup">

<div id="sched54963" class="en_popup_content">

    <div class="en_popup_time">
        11:00am-11:40am (40m)
        Sponsored
        
    </div>

        
            <div class="en_popup_name">AI on IA</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_135162.jpg" data-speaker-id="135162">Vin Sharma (Intel)</span></div>
            <div class="en_popup_desc">Vin Sharma explores how Intel is investing in artificial intelligence and using open source software platforms, frameworks, and libraries, as well as Intel's hardware to advance the future.</div>
        

</div>

</div>

<div id="slot52500_p" class="slot_popup">

<div id="sched54988" class="en_popup_content">

    <div class="en_popup_time">
        11:50am-12:30pm (40m)
        Sponsored
        
    </div>

        
            <div class="en_popup_name">Deploying AI-based services in the data center for real-time responsive experiences</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_259924.jpg" data-speaker-id="259924">Sanford Russell (NVIDIA)</span></div>
            <div class="en_popup_desc">In the new era of artificial intelligence, every organization must examine how to extract intelligence from its data using deep learning. Sanford Russell explores how NVIDIA GPUs are deployed today to accelerate deep learning inference workloads in the data center.</div>
        

</div>

</div>

<div id="slot52501_p" class="slot_popup">

<div id="sched55569" class="en_popup_content">

    <div class="en_popup_time">
        1:30pm-2:10pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">Growing up: Continuous integration for machine-learning models</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_263216.jpg" data-speaker-id="263216">Zachary  Hanif (Capital One)</span></div>
            <div class="en_popup_desc">Developing and validating frequently updated models is core to professional data science teams. Zachary Hanif discusses the adaptation of CI tools and practices to solve model governance and accuracy tracking concerns in a complex environment with adversarial and temporal data complications. </div>
        

</div>

</div>

<div id="slot52766_p" class="slot_popup">

<div id="sched53961" class="en_popup_content">

    <div class="en_popup_time">
        2:20pm-3:00pm (40m)
        Impact on business and society
        
    </div>

        
            <div class="en_popup_name">What I learned by replacing middle-class manufacturing jobs with ML and AI</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_155541.jpg" data-speaker-id="155541">Eduardo Arino de la Rubia (Domino Data Lab)</span></div>
            <div class="en_popup_desc">Manufacturing in the United States is facing extreme pressures from globalization. Eduardo Arino de la Rubia synthesizes what he learned working side by side with the workers he was replacing with AI and ML, discussing their struggles, how they saw the technology the would take their jobs, the limitations of the technology, and what his real impact was in the face of globalization.</div>
        

</div>

</div>

<div id="slot52704_p" class="slot_popup">

<div id="sched54081" class="en_popup_content">

    <div class="en_popup_time">
        3:45pm-4:25pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">Deep learning: Modular in theory, inflexible in practice</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252236.jpg" data-speaker-id="252236">Diogo Almeida (Enlitic)</span></div>
            <div class="en_popup_desc">The high-level view of deep learning is elegant: composing differentiable components together trained in an end-to-end fashion. The reality isn't that simple, and the commonly used tools greatly limit what we are capable of doing. Diogo Almeida explains what we can do about it and offers a practical attempt at a deep learning library of the future.</div>
        

</div>

</div>

<div id="slot52708_p" class="slot_popup">

<div id="sched54002" class="en_popup_content">

    <div class="en_popup_time">
        4:35pm-5:15pm (40m)
        Implementing AI
        
    </div>

        
            <div class="en_popup_name">A peek at x.ai’s data science architecture</div>
            <div class="en_popup_speakers"><span data-photo-url="http://cdn.oreillystatic.com/en/assets/1/eventprovider/1/_@user_252112.jpg" data-speaker-id="252112">Angela Zhou (x.ai)</span></div>
            <div class="en_popup_desc">In any human-machine interaction, you need a dialogue model: the machine must understand and be able to respond appropriately. Angela Zhou discusses x.ai's AI personal assistant, Amy Ingram, who schedules meetings for you, focusing on the way x.ai has approached both understanding and responding.

</div>

</div>

</div>

<div id="slot52244_p" class="slot_popup">

<div class="en_popup_content">

    <div class="en_popup_time">
        8:00am-9:00am (1h)
        
        
    </div>

        
            <div class="en_popup_name">Break: Morning coffee service Sponsored by Capital One
            </div>
            
        

</div>

</div>

<div id="slot51994_p" class="slot_popup">

<div class="en_popup_content">

    <div class="en_popup_time">
        10:30am-11:00am (30m)
        
        
    </div>

        
            <div class="en_popup_name">Break: Morning Break
            </div>
            
        

</div>

</div>

<div id="slot51989_p" class="slot_popup">

<div class="en_popup_content">

    <div class="en_popup_time">
        12:30pm-1:30pm (1h)
        
        
    </div>

        
            <div class="en_popup_name">Break: Lunch Sponsored by Intel
            </div>
            
        

</div>

</div>

<div id="slot51997_p" class="slot_popup">

<div class="en_popup_content">

    <div class="en_popup_time">
        3:00pm-3:45pm (45m)
        
        
    </div>

        
            <div class="en_popup_name">Break: Afternoon Break
            </div>
            
        

</div>

</div>

<div id="slot52073_p" class="slot_popup">

<div id="sched54650" class="en_popup_content">

    <div class="en_popup_time">
        5:15pm-6:15pm (1h)
        
        
    </div>

        
            <div class="en_popup_name">Attendee Reception</div>
            <div class="en_popup_speakers"></div>
            <div class="en_popup_desc">Come enjoy delicious snacks and beverages with fellow O'Reilly AI attendees, speakers, and sponsors. </div>
        

</div>

</div>

</div>

    </div>




    </div><!-- en_main -->

<style>#sponsors_contacts.row { border-top: 2px solid #cacaca; }</style>
<div id="sponsors_contacts" class="row">

<div id="sponsor_container">

<!--sponsors title image-->
<div class="spacer">

 

</div>

<div id="sponsors">

<div class="sponsor_list_heading">

Presented by

</div>

<ul class="plain sponsorList">
<li>
<a href="http://www.oreilly.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/oreilly_logo_box.png" alt="O'Reilly Media" width="120" height="33" border="0" /><span
class="lazy_placeholder">O'Reilly Media</span></a>
</li>
</ul>
<div class="sponsor_list_heading">

Elite Sponsors

</div>

<ul class="plain sponsorList">
<li>
<a href="http://www.intel.com/machinelearning" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/intel.png" alt="Intel" width="120" height="82" border="0" /><span
class="lazy_placeholder">Intel</span></a>
</li>
<li>
<a href="http://www.nvidia.com/deeplearning" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/nvidia-color.png" alt="NVIDIA" width="120" height="90" border="0" /><span
class="lazy_placeholder">NVIDIA</span></a>
</li>
</ul>
<div class="sponsor_list_heading">

Impact Sponsors

</div>

<ul class="plain sponsorList">
<li>
<a href="http://www.capitalone.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/capitalone.png" alt="Capital One" width="120" height="42" border="0" /><span
class="lazy_placeholder">Capital One</span></a>
</li>
<li>
<a href="http://www.sap.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/SAP.jpg" alt="SAP" width="120" height="59" border="0" /><span
class="lazy_placeholder">SAP</span></a>
</li>
</ul>
<div class="sponsor_list_heading">

Premier Exhibitors

</div>

<ul class="plain sponsorList">
<li>
<a href="http://www.bons.ai" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/bonsai.png" alt="Bonsai" width="120" height="32" border="0" /><span
class="lazy_placeholder">Bonsai</span></a>
</li>
<li>
<a href="http://www.crowdflower.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/crowdflower.png" alt="CrowdFlower" width="120" height="19" border="0" /><span
class="lazy_placeholder">CrowdFlower</span></a>
</li>
<li>
<a href="http://deepsense.io/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/deepsense-io.png" alt="deepsense.io" width="120" height="23" border="0" /><span
class="lazy_placeholder">deepsense.io</span></a>
</li>
<li>
<a href="http://www.h2o.ai" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/h2o-ai.png" alt="H2o.ai" width="100" height="100" border="0" /><span
class="lazy_placeholder">H2o.ai</span></a>
</li>
</ul>
<div class="sponsor_list_heading">

Community Partners

</div>

<ul class="plain sponsorList">
<li>
<a href="https://chatbotsmagazine.com/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/chatbots.png" alt="Chatbots Magazine" width="120" height="22" border="0" /><span
class="lazy_placeholder">Chatbots Magazine</span></a>
</li>
<li>
<a href="http://ctovision.com/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/ctovision.gif" alt="CTOvision.com" width="120" height="14" border="0" /><span
class="lazy_placeholder">CTOvision.com</span></a>
</li>
<li>
<a href="http://www.datanami.com/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/datanami.gif" alt="Datanami" width="120" height="52" border="0" /><span
class="lazy_placeholder">Datanami</span></a>
</li>
<li>
<a href="http://www.enterprisetech.com/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/enterprisetech.png" alt="EnterpriseTech " width="120" height="38" border="0" /><span
class="lazy_placeholder">EnterpriseTech </span></a>
</li>
<li>
<a href="http://homeai.info/" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/homeai.png" alt="homeAI.info" width="120" height="74" border="0" /><span
class="lazy_placeholder">homeAI.info</span></a>
</li>
<li>
<a href="http://www.kdnuggets.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/kdnuggets.png" alt="KDnuggets" width="120" height="44" border="0" /><span
class="lazy_placeholder">KDnuggets</span></a>
</li>
<li>
<a href="https://twimlai.com" target="_blank"><img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" class="lazy" data-img-src="//cdn.oreillystatic.com/conferences/images/logos/twiml.png" alt="This Week in Machine Learning & Artificial Intelligence" width="120" height="33" border="0" /><span
class="lazy_placeholder">This Week in Machine Learning & Artificial
Intelligence</span></a>
</li>
</ul>

</div>

<div class="content_row">

<div id="contacts" class="grid mobile-stack">

<div class="col-1-3">

<h3>
Sponsorship Opportunities
</h3>
<p>
For exhibition and sponsorship opportunities, email Nathaniel Coon at
<a href="mailto:ncoon@oreilly.com">ncoon@oreilly.com</a>
</p>

</div>

<div class="col-1-3">

<h3>
Partner Opportunities
</h3>
<p>
For information on trade opportunities with O'Reilly conferences, email
<a href="mailto:partners@oreilly.com">partners@oreilly.com</a>
</p>

</div>

<div class="col-1-3">

<h3>
Contact Us
</h3>
<p>
View a complete list of
<a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/contact">AI
contacts</a>
</p>

</div>

</div>

<!-- /contacts -->

</div>

<!--content_row-->

</div>

<!-- /#sponsor_container -->

</div>

<!--div#sponsors_contacts-->
            <footer>
                    <!-- system/theme/after_main -->
                    

<div class="content_row">

<div class="grid mobile-stack">

<div class="footercol col-1-5">

    <ul>
        <li><strong>Information</strong></li>
        <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/about">About</a></li>
        <li><a href="/artificial-intelligence/ai-deep-learning-bots-ny/public/content/contact">Contact Us</a></li>


        <li><a href="http://oreilly.com/conferences/diversity.html" target="_blank">Diversity</a></li>
        <li><a href="http://oreilly.com/conferences/code-of-conduct.html" target="_blank">Code of Conduct</a></li>
        <li><a href="http://oreilly.com/oreilly/privacy.html" target="_blank">Privacy Policy</a></li>
    </ul>

</div>

<div class="footercol col-1-5">

<ul>
<li>
<strong>More O'Reilly Events</strong>
</li>
<li>
<a href="http://oreillydesigncon.com" target="_blank">Design
Conference</a>
</li>
<li>
<a href="http://fluentconf.com" target="_blank">Fluent Conference</a>
</li>
<li>
<a href="http://conferences.oreilly.com/nextcon/economy-us/" target="_blank">Next:Economy</a>
</li>
<li>
<a href="http://oscon.com" target="_blank">OSCON</a>
</li>
<li>
<a href="http://oreillysecuritycon.com" target="_blank">Security
Conference</a>
</li>
<li>
<a href="http://softwarearchitecturecon.com" target="_blank">Software
Architecture</a>
</li>
<li>
<a href="http://strataconf.com/" target="_blank">Strata + Hadoop
World</a>
</li>
<li>
<a href="http://velocityconf.com/" target="_blank">Velocity
Conference</a>
</li>
</ul>

</div>

<div class="footercol col-1-5">

<ul>
<li>
<strong>More O'Reilly Sites</strong>
</li>
<li>
<a href="http://conferences.oreilly.com" target="_blank">O'Reilly
Conferences</a>
</li>
<li>
<a href="http://oreilly.com" target="_blank">oreilly.com</a>
</li>
<li>
<a href="http://radar.oreilly.com" target="_blank">O'Reilly Radar</a>
</li>
<li>
<a href="http://oreilly.com/videos/" target="_blank">O'Reilly Video</a>
</li>
<li>
<a href="http://oreilly.com/webcasts/" target="_blank">O'Reilly
Webcasts</a>
</li>
<li>
<a href="https://www.youtube.com/user/OreillyMedia" target="_blank">O'Reilly
on YouTube</a>
</li>
</ul>

</div>

<div class="footercol col-1-5">

<ul class="social">
<li>
<a href="https://twitter.com/oreillyai" target="_blank"><img src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/social_twitter.svg" alt="Twitter" width="32" height="32" border="0" />Twitter</a>
</li>
<li>
<a href="https://www.facebook.com/OReilly" target="_blank"><img src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/social_facebook.svg" alt="Facebook"  width="32" height="32" border="0" />Facebook</a>
</li>
<li>
<a href="https://www.youtube.com/user/OreillyMedia" target="_blank"><img src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/social_youtube.svg" alt="YouTube"  width="32" height="32" border="0" />YouTube</a>
</li>
</ul>

</div>

<div class="footercol col-1-5">

<ul class="social">
<li>
<a href="https://plus.google.com/+oreillymedia/posts" target="_blank"><img src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/social_google_plus.svg" alt="Google+"  width="32" height="32" border="0" />Google+</a>
</li>
<li>
<a href="https://www.linkedin.com/company/8459" target="_blank"><img src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/social_linkedin.svg" alt="LinkedIn"  width="32" height="32" border="0" />LinkedIn</a>
</li>
</ul>

</div>

</div>

<!--grid-->

</div>

<!--content_row-->
            </footer>
       <div id="copyright">

<div class="content_row">

<p>
©2016, O'Reilly Media, Inc.  •  (800) 889-8969 or (707) 827-7019  • 
Monday-Friday 7:30am-5pm PT  •  All trademarks and registered trademarks
appearing on oreilly.com are the property of their respective owners. 
• \
<a href="mailto:conf-webmaster@oreilly.com" class="webmaster">conf-webmaster@oreilly.com</a>
</p>

</div>

</div>
<!--div#copyright-->
        </div><!-- div#en_body -->
    </div><!-- en_main_parts -->

</div>
<!-- en_content -->
<script src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/lazyload_min_v3.js"></script>
<script>
//debounce function
function debounce(a,b,c){var d;return function(){var e=this,f=arguments;clearTimeout(d),d=setTimeout(function(){d=null,c||a.apply(e,f)},b),c&&!d&&a.apply(e,f)}}

$(function(){
/* make links with class=external open up external */
           $("a.external").click(function (e) {
              e.preventDefault();
              window.open($(this).attr("href"));
           });

         

var viewport_width = Math.max( $(window).width(), window.innerWidth);

   

       



  










/* for responsive nav */    
         var pull = $('#pull'),
           menu = $('nav ul'),
               docHeight = $(document).height(),
           menuHeight = menu.height(),
               regButton = $('#reg_button');
               nav_overlay = $('#nav_overlay');
            $(pull).on('click', function(e) {
                e.preventDefault();
                menu.toggle();
                regButton.toggleClass('hide');
                nav_overlay.toggleClass('hide');
                docHeight = $(document).height();
                nav_overlay.css('height', docHeight);
                return false;
            });
    
    //resize functions
    var runUniversalFunctions = debounce(function() {
        var w = Math.max( $(window).width(), window.innerWidth);
        if(w > 320 && menu.is(':hidden')) {
            menu.removeAttr('style');                               
        } 
        
       if(w > 680) {  
                regButton.addClass('hide'); 
                nav_overlay.addClass('hide'); 
               
        } else {
                if($('nav ul.clearfix').is(':hidden') === false) { 
                   regButton.removeClass('hide'); 
                   nav_overlay.removeClass('hide'); 
                } else {
                   //$('nav ul.clearfix').addClass('hide');
                }
        }   
    }, 250);  
    window.addEventListener('resize', runUniversalFunctions);
  
    
    
});//function wrapper
      
</script>
<style>
#en_grid_dates #list_grid a { color:#999; }
#dates_select { display: none; }
#topic_select { display: none; }
#type_select { display: none; }
.session_name { font-weight: bold; }
.en_speakers {font-style: italic; }

.en_session {font-size: 15px; border-bottom: 1px solid #ccc; padding: 15px 0; }

h2 { margin-bottom: 0; }
div.list_header { display: none; max-width: 910px; width: 100%; margin: 0 auto; }
.hide { display: none; }
div#en_grid_topic_key #mobile-filter-header { display: none; }

@media only screen and (max-width: 985px) {
  div#en_grid_dates #dates_select, div#tag_key #tag_select, div#grid_track_key #type_select { display: block; }
   #topic_select { display: block; }
   #list_grid, #customize-schedule { display: none; }
  div#en_grid_container { display: none; }
  div.en_session { display: block !important; }
  div#en_grid_dates ul { display: none; }
  div#en_grid_dates { display: inline-block; }
  div#en_grid_topic_key { display: block; max-width: 910px; padding: 20px; }
  div#grid_track_key { max-width: 910px; padding: 0 20px; width: 100%; }
  div#en_grid_topic_key li, #tags { display: none; }
  div#en_grid_topic_key .closed, div#en_grid_topic_key .open { display: none; }
  div#en_grid_topic_key #mobile-filter-header { display: block; margin-bottom: 0.4rem; }
  div#grid_type_key div { display: none; }
  div.list_header { display: block !important; }
  #grid_track_key div li { display: none; }
  #topic-links { display: none; }
}

@media only screen and (max-width: 930px) {
  div#above-topics-grid { padding: 0 20px; max-width: 910px; }
}

@media only screen and (max-width: 502px) {
    #en_grid_topic_key { display: inline-block; width: 200px; margin-left: 0;}
}
@media only screen and (max-width: 450px) {
    .en_description, .en_speakers img { display: none; }
}
</style>
<script>

  var isListView = false;

$(function() {
  populateSelect($("#grid_track_key div li a"), "grid_track_key", "type_select", "Select a type");
  populateSelect($("#en_grid_dates ul a"), "en_grid_dates", "dates_select", "");
  populateSelect($("#en_grid_topic_key div li a"), "en_grid_topic_key", "topic_select", "Select a topic");
  //populateSelect($("#tags li a"), "tag_key", "tag_select", "Select a subtopic");
  $('#dates_select').append('<option value="/ai-deep-learning-bots-ny/public/schedule/personal">Personal schedule</option>');

  $.each($('#dates_select option'), function () {
    if ($(this).data('date') === $('#current_day').data('date')) {
      $(this).prop("selected", true);
    }
  });

   $('#dates_select, #topic_select, #tag_select, #type_select').bind('change', function () {
          var url = $(this).val(); // get selected value
          if (url) { // require a URL
              window.location = url; // redirect
          }
          return false;
  });

  $('.list, .sched_grid').on('click', function(e) {
    e.preventDefault();
    if ($(this).text() === $('.list').text()) {
     $("#en_grid_container").addClass("hide");
     $(".en_session").removeClass("hide");
      isListView = true;
      addDayLinkParam("view", 'list');
    } else {
      $("#en_grid_container").removeClass("hide")
      $(".en_session").addClass("hide");
      isListView = false;
      addDayLinkParam("view", 'grid');
    }
    $(this).addClass('active');
    $(this).siblings().first().removeClass('active').addClass('inactive');
    filter();
  });

var slot_listings = [];
  $('.slot_popup .en_popup_content').each(function(index, slot) {
    slot_listings.push(buildSlotObject(slot));
  });

var chron_slot_listings = putInChronOrder(slot_listings);

chron_slot_listings.forEach(function(session) {
if(session.proposal_description !== "To be confirmed") {

  $('#en_main').append('<div class="en_session en_clearfix">' + '<div class="session_name">' + buildSessionLink(session.proposal_id, session.proposal_name) + '</div><div class="session_time_room">' + session.time_block + ' ' + session.room_name + '</div><div class="topics">' + session.topics + '</div><div class="en_speakers">' + buildSpeakerList(session.speakers) + '</div><div class="en_description">' + session.proposal_description + '</div></div>');

}
});

$('.en_speakers img').each(function() {
  if ($(this).length > 2) {
    $(this).next().css({'display': 'block', 'clear' : 'both'}); }  });

function buildSlotObject(slot) {
  var slot_id = getSlotId(slot);
  var slot_info = getSlotData(slot_id);
  return {
    "id" : slot_id,
    "proposal_id" : getProposalId(slot),
    "proposal_name" : getProposalName(slot),
    "speakers" : getSpeakers(slot),
    "topics" : getRoomOrTopics(slot_info, "topic", "topic_key"),
    "room_name" : getRoomOrTopics(slot_info, "room", "room_title"),
    "start_time" : get24HourTime(getProposalTimeBlock(slot, 1)),
    "time_block" : getProposalTimeBlock(slot, 0),
    "proposal_description" : getDescription(slot)
  };
}

function buildSpeakerList(speakers) {
  var speaker_photos = "";
  var speaker_list = [];

  $(speakers).each(function(index, speaker) {
    if ($(speaker).html() !== "") {
      var speaker_id = $(speaker).data('speakerId');
      if ($(speaker).data('photoUrl') !== "" && $(speaker).data('photoUrl') !== undefined && $(speaker).data('photoUrl') !== "undefined") {
        var photo_url = $(speaker).data('photoUrl').replace('dev.assets.en.oreilly.com', 'cdn.oreillystatic.com/en/assets');
        speaker_photos += '<img src="//cdn.oreillystatic.com/oreilly/images/transparent-1px.png" data-img-src="' + photo_url +'" alt="" class="lazy" width="75" height="100" style="float:left;margin:0 10px 10px 0;" />';
      }
      var affiliation = ($(speaker).data('affiliation') !== "undefined" && $(speaker).data('affiliation') !== undefined) ? '(' + $(speaker).data('affiliation') + ')' : "";
      speaker_list.push('<a href="/ai-deep-learning-bots-ny/public/schedule/speaker/' + $(speaker).data('speakerId') + '">' + $(speaker).text() +'</a> ' + affiliation);
    }

  });

  return (speaker_list.length) ? speaker_photos + speaker_list.join(", ") : "";
}

function putInChronOrder(slot_listings) {
  return slot_listings.sort(function(a, b) {
    if (a.start_time > b.start_time) {
      return 1;
    } else if (a.start_time < b.start_time) {
      return -1;
    }
    return 0;
  });

}

function getSlotId(slot) {
  return $(slot).parent().attr('id').substr(0, $(slot).parent().attr('id').length-2);
}

function getSpeakers(slot) {
  var speakers = $(slot).find(".en_popup_speakers span");
  return (speakers !== null) ? speakers : "";
}

function getSlotData(slot_id) {
  return $('#' + slot_id).attr('class').split(' ');
}

function getProposalId(slot) {
  var psched_id = $(slot).attr("id");
  return (typeof(psched_id) !== "undefined") ? psched_id.replace("sched", "") : 0;
}

function getProposalName(slot) {
  return $(slot).find($('.en_popup_name')).text();
}

function getProposalTimeBlock(slot, get_start_time) {
  var time_contents = getPopupTimeContents(slot);
  var timestring = "";
  
     timestring = (get_start_time) ? /^\d+:\d+(a|p)m/g : /\d+:\d+(a|p)m-\d+:\d+(a|p)m/g;
  
   return time_contents.match(timestring)[0];
}

function getPopupTimeContents(slot) {
  return $(slot).find($('.en_popup_time')).text().trim();
}

function get24HourTime(slot_time) {
  
  var hour_string = /^\d+/g;
  var minute_string = /\d+(?=a|p)/g;
  var ampm_string = /(a|p)m/g;
  var slot_hour = Number(slot_time.match(hour_string)[0]);
  var minutes = slot_time.match(minute_string)[0];
  var ampm = slot_time.match(ampm_string)[0];

  if (ampm === "pm" && slot_hour < 12) {
    slot_hour += 12;
  } else if (ampm === "am" && slot_hour < 10) {
    slot_hour = "0" + slot_hour;
  }
  slot_time = slot_hour + ":" + minutes;
  
  return slot_time;
}

function getDescription(slot) {
  return $(slot).find($('.en_popup_desc')).text();
}

function getRoomOrTopics(slot_info, search_type, prepend_info) {//topic, room / topic_key, room_title
  var slot_data = [];
  var slot_text = [];
  $.each(slot_info, function(index, info) {
    if (info.indexOf(search_type) !== -1) {
      slot_data.push(slot_info[index].replace(search_type, ""));
    }
  });
  $.each(slot_data, function(index, value_id) {
    if (search_type == "topic") {
      slot_text.push('<a href="/ai-deep-learning-bots-ny/public/schedule/topic/' + value_id +'">' + $('#' + prepend_info + '_' + value_id).text() + '</a>');
    } else {
      slot_text.push($('#' + prepend_info + '_' + value_id).text());
    }
  });
  return (slot_text.length === 1) ? slot_text[0] : slot_text.join(", ");
}

function addPersonalScheduler (proposal_id, proposal_name) {
  return (proposal_id) ? '<div class="en_session_psched" id="psched' + proposal_id + '" style="float: right;"><a href="/ai-deep-learning-bots-ny/public/schedule/add/' + proposal_id + '" class="en_psched_add" title="Add ' + proposal_name + ' to your personal schedule"><img src="/images/personal-schedule-icon.png" width="17" height="18" alt="Add ' + proposal_name + ' to your personal schedule"></a></div>' : '';
}

function populateSelect(options, parent_id, select_id, default_text){
  $("#"+parent_id).append('<select id="' + select_id + '"></select>');
  if (select_id !== "dates_select") {
    $("#"+select_id).append("<option>" + default_text + "</option>");
  }
    $.each(options, function(key, value) {
     $("#"+select_id)
         .append($("<option></option>")
         .attr("value",$(value).attr("href"))
         .attr("data-date", $(value).data('date'))
         .text($(value).text()));
    });
}

});

function changeDisplay(selector, display_value) {
  selector.css('display', display_value);
}//changeDisplay()

function buildSessionLink(proposal_id, proposal_name) {
  return (proposal_id !== 0 && proposal_id !== "") ? '<a href="/ai-deep-learning-bots-ny/public/schedule/detail/' + proposal_id + '">' + proposal_name + '</a>' : proposal_name;
}//buildSessionLink()

//Adds url param to all day button links
function addDayLinkParam(paramName, paramValue) {
      $("#en_grid_dates ul a").each(function() {
         $(this).attr("href", removeDayLinkParam($(this).attr("href"))+"?"+paramName+"="+paramValue);
       });
}

//Strips out all url parameters
function removeDayLinkParam(url) {
  return url.split("?")[0];
}

  
     addDayLinkParam("view", 'list');
     $("#en_grid_container").addClass("hide");
     $('.list').addClass('active');
     $('.sched_grid').removeClass('active').addClass('inactive');
     isListView = true;
   

</script>
<style>
.filter_color { background-color: #d0e2f8 !important; }
.filter_color_click { background-color: #d0e2f8 !important; }
.hide { display: none !important; }
div#slot_grid div[class*="topic"] { background-color: #f4f4f4; }
#slot_grid div.slot:not(.not_session) { background-color: #f4f4f4; }
#slot_grid #slot20815, #slot_grid #slot20860 { background-color: #ded; }
#slot_grid #slot20785, #slot_grid #slot20540, #slot_grid #slot20824 { background-color: #b6c2aa; }

div.slot_active { background-color: #ddd !important; }
div.slot_active.filter_color_click { background-color: #c5dcf7 !important; }
div.slot_active_filtered { background-color: #A7C1E2 !important; }
</style>
<script>

/////////////////////////////////////////
//
// Grid Filtering
// 
////////////////////////////////////////
var topics;

$(document).ready(function(){
    topics = $("#en_grid_topic_key div li");

    topics.on('mouseenter', function(){
      fillTopicButtonHover($(this));
    });

    topics.on('mouseleave', function(){
      unFillTopicButtonHover($(this));
    });

    topics.on('click', function(e){
      e.preventDefault();
      if($(this).hasClass("filter_color_topic")) {
        unFillTopicButtonClick($(this));
      } else {
        fillTopicButtonClick($(this));
      }
      filter();
    });
});

/////////////////////////////////////////
//
// filter()
// Called each time a topic is clicked or hovered
//
////////////////////////////////////////

function filter() {

    //Get all of the selected topic buttons
    var selectedTopics = $("#en_grid_topic_key div li.filter_color_topic");

    //Get the topic name from each list item
    var selected_list_items = $(".en_session .topics a");

    //Check if any topics are selected
    if(selectedTopics.length != 0) {

      //Initialize empty array that will hold the list view items to show
      var viewsToShow = [];

      //Loop through each selected topic button
      $.each(selectedTopics, function( key, value ) {
            //Populate viewsToShow
            populateViewsToShow(selected_list_items, getTopicName(value), viewsToShow);
          });

      //Remove all filters in grid and list view
      removeAllFilters();

      //Check if the Grid or Listview is visible
      if(isListView) {
        //List view is visible
        showFilteredList(viewsToShow)
      } else {
        //Grid view is visible
        showFilteredGrid(selectedTopics)
      }
    } else {
      //No topics are selected so hide all grid filtering and show all list view items
      resetGridAndList(isListView);
    }
}

//////////////////////////////////////////////////////////////////////////
//
// populateViewsToShow(selectedListItems, selected_topic, viewsToShow)
// Function determines if a list item belongs in the viewsToShow array
// @Param selectedListItems - List of all topics 
// @Param selected_topic - Current topic
// @Param viewsToShow - The array of viewsToShow
//
//////////////////////////////////////////////////////////////////////////

function populateViewsToShow(selectedListItems, selected_topic, viewsToShow) {
  //Loop through all list items
  $.each(selectedListItems, function( key, value ) {
      //If the name of the selected topic button equals the topic found on the list view item,
      //push the list view item into viewsToShow
      if(selected_topic.trim() === $(value).text().trim()) {
         viewsToShow.push($(value).parents(".en_session"))
      }
  });
}

//////////////////////////////////////////////////
//
// showFilteredList(viewsToShow)
// @Param viewsTopShow - The array of views to show
// Shows all list items in the viewsToShow array
//
//////////////////////////////////////////////////

function showFilteredList(viewsToShow) {
  $.each(viewsToShow, function( key, value ) {
     $(this).css("display", 'block');
  });
}

/////////////////////////////////////////////////////////////////////
//
// showFilteredGrid(selectedTopics)
// @Param selectedTopics - The currently highlighted topics
// Highlights all slots who's topic is contained in selectedTopics
//
/////////////////////////////////////////////////////////////////////

function showFilteredGrid(selectedTopics){
  $.each(selectedTopics, function( key, value ) {
     addFilter(getTopicId($(this)));
  });
}

///////////////////////
//
// Utility Functions
//
///////////////////////

function getTopicId(topic) {
       return $(topic).attr("id").replace( /^\D+/g, '');
}

function getTopicName(topic) {
       return $(topic).find("a").text();
}

function fillTopicButtonHover(topic) {
   $(topic).addClass("filter_color_topic_hover");
   $("#slot_grid .topic"+getTopicId(topic)).addClass("filter_color");
}

function unFillTopicButtonHover(topic) {
   $(topic).removeClass("filter_color_topic_hover");
   $("#slot_grid .topic"+getTopicId(topic)).removeClass("filter_color");
}

function fillTopicButtonClick(topic) {
   $(topic).addClass("filter_color_topic");
}

function unFillTopicButtonClick(topic) {
   $(topic).removeClass("filter_color_topic");
}

function removeAllFilters() {
    $(".en_session").css("display", 'none');
    $("div#slot_grid div[class*='topic']").removeClass("filter_color");
    $("div#slot_grid div[class*='topic']").removeClass("filter_color_click");
}

function resetGridAndList(isListView) {
        $(".en_session").css("display", 'block');
        $("#slot_grid div").removeClass("filter_color");
        $("#slot_grid div").removeClass("filter_color_click");
        if(!isListView) {
              $(".en_session").css("display", 'none');
        }
}

function addFilter(topicId) {
   $("#slot_grid .topic"+topicId).addClass("filter_color_click");
}

function removeFilter(topicId) {
   $("#slot_grid .topic"+topicId).removeClass("filter_color_click");
}

function toggleFilter(topicId) {
   $("#slot_grid .topic"+topicId).toggleClass("filter_color");
}

//Listener for displaying slot popups on the loaded grid
$(document).on("mouseenter", "div#slot_grid .slot", function(e) {
    if($(this).hasClass("filter_color")) {
       $(this).addClass("slot_active_filtered")
    } else {
       $(this).addClass("slot_active")
    }
});

//Listener for hiding slot popups on the loaded grid
$(document).on("mouseleave", "div#slot_grid .slot", function(e) {
  var pid = "#"+$(this).attr("id")+"_p";
 $('body').unbind('mousemove', update);
 $('#en_gridpop').remove();

    if($(this).hasClass("filter_color")) {
       $(this).removeClass("slot_active_filtered")
    } else {
        $(this).removeClass("slot_active");
    }

});

</script>
<style>
.day_header {display: inline-block; position: absolute; width: 100%; top: -40px; background-color: #d3002d; text-align: center; height: 40px; line-height: 36px; color:white; }
.day_header h4 { display: block; margin: 0 auto; }
.closed::before { content: "+"; cursor: pointer; display: inline-block; color: #fff; background: #444; border-radius: 2px; padding: 1px 5px 2px; margin-right: 5px; }
.open::before { content: "\2013"; cursor: pointer; display: inline-block; color: #fff; background: #444; border-radius: 2px; padding: 1px 5px 2px; margin-right: 5px; }
</style>
<script src="//cdn.oreillystatic.com/en/assets/1/eventprovider/1/accordion.js"></script>
<script>

var day = 26;
var grid = $("#slot_grid");

$("#en_grid_topic_key h3").text("Filter by topic")

addAmpersands();

if(day == 26) {
  //grid.prepend(createHeader("Included in Gold & Silver passes"));
}

if(day == 27) {
  //grid.prepend(createHeader("Included in Gold & Silver passes"));
}

function createHeader(title) {
  return '<div class="day_header"><h4>'+ title +'</h4></div>'
}

function addAmpersands() {
  $("#en_grid_topic_key div li a").each(function(){ $(this).text($(this).text().replace("and", '&')) });
  $(".en_session .topics a:contains('and')").each(function(){
      $(this).text($(this).text().replace("and", '&'));
  });
}

function removeTopic(topic) {
  topic.remove();
}

function updateKeynoteToComeLinks(slot, url) {
  slot.find(".summary a:contains('Keynotes')").attr("href", url);
}

function disableKeynoteLinks(slot) {
slot.find(".summary a:contains('Keynotes')").each(function(){
     $(this).click(function(e) {
         e.preventDefault();
     });
     $(this).css({ "color": "#000", "text-decoration": "none", "cursor": "default" });
});
}


//remove popup for keynote umbrella slot
//$('div#slot20525').unbind('mouseenter');
</script>
<script>
   $('.slot').has('acronym[title="To be confirmed"]').css('display','none');
</script>
<script>
//change Optimized Business Day topic link so it goes to article instead of topic page
$('#topic_key_1395 a').attr('href', '/devops-web-performance-2015/public/content/optimized-business-day');
var tags = [];
var unique_tags = [];
var unique_tag_names = [];
$('#en_grid_topic_key').after('<div id="tag_key"><ul id="tags"></ul></div>');
var tags_parent = $('#tags');

$('.summary').each(function() {
    if ($(this).data('tags') !== "") {
        var tag_data = $(this).data('tags').split(',');
        $.each(tag_data, function(i) { 
          tag_data[i] = this.split(':');
        });
        tags.push(tag_data);
    }
});

$.each(tags, function(i, tag) {
    $.each(tag, function(j, tag_value) {
        if($.inArray(tag_value[0], unique_tags) === -1) {
            unique_tags.push(tag_value[0]);
            unique_tag_names.push(tag_value[1]);
        } 
    });
}); 

$.each(unique_tag_names, function(i, unique_tag_name){
    tags_parent.append('<li><a href="/ai-deep-learning-bots-ny/public/schedule/tag/'+ unique_tags[i] +'">' + unique_tag_name + '</a></li>');
});
</script>
<script language="javascript" type="text/javascript">
<!--
    // Initialize Banners
    $( function () {
             if ($('div.banners').length) {
              $( ".banners" ).each( function ( i, e ) {
                      var banners = new Array();
                      $( e ).find( 'img' ).each( function( i0, e0 ) {
                              banners.push( $( e0 ) );
                          });
                      
                      var b = banners[ Math.floor( Math.random() * banners.length ) ];
                     b.attr( 'class', 'lazy' );
                     b.css('height', 'auto');
                      
                  });
               $('.banners > a > img').each(function() {           
                  if ($(this).height() === 0) {
            $(this).parent().css('display', 'none');
              }
                });
             }//endif
        });
//-->
</script>
<!-- site catalyst -->
<!--Schedule -->
<script language="JavaScript" type="text/javascript">
<!--
var localScAcct = "orainy"; 
//!-->
</script>
<script language="JavaScript" type="text/javascript">
<!--//
 /* Specify the Report Suite ID(s) to track here */ 
/* localScAcct is specified in content/scripts/sitecatalyst_cfg */
//var globalScAcct = "ororeillyglobaldev";
var globalScAcct = "orglobal";

var s_account = localScAcct + "," + globalScAcct;
/*s_code.js must be called via the current protocol to avoid mixed content warnings */
var s_code_protocol;
var s_code_url = "cdn.oreillystatic.com/assets/js/s_code.js";
if (window.location.protocol == "https:"){
document.write('<script id="s_code_script" type="text/javascript" src="https://' + 'cdn.oreillystatic.com/assets/js/s_code.js' + '"><' + '/script>');
}else{
document.write('<script id="s_code_script" type="text/javascript" src="http://' + 'cdn.oreillystatic.com/assets/js/s_code.js' + '"><' +'/script>');
}
//!-->
</script>
<script language="JavaScript" type="text/javascript">
<!--
var myChannel, myPageName, myTitle, mySeries, myEvent, myEventTitle, mySection, mySection2, mySection3, myLoggedStatus,myEventPhase,localScAcct,myPubDate,mySystemPageType;

if(typeof(myTitleAppend) == 'undefined')
var myTitleAppend = "";
else myTitleAppend = ": " + myTitleAppend;

myChannel = "confs";

myTitle       = "schedule" + myTitleAppend;


mySection   = new Array(myChannel);
mySeries = "artificial-intelligence";

mySection.push(mySeries);
mySection2 = mySection.slice(); 



var myEventStartDate = new Date ("September 26, 2016");
var today            = new Date();
if (today > myEventStartDate){
     myEventPhase = "post-conference";
}
 myPubDate = "09/26/2016"; 
myEventTitle = "Artificial Intelligence 2016";

myEvent      = "orainy2016"
mySection2.push(myEvent)

mySection3 = mySection2.slice(); 
mySystemPageType = "schedule";


mySection3.push(mySystemPageType)
myPageName   = myChannel + ":" + myEvent + " " + myTitle;
mySection    = mySection.join(":");
mySection2   = mySection2.join(":");
mySection3   = mySection3.join(":");

myLoggedStatus = "logged out";

/* You may give each page an identifying name, server, and channel on
the next lines..... */
s.pageName = myPageName.toLowerCase(); 
//s.server   = ""; OK TO DELETE THIS LINE?
s.channel  = myChannel;
//s.pageType = "";OK TO DELETE THIS LINE?
s.prop1  = mySection;
s.prop2  = mySection2;
s.prop3  = mySection3;
s.prop4  = mySystemPageType; //not using this currently
s.prop5  = myTitle;
s.prop7  = myPubDate;
s.prop15 = s.eVar24 = myLoggedStatus;
/*s.prop29 = myEventPhase;*/ //this has more work to do.
s.prop38 = myEventTitle;

/* Conversion Variables */
s.campaign="";
s.state="";
s.zip="";
s.events="";  // need way to distinguish amongst these
s.products="";     // only put products on for purchases.
s.purchaseID="";
s.eVar1="";
s.eVar2="";
s.eVar3="";
s.eVar4="";
s.eVar5="";

/************* DO NOT ALTER ANYTHING BELOW THIS LINE ! **************/
var s_code=s.t();if(s_code)document.write(s_code)//--></script>
<script language="JavaScript" type="text/javascript"><!--
if(navigator.appVersion.indexOf('MSIE')>=0)document.write(unescape('%3C')+'\!-'+'-')
//--></script>
<noscript>
<a href="http://www.omniture.com" title="Web Analytics"><img
src="http://ororeillyglobaldev.122.2O7.net/b/ss/ororeillyglobaldev/1/H.20.2--NS/0"
height="1" width="1" border="0" alt="" /></a>
</noscript>
<!--/DO NOT REMOVE/-->
<!-- End SiteCatalyst code version: H.20.2. -->
<!-- crazy egg heatmap -->
<script type="text/javascript">
setTimeout(function(){var a=document.createElement("script"); var b=document.getElementsByTagName('script')[0]; a.src=document.location.protocol+"//dnn506yrbagrg.cloudfront.net/pages/scripts/0011/6381.js?"+Math.floor(new Date().getTime()/3600000); a.async=true;a.type="text/javascript";b.parentNode.insertBefore(a,b)}, 1);
</script>
<!-- VE Interactive -->
<div class="remarketing">

<script type="text/javascript">
!function(){var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.src="//configusa.veinteractive.com/tags/493E3498/F965/4860/8BDA/402A36B3B53F/tag.js";var b=document.getElementsByTagName("head")[0];if(b)b.appendChild(a,b);else{var b=document.getElementsByTagName("script")[0];b.parentNode.insertBefore(a,b)}}();
</script>

</div>

<!-- js/chartbeat_footer -->
<script type="text/javascript">
    var _sf_async_config={uid:1632,domain:"conferences.oreilly.com"};
    (function(){
        function loadChartbeat() {
            window._sf_endpt=(new Date()).getTime();
            var e = document.createElement('script');
            e.setAttribute('language', 'javascript');
            e.setAttribute('type', 'text/javascript');
            e.setAttribute('src',
            (("https:" == document.location.protocol) ? "https://a248.e.akamai.net/chartbeat.download.akamai.com/102508/" : "http://static.chartbeat.com/") +
            "js/chartbeat.js");
            document.body.appendChild(e);
        }
        
        var oldonload = window.onload;
        window.onload = (typeof window.onload != 'function') ?
        loadChartbeat : function() { oldonload(); loadChartbeat(); };
    })();
</script>
<div class="remarketing">

<script type="text/javascript">
    window._rtbms = window._rtbms || [];
    window._rtbms.push({"id": "4E7077F0"});
    (function(r, s) {
        r = document.createElement('script'); r.type = 'text/javascript'; r.async = true;
        
        r.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'track.rtb-media.me/rtbm.js';
        
        s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(r, s);
    })();
</script>
<noscript>
<img style="display:none;" src="//track.rtb-media.me/pixel4E7077F0.gif"/>
</noscript>

</div>

</body>
</html>
