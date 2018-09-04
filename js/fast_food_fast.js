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
//defining what happens when a user clicks the signup button
document.getElementById("register").addEventListener("click",function(){
   var content_area = document.getElementById('content_area');
   var typewriter_div = document.getElementById('typewriter_div');
   var signup_form = document.getElementById('signup_form');
   var login_form = document.getElementById('site_login_form');
   document.body.style.backgroundImage="url(images/background.jpg)";
   login_form.style.display="none";
   typewriter_div.style.display = "none";
   content_area.style.display = "none";
   signup_form.style.display = "block";
});

//hide typewritter  div 
function hide_typewriter_div(){
    document.getElementById("typewriter_div").style.display="none";
}

//specifying the time the div fadesout
//setTimeout(hide_typewriter_div,9000);

document.getElementById("enter_account").addEventListener("click",function(){
    var content_area = document.getElementById('content_area');
    var typewriter_div = document.getElementById('typewriter_div');
    var signup_form = document.getElementById('signup_form');
    var login_user_form = document.getElementById('site_login_form');
    document.body.style.backgroundImage="url(images/background.jpg)";
    typewriter_div.style.display = "none";
    content_area.style.display = "none";
    signup_form.style.display = "none";
    login_user_form.style.display="block";
    
});

