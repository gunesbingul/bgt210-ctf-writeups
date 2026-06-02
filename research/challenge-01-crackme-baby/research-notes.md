# Research Notes — Challenge 01: CrackMe Baby
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## Araştırdığım Konu

ELF binary'lerde hardcoded serial korumasının nasıl çalıştığı ve `strings` + `ltrace` ile nasıl tespit edildiği.

---

## Ön Araştırma — ELF Binary Yapısı

ELF (Executable and Linkable Format), Linux'ta kullanılan standart binary formatıdır.

| Bölüm | İçerik |
|-------|--------|
| `.text` | Çalıştırılabilir kod |
| `.rodata` | Salt okunur veriler (hardcoded stringler burada!) |
| `.data` | Başlatılmış global değişkenler |
| `.bss` | Başlatılmamış global değişkenler |
| `.plt` / `.got` | Dinamik kütüphane bağlantıları |

**Önemli Bulgu:** Hardcoded serials ve flag'ler çoğunlukla `.rodata` bölümünde saklanır. `strings` komutu bu bölümleri okur.

---

## strcmp Güvenlik Açığı

```c
// GÜVENSİZ — kolayca ltrace ile tespit edilir
if (strcmp(user_input, "s3cr3t_k3y_42") == 0) { ... }

// DAHA GÜVENLI — hash karşılaştırması
if (sha256(user_input) == stored_hash) { ... }
```

`strcmp` library call olduğu için `ltrace` tarafından anında yakalanır. Her iki argüman bellekte plaintext olarak görünür.

---

## ltrace Nasıl Çalışır?

`ltrace`, dinamik olarak bağlı kütüphane çağrılarını (libc vb.) gerçek zamanlı yakalar:

```bash
ltrace ./<binary>              # tüm çağrılar
ltrace -e strcmp ./<binary>    # sadece strcmp
ltrace -e 'str*' ./<binary>   # string ile başlayan tüm fonksiyonlar
```

Çıktıda gösterilen format:
```
fonksiyon_adı(arguman1, arguman2) = dönüş_değeri
```

---

## Ghidra Analizi — .rodata Bölümü

Ghidra'da `.rodata`'yı incelemek için:
1. `Window → Memory Map` → `.rodata` satırına çift tıkla
2. Ya da `Defined Strings` penceresini aç → tüm hardcoded stringler listelenir
3. String üzerine çift tıkla → kod içindeki referans lokasyonuna atla

---

## Bulunan Kaynaklar

- [ELF Format Specification](https://refspecs.linuxfoundation.org/elf/elf.pdf)
- [ltrace Man Page](https://man7.org/linux/man-pages/man1/ltrace.1.html)
- [Ghidra String Search Guide](https://ghidra-sre.org)
- [CrackMes.one — Baby Series](https://crackmes.one)

---

## Temel Bulgular

1. `.rodata` bölümü → hardcoded stringler için ilk bakılacak yer
2. `strcmp` → `ltrace` ile anında yakalanır, her iki argüman görünür
3. `strings -n 6` → en az 6 karakter — kısa anlamsız stringlerde gürültüyü azaltır
4. Dinamik bağlantılı binary → `ltrace` çalışır; statik bağlantılı → çalışmaz

---

## Kalan Sorular

- [ ] Statik bağlantılı binary'de aynı saldırı nasıl yapılır?
- [ ] `strcmp` yerine `memcmp` kullanan binary'lerde ltrace yine gösterir mi?

---

## Sonuç

Bu challenge, en temel RE korumasını — hardcoded plaintext serial — gösteriyor. Gerçek dünya uygulamalarında bu yöntem asla kullanılmamalıdır. `strings` + `ltrace` kombinasyonu bu tür korumaları saniyeler içinde kırar.
