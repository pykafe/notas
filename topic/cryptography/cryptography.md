### **Bem-vindo cryptography**

Instalasaun:

Imi bele install cryptography usa pip:

```$ pip install cryptography```

[Cryptography](https://cryptography.io/en/latest/) inklui parte rua ida ne’e mak “high level recipes” no “low level interfaces” ba cryptographic algorithms  komum mak hanesan sysmmetric cipher, message digests no chave derivasaun ba funsaun(key derivation function). Exemplo hanesan, atu encrypt ba buat ruma ho cryptographic’s  “high level symmetric encryption recipe”:

``` python
>>>from cryptography.fernet import Fernet
>>>key = Fernet.generate_key()
>>>f=Fernet(key)
>>>token = f.encrypt(b"Hello pykafe.")
>>>token
>>>'gAAAAABZTHeYe5qGgDZhW3JB31mK8gJomVH8ZxjDGMkVZ8BbfB-ZbYZfw_T4sIASmdy8FvCFvlIr-zmABc46CJGRt3oMPMPfqw=='
>>f.decrypt(token)
>>>'Hello pykafe.'
```
Se ita boot sira interese atu aprende barak kona ba field husi cryptography, ami recomenda ba imi , [crypto 101, by Laurens Van Houtven.](https://www.crypto101.io/)



[Django Framework](https://docs.djangoproject.com/en/1.11/topics/signing/)

### **Cryptographic signing**

Regra osan mean husi security web aplikasaun ne’e data nunka konfiansa husi fonte untrusted. Dala ruma ne’e bele usa atu passa data atraves untrusted medium.  "Cryptographically signed" nia valor bele passa atraves untrusted canal safe  iha koinesimentu ida ne’e tampering sei sai detekta.

**Protesaun ba SECRET_KEY**
Wainhira ita atu kria  projectu django foun ita startproject, iha file settings.py ne’e kriasaun automaticamente no hetan valor random  secret_key. Valor ne’e iha chave ba securing signed data – ne’e importante atu ita kontinua ne’e seguru, ou atakador bele usa ida ne’e ba generate valor sira ne’ebe hau signed.

**Usa ba low-level API**
```python
>>> from django.core.signing import Signer
>>>Signer = Signer()
>>>value = signer.sign(“catalpa international”)
>>>value
>>>original = signer.unsign(value)
>>>original
>>>from datetime import timedelta
>>>from django.core.signing import TimestampSigner
>>>signer = TimestampSigner()
>>>value = signer.sign(‘helllo’)
>>>value
>>>signer.unsign(value)
>>>signer.unsign(value, max_age=10)
>>>signer.unsign(value, max_age=20)
>>>signer.unsign(value, max_age=timedelta(seconds=20))
```

**Protesaun ba strutura data complexo**

Se ita hakarak atu proteja lista, tuple ou dictionary ita bele halo usa signin module’s dumps no funsaun loads.

```python
>>>from django.core import signing
>>>value = signing.dumps({“Niko”: “Mario”})
>>>value
>>>signing.loads(value)
```
Translate by: Ano