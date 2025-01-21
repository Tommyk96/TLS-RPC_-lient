#tls_config.py
import ssl
import logging
from io import StringIO

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.set_ciphers('TLSv1.2')  # или нужная версия


# Логгер для отслеживания ошибок и загрузки сертификатов
logger = logging.getLogger(__name__)

# Сертификат в виде строки
CERTIFICATE = '''-----BEGIN CERTIFICATE-----
MIIDNjCCAh4CAwX1szANBgkqhkiG9w0BAQsFADBpMQswCQYDVQQGEwJSVTEMMAoG
A1UECAwDVWZhMQwwCgYDVQQHDANVZmExDDAKBgNVBAoMA3NsYjEMMAoGA1UEAwwD
c2xiMSIwIAYJKoZIhvcNAQkBFhNzdXBwb3J0QHNsYi5tZWR2LnJ1MB4XDTI0MDYy
NDEyMDAxOVoXDTI1MDYyNDEyMDAxOVowVzELMAkGA1UEBhMCUlUxDzANBgNVBAgM
Bk1vc2NvdzEPMA0GA1UEBwwGTW9zY293MQ0wCwYDVQQKDARUZXN0MRcwFQYDVQQD
DA50ZXN0QHRlc3QudGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEB
AJWdgDfGwHt4tQc7SQdZrI2y6EMn25t28xL7LFRsx0J1FjCei5+0m+PSN57VyETG
6ZAJGgKgkfgoDHCBxz5iLAw38tSpKxR4RvVlnsWgOi7i/eix75SN5mO0qZVkVcht
cWbvSsfCxyrSpjIRhk7P5p6cQczNLpsglm2yK7+1XhXTHH//OGQrm4bVWh2wInYu
d0uVPpApqnprHvHM5WgY4+8enAOqXa+wcZ2JNv/jTOE9w/dnjY5A3GjOmYB2evmu
4VafVdQgOpE+RXIoHMxnrnQRjgLVV1KaG9vn5aUOYgeaLe7rTrVttXc2OaietdEx
32cJCGlGtdEdJxfbsFXmMNcCAwEAATANBgkqhkiG9w0BAQsFAAOCAQEACqiZoku2
YQFqQ/h56WqEZtehYuS7ia3XfhOTKN5jeTV3R2dFc7waxu6hCwNIHdi+rFUffJu/
vszrVbtQIoRZv3H0x0e8ZoMfdgws4xkAcdmQ6jA7MdPd/LBMPFmz9vN9N/i1uwPh
OTBqIuY8fXxwSolpqgAv2qHb7gPcSTLQfhGgcC9txSFJbQAae2lOBz5LrPMH4wfG
5NNQkLnJOfPT9aXKh0ebmYYlUlgGIbU2BqlhklMVyyDA8mU6gq/+0iI667efh/tA
UvwT7ElfIUFyZmQKyquHlUgl4jCRn3jC6IJjXtL7vvJ9D+iNCp6vz02iAdW/dCoT
EYJi14GirXpX0g==
-----END CERTIFICATE-----'''

