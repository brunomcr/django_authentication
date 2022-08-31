# 📘 Django Authentication
A example of using authentication with Django.

<br>

### 📑 Main technologies:

<li>Poetry 1.1.14</li>
<li>Python 3.10</li>
<li>Django 4.1</li>
<li>SQLite </li>

<br>

### ⚙️Settings.py
```
# Email

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
* Sending emails from the console backend. This backend is not intended for use in production

<br>

### 💻 How to use:

- Clone the repository:
```
$ git clone https://github.com/brunomcr/django_authentication.git
$ cd django_authentication/
```

- Install dependencies:
```
$ poetry install
```

- Create a structure in the database:
``` 
$ poetry run python manage.py migrate
```

- Start the development server:
```
$ poetry run python manage.py runserver
```

<br>

✅ With the server running, you just need to visit the project endpoints with your browser!

https://user-images.githubusercontent.com/61769161/187677116-14dcbdf5-45f4-4d7c-9bf5-74c67ad4a212.mp4
