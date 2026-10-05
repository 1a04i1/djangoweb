from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import ProductForm
from .models import Product


# =========================================================
# USER PORTAL
# =========================================================

def home(request):
    products = Product.objects.filter(stock__gt=0)

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )


def product_list(request):
    products = Product.objects.filter(stock__gt=0)

    return render(
        request,
        "product_list.html",
        {
            "products": products
        }
    )


def product_detail(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )

    return render(
        request,
        "product_detail.html",
        {
            "product": product
        }
    )


# =========================================================
# USER REGISTRATION
# =========================================================

def register_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Required validation
        if not username or not password:

            messages.error(
                request,
                "Username and password are required."
            )

            return redirect("register")

        # Check existing username
        if User.objects.filter(
            username=username
        ).exists():

            messages.error(
                request,
                "Username already exists."
            )

            return redirect("register")

        # Create user
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Registration successful. Please login."
        )

        return redirect("login")

    return render(
        request,
        "register.html"
    )


# =========================================================
# USER LOGIN
# =========================================================

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )

        # Login successful
        if user is not None:

            login(
                request,
                user
            )

            messages.success(
                request,
                "Login successful!"
            )

            return redirect("/")

        # Login failed
        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "login.html"
    )


# =========================================================
# USER LOGOUT
# =========================================================

def user_logout(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")


# =========================================================
# ADMIN PORTAL
# =========================================================

def admin_dashboard(request):

    products = Product.objects.all()

    total_products = products.count()

    total_stock = sum(
        product.stock
        for product in products
    )

    available_products = products.filter(
        stock__gt=0
    ).count()

    out_of_stock = products.filter(
        stock=0
    ).count()

    return render(
        request,
        "admin_dashboard.html",
        {
            "total_products": total_products,
            "total_stock": total_stock,
            "available_products": available_products,
            "out_of_stock": out_of_stock,
        },
    )


# =========================================================
# ADMIN - ADD PRODUCT
# =========================================================

def admin_add_product(request):

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product added successfully!"
            )

            return redirect(
                "admin_products"
            )

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ProductForm()

    return render(
        request,
        "admin_add_product.html",
        {
            "form": form
        }
    )


# =========================================================
# ADMIN - VIEW / MANAGE PRODUCTS
# =========================================================

def admin_products(request):

    products = Product.objects.all()

    return render(
        request,
        "admin_products.html",
        {
            "products": products
        }
    )


# =========================================================
# ADMIN - EDIT PRODUCT
# =========================================================

def admin_edit_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Product updated successfully!"
            )

            return redirect(
                "admin_products"
            )

        messages.error(
            request,
            "Please correct the errors below."
        )

    else:

        form = ProductForm(
            instance=product
        )

    return render(
        request,
        "admin_edit_product.html",
        {
            "form": form,
            "product": product
        }
    )


# =========================================================
# ADMIN - DELETE PRODUCT
# =========================================================

def admin_delete_product(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    if request.method == "POST":

        product.delete()

        messages.success(
            request,
            "Product deleted successfully!"
        )

        return redirect(
            "admin_products"
        )

    return render(
        request,
        "admin_delete_product.html",
        {
            "product": product
        }
    )