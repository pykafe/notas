## Python executable file ba windows

**Python executable windows: py2exe or PyInstaller**

python executable mak atu kria ka exekuta file (windows) nia mak ita presiza uza tools sira nee: Py2exe ka PyInstaller.  

**1. Pyinstaller** 

PyInstaller mak programa ida nebe uza kria ka konverte Python scripts ba file windows nian. PyInstaller bele  hakerek iha Python nebe la presiza uzuáriu ba instala Python. Ida nee hanesan opsaun ida nebe diak tebes kuandu ita presiza atu fahe programa ida ba uzuáriu ikus hanesan aplikasaun standalone ida.



Module no etap sira nebe kria ka converte file .py ba .exe iha sistema ubuntu

### Atu hahu:

1. prepara python no install python tuir verzaun no enviromentu nebe ita uza iha Sistema operasaun ubuntu.

2. install framework sira ba projectu nian laran hanesan:

   - pyinsttaller 
   - cx_freeze
   - tkinter

**Etapa compile python script :**

3. kria python file tuir filenaran.py

   ```
   # test.py
   import tkinter
   from tkinter import *
   root = Tk()
   root.title('Test aplikasaun ida')
   Label(text='Mai ita aprende python hamutuk').pack(pady=15)
   root.mainloop()
   print ("Susesu, Rai ona prosesu nee!")
   ```

4. kria setup script file ho naran setup.py

   ```
   import sys
   from cx_Freeze import setup, Executable

   setup(
   	name = "nicko",
   	version = "1.0",
       options = {'build_exe':{'packages': ['filenaran']}},
   	description = 'Koko kria app',
       executables = [Executable("test.py")]
   )
   ```

5. bele run python build ka execultable

   - `python setup.py build`
   - `python setup.py install`
   - `pyinstaller filenaran.py`
   - `pyinstaller --onefile --windowed filenaran.py`




**2. Py2exe**  

Py2exe mak prolongamentu Python Distutils ida nebe konverte Python scripts (.py) ba Windows Microsoft executables (.exe). Executables hirak ne'e bele konkorre ba sistema ida la ho Python ona ka la presiza instalasaun Python.


Module no etap sira nebe kria ka converte file .py ba .exe iha sistema windows

**Etapa sira konaba compile python script:**
1. prepara python no install python tuir verzaun no enviromentu nebe ita uza iha Sistema operasaun windows.
2. install framework sira ba projectu nian laran hanesan:
   - py2exe
3. kria python file tuir hello.py 
```
print ("Hello World")
```
4. kria setup script file ho naran setup.py
```
from distutils.core import setup
import py2exe

setup(name='niko',
      version='1.0',
      description='Koko kria aplikasaun Python nian',
      author='Joanico Barros',
      author_email='joanicobarros@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages_dir = {'utils' : 'X/', 'printing': 'X/utils/'},
      script=['connection-stats/hello.py']
     )
```
5. Bele run python build ka execultable


-  `python setup.py bdist`
-  `python setup.py bdist --format=wininst`
-  `python setup.py bdist --format=msi`


### Referensia: 

https://stackoverflow.com/questions/41570359/how-can-i-convert-a-py-to-exe-for-python-3-6

http://www.py2exe.org/index.cgi/Tutorial

https://mborgerson.com/creating-an-executable-from-a-python-script/

https://www.pythoncentral.io/pyinstaller-package-python-applications-windows-mac-linux/

https://milkator.wordpress.com/2014/07/19/windows-executable-from-python-developing-in-ubuntu/

https://github.com/pyinstaller/pyinstaller/issues/1566

https://fernandofreitasalves.com/how-to-create-python-exe-with-msi-installer-and-cx_freeze/

