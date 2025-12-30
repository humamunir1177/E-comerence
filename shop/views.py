from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import Customer_user, Product  # Use Customer_user instead of Customer


def home_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


@login_required
def my_account(request):
    return render(request, 'my_account.html')


def Sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # SignUpForm already saves User and Customer_user
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("my_account")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {'form': form})


def product_detail_html(request):
    product = Product.objects.first()
    if not product:
        return render(request, 'product_detail.html', {'error': 'No products available'})
    return render(request, 'product_detail.html', {'product': product})


def checkout_cart(request):
    return render(request, 'checkout_cart.html')


def checkout_info(request):
    return render(request, 'checkout_info.html')


def checkout_payment(request):
    return render(request, 'checkout_payment.html')


def checkout_complete(request):
    return render(request, 'checkout_complete.html')


def index_fixed_header(request):
    return render(request, 'index_fixed_header.html')


def index_inverse_header(request):
    return render(request, 'index_inverse_header.html')


def product(request):
    return render(request, 'product.html')


def search_results(request):
    return render(request, 'search_results.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def about_us(request):
    return render(request, 'about_us.html')


def faq(request):
    return render(request, 'faq.html')


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
            print("Profile form errors:", u_form.errors, p_form.errors)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=customer)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile_update.html', context)

