# Research Notes — Challenge 05: unpackme
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## Araştırdığım Konu

Binary packing ve unpacking — UPX paketleyicisinin nasıl çalıştığı, nasıl tespit edildiği ve nasıl geri açıldığı.

---

## Ön Araştırma — Binary Packing Nedir?

Binary packing, çalıştırılabilir dosyaların sıkıştırılması ve/veya şifrelenmesi işlemidir.

| Amaç | Açıklama |
|------|----------|
| Boyut küçültme | Disk alanı tasarrufu |
| Obfuscation | Statik analizi zorlaştırma |
| Anti-RE | Disassembler'ı yanıltma |

**Nasıl çalışır:**
```
Orijinal binary
      ↓
  Sıkıştır/şifrele
      ↓
Unpacker stub ekle (küçük kod)
      ↓
Paketlenmiş binary

Çalışma zamanında:
  1. Unpacker stub çalışır
  2. Orijinal kodu belleğe açar
  3. Kontrolü açılmış koda devreder
```

---

## UPX — Ultimate Packer for eXecutables

| Özellik | Detay |
|---------|-------|
| Açık kaynak | ✅ github.com/upx/upx |
| Platform desteği | Linux, Windows, macOS, Android |
| Sıkıştırma oranı | Genellikle %40-70 |
| Unpack | `upx -d binary` — tek komut |
| İmza | Binary içinde `UPX!` stringleri |

**UPX tespiti:**
```bash
# Yöntem 1: file komutu
file binary  # "UPX compressed" yazar

# Yöntem 2: strings
strings binary | grep UPX

# Yöntem 3: hex editor
# İlk birkaç byte'ta "UPX!" magic bytes
```

---

## Packing Sonrası strings Davranışı

```bash
# Paketlenmiş binary → strings anlamsız
$ strings packed_binary
UPX!
...gürültü...
@8Zx

# Açılmış binary → gerçek stringler
$ strings unpacked_binary
What's my favorite number?
picoCTF{up><_m3_f7w_5c717b6e}
```

Packing, `strings` aracını etkisiz kılar — bu yüzden packing tespiti her zaman ilk adım olmalı.

---

## Diğer Yaygın Packerlar

| Packer | Zorluk | Tespit | Unpack |
|--------|--------|--------|--------|
| UPX | Kolay ⭐ | `file` / `strings` | `upx -d` |
| MPRESS | Orta ⭐⭐ | PE imzası | Manuel / araç |
| Themida | Zor ⭐⭐⭐⭐ | Anti-debug içerir | Çok zor |
| VMProtect | Çok Zor ⭐⭐⭐⭐⭐ | VM bytecode | Akademik araştırma |

---

## Bulunan Kaynaklar

- [UPX GitHub](https://github.com/upx/upx)
- [picoCTF unpackme challenge](https://picoctf.org)
- [Detecting Packers — REMnux](https://remnux.org)
- [Dynamic Unpacking Techniques](https://trailofbits.github.io/ctf/reversing/)

---

## Temel Bulgular

1. Packing tespiti → her zaman `file` ile başla
2. UPX → en yaygın CTF packeri, `upx -d` ile kolayca açılır
3. Unpack sonrası → normal analiz akışına dön
4. Dinamik unpacking (manuel) → packed binary'yi GDB'de çalıştır, unpacker stub bittikten sonra bellek dökümü al

---

## Sonuç

Bu challenge, packing'in tek katmanlı bir savunma olduğunu ve yaygın paketleyiciler (UPX gibi) için tek komutun yeterli olduğunu gösteriyor. Daha gelişmiş koruma için custom packerlar veya VM-based obfuscation kullanılır — bunların açılması çok daha fazla uzmanlık gerektirir.
