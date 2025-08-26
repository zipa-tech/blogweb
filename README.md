## SOURCE CODE FOR DJANGO WEB COURSE
1. create a any empty folder to hold your django project <blogweb>

2. install django
```bash
    $ pip install django
```

3. create a django-project

```bash
    $ django-admin startproject name-of-project . eg ::: blogweb_project
```

4. runserver to confirm if django is well configured.

```bash
    $ python.exe manage.py runserver <port-number>
    # access the service at http://127.0.0.1:<port-number>
```

5. Apply Migrations
```bash
    $ python.exe manage.py migrate
```

6. create the superuser to view the admin side
```bash
    $ python.exe manage.py createsuperuser
    # prompted to enter username and password (the password is not viisble for protection)
```
5. 
python.exe .\manage.py startapp blog