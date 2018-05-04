$(document).ready(function(){
	for (var i = 0; i < 4; i++){
		var f=function(j){
		$('body').append($('<button/>',{text:i,
			click:function(){alert(j);}}
			));
		
			};
			f(i);
		}
	
});