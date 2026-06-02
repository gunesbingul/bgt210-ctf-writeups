# Research Notes — Challenge 04: Easy Crack Me
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## Araştırdığım Konu

Windows PE binary'lerde çok aşamalı serial doğrulama mantığının Ghidra ve x64dbg ile analizi.

---

## Ön Araştırma — Windows PE Formatı

PE (Portable Executable), Windows'ta kullanılan binary formatıdır.

| Bölüm | İçerik |
|-------|--------|
| `.text` | Çalıştırılabilir kod |
| `.rdata` | Salt okunur veriler (stringler burada) |
| `.data` | Başlatılmış global değişkenler |
| Import Table | DLL bağımlılıkları (kernel32.dll, user32.dll) |
| Export Table | DLL'lerin dışa açtığı fonksiyonlar |

**ELF vs PE Karşılaştırması:**

| Özellik | ELF (Linux) | PE (Windows) |
|---------|-------------|--------------|
| Debugger | GDB | x64dbg / OllyDbg |
| Decompiler | Ghidra / r2 | Ghidra / IDA |
| String section | `.rodata` | `.rdata` |
| Library trace | `ltrace` | API Monitor |

---

## Çok Aşamalı Kontrol Stratejisi

Bu challenge 3 aşamalı kontrol kullanıyor:

```
Girdi
  ↓
Adım 1: input[1] == 'E'?         → erken çıkış
  ↓
Adım 2: input[2..4] == "asy"?    → erken çıkış
  ↓
Adım 3: strcmp(input, "Ea5yR3versing") == 0?  → başarı / başarısız
```

Bu yapının amacı: tek bir `strcmp` çağrısı yerine erken çıkış noktaları ekleyerek analizi zorlaştırmak. Ancak Ghidra tüm dalları gösterir.

---

## Ghidra Kullanım Notları

**Başarı mesajından geriye doğru çalışma:**
1. `Window → Defined Strings` → "Congratulations" ara
2. Çift tıkla → `.rdata` bölümüne atlar
3. Sağ tık → `References → Find References` → kod konumuna gider
4. Oradaki fonksiyonu incele — başarı dalının üstündeki koşul nedir?

**Fonksiyon ağacı görüntüleme:**
- `Window → Call Trees` → hangi fonksiyon nereden çağrılıyor

---

## x64dbg Breakpoint Teknikleri

```
Seçenek 1: API Breakpoint
  → Sağ tık → Follow in Disassembler → strcmp adresi
  → F2 ile breakpoint ekle

Seçenek 2: Sembol Breakpoint
  → Symbols sekmesi → strcmp bul → F2

Seçenek 3: Memory Breakpoint
  → Girdi buffer adresine yazma breakpoint'i
```

Breakpoint tetiklendiğinde register durumu:
```
x86:  EAX = 1. argüman, EDX = 2. argüman
x64:  RCX = 1. argüman, RDX = 2. argüman
```

---

## Bulunan Kaynaklar

- [reversing.kr Easy Crack Me](http://reversing.kr)
- [Ghidra Tutorial — PE Analysis](https://ghidra-sre.org)
- [x64dbg Documentation](https://x64dbg.com)
- [PE Format Reference](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format)

---

## Temel Bulgular

1. PE analizi için Ghidra hem Linux hem Windows binary'leri destekler
2. Çok aşamalı kontroller — her birini bağımsız olarak karşıla
3. x64dbg ile dinamik analiz, statik bulguları doğrular
4. Başarı mesajından geriye gitme — en hızlı Ghidra stratejisi

---

## Sonuç

Bu challenge, Windows PE binary analizinin temel iş akışını gösteriyor. Ghidra'nın decompiler'ı çok aşamalı mantığı okunabilir C koduna dönüştürüyor. x64dbg ile dinamik doğrulama, statik analizin doğruluğunu teyit ediyor. Bu iki aracın birlikte kullanımı — statik + dinamik — profesyonel RE iş akışının temelidir.
