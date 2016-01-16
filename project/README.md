# how to make project?
    - mkproject Issues
    - git clone https://catalpainternational/issues.git/
    - cd Issues
    - cd support
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver --settings=support.settings.local
    - python manage.py createsuperuser --username="ano" --email="exemplo@yahoo.com"
    - ctrl + c
    - git add .
    - git commit -m "exemplo"
    - git push origin exemplo
    - git pull


# Writing your first Django app
## We’ll assume you have Django installed already. You can tell Django is installed and which version by running the following command:
    - python -c "import django; print(django.get_version())"
# Creating a project
## From the command line, cd into a directory where you’d like to store your code, then run the following command:
    - django-admin startproject issues
## Let’s look at what startproject created:
- issues/
   - manage.py
       - mysite/
          - __init__.py
                - settings.py
                    - urls.py
                        - wsgi.py
Devel/Issues/Issues/support/
-bdd/
    -features
        -steps
            create.py
            home.py
            login.py
            logout.py
    __init__.py
    __init__.pyc

-fitutures/
    categories.json
    contacts.json
    hardware.json
    ligauser.json
    sources.json
-Issues/
-locale/
-profiles/
-support/
-test/
db.sqlite3
fabfile.py
manage.py

# The question and answer for this issue, you should see like this:
## what is python?
## what is django?
## what is virtualens?
## what is sqlite3?
## what is postgresql?
## what is rosetta?
## what is javasscript?
## what is css?
## what is html?
## what is endless pagination?
## what is flat?
## what is haystack?
## what is regitrations?
## what is vim?
## what is django behave?
## what is rest framework?
## what is rest framework authtoken?



