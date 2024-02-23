from django.urls import path
from .views import product_index, product_detail

urlpatterns = [
    path("", product_index, name="product_index"),
    path("<int:pk>/", product_detail, name="product_detail"),
]
