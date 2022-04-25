from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('client', ClientViewSet, basename='client')

urlpatterns = [
    # path('product/', views.product_view),
    # path('product/<int:pk>/', views.product_detail),
    path('', include(router.urls)),

]
