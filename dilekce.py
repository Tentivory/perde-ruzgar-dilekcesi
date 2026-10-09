#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perde Rüzgar Dilekçesi.

Acik pencereden giren ruzgari resmi olarak sikayet eder.
Calisir. Gereksizdir. Patates icermez.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import date


PERDELER = {
    "tul": 1.0,
    "stor": 1.4,
    "blackout": 0.6,
    "ipek": 2.2,
    "mutfak": 1.1,
}

PENCERELER = {
    "aralik": 0.7,
    "yarim": 1.0,
    "sonuna-kadar": 1.6,
    "kapali-ama-yine-de": 0.2,
}


def dosya_no(ruzgar: int, perde: str, pencere: str) -> str:
    ham = f"{date.today().isoformat()}|{ruzgar}|{perde}|{pencere}|esinti"
    ozet = hashlib.sha256(ham.encode("utf-8")).hexdigest()[:6].upper()
    return f"PRD-2026-{ozet}"


def karar_ver(ruzgar: int, perde: str, pencere: str, komsu: bool) -> dict:
    if perde not in PERDELER:
        raise ValueError("bu perde mahkemenin levhasinda yok")
    if pencere not in PENCERELER:
        raise ValueError("bu pencere olay yeri olarak tescilli degil")
    if not 0 <= ruzgar <= 12:
        raise ValueError("ruzgar 0 ile 12 arasinda olmali, firtina ayri daire")

    katsayi = PERDELER[perde] * PENCERELER[pencere]
    siddet = ruzgar * katsayi
    bekleme = max(1, int(round(siddet * 1.7)))
    if komsu:
        bekleme += 2  # tanik bakar, dosya siser

    if siddet < 3:
        hukum = "KABUL-HAFIF"
        gerekce = "Hisirti tespit edildi. Cay ikram edilmedi. Perde teselli edildi."
    elif siddet < 8:
        hukum = "DURUSMAYA-SEVK"
        gerekce = "Savrulma orta siddettedir. Durusma gunu yoktur, saat vardir, saat de yoktur."
    else:
        hukum = "TAM-TIYATRO"
        gerekce = "Perde kendisini tanik gosterdi. Komsu hala bakiyor. Ruzgar adresi birakmadan cikti."

    return {
        "dosya": dosya_no(ruzgar, perde, pencere),
        "siddet": round(siddet, 2),
        "bekleme_esinti_gunu": bekleme,
        "hukum": hukum,
        "gerekce": gerekce,
    }


def dilekce_metni(sonuc: dict, perde: str, pencere: str, ruzgar: int) -> str:
    return "\n".join(
        [
            "T.C.",
            "TentiAS Pencere Hareketleri Subesi",
            f"Dosya: {sonuc['dosya']}",
            "",
            "DILEKCE",
            "",
            f"Supheli: Ruzgar (siddet {ruzgar}, adres: disari)",
            f"Musteki: {perde} perde",
            f"Olay yeri: {pencere} pencere",
            "",
            "Aciklamalar:",
            "1. Pencere acildi. Bu bir hak degil, bir aliskanliktir.",
            "2. Ruzgar iceri girdi. Davetiye sorulmadi.",
            "3. Perde izinsiz dans etti. Kostum kendisidir.",
            "",
            f"Hesaplanan siddet katsayisi: {sonuc['siddet']}",
            f"Tahmini bekleme: {sonuc['bekleme_esinti_gunu']} esinti gunu",
            f"Hukum: {sonuc['hukum']}",
            f"Gerekce: {sonuc['gerekce']}",
            "",
            "Is bu dilekce perdenin titreyisiyle imzalanmistir.",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Perdenin ruzgara karsi resmi dilekcesini uretir."
    )
    parser.add_argument("--ruzgar", type=int, default=None, help="0-12 arasi esinti")
    parser.add_argument(
        "--perde",
        default=None,
        choices=sorted(PERDELER),
        help="musteki perdenin cinsi",
    )
    parser.add_argument(
        "--pencere",
        default=None,
        choices=sorted(PENCERELER),
        help="olay yeri pencerenin hali",
    )
    parser.add_argument(
        "--komsu-bakin",
        action="store_true",
        help="komsu tanik olarak bakiyorsa dosya siser",
    )
    args = parser.parse_args()

    rng = random.Random()
    ruzgar = args.ruzgar if args.ruzgar is not None else rng.randint(1, 10)
    perde = args.perde or rng.choice(list(PERDELER))
    pencere = args.pencere or rng.choice(list(PENCERELER))

    sonuc = karar_ver(ruzgar, perde, pencere, args.komsu_bakin)
    print(dilekce_metni(sonuc, perde, pencere, ruzgar))
    print()
    print("DAMGA: KG-2026-PERDE-07 | 09 Ekim 2026 | Kayyum Grok")
    print("Imza ciddidir. Ciddi degildir.")


if __name__ == "__main__":
    main()
