<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="docs/assets/istinye-university-logo.webp" alt="Istinye University" width="180"/>
  </a>

  # CTF Reverse Engineering Write-ups
  ### CTF Tersine Mühendislik Çözüm Yazıları

  ![GitHub](https://img.shields.io/badge/GitHub-Private-red?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT210-purple?style=flat-square)
  ![Topic](https://img.shields.io/badge/Topic-23-orange?style=flat-square)
  ![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)
</div>

---

## 🎓 Instructor / Danışman

| | |
|---|---|
| **Name / Ad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **Email** | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |
| **LinkedIn** | [keyvanarasteh](https://www.linkedin.com/in/keyvanarasteh/) |
| **Website** | [qline.tech](https://qline.tech) |

---

## 👤 Student / Öğrenci

| | |
|---|---|
| **Name / Ad Soyad** | Güneş Bingül |
| **Student ID / Öğrenci No** | `2320191055` |

---

## 📚 Course Information / Ders Bilgileri

| | |
|---|---|
| **Course Name / Ders Adı** | Reverse Engineering / Tersine Mühendislik |
| **Course Code / Ders Kodu** | BGT210 |
| **Credits / Kredi** | 3 ECTS |
| **Semester / Dönem** | 2025-2026 Spring / 2025-2026 Bahar |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |
| **Topic No / Konu No** | #23 |

---

## 📋 Project Overview / Proje Özeti

**EN:**
This project covers **Topic #23 — CTF Reverse Engineering Write-ups** from the BGT210 Reverse Engineering course at Istinye University. Five CTF (Capture The Flag) reverse engineering challenges were selected from platforms including picoCTF, CrackMes.one, and reversing.kr. Each challenge is documented with deep research notes, a step-by-step write-up, tool usage analysis, and key findings. The project demonstrates practical application of static analysis, dynamic analysis, packing detection, and keygen development techniques learned throughout the course.

**TR:**
Bu proje, İstinye Üniversitesi BGT210 Tersine Mühendislik dersinin **23. Konusu — CTF Tersine Mühendislik Çözüm Yazıları**'nı kapsamaktadır. picoCTF, CrackMes.one ve reversing.kr gibi platformlardan 5 CTF meydan okuması seçilmiştir. Her meydan okuma; derin araştırma notları, adım adım çözüm yazısı, araç kullanım analizi ve temel bulgularla belgelenmiştir. Proje; ders boyunca öğrenilen statik analiz, dinamik analiz, paket açma ve keygen geliştirme tekniklerinin pratik uygulamasını sergilemektedir.

---

## 🗂 Repository Structure / Repo Yapısı

```
.
├── README.md                          ← Bu dosya / This file
├── ROADMAP.md                         ← Proje yol haritası / Project roadmap
├── Dockerfile                         ← Docker ortamı / Docker environment
├── docker-compose.yml                 ← Docker compose
├── .env.example                       ← Ortam değişkenleri / Environment variables
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── modules/
│   │   └── ctf-writeups-module.md     ← Modül dokümantasyonu
│   │
│   ├── research/                      ← Derin araştırma klasörü
│   │   ├── challenge-01-crackme-baby/
│   │   │   ├── writeup.md             ← Çözüm yazısı
│   │   │   └── research-notes.md     ← Araştırma notları
│   │   ├── challenge-02-vault-door-1/
│   │   │   ├── writeup.md
│   │   │   └── research-notes.md
│   │   ├── challenge-03-keygenme-py/
│   │   │   ├── writeup.md
│   │   │   └── research-notes.md
│   │   ├── challenge-04-easy-crackme/
│   │   │   ├── writeup.md
│   │   │   └── research-notes.md
│   │   ├── challenge-05-unpackme/
│   │   │   ├── writeup.md
│   │   │   └── research-notes.md
│   │   └── infographic.html           ← Görsel RE akış rehberi
│   │
│   └── references/
│       └── tools-and-resources.md     ← Araçlar ve kaynaklar
│
├── src/
│   └── helper_scripts/
│       └── string_extractor.py        ← Analiz yardımcı scripti
│
└── reports/                           ← Çıktı raporları
```

---

## 🚀 Getting Started / Kurulum

```bash
git clone https://github.com/gunesbingul/bgt210-ctf-writeups
cd bgt210-ctf-writeups
cp .env.example .env
docker-compose up -d
```

---

## 🏆 CTF Challenges Solved / Çözülen CTF Meydan Okumaları

| # | Challenge | Platform | Difficulty | Core Technique | Status |
|---|-----------|----------|------------|----------------|--------|
| 1 | CrackMe Baby — Serial Check | CrackMes.one | Easy ⭐ | `strings` + `ltrace` → hardcoded serial | ✅ |
| 2 | vault-door-1 | picoCTF | Easy ⭐ | Java source reading + Python index map | ✅ |
| 3 | keygenme-py | picoCTF | Medium ⭐⭐ | MD5 + XOR reversal → keygen script | ✅ |
| 4 | Easy Crack Me | reversing.kr | Easy ⭐ | Ghidra + x64dbg → multi-stage check | ✅ |
| 5 | unpackme | picoCTF | Medium ⭐⭐ | UPX detection → `upx -d` → Ghidra | ✅ |

---

## 📊 Deliverables / Teslimler

| Deliverable | Status |
|-------------|--------|
| 5 CTF write-ups (step-by-step) | ✅ |
| Deep research notes per challenge | ✅ |
| Tool commands documented | ✅ |
| HTML Visual Infographic (RE Flow) | ✅ |
| Python helper script | ✅ |
| Docker environment | ✅ |
| References & resources | ✅ |

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| `file` | Binary type identification |
| `strings` | Printable string extraction |
| `ltrace` | Library call tracing |
| `strace` | System call tracing |
| `upx` | Packing/unpacking |
| `Ghidra` | Static decompilation & disassembly |
| `GDB` | Dynamic debugging (Linux) |
| `x64dbg` | Dynamic debugging (Windows) |
| `objdump` | Static binary analysis |
| `Python 3` | Helper scripts & keygen |

---

## 📚 Documentation / Belgeleme

Deep research notes → [`docs/research/`](./docs/research/)  
Module documentation → [`docs/modules/ctf-writeups-module.md`](./docs/modules/ctf-writeups-module.md)  
Tools & references → [`docs/references/tools-and-resources.md`](./docs/references/tools-and-resources.md)  
Visual RE flow → [`docs/research/infographic.html`](./docs/research/infographic.html)

---

## 🔗 References / Kaynaklar

- [picoCTF](https://picoctf.org) — Free CTF platform
- [CrackMes.one](https://crackmes.one) — Community crackme binaries
- [reversing.kr](http://reversing.kr) — Classic RE challenges
- [Ghidra](https://ghidra-sre.org) — NSA reverse engineering suite
- [CTF Field Guide](https://trailofbits.github.io/ctf/reversing/) — Trail of Bits
- [radare2 Book](https://book.rada.re) — Binary analysis reference
