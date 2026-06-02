# Research Notes — Challenge 02: vault-door-1
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## Araştırdığım Konu

Java kaynak kodunda obfuscation olarak kullanılan "indis karıştırma" tekniği ve tersine çevirme yöntemi.

---

## Ön Araştırma — Java Source-Level Obfuscation

Java'da kaynak seviyesinde obfuscation teknikleri:

| Teknik | Açıklama | Çözüm |
|--------|----------|-------|
| İndis karıştırma | `charAt(n)` sırası karıştırılmış | Python dict ile eşleştir |
| String parçalama | String parçalara bölünmüş | Birleştir |
| Char casting | `(char)(65)` → 'A' | Cast değerlerini hesapla |
| XOR encoding | `(char)(val ^ 0x42)` | XOR'u geri al |

---

## charAt() Güvenlik Analizi

```java
// ZAYIF — indis karıştırma kolayca tersine çevrilir
password.charAt(0) == 'd' &&
password.charAt(5) == '4' &&
// ...

// DAHA GÜÇLÜ — hash + salt
MessageDigest.getInstance("SHA-256")
    .digest((password + salt).getBytes())
```

`charAt()` karşılaştırması ne kadar karıştırılırsa karıştırılsın, her indis bağımsız olarak okunabilir ve bir sözlükte toplanabilir.

---

## Python Çözüm Yaklaşımı

```python
# Genel yaklaşım: regex ile Java kodundan otomatik parse
import re

java_code = open("VaultDoor1.java").read()
matches = re.findall(r'charAt\((\d+)\)\s*==\s*\'(.)\'', java_code)
chars = {int(i): c for i, c in matches}
password = ''.join(chars[i] for i in range(max(chars)+1))
print(password)
```

Bu yaklaşım, Java dosyasını elle okumak zorunda kalmadan otomatik parse eder.

---

## Bulunan Kaynaklar

- [picoCTF vault-door series](https://picoctf.org) — 8 challenge serisi, her biri farklı Java obfuscation
- [Java charAt() docs](https://docs.oracle.com/en/java/docs)
- [Python re module](https://docs.python.org/3/library/re.html)

---

## Temel Bulgular

1. Java kaynak obfuscation — binary analiz gerekmez, mantık okuma yeterlidir
2. İndis karıştırma — en basit obfuscation tekniklerinden biri
3. Otomatik regex parse — büyük charAt zincirlerini elle okumak yerine script ile çöz
4. picoCTF vault-door serisi — 1'den 8'e giderek zorlaşır, her seviye farklı teknik

---

## Sonuç

Bu challenge, kaynak seviyesi obfuscation'ın ne kadar zayıf olduğunu gösteriyor. Kod ne kadar karıştırılırsa karıştırılsın, okunabilir kaynak varsa tersine çevirmek için binary araçlara gerek yoktur. Gerçek koruma ancak derleme sonrası yapılan obfuscation (ProGuard, R8) ile sağlanabilir.
