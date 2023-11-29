### Django REST Framework test

In this repository I upload a technical test of knowledge of the Django REST Framework from a local company, if you want to test it, follow the next steps:

1.- Clone this repository:

                            git clone https://github.com/nicds-dev/django_test.git 

2.- Create your own virtual environment :

                            virtualenv your_name_venv
                            python3 -m venv your_name_venv 

3.- Active virtual environment.

                            your_name_venv\Scripts\activate
                            source your_name_venv/bin/activate 

4.- Install libraries.

                            (env) pip install -r requirements.txt 

5.- In the settings.py file create your own configuration for the connection to your database.

6.- In the project base run the commands:

                            (env) python3 manage.py makemigrations
                            (env) python3 manage.py migrate
                            (env) python3 manage.py runserver 
