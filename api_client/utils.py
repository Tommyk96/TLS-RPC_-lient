# utils.py
import json
import ssl
import http.client
import tempfile
from django.conf import settings

def call_jsonrpc_method(method, params=None):
    url = "slb.medv.ru"
    endpoint = "/api/v2/"

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

    # Создание временных файлов для сертификата и ключа
    def create_temp_cert_and_key(cert, key):
        cert_file = tempfile.NamedTemporaryFile(delete=False)
        cert_file.write(cert.encode())
        cert_file.close()

        key_file = tempfile.NamedTemporaryFile(delete=False)
        key_file.write(key.encode())
        key_file.close()

        return cert_file.name, key_file.name

    cert_file, key_file = create_temp_cert_and_key(settings.CERTIFICATE, settings.PRIVATE_KEY)

    # Настройка сертификатов и ключа для двусторонней TLS-авторизации
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile=cert_file, keyfile=key_file)

    # Подключение и отправка запроса
    connection = http.client.HTTPSConnection(url, context=context)
    connection.request("POST", endpoint, body=payload, headers=headers)

    # Получение ответа
    response = connection.getresponse()
    data = response.read().decode()
    connection.close()

    # Возвращаем распарсенный ответ в формате JSON
    return json.loads(data)


