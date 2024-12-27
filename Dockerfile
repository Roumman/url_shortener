# Используем официальный Python 3.11 как базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости проекта
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Объявляем том для хранения данных
VOLUME /app/data

# Открываем порт 80
EXPOSE 80

# Запускаем приложение с помощью uvicorn на порту 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
