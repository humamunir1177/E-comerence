from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('my_account/', views.my_account, name='my_account'),
    path('signup/', views.Sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('product_detail.html/', views.product_detail_html, name='product_detail.html'),
    path('product.html/', views.product, name='product'),
    path('search_results.html/', views.search_results, name='search_results'),
    path('checkout_payment.html/', views.checkout_payment, name='checkout_payment'),
    path('checkout_complete.html/', views.checkout_complete, name='checkout_complete'),
    path('index_fixed_header.html/', views.index_fixed_header, name='index_fixed_header'),
    path('index_inverse_header.html/', views.index_inverse_header, name='index_inverse_header'),
    path('checkout_payment.html/', views.checkout_payment, name='checkout_payment'),
    path('contact_us.html/', views.contact_us, name='contact_us'),
    path('about_us.html/', views.about_us, name='about_us'),
    path('faq.html/', views.faq, name='faq'),
    path('checkout_cart.html', views.checkout_cart, name='checkout_cart'),
    path('checkout_info.html', views.checkout_info, name='checkout_info'), 
    path('checkout_payment.html', views.checkout_payment, name='checkout_payment'),
    path('profile_update', views.profile_update, name="profile_update")  
   
    


    
]
