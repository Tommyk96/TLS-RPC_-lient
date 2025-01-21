# api_client/urls.py
from django.urls import path
from .views import JsonRpcView

urlpatterns = [
    path('', JsonRpcView.as_view(), name='jsonrpc_view'),  # Путь для GET-запроса на корень
    path('jsonrpc-endpoint/', JsonRpcView.as_view(), name='jsonrpc_endpoint'),  # Путь для POST-запроса на /jsonrpc-endpoint/
]


# api_client/urls.py
#from django.urls import path
#from .views import JsonRpcView, index  # Исправлено на JsonRpcView

#urlpatterns = [
#    path('', index, name='index'),  # Путь для главной страницы
#    path('jsonrpc-endpoint/', JsonRpcView, name='jsonrpc_view'),
#]
# api_client/urls.py
#from jsonrpc_client import settings 
#from django.urls import path
#from .views import JsonRpcView

#urlpatterns = [
#    path('', JsonRpcView.as_view(), name='jsonrpc'),
    # Other URL patterns
#]



# api_client/urls.py
#from jsonrpc_client import settings 
#from django.urls import path
#from .views import JsonRpcView
#from . import views

#urlpatterns = [
#    path('', views.JsonRpcView.as_view(), name='jsonrpc_view'),  # Если используется класс на основе представления
#    #path('jsonrpc-endpoint/', views.jsonrpc_view, name='jsonrpc_view'),  # Если используется обычная функция
#    # Другие маршруты
#]



