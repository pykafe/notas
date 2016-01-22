# KODIGU GIT NIAN
##PROSSESSU ASSECU BA GIT IHA TERMINAL:
###Exemplu iha projetu issues nian:
	➜  ~  workon Issues 
	(Issues)➜  Issues  cd Issues 
	(Issues)➜  Issues git:(master) 

Clone repository husi [github](https://github.com/catalpainternational/issues.git) 

**git clone** hanesan prossesu ida ne'ebe atu halo ligasaun ita nia projetu ne'ebe ita halo iha ita nia komputador ho server [github](https://github.com/catalpainternational/issues.git) 

	(Issues)➜  Issues git:(master) git clone https://github.com/catalpainternational/issues.git
Kria **branch** foun antes atu halo ita nia serbisu iha ita nia projetu laran

	(Issues)➜  Issues git:(master) git checkout -b ony_branch origin

**Commit** ka halo komentariu antes atu push ba server [github](https://github.com/catalpainternational/issues.git) 
	
	(Issues)➜  Issues git:(ony_branch) git commit -m "fo komentariu iha ne'e"


**Push** ka dudu branch foun to'o server [github](https://github.com/catalpainternational/issues.git) 

	(Issues)➜  Issues git:(ony_branch)git push -u origin ony_branch
 

##Ho git  ita bele kontrola no kolabora hamutuk ita nia source kode
####Funsaun kodigu git nian
Remove branch

	(Issues)➜  Issues git:(ony_branch)git rm ony_branch

Show modified
	(Issues)➜  Issues git:(ony_branch)git status

Git **add**  hanesan atu aseita file ne'ebe mak ita modifika ka aumenta iha ita nia projetu laran, antes atu halo commit ka push ba server [github](https://github.com/catalpainternational/issues.git) nian.

	(Issues)➜  Issues git:(ony_branch)git add support/issues/templates/base.html

Ka ita bele **add all** exemplu

	(Issues)➜  Issues git:(ony_branch)git add .

Git **commit**  nia funsaun atu halo komentariu ante atu push ba server [github](https://github.com/catalpainternational/issues.git).

	(Issues)➜  Issues git:(ony_branch) git commit -m "fo komentariu iha ne'e"

Git **push** nia funsaun atu dudu ita projetu ne'ebe ita halo modifika ka aumenta ona ba server [github](https://github.com/catalpainternational/issues.git).

	(Issues)➜  Issues git:(ony_branch)git push

Git **pull** nia funsaun atu dada file ne'ebe mak team project sira push ona ba server [github](https://github.com/catalpainternational/issues.git), mai ita nia komputador