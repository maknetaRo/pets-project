# It's a django REST project. 

## How to run the project.

1. Make sure you're inside the django-project folder.

2. Create virutal environment

`python -m venv env`

3. Activate the virtual environment

`source env/bin/activate`

4. Now install all the requirements

`pip install -r requirements.txt`

5. Create .env file with secrets like SECRET_KEY and DEBUG

If you need, you can generate a new secret key here: https://djecrety.ir/

or running this command in a command line

`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

5. Run the Django server

`python manage.py runserver`