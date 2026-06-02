# Write-up: unpackme (picoCTF)
**Platform:** picoCTF | **Difficulty:** Medium ⭐⭐ | **Date:** 2026-06-02  
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🎯 Objective / Hedef

Binary paketlenmiş. Paketi aç ve gizli flag'i bul.  
The binary is packed. Unpack it and find the hidden flag.

---

## 🧠 Thought Process / Düşünce Süreci

**EN:** `strings` on a packed binary returns mostly garbage. The real strings are compressed inside. Detect the packer → unpack → treat as a normal binary.

**TR:** Paketlenmiş binary üzerinde `strings` çoğunlukla anlamsız karakter döndürür. Gerçek stringler içeride sıkıştırılmış. Paketleyiciyi tespit et → aç → normal binary gibi analiz et.

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| `file` | UPX packing tespiti |
| `strings` | Packer imzasını doğrula |
| `upx` | Paketi aç |
| `strings` (tekrar) | Açılmış binary'de gerçek stringler |
| `Ghidra` | Program akışını doğrula |

---

## 📋 Step-by-Step Solution / Adım Adım Çözüm

### Adım 1 — Dosyayı tanımla

```bash
$ file unpackme
unpackme: ELF 64-bit LSB executable, x86-64, UPX compressed
```

`file` doğrudan UPX paketlemesini tespit etti.

---

### Adım 2 — Strings ile doğrula

```bash
$ strings unpackme | grep -i upx
UPX!
$Info: This file is packed with the UPX executable packer
$Id: UPX 4.02
```

UPX imza stringleri görünüyor — hangi paketi açıcıyı kullanacağımızı kesin biliyoruz.

---

### Adım 3 — Paketi aç

```bash
$ upx -d unpackme -o unpackme_unpacked

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     28672 <-     12288   42.86%   linux/amd64   unpackme_unpacked

Unpacked 1 file.
```

Dosya boyutu ~12KB'den ~28KB'ye çıktı — orijinal kod geri yüklendi.

---

### Adım 4 — Açılmış binary'de strings çalıştır

```bash
$ strings unpackme_unpacked | grep -i picoctf
picoCTF{up><_m3_f7w_5c717b6e}
```

Flag plaintext olarak görünüyor.

---

### Adım 5 — Ghidra ile program akışını doğrula

```c
int main() {
    int input;
    printf("What's my favorite number? ");
    scanf("%d", &input);
    if (input == 754635) {
        printf("picoCTF{up><_m3_f7w_5c717b6e}\n");
    } else {
        printf("Is this a keygenme?\n");
    }
    return 0;
}
```

Flag, `input == 754635` koşulunda yazdırılıyor. `strings` ile `.rodata`'dan zaten okuduk.

---

## 🏁 Flag

```
picoCTF{up><_m3_f7w_5c717b6e}
```

---

## 📌 Key Findings / Temel Bulgular

| Bulgu | Detay |
|-------|-------|
| Packer | UPX 4.02 |
| Unpack yöntemi | `upx -d` — tek komut |
| Koruma sonrası | Plaintext flag `.rodata`'da |
| Magic number | 754635 |

**RE Dersi:** Packing tek katmanlı savunmadır. Paketi aç → normal analiz. Yaygın packerlar: UPX (kolay), MPRESS (orta), Themida (zor).

---

## 🔍 Technique Catalog

| Teknik | Kullanıldı mı? | Not |
|--------|---------------|-----|
| Packing tespiti (`file`) | ✅ | UPX anında tanındı |
| `strings` (packed) | ✅ | Sadece imza görüldü |
| UPX unpacking | ✅ | `upx -d` tek komut |
| `strings` (unpacked) | ✅ | Flag plaintext |
| Ghidra | ✅ | Akış ve magic number doğrulandı |
