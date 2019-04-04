# Imposter Syndrome App

## Authors
Denis Murphy </br>
Gazifah

## Purpose of Application

Application created to help the user to identify the source of their imposter syndrome feelings.
The application contains 3 sequenced questions.

# Instructions

Run the following commands to set up a virtual environment locally on your machine and the set up the barebones folders of the project.

```
mkdir crush_the_imposter
conda create --name imposter_app python=3
cd imposter_app
source activate imposter_app
pip install django
django-admin startproject imposter_app
cd imposter_app
python manage.py startapp questions
touch .gitignore
touch README.md

```
### Install Libraries

```
pip install requirements.txt

```
### Update database before running local server

```
python manage.py makemigrations
python manage.py runserver

```

### Create a User to Login to admin

```
python manage.py createsuperuser

```
