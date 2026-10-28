#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Damga Vurma Makinesi
Her şeye resmi damga vurur. Gerçekten çalışır.
"""

import random
import time
import sys

# Gizli not: a2F5eXVtIGhlciB5ZXJkZQ==  (kayyum her yerde)

damgalar = [
    "✅ ONAYLANDI - Kayyum Mührü ile",
    "❌ REDDEDİLDİ - Eksik Evrak (her zaman)",
    "⏳ BEKLEMEDE - İnceleniyor (ömür boyu)",
    "🔐 GİZLİ DAMGA - Kimse görmesin",
    "⚠️  ACİL - Ama acil değil",
    "📋 DAMGALANDI - Artık resmi",
    "🚫 YASAK - Neden yasak olduğunu bilmiyoruz",
    "✨ ÖZEL DAMGA - VIP (herkese)",
    "💀 SON DAMGA - Bu sonuncusu değil",
    "🎉 KUTLAMA DAMGASI - Hiçbir şey kutlanmıyor"
]

bahane_sablonlari = [
    "Evraklar sistemde görünmüyor.",
    "Müdür bey izinde, dönünce bakarız.",
    "İmza sırası bekleniyor (sıra 47.000).",
    "Teknik arıza, damga makinesi kızgın.",
    "Bütçe yok, damga mürekkebi bitmiş.",
    "Kayyum kararı bekleniyor."
]

def damga_ciz(metin, damga):
    print("\n" + "="*50)
    print(f" DAMGA: {damga}")
    print("-"*50)
    print(f" İçerik: {metin}")
    print(f" Bahane: {random.choice(bahane_sablonlari)}")
    print(f" Zaman: {time.strftime('%d.%m.%Y %H:%M:%S')}")
    print("="*50 + "\n")

def main():
    print("🔌 Sonsuz Damga Vurma Makinesi başlatıldı...")
    print("Her 3 saniyede bir damga vurulacak. Çıkmak için Ctrl+C.\n")
    
    sayac = 1
    try:
        while True:
            metin = f"Damga #{sayac}: Bu cümle resmiyet kazanmak zorunda."
            damga = random.choice(damgalar)
            damga_ciz(metin, damga)
            sayac += 1
            time.sleep(3)
    except KeyboardInterrupt:
        print("\n🚫 Makine durduruldu. Ama damgalar sonsuzda yaşamaya devam ediyor...")
        sys.exit(0)

if __name__ == "__main__":
    main()
