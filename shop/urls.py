from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import product_detail


urlpatterns = [
    path('', views.home_page, name='home_page'),  
    path('my_account/', views.my_account, name='my_account'),  
    path("signup/", views.Sign_up, name="signup"),  
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product/', product_detail, name='product_detail'),
    path('product_detail.html', product_detail, name='product_detail_html'),
    

]
