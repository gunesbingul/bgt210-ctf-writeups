# Write-up: vault-door-1 (picoCTF)
**Platform:** picoCTF | **Difficulty:** Easy ⭐ | **Date:** 2026-06-02  
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🎯 Objective / Hedef

Java kaynak dosyası verilmiş. Vault'u açan doğru şifreyi bul.  
A Java source file is provided. Find the correct password that unlocks the vault.

---

## 🧠 Thought Process / Düşünce Süreci

**EN:** Source code is given — no binary tools needed. Pure logic reading. The validation function checks characters at specific (shuffled) indices. Map each index to its character, reconstruct the string.

**TR:** Kaynak kod verilmiş — binary araç gerekmez. Saf kod okuma. Doğrulama fonksiyonu, karakterleri karışık indislerde kontrol ediyor. Her indisi karakteriyle eşle, string'i yeniden oluştur.

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| Metin editörü | Java kaynak okuma |
| Python 3 | İndis → karakter eşleştirmesi ile şifreyi yeniden oluştur |

---

## 📋 Step-by-Step Solution / Adım Adım Çözüm

### Adım 1 — Kaynak dosyayı oku

`VaultDoor1.java` içeriği (sadece `checkPassword` fonksiyonu):

```java
public boolean checkPassword(String password) {
    return password.length() == 32 &&
           password.charAt(0)  == 'd' &&
           password.charAt(29) == 'a' &&
           password.charAt(4)  == 'r' &&
           password.charAt(2)  == '5' &&
           password.charAt(23) == 'r' &&
           password.charAt(3)  == 'c' &&
           password.charAt(17) == '4' &&
           password.charAt(1)  == '3' &&
           password.charAt(7)  == 'b' &&
           password.charAt(10) == '_' &&
           password.charAt(5)  == '4' &&
           password.charAt(9)  == '3' &&
           password.charAt(11) == 't' &&
           password.charAt(15) == 'c' &&
           password.charAt(8)  == 'l' &&
           password.charAt(12) == 'H' &&
           password.charAt(20) == 'c' &&
           password.charAt(14) == '_' &&
           password.charAt(6)  == 'c' &&
           password.charAt(24) == '5' &&
           password.charAt(18) == 'r' &&
           password.charAt(13) == '3' &&
           password.charAt(19) == '4' &&
           password.charAt(21) == 'T' &&
           password.charAt(16) == 'H' &&
           password.charAt(27) == 'f' &&
           password.charAt(30) == 'c' &&
           password.charAt(25) == '_' &&
           password.charAt(22) == '3' &&
           password.charAt(28) == 'l' &&
           password.charAt(26) == 'f' &&
           password.charAt(31) == 'e';
}
```

---

### Adım 2 — Python ile şifreyi yeniden oluştur

```python
chars = {
    0:'d',  1:'3',  2:'5',  3:'c',  4:'r',  5:'4',  6:'c',
    7:'b',  8:'l',  9:'3', 10:'_', 11:'t', 12:'H', 13:'3',
   14:'_', 15:'c', 16:'H', 17:'4', 18:'r', 19:'4', 20:'c',
   21:'T', 22:'3', 23:'r', 24:'5', 25:'_', 26:'f', 27:'f',
   28:'l', 29:'a', 30:'c', 31:'e'
}

password = ''.join(chars[i] for i in range(32))
print(f"picoCTF{{{password}}}")
```

**Çıktı:**
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

---

### Adım 3 — Doğrula

Flag platforma gönderildi → ✅ Kabul edildi.

![vault-door-1 challenge sayfası](screenshots/vault-door-1-challenge.png)  
*picoCTF platform — vault-door-1 challenge sayfası ve flag giriş ekranı*

---

## 🏁 Flag

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}
```

---

## 📌 Key Findings / Temel Bulgular

| Bulgu | Detay |
|-------|-------|
| Koruma türü | İndis karıştırma — source-level obfuscation |
| Çözüm yöntemi | Python sözlüğü ile indis eşleştirme |
| Binary araç | Gerekmedi |
| Çözüm süresi | ~5 dakika |

**RE Dersi:** Kaynak varsa asıl zorluk araç kullanmak değil, *mantığı okumaktır*. Veri yapısını haritala, 10 satır Python yaz, bitti.

---

## 🔍 Technique Catalog

| Teknik | Kullanıldı mı? | Not |
|--------|---------------|-----|
| Kaynak kodu analizi | ✅ | Temel yöntem |
| Python indis eşleştirme | ✅ | 10 satırda çözüm |
| Binary araçlar | ❌ | Gerekmedi |
