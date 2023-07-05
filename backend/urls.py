from django.urls import path
from backend import views

urlpatterns = [
    path('intropage/',views.intropage,name="intropage"),
    path('addpage/',views.addpage,name="addpage"),
    path('saveadd/',views.saveadd,name="saveadd"),
    path('display/',views.display,name="display"),
    path('editcategory/<int:dataid>',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>',views.deletecategory,name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/',views.saveproduct,name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>',views.deleteproduct,name="deleteproduct"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),







]