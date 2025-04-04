# Wagtail-POC

### Install virtual env, if already not exist.

```
pip install virtualenv
```

### Create virtual environment.

```
virtualenv venv
```

### Activate virtual env (change command according to your OS).

```
source ./venv/Scripts/activate
```

### Install python dependencies.

```
pip install -r requirements.txt
```

### Make migrations and migrate

```
python manage.py makemigrations
python manage.py migrate
```

### Run django server.

```
python manage.py runserver 0.0.0.0:8000
```

### Create super user. (open in new terminal)

```
python manage.py createsuperuser
```

You can set both username and passsword to `admin` in order to make it simple (easy to remember).

## Django Admin Panel

```
http://127.0.0.1:8000/admin/
```

## Rest APIs directly using django rest framework.

```
http://127.0.0.1:8000/polls/questions/
```

## Wagtail Admin Panel/Dashboard

```
http://127.0.0.1:8000/cms/
```

## Wagtail APIs (headless, to be consumed on any platform/device)

```
http://127.0.0.1:8000/api/v2/pages/
```

## include additional fields on pages listing.

```
http://localhost:8000/api/v2/pages/?type=main.PostPage&fields=body,post_image,tags,category
```
