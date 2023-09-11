from django.urls import path
from . import views

urlpatterns = [
   path("", views.home_page),
   path("home", views.home_page),
   path("add_product", views.add_product_view),
   path("products/delete/<str:product_id>", views.delete_product_view),
   path("products/change_field/<str:product_id>/<str:field_name>", views.field_edit),
   path("products/add_field/<str:product_id>", views.field_add),
   path("products/<str:product_id>", views.product_info),
]