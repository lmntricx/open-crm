from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dash, name='dashboard'),
    path("", views.dash, name='dashboard'),
    path("dashboard/newcustomer", views.newCustomer, name='newcustomer'),
    path("dashboard/products",views.products,name="products"),
    path("dashboard/products/delete/<int:product_id>/", views.product_delete, name='product_delete'),
    path("dashboard/neworder",views.newOrder,name="neworder"),
    path("dashboard/orders", views.orders, name='orders'),
    path("dashboard/employees", views.employees, name='employees')
]