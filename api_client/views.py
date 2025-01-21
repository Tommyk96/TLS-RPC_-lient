from django.shortcuts import render  # Импортируем функцию render
import json
import logging
from django.http import JsonResponse
from django.views import View
from .utils import call_jsonrpc_method

# Логгер для ошибок
logger = logging.getLogger(__name__)

class JsonRpcView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        try:
            # Парсим тело запроса как JSON
            data = json.loads(request.body)
            method = data.get('method')
            params = data.get('params', {})

            # Вызов JSON-RPC метода
            result = call_jsonrpc_method(method, params)

            # Возвращаем успешный ответ
            return JsonResponse({
                'jsonrpc': '2.0',
                'result': result,
                'id': data.get('id')
            })
        except json.JSONDecodeError:
            logger.error('Invalid JSON format')
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.exception('Error processing JSON-RPC request')  # Логируем исключение
            return JsonResponse({'error': str(e)}, status=500)



