(function($){
	$.fn.jsorder = function(setting){
		//Initialize setting
		var opts = $.extend({}, $.fn.jsorder.defaults, setting);
		//read cookie
		var initdata = {};
		if(opts.savecookie && $.cookie(opts.cookiename)!=null && .cookie(opts.cookiename)!=''){
			initdata = eval('(' + $.cookie(opts.cookiename) + ')');
		}
		//initialize item panel;
		$("body").data(opts.staticname, initdata);
		//initialize pages
		var order = {};//
		var order_result = {};
		var result = {
			info : function(price, count){
				return "";
			}
			addItemNum : function(name, id, price){
				var 
			}
		}
	}
})(jQuery);