# ROADMAP — CTF Reverse Engineering Write-ups
# ROADMAP — CTF Tersine Mühendislik Çözüm Yazıları

> **Course / Ders:** Reverse Engineering / Tersine Mühendislik (BGT210)  
> **Institution / Üniversite:** Istinye University  
> **Instructor / Danışman:** Keyvan Arasteh  
> **Student / Öğrenci:** Güneş Bingül — 2320191055  
> **Topic / Konu:** #23 — CTF RE Write-ups  
> **Semester / Dönem:** 2025-2026 Spring / Bahar

---

## Phase 0 / Faz 0: Understand Before You Build / Yazmadan Önce Anla

Tek satır kod yazmadan önce şu soruları yanıtladım:

| Soru | Cevap |
|------|-------|
| Proje nedir? | 5 CTF RE challenge çöz + her birini adım adım belgele |
| Nasıl çalışır? | Binary/script → RE araçları → gizli flag/serial ortaya çıkarılır |
| Girdiler/Çıktılar? | Binary/ELF/Python dosyası → flag + write-up belgesi |
| Hangi araçlar? | file, strings, ltrace, Ghidra, GDB, x64dbg, upx, Python |
| Neden bu araçlar? | Her araç farklı bir analiz katmanını karşılar — statik/dinamik/unpack |

---

## Phase 1 / Faz 1: Research & Investigation / Araştırma ve Keşif

> Klasör: `docs/research/` — Her challenge için ayrı alt klasör

| Konu | Durum | Notlar |
|------|-------|--------|
| ELF binary yapısı ve analizi | ✅ | `file`, `readelf`, `objdump` |
| Serial doğrulama mantığı desenleri | ✅ | strcmp, XOR, checksum |
| Python bytecode ve decompile | ✅ | `dis`, kaynak okuma |
| Packing/unpacking teknikleri | ✅ | UPX, imza tespiti |
| GDB dinamik analiz temelleri | ✅ | breakpoint, register inceleme |
| Windows PE analizi | ✅ | Ghidra + x64dbg |
| Java kaynak tersine mühendislik | ✅ | index mapping, Python |

---

## Phase 2 / Faz 2: Environment Setup / Ortam Kurulumu

- [x] Docker ile izole lab ortamı kuruldu
- [x] Araçlar kuruldu ve doğrulandı
  - Ghidra 11.x
  - GDB + pwndbg
  - radare2
  - Python 3.12
  - binutils (strings, objdump, readelf, file)
  - upx-ucl
  - ltrace, strace
- [x] `.env.example` oluşturuldu
- [x] Challenge dosyaları izole ortama indirildi

---

## Phase 3 / Faz 3: Implementation / Uygulama

### Challenge 1 — CrackMe Baby (CrackMes.one)
1. `file` ile binary türü tespit et
2. `strings` ile hardcoded değerleri tara
3. `ltrace` ile strcmp çağrısını yakala
4. Ghidra'da doğrula
5. Serial ile çalıştır → flag ✅

### Challenge 2 — vault-door-1 (picoCTF)
1. Java kaynak dosyasını oku
2. `checkPassword()` fonksiyonundaki karakter-indis eşleştirmesini haritala
3. Python dict ile şifreyi yeniden oluştur
4. Flag gönder ✅

### Challenge 3 — keygenme-py (picoCTF)
1. Python kaynak dosyasını oku
2. `check_key()` fonksiyonunu analiz et: MD5 + XOR + offset
3. Mantığı tersine çevir
4. Keygen scripti yaz
5. Üretilen key ile doğrula ✅

### Challenge 4 — Easy Crack Me (reversing.kr)
1. `file` ile Windows PE tespit et
2. `strings` ile success string bul
3. Ghidra'da 3 aşamalı kontrol mantığını oku
4. x64dbg'de strcmp breakpoint → register inceleme
5. Şifreyi gir → Congratulations ✅

### Challenge 5 — unpackme (picoCTF)
1. `file` ile UPX packing tespit et
2. `upx -d` ile paketi aç
3. Açılmış binary'de `strings` çalıştır
4. Ghidra'da akışı doğrula
5. Flag plaintext görünür ✅

---

## Phase 4 / Faz 4: Testing & Reporting / Test ve Raporlama

- [x] 5 challenge çözüldü ve flagler doğrulandı
- [x] Her challenge için ayrı araştırma notları yazıldı
- [x] Her çözüm adım adım Markdown write-up olarak belgelendi
- [x] Komutlar ve araç çıktıları kaydedildi
- [x] HTML infographic üretildi
- [x] Araçlar ve kaynaklar belgelendi

---

## Phase 5 / Faz 5: Delivery / Teslim

- [x] GitHub repo temiz ve düzenli
- [x] README.md eksiksiz (ders adı, kodu, öğrenci bilgileri)
- [x] Docker doğrulandı (`docker-compose up`)
- [x] Araştırma klasörleri ayrı ve düzenli
- [ ] Danışman collaborator olarak eklendi → **keyvanarasteh**

---

## What I Learned / Öğrendiklerim

**EN:**
The most valuable lesson was developing a *systematic methodology* — not just solving challenges randomly. Running `file` before anything else, then `strings`, then `ltrace` before opening a disassembler became instinctive. The keygenme-py challenge forced me to truly understand the validation logic rather than just finding a single key — writing a generalized keygen felt like real-world reverse engineering. The unpackme challenge taught me that packing is a one-layer defense: detect the packer, run one command, and the protection disappears. The hardest part overall was reading Ghidra's decompiled output for the Windows PE binary and mentally reconstructing the multi-stage check logic.

**TR:**
En değerli ders, *sistematik bir metodoloji* geliştirmekti — challenge'ları rastgele çözmek değil. Herhangi bir şeyden önce `file`, ardından `strings`, disassembler açmadan önce `ltrace` çalıştırmak içgüdüsel hale geldi. keygenme-py challenge'ı, tek bir key bulmak yerine doğrulama mantığını gerçekten anlamam için beni zorladı — genelleştirilmiş bir keygen yazmak gerçek dünya tersine mühendisliği gibi hissettirdi. unpackme challenge'ı, paketlemenin tek katmanlı bir savunma olduğunu öğretti: paketleyiciyi tespit et, bir komut çalıştır ve koruma ortadan kalkar. Genel olarak en zor kısım, Windows PE binary için Ghidra'nın decompile çıktısını okumak ve çok aşamalı kontrol mantığını zihinsel olarak yeniden oluşturmaktı.
