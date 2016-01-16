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

## The question and answer for this issue, you should see like this:
## what is python?
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
## what is django?
Django (/ˈdʒæŋɡoʊ/ jang-goh) is a free and open source web application framework, written in Python. A web framework is a set of components that helps you to develop websites faster and easier.
## what is virtualens?
 virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.
## what is sqlite3?
 SQLite is an in-process library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. The code for SQLite is in the public domain and is thus free for use for any purpose, commercial or private. SQLite is the most widely deployed database in the world with more applications than we can count, including several high-profile projects.
## what is postgresql?
PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. It runs on all major operating systems, including Linux, UNIX (AIX, BSD, HP-UX, SGI IRIX, Mac OS X, Solaris, Tru64), and Windows. It is fully ACID compliant, has full support for foreign keys, joins, views, triggers, and stored procedures (in multiple
languages). It includes most SQL:2008 data types, including INTEGER, NUMERIC, BOOLEAN, CHAR, VARCHAR, DATE, INTERVAL, and TIMESTAMP. It also supports storage of binary large objects, including pictures, sounds, or video. It has native programming interfaces for C/C++, Java, .Net, Perl, Python, Ruby, Tcl, ODBC, among others, and exceptional documentation.
## what is rosetta?
Rosetta is a dynamic binary translator for Mac OS X that allows many PowerPC applications to run on certain Intel-based Macintosh computers without modification.
## what is javasscript?
JavaScript is a programming language used to make web pages interactive. It runs on your visitor's computer and doesn't require constant downloads from your website. JavaScript is often used to create polls and quizzes.
## what is css?
- CSS stands for Cascading Style Sheets.
- CSS describes how HTML elements are to be displayed on screen, paper, or in other media.
- CSS saves a lot of work. It can control the layout of multiple web pages all at once.
- External stylesheets are stored in CSS files.
## what is html?
## what is endless pagination?
## what is flat?
## what is haystack?
## what is regitrations?
## what is vim?
## what is django behave?
## what is rest framework?
## what is rest framework authtoken?



