from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('my_account/', views.my_account, name='my_account'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('about_us.html/', views.about_us, name='about_us'),
    path('contact_us.html/', views.contact_us, name='contact_us'),
    path('faq.html/', views.faq, name='faq'),
    path('search_results.html/', views.search_results, name='search_results'),
    path('product.html/', views.product, name='product'),
    path('product_detail.html/', views.product_detail_default, name='product_detail_default'),  
    path('product_detail.html/<int:id>/', views.product_detail, name='product_detail'),
    path('product_list.html/', views.product_list, name='product_list'),
    path('categories.html/', views.category_list, name='category_list'),
    path('product-detail.html/', views.product_detail, name='product_detail_dash'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<str:key>/', views.remove_from_cart, name='remove_cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout_cart.html/', views.checkout_cart, name='checkout_cart'),
    path('checkout_info.html/', views.checkout_info, name='checkout_info'),
    path('checkout_payment.html/', views.checkout_payment, name='checkout_payment'),
    path('checkout_complete.html/', views.checkout_complete, name='checkout_complete'),
    path('stripe_checkout/', views.stripe_checkout, name='stripe_checkout'),
    path('index_fixed_header.html/', views.index_fixed_header, name='index_fixed_header'),
    path('index_inverse_header.html/', views.index_inverse_header, name='index_inverse_header'),
]
