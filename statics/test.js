$(function(){
	for (var i = 0;i <100; i++) {
		var msg=$('<div>Hello World</div>');
		msg.css('font-size',i);
		$('body').append(msg);
	}});

$(function(){
	var gb=$('<div/>');
	gb.append($('<div/>',{text:'Great Britain'}));
	gb.append($('<img/>',{src:'../statics/flags/bo.gif'}));

	$("#countries").append(gb);
	$("#countries").attr("id","gid");
});

$(function(){
	$('#fr img').css({
		background:"red",
		border:"3px blue solid"
	});
});

$(function(){
	$('#fi img').css({
		background:"red",
		border:"3px blue solid"
	});
});

$(function(){
	$('#gid img').css({
		background:"red",
		border:"3px blue solid"
	});
});
$(function(){
	$('p:first-child').css('border','solid');
	$('p:nth-child(1)').css('border','solid');
	$('p:eq(1)').css('border','solid');
	$('p:last').css('border','solid');
});

$(function(){
	var ca={
		cname:"A J Cumming",
		caddress:{
			street:"10 Collinton Rd",
			town:"Edinburgh",
			post_code:"EH14 5Dt"

		},
		transaction:[
		{whn:"2014-01-11",nar:"Cash Withdrawal",amt:-100},
		{whn:"2014-01-11",nar:"BUS Fare",amt:-35},]
	};
	alert(ca.transaction[1].nar);
});
$(function(){
	$('#key th').css('color','red');
});
$(function(){
	$('#key th').css({
		background:"yellow",
		border:"3px blue solid"
	});
});
$(function(){
	$('body').append($('<div>Hide key</div>'));
});
$(function(){
	$('body').prepend($('<div>',{text:'Hide key',css:{color:'blue'}}));
});
$(function(){
	var elem=$('<div/>');
	elem.html('An example element');
	elem.css('border','solid blue');
	$('body').append(elem);
});
