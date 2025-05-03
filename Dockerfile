FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Добавляем аргумент сборки
ARG BOT_TOKEN

# Присваиваем его переменной окружения
ENV BOT_TOKEN=${BOT_TOKEN}

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY . .

# Запуск FastAPI приложения
CMD ["python", "bot.py"]
