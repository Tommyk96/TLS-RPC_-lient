# utils.py
import os
import requests
import json
import logging
from django.conf import settings

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def call_jsonrpc_method(method, params=None):
    url = "https://slb.medv.ru/api/v2/"
    
    # Путь к файлам сертификатов
    cert_file = '/tmp/cert.pem'
    key_file = '/tmp/key.pem'

    # Записываем сертификат и ключ в файлы
    with open(cert_file, 'w') as f:
        f.write(settings.CERTIFICATE)  # Записываем строку сертификата в файл

    with open(key_file, 'w') as f:
        f.write(settings.PRIVATE_KEY)  # Записываем строку приватного ключа в файл

    # Формируем JSON-RPC запрос
    payload = json.dumps({
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "id": 1
    })

    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload))
    }

    try:
        # Отправка запроса с сертификатами и включение верификации
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            cert=(cert_file, key_file),  # Передаем путь к файлам сертификатов
            verify=True  # Включаем верификацию сертификата сервера
        )
        logger.debug(f"Request sent to {url}.")
        
        # Ответ от сервера
        data = response.json()
        logger.debug("Response received from server.")

        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error occurred: {e}")
        return {"error": str(e)}
