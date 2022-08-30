# 📘 Django Authentication
Authentication with Django

<br>

### ⚙️ Main technologies:

<li>Python</li>
<li>Django</li>    
<li>SQLite</li>

<br>

### 🛠️ Main tools:

<li>Poetry</li>
<li>Black</li>

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

- Create a super user:
``` 
$ poetry run python manage.py createsuperuser
```

- Start the development server:
```
$ poetry run python manage.py runserver
```
