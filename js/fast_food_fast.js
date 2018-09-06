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
// make order function
function MakeOrder(){
    var make_order = document.getElementById("make_order");
    var content_holder = document.getElementById("content_holder");
    var order_history = document.getElementById("order_history");
    order_history.style.display = "none";
    content_holder.style.display ="none";
    make_order.style.display = "block";
    
}
//returning back to home
function BackHome(){
    var make_order = document.getElementById("make_order");
    var content_holder = document.getElementById("content_holder");
    var order_history = document.getElementById("order_history");
    order_history.style.display ="none";
    make_order.style.display = "none"; 
    content_holder.style.display ="block";
     
}
//view ordering history
function ViewHistory(){
    var order_history = document.getElementById("order_history");
    var make_order = document.getElementById("make_order");
    var content_holder = document.getElementById("content_holder");
    make_order.style.display = "none"; 
    content_holder.style.display ="none";
    order_history.style.display = "block"
}
//manage fast-food-items
function ManageItems(){
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    addItem.style.display ="none";
    customer_orders.style.display="none";
    food_items.style.display="block";

}
//manage orders
function ManageOrders(){
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    addItem.style.display ="none";
    food_items.style.display="none";
    customer_orders.style.display="block";
}
//function to delete food items

//adding a food item
function AddNewItem(){
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    food_items.style.display="none";
    customer_orders.style.display="none";
    addItem.style.display = "block";
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



