#KRIA PROJETU FOUN HO NARAN ISSUES
## Install django
        -sudo su
        -apt-get install python-pip
        -apt-get install mysql-server
        -apt-get pip install django
        -pip uninstall django


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
7. Views atu halo nia logika. Hanesan iha server.py karik ita fo fatin template index nian.
8. Admin.py ita bele defini ita nia models sira.
