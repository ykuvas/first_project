print('Hello from repository!')

from dotenv import load_dotenv
import os

def print_author():
    # Загружаем переменные из .env
    load_dotenv()

    # Получаем значение AUTHOR
    author = os.getenv('AUTHOR')

    print(f"Автор проекта: {author}")

# Вызов функции для проверки
print_author()


