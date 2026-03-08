# Django Course Project

A simple **Django web application** to manage and display courses using **Python 3** and **HTML Templates**.

---

## 🚀 Project Overview

This project demonstrates the basics of building a Django application including:

- Creating models
- Running migrations
- Using Django Admin
- Rendering HTML templates
- Displaying data from the database

The application allows you to **add courses through the admin panel** and **display them on a web page**.

---

## 🛠 Requirements

Make sure you have the following installed:

- Python 3
- pip
- Django

---

## ⚙️ Environment Setup

### Linux / macOS

Activate the virtual environment:

```bash
source /home/caesar/venv/bin/activate
```

Install Django:

```bash
pip install django
```

---

### Windows (CMD)

Activate the virtual environment:

```cmd
\home\caesar\venv\Scripts\activate
```

Install Django:

```cmd
pip install django
```

---

## 🗄 Database Setup

Apply migrations to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👤 Create Admin User

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set:

- Username
- Email
- Password

---

## ▶️ Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to:

```
http://127.0.0.1:8000/
```

### If Port 8000 is Already in Use (Linux)

```bash
fuser -k 8000/tcp
```

Then run the server again.

---

## 🔗 Important URLs

| Page | URL |
|-----|-----|
| Courses Page | http://127.0.0.1:8000/courses/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |

---

## 📁 Project Structure

```
django-course-project
│
├── manage.py
├── db.sqlite3
│
└── myapp
    ├── models.py
    ├── views.py
    ├── admin.py
    └── templates
        └── courses.html
```

---

## 📌 Important Files

### Models
`myapp/models.py`

Defines the **Course model** and its fields (title, description, etc.).

---

### Views
`myapp/views.py`

Handles retrieving data from the database:

```python
Course.objects.all()
```

And sending it to templates.

---

### Templates
`myapp/templates/courses.html`

Displays courses using Django template syntax:

```html
{% for course in courses %}
    <h2>{{ course.title }}</h2>
{% endfor %}
```

---

## 🎯 Features

- Django Admin panel
- Course model
- HTML templates
- Dynamic course display
- Simple project structure for learning Django

---

## 📚 Learning Goals

This project helps beginners understand:

- Django project structure
- Models & migrations
- Admin panel
- Views and templates
- Rendering dynamic data

---

## 🧑‍💻 Author

**Medo Ahmed**

Backend Developer (Learning Django & Web Development)
