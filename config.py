from decouple import config


def telegram_token_validation() -> str:
    """
    Примитивная валидация телеграм токена
    (Проверка на пример токена и его отсутствие)
    :return: str: Телеграм токен
    """
    token = config('TELEGRAM_TOKEN')

    if token.startswith('<') or not token:
        raise Exception('Invalid or missing TELEGRAM_TOKEN in the .env file')

    return token


TELEGRAM_TOKEN = telegram_token_validation()