# Приватный ключ в виде строки
PRIVATE_KEY = '''-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCVnYA3xsB7eLUH
O0kHWayNsuhDJ9ubdvMS+yxUbMdCdRYwnouftJvj0jee1chExumQCRoCoJH4KAxw
gcc+YiwMN/LUqSsUeEb1ZZ7FoDou4v3ose+UjeZjtKmVZFXIbXFm70rHwscq0qYy
EYZOz+aenEHMzS6bIJZtsiu/tV4V0xx//zhkK5uG1VodsCJ2LndLlT6QKap6ax7x
zOVoGOPvHpwDql2vsHGdiTb/40zhPcP3Z42OQNxozpmAdnr5ruFWn1XUIDqRPkVy
KBzMZ650EY4C1VdSmhvb5+WlDmIHmi3u6061bbV3NjmonrXRMd9nCQhpRrXRHScX
27BV5jDXAgMBAAECggEANml9+IsBdMYs/DDM+e3cifofa1EDFrK3a1dKw3d+Lka7
57m5aL88FKpezRbNy2mWBuqweXUhMSGLiJ1CM4dropP0bfAKOVsW32dyS0he8K9g
DXEtAxdqSyeopyrC4e4fmIJ9bVICsinDBKGH+YC1zEhiy9NxWDyNSN7L92BEE+ZR
FNlvDDTf9oripVY494uKc3rm5XPKmWVQwBRHSom625ajNtG0od6TrVsyrRMDWzKu
7cgM3F4AtkfrYa5tbMKnotYXG3gfihT53G0lsK6cHPS9lh+ja6PrWZJU1f7HTz9e
plsCgY/ZH53qAqxxQCzb3JN2pwpk0hJpP3e7S8+hqQKBgQDSaLXmCYI3pTQK475L
V10QDtOPBEOy9F7sWDPr7g4eXM8QnJPPldZCAXsHyaqHG9pq2fXfWc+hATtq0/Ph
f2Cb7TdaUtt7Fr/mVpWyZMODWV2HJ/uLUdKHkTmWqbtV58lBToTKadTt51S0XQNC
WyWX3tISW/aOV5DJmQB/zEEvDwKBgQC2CJZqFvPzVIJeZ+67pIjfAyv2E7qd4oP6
C7kQWIEAYmV374HL5ED4CwpuIMq+xszQvCTcehCxiJMNO0Rs91UXtcPWecN/z4MB
upPhaJwvUcBFUE8bUKOAUcXwarRfCX60gln+nCjDL4ECKol6Kt31qVtrCN8ORwQa
1wAQqKHhuQKBgQCxt1N7+qgLy/OLBxUhmaa2+27hKx7rNdA/G7ivG6C9MHKMe1O1
T79qfMmnqEPqXjI7ceFkRv1B5kKDVoZ0/hthWBkap0VOT8bCDHvf84/Xj1GZ6MFj
yTZi3tyfTrk2M9Ie4Ozz8jOwxWUb+jvYfhfgkIkqjJZRX9ChFiP/zUt5LQKBgChY
HOYkciri9wXvaQTjgYZT0KF4W+r0MiXwBTMvOmAYbr63MYA79X5EDCq+T9EahHha
ypym3R5L07OiCBdSdeSMX3wgfojMOA/hBzd1FPCT4NY751x5cdNVzFXtgE5z70YY
gdOhTpN76s7NGK0f5RO2VlGRpMYoTSuZrSUECuTZAoGAW/nxI9T1uQdbQqOHANRn
0nrJF6yK5EtSpQqgDMkpQR1Rm3v6DtsnS3kxzaBInjI+TLOVwoe5LtfvCP1CIfmO
WaoxaJ6exwhzMIYRnIOKaTo+kvcrcZODAqLzsicYlJI3swrK2DE5hkM8Y0//t7nx
PjChutV5gBYfDNiR8twClXY=
-----END PRIVATE KEY-----'''

# SHA1 отпечаток сертификата
CERTIFICATE_SHA1 = "97 65 11 62 C3 D3 DC 93 50 E1 5A E4 F2 3F EE FB 35 30 28 25"

# MD5 отпечаток сертификата
CERTIFICATE_MD5 = "56 12 4A 00 09 82 F5 DC CF D0 91 09 5F 21 B9 DC"

# Отпечаток публичного ключа (SHA1)
PUBLIC_KEY_SHA1 = "CA DA EB 20 3B 19 22 9C F1 0A 7C 3F 31 26 93 4A 4E 5C A7 FF"

# Алгоритм подписи для сертификата (например, RSA)
SIGNATURE_ALGORITHM = "1.2.840.113549.1.1.11"  # Этот алгоритм соответствует SHA256withRSA


# Функция для загрузки SSL-контекста
def load_ssl_context(cert_str, key_str):
    try:
        # Логируем сертификаты и ключи
        logger.debug(f"Loading certificate: {cert_str[:50]}...")  # Логируем начало строки для анализа
        logger.debug(f"Loading private key: {key_str[:50]}...")  # Логируем начало строки для анализа

        # Загружаем сертификат и ключ из строк
        cert_file = StringIO(cert_str)
        key_file = StringIO(key_str)

        # Создание SSL-контекста
        context = ssl.create_default_context()
        context.load_cert_chain(certfile=cert_file, keyfile=key_file)
        logger.info("SSL context successfully loaded.")
        return context
    except ssl.SSLError as e:
        logger.error(f"SSL error: {str(e)}")
        raise

# Пример использования функции для загрузки SSL-контекста
if __name__ == "__main__":
    try:
        context = load_ssl_context(CERTIFICATE, PRIVATE_KEY)
        print("SSL context loaded successfully")
    except Exception as e:
        print(f"Error loading SSL context: {e}")
