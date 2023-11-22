from django.urls import path
from .views import ProductListView, ProductDetailView, ColorListView, SizeListView, ColorDetailView, SizeDetailView, ProductGeneralListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('general', ProductGeneralListView.as_view(), name='product-general-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('color', ColorListView.as_view(), name='color-list'),
    path('color/<int:pk>/', ColorDetailView.as_view(), name='color-detail'),

    path('size', SizeListView.as_view(), name='size-list'),
    path('size/<int:pk>/', SizeDetailView.as_view(), name='size-detail'),
]
