
# Проект для показа работы html - шаблонов в Django


## Установка и запуск

Следуйте этим шагам, чтобы запустить приложение на локальной машине.

### 1. Клонируйте репозиторий

Сначала клонируйте репозиторий на свою локальную машину:

```bash
git clone https://github.com/MrArtur0074/django-itfest.git
cd django-itfest
```

### 2. Создайте виртуальное окружение

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта. Вы можете создать его с помощью следующей команды:

```bash
python -m venv venv
```

### 3. Активируйте виртуальное окружение

Активируйте ваше виртуальное окружение:

- **Для Windows:**

```bash
venv\Scripts\activate
```

- **Для macOS и Linux:**

```bash
source venv/bin/activate
```

### 4. Установите зависимости

После активации виртуального окружения установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

### 5. Настройте базу данных

Если ваше приложение использует базу данных, выполните миграции:

```bash
python manage.py migrate
```

### 6. Запустите сервер

Теперь вы можете запустить сервер разработки:

```bash
python manage.py runserver
```

### 7. Откройте браузер

Перейдите в браузер и введите:

```
http://127.0.0.1:8000/
```

### 8. Админка

```
http://127.0.0.1:8000/admin
```

Доступы:
admin
admin
