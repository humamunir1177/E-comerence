from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Customer_user, Product  
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            Customer_user.objects.create(
                user=user,
                phone=form.cleaned_data['phone']
            )

            login(request, user)
            return redirect("my_account")
    else:
        form = SignUpForm()

    return render(request, "sign_up.html", {'form': form})


def product_detail(request):
    return render(request, 'product_detail.html')
def home_page(request):
    return render(request, 'index.html') 