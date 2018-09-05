window.onscroll = function() {myFunction()};

var header = document.getElementById("site_navbar");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {  
    header.classList.add("sticky");
    document.getElementById("site_navbar").style.backgroundColor = "black";
  } else {
    header.classList.remove("sticky");
    document.getElementById("site_navbar").style.backgroundColor = "";
  }
}
//defining what happens when a user clicks the signup button
document.getElementById("register").addEventListener("click",function(){
    var all_sections = document.querySelectorAll("section");
    var login_user_form = document.getElementById('site_login_form');
    var site_signup_form = document.getElementById('site_signup_form');
    document.body.style.backgroundImage="url(images/background.jpg)";
    var i;
    for (i = 0; i < all_sections.length; i++) {
        all_sections[i].style.display = "none";
    }
    
    login_user_form.style.display = "none";
    site_signup_form.style.display = "block";
     
});

//Adding action when user clicks on the login link in navbar
document.getElementById("enter_account").addEventListener("click",function(){
    var all_sections = document.querySelectorAll("section");
    var login_user_form = document.getElementById('site_login_form');
    var site_signup_form = document.getElementById('site_signup_form');
    document.body.style.backgroundImage="url(images/background.jpg)";
    var i;
    for (i = 0; i < all_sections.length; i++) {
        all_sections[i].style.display = "none";
    }
    site_signup_form.style.display="none";
    login_user_form.style.display = "block";

     
});



