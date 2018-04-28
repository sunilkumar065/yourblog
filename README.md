# Web-browsable BLOG API

A simple blog api which lets users perform CRUD operations for a blog-post. Users can add comments and upvote the posts they like.

Non registered user can only view posts. One has to register himself to be able to create his own post or add comments on post.

## How to run?
1. Clone the repository using ```git clone https://github.com/lunaticboy/yourblog.git```
2. Activate your virtualenv and install all dependencies using
 ```pip install -r requirements.txt```
3. Set up your database configurations in */yourblog/settings.py*.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name_of_your database',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': ''
    }
}
```
4. Run migrations if required.
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run ```python manage.py runserver``` to start django server.
6. Yay.!! Server is running at [127.0.0.1:8000](http://127.0.0.1:8000)

___
Footnotes:
* [Installing django](https://docs.djangoproject.com/en/2.0/intro/install/)
* [Installing django-rest-framework](http://www.django-rest-framework.org/#installation)
