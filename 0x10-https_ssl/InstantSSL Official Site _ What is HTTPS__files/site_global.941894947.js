$(function(){function e(i){i?(c.addClass("active").fadeIn(150),$("input[name=q]",l).focus(),setTimeout(function(){l.on("clickout",function(){e(!1)})},500)):(c.removeClass("active").fadeOut(150),l.off("clickout"))}var i=$("html"),t=$(".main-nav-brands");$("li[data-toggle=dropdown]",t).hover(function(){var e=$(this);e.addClass("hover").find(".dropdown-menu").show()},function(){var e=$(this);e.find(".dropdown-menu").hide(),setTimeout(function(){e.removeClass("hover")},100)}),$("#utility-nav-cart").hover(function(){var e=$(this);e.hasClass("full")&&!i.hasClass("active-mobile-nav")&&e.addClass("hover").find(".cart-dropdown").show()},function(){var e=$(this);e.find(".cart-dropdown").hide(),setTimeout(function(){e.removeClass("hover")},100)});var a=$(".mobile-nav"),s=$("#toggle-mobile-nav");$("li.has-sub-menu",a).addClass("collapsed").find("ul.sub-menu").hide(),s.click(function(e){e.preventDefault(),$(this).hasClass("is-active")?($(this).removeClass("is-active"),i.removeClass("active-mobile-nav"),$("a",a).attr("tabindex","-1")):($(this).addClass("is-active"),i.addClass("active-mobile-nav"),$("a",a).attr("tabindex","0"))}),$("a[data-toggle]",a).click(function(e){e.preventDefault();var i=$(this).parent("li");i.hasClass("collapsed")?i.removeClass("collapsed").find("ul.sub-menu").slideDown(150):i.addClass("collapsed").find("ul.sub-menu").slideUp(150)});var o=$(".sectigo-mobile-nav"),n=$("#toggle-sectigo-mobile-nav");n.click(function(e){e.preventDefault(),$(this).hasClass("is-active")?($(this).removeClass("is-active"),o.slideUp(150)):($(this).addClass("is-active"),o.slideDown(150))}),$(".main-item button",o).click(function(e){e.preventDefault();var i=$(this).attr("data-target"),t=$("ul.sub-"+i,o);$(this).hasClass("is-active")?($(this).removeClass("is-active"),t.slideUp(150)):($(this).addClass("is-active"),t.slideDown(150))}),$siteSearch=$("form.site-header__search"),$siteSearchField=$("input",$siteSearch),$("button",$siteSearch).click(function(e){if(e.preventDefault(),$siteSearch.hasClass("active")){var i=$siteSearchField.val();""!==i&&$siteSearch.submit()}else $siteSearch.addClass("active"),$siteSearchField.focus()}),$(document).mouseup(function(e){$siteSearch.is(e.target)||0!==$siteSearch.has(e.target).length||$siteSearch.removeClass("active")});var c=$(".search-overlay"),l=$("form",c);$(".show-mobile-search").click(function(i){i.preventDefault(),e(!0)}),$(".close-mobile-search").click(function(i){e(!1)}),$(document).keyup(function(i){27===i.keyCode&&c.hasClass("active")&&e(!1)}),$('a[href="#chat"]').click(function(e){e.preventDefault(),window.Helpdotcom.chat.maximize()}),$(".close-cookies-notice").click(function(e){e.preventDefault(),$(".cookie-notice").hide()}),$(".accept-cookies").click(function(e){e.preventDefault(),$(".cookie-notice").hide(),$.ajax({url:"/actions/site-module/site/accept-cookies",cache:!1,type:"GET"})}),$(".utility-nav li.utility-dropdown").hover(function(){$(this).find(".utility-dropdown-options").fadeIn(50)},function(){$(this).find(".utility-dropdown-options").fadeOut(50)}),$(".ssl-mobile-js").on("click",function(){console.log("1"),$(".ssl-mobile-nav").toggleClass("ssl-mobile-nav--open")})});