from django.urls import path
from . import views


urlpatterns = [
    # USER PORTAL
    path("", views.home, name="home"),

    path(
        "products/",
        views.product_list,
        name="product_list"
    ),

    path(
        "products/<int:id>/",
        views.product_detail,
        name="product_detail"
    ),

    # ADMIN PORTAL
    path(
        "admin-portal/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

    path(
        "admin-portal/add/",
        views.admin_add_product,
        name="admin_add_product"
    ),

    path(
        "admin-portal/products/",
        views.admin_products,
        name="admin_products"
    ),

    path(
        "admin-portal/edit/<int:id>/",
        views.admin_edit_product,
        name="admin_edit_product"
    ),

    path(
        "admin-portal/delete/<int:id>/",
        views.admin_delete_product,
        name="admin_delete_product"
    ),

    path("register/", views.register_user, name="register"),
path("login/", views.user_login, name="login"),
path("logout/", views.user_logout, name="logout"),
]