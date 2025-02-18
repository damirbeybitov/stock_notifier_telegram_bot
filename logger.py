import os
import logging
from functools import partial

def init_logger(name, log_level=logging.INFO, log_file="log/app.log"):
    """
    Инициализирует логгер для приложения.
    
    :param log_level: Уровень логирования (по умолчанию INFO).
    :param log_file: Путь к файлу логов (по умолчанию "log/app.log").
    :return: Логгер
    """

    # Создаем директорию для логов, если она не существует
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(name)  # Указываем имя логгера
    logger.setLevel(log_level)

    if not logger.hasHandlers():
        # Создаем обработчик для записи в файл
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Формат сообщений
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Создаем обработчик для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)

        # Добавляем обработчики к логгеру
        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)

    # Создаем новый метод logger.error с параметром exc_info=True по умолчанию
    logger.error = partial(logger.error, exc_info=True)

    return logger

# Configure Uvicorn to use the custom logger
logging.getLogger("uvicorn").handlers = logging.getLogger("server").handlers
logging.getLogger("uvicorn.access").handlers = logging.getLogger("server").handlers