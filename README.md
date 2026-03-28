# Random Jokes API

Простой сервис для генерации случайных шуток.  
Фронтенд подключён через Nginx (обслуживание статики и проксирование API).

---

## Функционал

- Получение случайной шутки (GET `/joke`)
- Rate limiting — ограничение количества запросов с одного IP

---

## Технологии

- Python 3.11+
- FastAPI
- Redis (rate limiting)
- Vanilla JS + Tailwind CSS
- Docker и Docker Compose
- Nginx (для фронтенда и проксирования API)

---

## Запуск через Docker (рекомендуется)

1. Клонируем репозиторий:

```bash
git clone https://github.com/c-dvoid/random_jokes.git
cd random_jokes
```

2. Запускаем через Docker Compose:

```bash
docker compose up --build
```

Приложение будет доступно на `http://localhost`

---

## Локальный запуск (для разработки)

1. Клонируем репозиторий:

```bash
git clone https://github.com/c-dvoid/random_jokes.git
cd random_jokes
```

2. Создаём виртуальное окружение и устанавливаем зависимости:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
```

3. Запускаем сервер:

```bash
uvicorn app.main:app --reload
```

Приложение будет доступно на `http://localhost:8000`