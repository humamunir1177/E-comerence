import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Customer_user
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm


stripe.api_key = settings.STRIPE_SECRET_KEY  

def home_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


@login_required
def my_account(request):
    return render(request, 'my_account.html')

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("my_account")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {'form': form})

@login_required
def profile_update(request):
    customer, created = Customer_user.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=customer)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('my_account')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=customer)
    return render(request, 'profile_update.html', {'u_form': u_form, 'p_form': p_form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def product_detail_default(request):
    product = Product.objects.first()  
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

def faq(request):
    return render(request, 'faq.html')

def search_results(request):
    return render(request, 'search_results.html')

def index_fixed_header(request):
    return render(request, 'index_fixed_header.html')

def index_inverse_header(request):
    return render(request, 'index_inverse_header.html')


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': product.price,
            'image': product.image.url,
            'quantity': 1,
        }

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('checkout_cart')

def remove_from_cart(request, key):
    cart = request.session.get('cart', {})
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('checkout_cart')

def cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart.html', {'cart': cart, 'total': total})


def checkout_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'checkout_cart.html', {'cart': cart, 'total': total})

def checkout_info(request):
    return render(request, 'checkout_info.html')

def checkout_payment(request):
    if request.method == "POST":
        
        return redirect('checkout_complete')
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {
        'cart': cart,
        'total': total,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'checkout_payment.html', context)

def checkout_complete(request):
    return render(request, 'checkout_complete.html')

@login_required
def stripe_checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty!")
        return redirect('checkout_cart')

    total = sum(item['price'] * item['quantity'] for item in cart.values())
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(total * 100), 
                'product_data': {'name': 'E-commerce Order'}
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/checkout_complete.html/',
        cancel_url='http://127.0.0.1:8000/checkout_cart.html/'
    )

    return redirect(session.url)
