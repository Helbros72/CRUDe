from django.contrib import admin
from django.urls import path, include

from app_api.views import ProductsView, ProductCreateView

urlpatterns = [
    path("product/", ProductsView.as_view()),
    path("cp/", ProductCreateView.as_view()),

]
