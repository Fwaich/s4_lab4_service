# DevOps Lab Service

Простой backend-сервис для лабораторной работы.

## Возможности

- создание задач
- обработка задач (с задержкой)
- сбор метрик (/metrics)

## Запуск (локально)

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Эндпоинты

GET /
POST /tasks
GET /tasks
POST /tasks/{id}/process
GET /metrics