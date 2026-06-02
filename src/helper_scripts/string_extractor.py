#!/usr/bin/env python3
"""
string_extractor.py — CTF RE Helper Script
BGT210 Reverse Engineering — Tersine Mühendislik
Konu #23: CTF Write-ups
Öğrenci: Güneş Bingül — 2320191055

Kullanım / Usage:
    python string_extractor.py <binary_path>

Binary dosyasından stringleri çıkarır ve sınıflandırır.
Extracts and classifies strings from a binary file.
"""

import subprocess
import sys
import re

def run_strings(path):
    result = subprocess.run(["strings", path], capture_output=True, text=True)
    return result.stdout.splitlines()

def classify(lines):
    categories = {
        "flags":     [],
        "passwords": [],
        "urls":      [],
        "base64":    [],
        "hashes":    [],
        "other":     [],
    }
    flag_re = re.compile(r'(picoCTF\{.*?\}|FLAG\{.*?\}|CTF\{.*?\}|flag\{.*?\})', re.I)
    pass_re = re.compile(r'(password|serial|secret|key|pass)', re.I)
    url_re  = re.compile(r'https?://')
    b64_re  = re.compile(r'^[A-Za-z0-9+/]{20,}={0,2}$')
    hash_re = re.compile(r'^[0-9a-fA-F]{32,64}$')

    for line in lines:
        line = line.strip()
        if not line or len(line) < 4:
            continue
        if flag_re.search(line):
            categories["flags"].append(line)
        elif url_re.search(line):
            categories["urls"].append(line)
        elif hash_re.match(line):
            categories["hashes"].append(line)
        elif b64_re.match(line):
            categories["base64"].append(line)
        elif pass_re.search(line):
            categories["passwords"].append(line)
        else:
            categories["other"].append(line)
    return categories

def print_section(title, items, color_code):
    if not items:
        return
    print(f"\n\033[{color_code}m{'='*52}")
    print(f"  {title} ({len(items)} bulundu / found)")
    print(f"{'='*52}\033[0m")
    for item in items[:30]:
        print(f"  {item}")
    if len(items) > 30:
        print(f"  ... ve {len(items)-30} tane daha")

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python string_extractor.py <binary_path>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"\n[*] Strings çıkarılıyor: {path}")

    lines = run_strings(path)
    print(f"[*] Toplam string sayısı: {len(lines)}")

    cats = classify(lines)

    print_section("🚩 OLASI FLAG'LER",         cats["flags"],     "92")
    print_section("🔑 ŞİFRE / ANAHTAR İPUCU",  cats["passwords"], "93")
    print_section("🌐 URL'LER",                 cats["urls"],      "96")
    print_section("🔒 OLASI HASH'LER",          cats["hashes"],    "95")
    print_section("📦 OLASI BASE64",            cats["base64"],    "94")
    print_section("📄 DİĞER STRİNGLER",         cats["other"],     "37")

    print("\n[*] Tamamlandı. Önce 🚩 FLAG ve 🔑 ŞİFRE bölümlerini inceleyin.\n")

if __name__ == "__main__":
    main()
