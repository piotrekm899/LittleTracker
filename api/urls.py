from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('item/', views.add_item_to_cart, name="add-item-to-cart"),
]
