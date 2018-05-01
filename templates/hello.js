//hello.js
$(document).ready(function(){
	alert("Hello world");
});

$(function(){
	var msg = $('<div>Hello World</div>');
	$('body').append(msg);
});