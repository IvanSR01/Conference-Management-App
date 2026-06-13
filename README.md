# Conference Server

Веб-приложение для хранения и управления информацией об участниках конференций.

Проект разработан в рамках учебной практики с использованием современного Python-стека: FastAPI, SQLAlchemy и PostgreSQL.

## Возможности

* Просмотр списка участников конференций
* Добавление новых участников
* Редактирование информации об участниках
* Удаление участников
* Поиск по участникам
* Валидация данных на стороне клиента и сервера
* Защита от повторной регистрации одного участника на одну конференцию

## Используемые технологии

### Backend

* Python 3
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript (Fetch API)

### Infrastructure

* Git
* Nginx
* systemd
* ALT Linux

## Структура проекта

```text
app/
│
├── routers/
│   └── participants.py
│
├── services/
│   └── participant_service.py
│
├── schemas/
│   └── participant.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── config.py
├── database.py
├── models.py
└── main.py
```

## Настройка проекта

### 1. Клонирование репозитория

```bash
git clone <repository_url>
cd conference-server
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
```

Активация:

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Linux:

```bash
source .venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создать файл `.env` в корне проекта:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=conference_db
DB_USER=postgres
DB_PASSWORD=password
```

### 5. Запуск приложения

```bash
python -m uvicorn app.main:app --reload
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000
```

## Модель данных

Участник конференции содержит следующие поля:

| Поле            | Описание             |
| --------------- | -------------------- |
| id              | Идентификатор        |
| full_name       | ФИО участника        |
| email           | Электронная почта    |
| organization    | Организация          |
| conference_name | Название конференции |

## Ограничения

В системе запрещена повторная регистрация участника на одну и ту же конференцию.

Уникальность определяется по комбинации:

```text
email + conference_name
```

## REST API

| Метод  | Endpoint           | Описание                    |
| ------ | ------------------ | --------------------------- |
| GET    | /                  | Получение списка участников |
| POST   | /participants      | Создание участника          |
| PUT    | /participants/{id} | Обновление участника        |
| DELETE | /participants/{id} | Удаление участника          |

## Автор

Студенческий проект по дисциплине веб-разработки и администрирования серверных приложений.
