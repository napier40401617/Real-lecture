$(document).ready(function(){
	$('ul')
	.find('li:first-child')
	.css('color','red')
	.end()
	.css('border','solid');
});