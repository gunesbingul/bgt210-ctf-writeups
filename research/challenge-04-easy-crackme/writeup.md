# Write-up: Easy Crack Me (reversing.kr)
**Platform:** reversing.kr | **Difficulty:** Easy ⭐ | **Date:** 2026-06-02  
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🎯 Objective / Hedef

Windows PE binary şifre istiyor. Doğru şifreyi bul.  
A Windows PE binary asks for a password. Find the correct password.

---

## 🧠 Thought Process / Düşünce Süreci

**EN:** Windows PE binary — plan: static first with Ghidra, then dynamic with x64dbg if needed. Expected: user input goes through checks, compared against a constant.

**TR:** Windows PE binary — plan: önce Ghidra ile statik, gerekirse x64dbg ile dinamik. Beklenti: kullanıcı girdisi kontrollerden geçirilip sabit değerle karşılaştırılıyor.

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| `file` | PE yapısını tanımla |
| `strings` | Success string bul |
| `Ghidra` | Statik decompile — doğrulama mantığını oku |
| `x64dbg` | Dinamik debug — strcmp breakpoint |

---

## 📋 Step-by-Step Solution / Adım Adım Çözüm

### Adım 1 — Dosyayı tanımla

```bash
$ file EasyCrackMe.exe
EasyCrackMe.exe: PE32 executable (GUI) Intel 80386, for MS Windows
```

32-bit Windows GUI uygulaması.

---

### Adım 2 — Strings ile tara

```bash
$ strings EasyCrackMe.exe
...
Congratulations!
EasyCrackMe
Incorrect Password
```

`Congratulations!` var ama plaintext şifre görünmüyor → Ghidra gerekli.

---

### Adım 3 — Ghidra ile statik analiz

`Window → Defined Strings` → `Congratulations` → çift tıkla → referans lokasyonuna atla.

Decompile çıktısı (sadeleştirilmiş):

```c
void validate_password(char *input) {
    // Kontrol 1: ikinci karakter 'E' olmalı
    if (input[1] != 'E') {
        MessageBox(NULL, "Incorrect Password", "EasyCrackMe", MB_OK);
        return;
    }
    // Kontrol 2: 2. indisten itibaren "asy" olmalı
    if (strncmp(input + 2, "asy", 3) != 0) {
        MessageBox(NULL, "Incorrect Password", "EasyCrackMe", MB_OK);
        return;
    }
    // Kontrol 3: tam string karşılaştırması
    if (strcmp(input, "Ea5yR3versing") != 0) {
        MessageBox(NULL, "Incorrect Password", "EasyCrackMe", MB_OK);
        return;
    }
    MessageBox(NULL, "Congratulations!", "EasyCrackMe", MB_OK);
}
```

3 aşamalı kontrol — tümünü karşılayan string: `Ea5yR3versing`

---

### Adım 4 — x64dbg ile doğrula

`strcmp` çağrısına breakpoint → binary çalıştır → breakpoint tetiklendiğinde:

```
EAX → girdi stringimiz
EDX → "Ea5yR3versing"
```

Statik analizimiz doğrulandı.

---

### Adım 5 — Şifreyi gir

```
Şifre: Ea5yR3versing
→ ✅ Congratulations!
```

---

## 🏁 Flag / Şifre

```
Ea5yR3versing
```

---

## 📌 Key Findings / Temel Bulgular

| Bulgu | Detay |
|-------|-------|
| Koruma türü | Çok aşamalı kontrol (3 adım) |
| Karşılaştırma | `strncmp` + `strcmp` |
| Anti-debug | Tespit edilmedi |
| Packing | Tespit edilmedi |

**RE Dersi:** Çok aşamalı kontroller, her adımın bağımsız olarak kırılabileceğini ve sonuçların birleştirileceğini gösteriyor. Her zaman başarı mesajından geriye doğru tüm dalları takip et.

---

## 🔍 Technique Catalog

| Teknik | Kullanıldı mı? | Not |
|--------|---------------|-----|
| PE tanımlama | ✅ | `file` komutu |
| `strings` recon | ✅ | Başarı string'i bulundu |
| Ghidra statik | ✅ | 3 aşamalı kontrol okundu |
| x64dbg dinamik | ✅ | Breakpoint ile doğrulandı |
