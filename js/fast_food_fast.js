function display_test(){

    var fast_food_fast_header = document.getElementById('site_header');
    fast_food_fast_header.innerHTML = "";
    fast_food_fast_header.innerHTML = "Make Your Order 24 / 7";
    
}

function display_original_test(){
    var fast_food_fast_header = document.getElementById('site_header');
    fast_food_fast_header.innerHTML = "";
    fast_food_fast_header.innerHTML = "Fast-Food-Fast";
}

document.getElementById("register").addEventListener("click",function(){
   var content_area = document.getElementById('content_area');
   var typewriter_div = document.getElementById('typewriter_div');
   var signup_form = document.getElementById('signup_form');
   var login_form = document.getElementById('site_login_form');
   typewriter_div.style.display = "none";
   content_area.style.display = "none";
   login_form.style.display="none";
   signup_form.style.display = "block";
  

});

document.getElementById("enter_account").addEventListener("click",function(){
    var content_area = document.getElementById('content_area');
    var typewriter_div = document.getElementById('typewriter_div');
    var signup_form = document.getElementById('signup_form');
    var login_form = document.getElementById('site_login_form');
    typewriter_div.style.display = "none";
    content_area.style.display = "none";
    signup_form.style.display = "none";
    login_form.style.display="block";
    
});