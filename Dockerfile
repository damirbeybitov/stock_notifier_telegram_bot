FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY . .

# Запуск FastAPI приложения
CMD ["uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8000"]
