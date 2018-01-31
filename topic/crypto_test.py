#PYTHON  SHELL

####PYTHON SHELL FROM ISSUES PROJECT
	>>> User.objects.filter(is_staff=False)
	[<User: Boby>, <User: mary>, <User: nany>]
	>>> User.objects.filter(is_staff=True)
	[<User: ony>]
	>>> User.objects.exclude(is_staff=True)
	[<User: Boby>, <User: mary>, <User: nany>]
	>>> from django.db.models import Avg, Sum, Count
	>>> user.assigned_issues.all()
	[<Issue: Issue 1 created 2015-10-10>, <Issue: Issue 2 created 2015-10-10>, <Issue: Issue 3 created 2015-10-10>, <Issue: Issue 4 created 2015-10-10>, <Issue: Issue 5 created 2015-10-10>, <Issue: Issue 6 created 2015-10-12>, <Issue: Issue 9 created 2015-10-18>, <Issue: Issue 10 created 2015-10-18>, <Issue: Issue 11 created 2015-10-18>, <Issue: Issue 12 created 2015-10-18>]

	>>> User.objects.aggregate(Count('assigned_issues'), Count('issuecomment'))
	{'issuecomment__count': 199, 'assigned_issues__count': 199}
	>>> User.objects.all().count()
	4
	>>> 
	>>> 
	>>> 
	>>> users = User.objects.annotate(Count('assigned_issues', distinct=True))
	>>> User.objects.aggregate(Count('assigned_issues'))
	{'assigned_issues__count': 13}
	>>> total_assigned_issues = User.objects.aggregate(Count('assigned_issues'))
	>>> total_assigned_issues
	{'assigned_issues__count': 13}
	
	>>> total_assigned_issues = total_assigned_issues['assigned_issues__count']
	>>> total_assigned_issues
	13 
	>>> for user in users:
	...     print user.username, user.assigned_issues__count / total_assigned_issues * 100.0
	... 
	ony 0.0
	Boby 0.0
	mary 0.0
	nany 0.0
	>>> 
	>>> 
	>>> 

	os.path.abspath('/")
	os.path.abspath('hello.txt')
	os.path.

###RUN TEST PHOTOGRAF
	py.test lesson1/test_task4.py

	>>> from lesson1.task4 import get_shifted_letter
	>>> from lesson1.task5 import get_shifted_letter
	>>> from lesson1.task5 import get_shifted_string
	>>> get_shifted_string('AGORA', 2)
	'CIQTC'


	>>> from lesson1.task6 import get_solutions
	>>> get_solutions()
ILOD IDOL PDL
PDL KDNVRORN KDX
VH ODH, KDX PDWH
VH PDN KDGRPL R

JMPE JEPM QEM
QEM LEOWSPSO LEY
WI PEI, LEY QEXI
WI QEO LEHSQM S

KNQF KFQN RFN
RFN MFPXTQTP MFZ
XJ QFJ, MFZ RFYJ
XJ RFP MFITRN T

LORG LGRO SGO
SGO NGQYURUQ NGA
YK RGK, NGA SGZK
YK SGQ NGJUSO U

MPSH MHSP THP
THP OHRZVSVR OHB
ZL SHL, OHB THAL
ZL THR OHKVTP V

NQTI NITQ UIQ
UIQ PISAWTWS PIC
AM TIM, PIC UIBM
AM UIS PILWUQ W

ORUJ OJUR VJR
VJR QJTBXUXT QJD
BN UJN, QJD VJCN
BN VJT QJMXVR X

PSVK PKVS WKS
WKS RKUCYVYU RKE
CO VKO, RKE WKDO
CO WKU RKNYWS Y

QTWL QLWT XLT
XLT SLVDZWZV SLF
DP WLP, SLF XLEP
DP XLV SLOZXT Z

RUXM RMXU YMU
YMU TMWEAXAW TMG
EQ XMQ, TMG YMFQ
EQ YMW TMPAYU A

SVYN SNYV ZNV
ZNV UNXFBYBX UNH
FR YNR, UNH ZNGR
FR ZNX UNQBZV B

TWZO TOZW AOW
AOW VOYGCZCY VOI
GS ZOS, VOI AOHS
GS AOY VORCAW C

UXAP UPAX BPX
BPX WPZHDADZ WPJ
HT APT, WPJ BPIT
HT BPZ WPSDBX D

VYBQ VQBY CQY
CQY XQAIEBEA XQK
IU BQU, XQK CQJU
IU CQA XQTECY E

WZCR WRCZ DRZ
DRZ YRBJFCFB YRL
JV CRV, YRL DRKV
JV DRB YRUFDZ F

XADS XSDA ESA
ESA ZSCKGDGC ZSM
KW DSW, ZSM ESLW
KW ESC ZSVGEA G

YBET YTEB FTB
FTB ATDLHEHD ATN
LX ETX, ATN FTMX
LX FTD ATWHFB H

ZCFU ZUFC GUC
GUC BUEMIFIE BUO
MY FUY, BUO GUNY
MY GUE BUXIGC I

ADGV AVGD HVD
HVD CVFNJGJF CVP
NZ GVZ, CVP HVOZ
NZ HVF CVYJHD J

BEHW BWHE IWE
IWE DWGOKHKG DWQ
OA HWA, DWQ IWPA
OA IWG DWZKIE K

CFIX CXIF JXF
JXF EXHPLILH EXR
PB IXB, EXR JXQB
PB JXH EXALJF L

DGJY DYJG KYG
KYG FYIQMJMI FYS
QC JYC, FYS KYRC
QC KYI FYBMKG M

EHKZ EZKH LZH
LZH GZJRNKNJ GZT
RD KZD, GZT LZSD
RD LZJ GZCNLH N

FILA FALI MAI
MAI HAKSOLOK HAU
SE LAE, HAU MATE
SE MAK HADOMI O

GJMB GBMJ NBJ
NBJ IBLTPMPL IBV
TF MBF, IBV NBUF
TF NBL IBEPNJ P

HKNC HCNK OCK
OCK JCMUQNQM JCW
UG NCG, JCW OCVG
UG OCM JCFQOK Q


	>>> my_string = "abcdefghijklmnopqrstuvxz"
	>>> len(my_string)
	24
	>>> my_string[2]
	'c'
	>>> my_string[3]
	'd'
	>>> my_string[4]
	'e'
	>>> my_string[5]
	'f'
	>>> my_string.find("j")
	9
	>>> my_string.find("10")
	-1


####DIFFERENTS WHICH PYTHON VERSION.
####Python-2.7. and Ptrhon-3.5.

Ptrhon-3.5.

	➜  enviroments  source venv3.5/bin/activate
	(venv3.5) ➜  enviroments  python 3 -m venv env3.5
	python: can't open file '3': [Errno 2] No such file or directory
	(venv3.5) ➜  enviroments  python3 -m venv env3.5 
	(venv3.5) ➜  enviroments  ls                         
	env2.7  env3.5  venv3.5
	(venv3.5) ➜  enviroments  rm -r venv3.5 
	(venv3.5) ➜  enviroments  ls
	env2.7  env3.5
	(venv3.5) ➜  enviroments  source env3.5/bin/activate 
	(env3.5) ➜  enviroments  ls
	env2.7  env3.5
	(env3.5) ➜  enviroments  




####BYTE_ARRAY:

	>>> hello ="hello"
	>>> hello
	'hello'
	>>> hello[0]
	'h'
	>>> hello[1]
	'e'
	>>> hello[2]
	'l'
	>>> byte_array = bytearray([128, 143, 104])
	>>> byte_array
	bytearray(b'\x80\x8fh')
	>>> byte_array[0]
	128
	>>> byte_array[2]
	104
	>>> byte_array[0] = 108
	>>> byte_array
	bytearray(b'l\x8fh')

####PYTHON STRING
	>>> a_string = "Hello i am a string"
	>>> a_string
	'Hello i am a string'
	>>> a_string.encode()
	b'Hello i am a string'
	>>> a_string.encode()[0]
	72
	>>> a_string.encode()[1]
	101
	>>> a_string.encode()[2]
	108
	>>> a_string.encode('ascii')
	b'Hello i am a string'
	>>> a_string.encode('latin1')
	b'Hello i am a string' 
	>>> byte_array =bytearray(a_string.encode('ascii'))
	>>> byte_array
	bytearray(b'Hello i am a string')
	>>> byte_array.decode('ascii')
	'Hello i am a string'
	>>> "hellooo".encode('ascii')
	b'hellooo'
	>>> type("hellooo".encode('ascii'))
	<class 'bytes'>
	>>> "hellooo".encode('ascii')[3]
	108
	>>> "hellooo".encode('ascii').decode('ascii')
	'hellooo'
	>>> type("hellooo".encode('ascii').decode('ascii'))
	<class 'str'>
	>>> type("string")
	<class 'str'>
	>>> type("string".encode('ascii'))
	<class 'bytes'>
	>>> 260 % 256
	4
	>>> 255 % 256
	255
	>>> 256 % 256
	0
	>>> 257 % 256
	1

