# MY NOTAS
# DATA: 07 DE FEVREREIRU 2015
## Tips install aplikasi iha linux
    -sudo su
    -apt-get install python-pip
    -apt-get install mysql-server
    -apt-get pip install django
    
    -pip uninstall django

    
## tips check file ne'ebe install ona:
    -pip freeze

# KRIA PROJETU FOUN HO DJANGO

## Install django

    1) Halo directory foun ba projetu
       mkdir <dir name>
       cd <dir name>  


    2) kria ita nia projectu nia naran, ita fo naran fahe.

       ony@ony-AO756 ~/Desktop/sabadu $ django-admin.py startproject fahe
       
       ony@ony-AO756 ~/Desktop/sabadu/fahe $ rm db.aqlite3


    3) kria fali ita nia database foun...

       ony@ony-AO756 ~/Desktop/sabadu/fahe $ python manage.py makemigrations
       ony@ony-AO756 ~/Desktop/sabadu/fahe $ python manage.py migrate



    4) Kria ka registu user foun

        Cony@ony-AO756 ~/Desktop/sabadu/fahe $ python manage.py createsuperuser


## Metodu atu hare table sira:

     ony@ony-AO756 ~/Desktop/sabadu/fahe $ python
    
    
     >>> import sqlite3
     >>> connection=sqlite3.connect("db.sqlite3")
     >>> def lista(entries):
     ... for entry in entries:
     ... print entry
     ...
     >>> entries = connection.execute("SELECT * FROM main.sqlite_master WHERE type='table';")
     >>> lista (entries)



## DJANGO
    ORM object relational mappe.
    diferente django ho bottle:
    django nia but hotu iha hotu tona, no ita temi det nia naran por ex. Template sira.

    1. App nia bele uza ba profile.
    2. Settings.py app sira inklui iha laran
    3. urls,py ita defini route sira iha funsun nia leten
    4. wsgi.py buat hotu-hotu iha nia fatin.
    5. Manage.py nia mak manager ba buat hotu-hotu ex. hanesan server.py
    6. Models.py nia funsaun atu tau estrutura base de dados nian.
    7 Views atu halo nia logika. Hanesan iha server.py karik ita fo fatin template index nian.
    8. Admin.py ita bele defini ita nia models sira.

## INHERITANCE
    Inheritance hanesan class ho subclass.
    Class geralmente hanesan typo..
    
    Instance = buat ne'ebe espesifiku liu, unique atu hanesan ho unique ID
    
### HALO CLASS HIERARCHY UZA PYTHON:
    ony@ony-AO756 ~/Desktop/sabadu/fahe $ python
    
    >>> class Lampu:
    ...
    def __init__(self,):
    ... self.kor = ''
    ... self.naruk = 10
    ... self.watt = 60
    ... self.fo_naroman = False
    ...
    >>> Lampu
    <class __main__.Lampu at 0xb766905c>
    >>> hau_nia_lampu = Lampu()
    >>> hau_nia_lampu
    <__main__.Lampu instance at 0xb767694c>
    >>> hau_nia_lampu.naruk
    10
    >>> hau_nia_lampu.watt
    ...
    fulun_kor = 'metan'
    ...
    >>> class Ikan(Animal):
    ...
    nani = True
    ...
    >>> hau_nia_ika = Ikan()
    >>> hau_nia_ikan = Ikan()
    >>> hau_nia_mammal = Mammal()
    >>> hau_nia_animal = Animal()
    >>>
    >>>
    >>> hau_nia_ikan.nani
    True
    >>> hau_nia_ikan.moris
    True
    >>> hau_nia_mammal.fulun_kor
    'metan'
    >>> hau_nia_mammal.moris
    True



