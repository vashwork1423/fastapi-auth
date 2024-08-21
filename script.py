import os

folders = [
    "app",
    "app/api",
    "app/api/v1",
    "app/api/v1/endpoints",
    "app/core",
    "app/services",
    "app/models",
    "app/schemas",
    "app/db",
    "alembic",
    "tests"
]

files = [
    "app/__init__.py",
    "app/main.py",
    "app/api/__init__.py",
    "app/api/v1/__init__.py",
    "app/api/v1/endpoints/__init__.py",
    "app/core/__init__.py",
    "app/core/config.py",
    "app/services/__init__.py",
    "app/models/__init__.py",
    "app/schemas/__init__.py",
    "app/db/__init__.py",
    "app/db/base.py",
    "app/db/session.py",
    ".gitignore",
    "requirements.txt",
    "README.md"
]

# Создание папок
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Создание файлов
for file in files:
    with open(file, 'w') as f:
        pass  # Создаёт пустой файл

print("Структура проекта создана.")
