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
    var EditItem = document.getElementById("EditItem");
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    addItem.style.display ="none";
    customer_orders.style.display="none";
    EditItem.style.display="none";
    food_items.style.display="block";

}
//manage orders
function ManageOrders(){
    var EditItem = document.getElementById("EditItem");
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    addItem.style.display ="none";
    food_items.style.display="none";
    EditItem.style.display="none";
    customer_orders.style.display="block";
}
//function to delete fast-food-fast items
function ItemDeleted(){
    alert("Item deleted");
}
//function to edit fast-food-items
function EditItem(){
    var EditItem = document.getElementById("EditItem");
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    var edit_item_name = document.getElementById("edit_item_name");
    var edit_item_price = document.getElementById("edit_item_price");
    addItem.style.display ="none";
    food_items.style.display="none";
    customer_orders.style.display="none";
    edit_item_name.value = "Pizza";
    edit_item_price.value ="40000";
    EditItem.style.display ="block";

}
//adding a food item
function AddNewItem(){
    var addItem = document.getElementById("addItem");
    var food_items = document.getElementById("food_items");
    var customer_orders = document.getElementById("customer_orders");
    food_items.style.display="none";
    customer_orders.style.display="none";
    addItem.style.display = "block";
}
//authenticating admins
function authenticateadmins(){
    var user_email = document.getElementById("user_email").value;
    var user_password = document.getElementById("user_password").value;
    if(user_email === "admin@gmail.com" && user_password === "admin123"){
        //redirecting to user dashboard
         window.location.href="admin_dashboard.html";
        //console.log("Fine");
    }else{
         //window.location.href="user_dashboard.html";
         alert("Invalid Email or Password!");
    }
}
//authenticating users
function authenticateusers(){
    var user_email = document.getElementById("user_email").value;
    var user_password = document.getElementById("user_password").value;
    
    if(user_email === "user@gmail.com" && user_password === "user123"){
        //redirecting to user dashboard
         window.location.href="user_dashboard.html";
        //console.log("Fine");
    }else{
         //window.location.href="user_dashboard.html";
         alert("Invalid Email or Password!");
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



