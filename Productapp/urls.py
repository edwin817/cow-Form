from django.urls import path
from Productapp import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('servicepage/',views.servicepage,name="servicepage"),
    path('productpage/<iteamcatg>/',views.productpage,name="productpage"),
    path('singleproductpg/<dataid>/',views.singleproductpg,name="singleproductpg"),
    path('cartpg/',views.cartpg,name="cartpg"),
    path('savecart/',views.savecart,name="savecart"),
    path('Deletecart/<int:dataid>/', views.Deletecart, name="Deletecart"),
    path('checkoutpg/',views.checkoutpg,name="checkoutpg"),
    path('savecheckout/',views.savecheckout,name="savecheckout"),
    path('',views.userloginpg,name="userloginpg"),
    path('usersavedata/',views.usersavedata,name="usersavedata"),
    path('userpg/',views.userpg,name="userpg"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('contactpg/',views.contactpg,name="contactpg"),

]