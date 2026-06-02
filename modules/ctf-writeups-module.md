# Module: CTF Reverse Engineering Write-ups (#23)
**Course / Ders:** BGT210 Reverse Engineering — Tersine Mühendislik  
**Institution:** Istinye University | **Student:** Güneş Bingül — 2320191055

---

## Purpose / Amaç

5 CTF reverse engineering challenge'ı seç, çöz ve her birini derin araştırma notları + adım adım write-up ile belgele.  
Select, solve, and document 5 CTF reverse engineering challenges with deep research notes and step-by-step write-ups.

---

## How It Works / Nasıl Çalışır

1. Platform'dan challenge binary veya kaynak dosyasını indir
2. RE metodolojisini uygula: `file` → `strings` → `ltrace` → Ghidra → GDB
3. Doğru cevabı (serial / flag / şifre) bul
4. Gerçek binary ile doğrula
5. Ayrı klasörde write-up + araştırma notları yaz

---

## Challenges / Meydan Okumalar

| # | Klasör | Platform | Zorluk | Teknik |
|---|--------|----------|--------|--------|
| 1 | `challenge-01-crackme-baby/` | CrackMes.one | ⭐ | strings + ltrace |
| 2 | `challenge-02-vault-door-1/` | picoCTF | ⭐ | Java source + Python |
| 3 | `challenge-03-keygenme-py/` | picoCTF | ⭐⭐ | MD5+XOR keygen |
| 4 | `challenge-04-easy-crackme/` | reversing.kr | ⭐ | Ghidra + x64dbg |
| 5 | `challenge-05-unpackme/` | picoCTF | ⭐⭐ | UPX unpack + Ghidra |

---

## RE Methodology / RE Metodolojisi

```
file      → tür, mimari, packing?
strings   → hardcoded değerler var mı?
ltrace    → strcmp/memcmp yakalanabilir mi?
Ghidra    → decompile, başarı string'inden geriye git
GDB/x64dbg → dinamik doğrulama
Python    → karmaşık yeniden yapılandırma için script
```

---

## Usage / Kullanım

```bash
docker-compose up -d
docker exec -it ctf-re bash
python src/helper_scripts/string_extractor.py <binary>
```

---

## Known Limitations / Bilinen Kısıtlamalar

- Gerçek binary dosyalar repoya dahil edilmemiştir (platform lisansları)
- Windows PE challenge'ları (challenge-04) Wine veya Windows VM gerektirir
- Screenshots klasörü boş — gerçek çalışmada araç çıktıları kaydedilmeli
