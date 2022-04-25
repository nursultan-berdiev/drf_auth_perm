from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('client.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),

]
