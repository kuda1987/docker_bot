# Используем официальный образ Python 3.11
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /python-bot

# Копируем файл зависимостей
COPY requirements.txt .

# Создаем и активируем виртуальное окружение для бота
RUN python -m venv venv
RUN . venv/bin/activate

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем все остальные файлы
COPY . .

# Определеяем команду, которая будет запущена при запуске контейнера
CMD ["python", "main.py"]