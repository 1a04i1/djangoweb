PRODUCT MANAGEMENT SYSTEM - EXAM PROJECT

Requirements covered:
- Django project and application
- MySQL database
- Product model
- Product ID, Name, Category, Price, Description, Stock Quantity, Image/Image URL
- Admin Portal: Add, View, Update, Delete
- User Portal: View available products and details
- Cards for user products
- Table for admin management
- Success/error messages
- Validation: required name, positive price, non-negative stock
- Django templates, forms, views, models and ORM
- Navigation between Admin and User portals
- Responsive Bootstrap UI
- Django built-in admin is also available at /admin/

SETUP:
1. Create/activate virtual environment.
2. Install:
   pip install django mysqlclient pillow django-crispy-forms crispy-bootstrap5
3. Create MySQL database:
   CREATE DATABASE productapp_db;
4. Check MySQL USER/PASSWORD in conj/settings.py.
5. Run:
   python manage.py makemigrations
   python manage.py migrate
6. Optional:
   python manage.py createsuperuser
7. Run:
   python manage.py runserver

PAGES:
Home: /
User Products: /products/
Product Details: /products/<id>/
Admin Dashboard: /admin-portal/
Admin Add: /admin-portal/add/
Admin Manage: /admin-portal/products/
Admin Edit: /admin-portal/edit/<id>/
Admin Delete: /admin-portal/delete/<id>/
Django Admin: /admin/
