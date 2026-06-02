# Write-up: CrackMe Baby — Serial Check
**Platform:** CrackMes.one | **Difficulty:** Easy ⭐ | **Date:** 2026-06-02  
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🎯 Objective / Hedef

Binary'nin geçerli girdi olarak kabul ettiği doğru seri numarasını bul.  
Find the correct serial number that the binary accepts as valid input.

---

## 🧠 Thought Process / Düşünce Süreci

**EN:** My approach: first understand what the file *is*, then gather quick intel with `strings`, only open a disassembler if still needed. I expected a simple string comparison or a small XOR transformation on the input.

**TR:** Yaklaşımım: önce dosyanın ne olduğunu anla, sonra `strings` ile hızlı bilgi topla, gerekirse disassembler aç. Basit bir string karşılaştırması ya da küçük bir XOR dönüşümü bekliyordum.

---

## 🛠 Tools Used / Kullanılan Araçlar

| Tool | Purpose |
|------|---------|
| `file` | Binary türünü belirle |
| `strings` | Hardcoded değerleri tara |
| `ltrace` | Çalışma zamanı kütüphane çağrılarını izle |
| `Ghidra` | Decompile ile doğrulama mantığını oku |

---

## 📋 Step-by-Step Solution / Adım Adım Çözüm

### Adım 1 — Dosyayı tanımla

```bash
$ file crackme_baby
crackme_baby: ELF 32-bit LSB executable, Intel 80386, dynamically linked
```

32-bit ELF Linux binary. Dinamik bağlantılı → `ltrace` ile izlenebilir.

---

### Adım 2 — Strings ile tara

```bash
$ strings crackme_baby
/lib/ld-linux.so.2
strcmp
puts
Enter serial:
Wrong serial!
Correct! Here is your flag: FLAG{...}
s3cr3t_k3y_42
```

`strings` hemen `s3cr3t_k3y_42` değerini ortaya çıkardı. Başarı ve hata mesajları da görünüyor.

---

### Adım 3 — Test et

```bash
$ ./crackme_baby
Enter serial: s3cr3t_k3y_42
Correct! Here is your flag: FLAG{cr4ckm3_b4by_w4s_3asy}
```

✅ İlk denemede doğrulandı.

---

### Adım 4 — ltrace ile doğrula

```bash
$ ltrace ./crackme_baby
Enter serial: test
strcmp("test", "s3cr3t_k3y_42") = -1
puts("Wrong serial!")
```

`strcmp` girdimizi birinci argüman, `s3cr3t_k3y_42`'yi ikinci argüman olarak alıyor. Klasik hardcoded seri kontrolü.

---

### Adım 5 — Ghidra ile kaynak mantığı

```c
int main(void) {
    char input[64];
    printf("Enter serial: ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;
    if (strcmp(input, "s3cr3t_k3y_42") == 0) {
        puts("Correct! Here is your flag: FLAG{cr4ckm3_b4by_w4s_3asy}");
    } else {
        puts("Wrong serial!");
    }
    return 0;
}
```

Obfuscation yok, anti-debug yok. Serial `.rodata` bölümünde düz metin.

---

## 🏁 Flag

```
FLAG{cr4ckm3_b4by_w4s_3asy}
```

---

## 📌 Key Findings / Temel Bulgular

| Bulgu | Detay |
|-------|-------|
| Koruma türü | Hardcoded serial — `.rodata`'da düz metin |
| Karşılaştırma | Direkt `strcmp` — hash/XOR yok |
| Anti-debug | Tespit edilmedi |
| Packing | Tespit edilmedi |
| Çözüm süresi | ~2 dakika |

**RE Dersi:** `strings` her zaman ilk çalıştırılacak araçtır. Kolay challenge'ların %30'u burada çözülür.

---

## 🔍 Technique Catalog

| Teknik | Kullanıldı mı? | Not |
|--------|---------------|-----|
| `strings` recon | ✅ | Serial anında bulundu |
| `ltrace` tracing | ✅ | strcmp davranışı doğrulandı |
| Ghidra static | ✅ | Kaynak mantığı okundu |
| GDB dynamic | ❌ | Gerekmedi |
| Packing detection | ❌ | Packed değil |
