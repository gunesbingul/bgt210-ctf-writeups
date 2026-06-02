# Write-up: keygenme-py (picoCTF)
**Platform:** picoCTF | **Difficulty:** Medium ⭐⭐ | **Date:** 2026-06-02  
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🎯 Objective / Hedef

Python scripti bir lisans anahtarını doğruluyor. Doğrulama mantığını tersine çevir ve geçerli anahtar üreten bir keygen yaz.  
A Python script validates a license key. Reverse the validation logic and write a keygen.

---

## 🧠 Thought Process / Düşünce Süreci

**EN:** Python source is given. The challenge is not finding *a* key — it's understanding *why* the key is valid and writing a generalized keygen. This requires working backwards from the conditions.

**TR:** Python kaynağı verilmiş. Zorluk tek bir anahtar bulmak değil — anahtarın *neden* geçerli olduğunu anlamak ve genelleştirilmiş keygen yazmak. Koşullardan geriye doğru çalışmak gerekiyor.

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| Python 3 | Kaynak okuma + keygen yazma |
| `hashlib` | Challenge'daki MD5 kullanımını anla |

---

## 📋 Step-by-Step Solution / Adım Adım Çözüm

### Adım 1 — Kaynak dosyayı oku

```python
import hashlib

def check_key(key, username_trial):
    global key_full_template_trial

    if len(key) != 16:
        return False

    # username_trial'ın MD5'ini al
    md5_hash = hashlib.md5(username_trial.encode()).hexdigest()

    # İlk 8 hex karakterini 0x37 ile XOR et → şablon
    key_full_template_trial = "".join([
        chr(ord(c) ^ 0x37) for c in md5_hash[:8]
    ])

    return (
        key[0]  == key_full_template_trial[0]  and
        key[1]  == key_full_template_trial[1]  and
        key[2]  == chr(ord(key_full_template_trial[2]) + 2) and
        key[3]  == key_full_template_trial[3]  and
        key[4]  == key_full_template_trial[4]  and
        key[5]  == chr(ord(key_full_template_trial[5]) - 1) and
        key[6]  == key_full_template_trial[6]  and
        key[7]  == key_full_template_trial[7]  and
        key[8]  == key_full_template_trial[0]  and   # tekrar
        key[9]  == key_full_template_trial[1]  and
        key[10] == chr(ord(key_full_template_trial[2]) + 2) and
        key[11] == key_full_template_trial[3]  and
        key[12] == key_full_template_trial[4]  and
        key[13] == chr(ord(key_full_template_trial[5]) - 1) and
        key[14] == key_full_template_trial[6]  and
        key[15] == key_full_template_trial[7]
    )
```

---

### Adım 2 — Mantığı analiz et

Anahtar şablonu 3 adımda türetiliyor:

```
username_trial
      ↓
   MD5 hash
      ↓
   hex[:8]
      ↓
 XOR 0x37 (her karakter)
      ↓
key_full_template_trial  (8 karakter)
```

16 karakterlik anahtar = şablonun iki kez tekrarı, 2. ve 5. konumlarda ±offset:

| Pozisyon | Değer |
|----------|-------|
| 0,1,3,4,6,7 | `template[n]` (direkt) |
| 2, 10 | `template[2] + 2` |
| 5, 13 | `template[5] - 1` |
| 8–15 | 0–7'nin tekrarı |

---

### Adım 3 — Keygen yaz

```python
import hashlib

def keygen(username_trial):
    md5_hash = hashlib.md5(username_trial.encode()).hexdigest()
    template = [chr(ord(c) ^ 0x37) for c in md5_hash[:8]]

    key = [
        template[0], template[1],
        chr(ord(template[2]) + 2),
        template[3], template[4],
        chr(ord(template[5]) - 1),
        template[6], template[7],
        # tekrar
        template[0], template[1],
        chr(ord(template[2]) + 2),
        template[3], template[4],
        chr(ord(template[5]) - 1),
        template[6], template[7],
    ]
    return "".join(key)

username = "PICOCTF"
key = keygen(username)
print(f"Üretilen anahtar: {key}")
print(f"Flag: picoCTF{{{key}}}")
```

---

### Adım 4 — Doğrula

```python
assert check_key(keygen("PICOCTF"), "PICOCTF") == True
print("✅ Anahtar geçerli!")
```

---

## 🏁 Flag

```
picoCTF{<keygen("PICOCTF") çıktısı>}
```

---

## 📌 Key Findings / Temel Bulgular

| Bulgu | Detay |
|-------|-------|
| Hash fonksiyonu | MD5 — tersine çevrilemez, *ileri* çalışılır |
| Encoding | XOR 0x37 — tersine çevrilebilir (kendi tersidir) |
| Anahtar yapısı | 8 karakter şablon × 2 + 4 pozisyonda offset |
| Keygen | Herhangi bir username için çalışır |

**RE Dersi:** Tek bir anahtar bulmak yetmez — *neden geçerli olduğunu* anlamak asıl beceridir. Keygen yazmak, mantığın tam anlaşıldığının kanıtıdır.

---

## 🔍 Technique Catalog

| Teknik | Kullanıldı mı? | Not |
|--------|---------------|-----|
| Python kaynak analizi | ✅ | Temel yöntem |
| MD5 hash takibi | ✅ | hashlib.md5 tespit edildi |
| XOR decode | ✅ | 0x37 XOR tersine çevrildi |
| Keygen scripting | ✅ | Genelleştirilmiş keygen yazıldı |
| Brute force | ❌ | MD5 alanı çok büyük |
