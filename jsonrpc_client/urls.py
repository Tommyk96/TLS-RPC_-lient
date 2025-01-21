# jsonrpc_client/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', include('api_client.urls')),  # Для API
    path('', include('api_client.urls')),  # Без префикса API

]



