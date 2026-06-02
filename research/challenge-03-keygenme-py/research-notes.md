# Research Notes — Challenge 03: keygenme-py
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## Araştırdığım Konu

Python tabanlı lisans doğrulama sistemlerinde MD5 + XOR kombinasyonunun tersine mühendisliği ve keygen geliştirme.

---

## Ön Araştırma — MD5 Hash Fonksiyonu

| Özellik | Detay |
|---------|-------|
| Çıktı uzunluğu | 128 bit = 32 hex karakter |
| Tersine çevrilebilir mi? | Hayır — tek yönlü fonksiyon |
| Kullanım amacı | Veri bütünlüğü, (eski) şifre saklama |
| Güvenli mi? | Hayır — collision saldırılarına karşı kırılgan |

**Önemli Bulgu:** MD5 tersine çevrilemez. Bu yüzden `username → MD5 → template` zincirinde *ileri* gidilir, geriye değil.

---

## XOR Encoding Analizi

```python
# XOR ile encoding
encoded = chr(ord('a') ^ 0x37)   # 'a' = 97, 97 ^ 55 = 86 = 'V'

# XOR kendi tersidir! Aynı işlem decode eder:
decoded = chr(ord('V') ^ 0x37)   # 86 ^ 55 = 97 = 'a'

# Yani: encode == decode (XOR için)
assert (ord('a') ^ 0x37 ^ 0x37) == ord('a')
```

XOR ile encode edilmiş değeri decode etmek için aynı anahtar ile tekrar XOR yapılır.

---

## Keygen Tasarım Prensipleri

İyi bir keygen:
1. **Deterministik** — aynı username her zaman aynı key'i üretir
2. **Genelleştirilmiş** — sadece bir username için değil, tümü için çalışır
3. **Doğrulanabilir** — `check_key(keygen(user), user) == True` her zaman

```python
# Test: keygen her zaman check_key'i geçmeli
for test_user in ["PICOCTF", "test", "user123", "admin"]:
    key = keygen(test_user)
    assert check_key(key, test_user) == True
    print(f"✅ {test_user}: {key}")
```

---

## Offset Pattern Analizi

```
Pozisyon:  0  1  2      3  4  5      6  7
Şablon:    t0 t1 t2+2   t3 t4 t5-1  t6 t7
           └──────────────────────────────┘
                      × 2 (tekrar)
Pozisyon:  8  9  10     11 12 13     14 15
```

Bu yapı gerçek dünya lisans sistemlerinde sıkça görülür — checksum karakterleri eklenerek basit brute force engellenmeye çalışılır.

---

## Bulunan Kaynaklar

- [hashlib Python docs](https://docs.python.org/3/library/hashlib.html)
- [XOR cipher explained](https://en.wikipedia.org/wiki/XOR_cipher)
- [picoCTF keygenme challenge](https://picoctf.org)
- [Keygen tutorial — LiveOverflow](https://www.youtube.com/@LiveOverflow)

---

## Temel Bulgular

1. MD5 → ileri çalış, geriye değil
2. XOR → kendi tersidir, `val ^ key ^ key == val`
3. Keygen = doğrulama fonksiyonunun tam tersi
4. Offset (+2, -1) → şablondan türetilmiş checksum karakterleri

---

## Sonuç

Bu challenge, gerçek dünya lisans sistemi tasarımının basit bir modelini sunuyor. MD5 + XOR kombinasyonu zayıf bir koruma sağlıyor çünkü XOR tersine çevrilebilir ve MD5 çıktısı deterministik. Gerçek lisans sistemleri RSA imzalama veya HMAC kullanır.
