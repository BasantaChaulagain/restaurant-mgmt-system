// $(document).ready(function(){
//     $(".sign-up-button").click(function(){
//         $("#sign-up-form").show().attr("class","sign-up-form-displayed")
//         $("index.html #log-in-form").hide()
//     });

//     $(".log-in-button").click(function(){
//         $("#sign-up-form").hide()
//         $("#log-in-form").show().attr("class","log-in-form-displayed")
//     });
// });



$(document).ready(function(){
    $(".image").click(function(){
	    if (!$(this).hasClass("item-selected")) {
	        $(this).addClass("item-selected")  
	        $(this).find("input").prop("checked",true) 
	        $(this).find("img:first-child").css("display","none")
	        $(this).find("img:nth-child(2)").css("display","inline")
	    } 

	    else  {
	        $(this).removeClass("item-selected")
	        $(this).find("input").prop("checked",false)
	        $(this).find("img:first-child").css("display","inline")
	        $(this).find("img:nth-child(2)").css("display","none")
	    }
	
	});
});