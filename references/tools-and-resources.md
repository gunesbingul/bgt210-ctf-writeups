# Tools & References / Araçlar ve Kaynaklar
**Course / Ders:** BGT210 Reverse Engineering | **Student:** Güneş Bingül — 2320191055

---

## 🛠 Tools Used / Kullanılan Araçlar

| Araç | Amaç | Kurulum |
|------|------|---------|
| `file` | Binary türü tespiti | `apt install file` |
| `strings` | Printable string çıkarma | `apt install binutils` |
| `ltrace` | Kütüphane çağrısı izleme | `apt install ltrace` |
| `strace` | Sistem çağrısı izleme | `apt install strace` |
| `upx` | Binary pack/unpack | `apt install upx-ucl` |
| `objdump` | Statik disassembly | `apt install binutils` |
| `readelf` | ELF yapı inceleme | `apt install binutils` |
| `GDB` | Dinamik debugger (Linux) | `apt install gdb` |
| `Ghidra` | Decompiler + disassembler | [ghidra-sre.org](https://ghidra-sre.org) |
| `x64dbg` | Dinamik debugger (Windows) | [x64dbg.com](https://x64dbg.com) |
| `radare2` | Binary analiz framework | [rada.re](https://rada.re) |
| `Python 3` | Helper script + keygen | [python.org](https://python.org) |

---

## 📚 Learning Resources / Öğrenme Kaynakları

| Kaynak | URL | Not |
|--------|-----|-----|
| picoCTF | https://picoctf.org | Başlangıç-orta CTF platformu |
| CrackMes.one | https://crackmes.one | Topluluk crackme binary'leri |
| reversing.kr | http://reversing.kr | Klasik RE challenge'ları |
| CTF Field Guide | https://trailofbits.github.io/ctf/reversing/ | Trail of Bits RE metodolojisi |
| Ghidra Docs | https://ghidra-sre.org | NSA RE aracı |
| radare2 Book | https://book.rada.re | r2 referans kitabı |
| pwn.college | https://pwn.college | Rehberli RE modülleri |
| LiveOverflow | https://youtube.com/@LiveOverflow | CTF walkthrough videoları |

---

## 🔑 RE Commands Cheatsheet / Komut Referansı

```bash
# Dosya tanımlama
file <binary>
readelf -h <binary>

# String çıkarma
strings <binary>
strings -n 8 <binary>
strings <binary> | grep -iE "flag|pass|key|correct"

# Çalışma zamanı izleme
ltrace ./<binary>
ltrace -e strcmp ./<binary>
strace ./<binary>

# Packing
strings <binary> | grep UPX
upx -d <packed> -o <unpacked>

# Statik analiz
objdump -d <binary>
objdump -s -j .rodata <binary>

# GDB
gdb ./<binary>
(gdb) b strcmp
(gdb) run
(gdb) x/s $rdi
(gdb) x/s $rsi
(gdb) info registers
```
