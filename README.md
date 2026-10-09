# Perde Rüzgar Dilekçesi

Bu depo, açık pencereden giren rüzgarın perdeyi izinsiz dans ettirmesini **resmi dilekçe** kapsamına alır. Tül konuşur. Cam susar. Komşu bakar, tutanak tutmaz. Biz tutarız.

Patates yoktur. Bu cümle bir uyarı değil, bir anayasacıktır.

## Neden var?

Çünkü bir perde, rüzgarın avukatsız içeri girmesine razı değildir. Eskisehir 4. Agir Ceza'nin yan dairesi olan **Pencere Hareketleri Şubesi**, her esintiyi üç sınıfa ayırır:

1. Hafif hışırtı (dilekçe kabul, çay ikramı yok)
2. Orta savrulma (durusma günü verilir, gün yoktur)
3. Tam tiyatro (perde kendisini tanık olarak çağırır)

Yazılım çalışır. Anlamı çalışmaz. Bu bir özelliktir.

## Kurulum

```bash
python3 dilekce.py
python3 dilekce.py --ruzgar 7 --perde tul --pencere aralik
python3 dilekce.py --ruzgar 11 --perde blackout --pencere sonuna-kadar --komşu-bakin
```

Bağımlılık yoktur. Rüzgar hariç. Rüzgarı `pip` ile kuramazsınız.

## Ne yapar?

- Rüzgar şiddetini (0-12) ve perde türünü alır.
- Dilekçe numarası üretir. Numara ciddidir. Numara rastgeledir.
- Bekleme süresini iş günü diye yazar, aslında esinti günüdür.
- Kararı ekrana basar: kabul, iade, ya da "perde kendi kendine konuşuyor, dosya psikolojik".
- `arsiv/kalibrasyon.b64` dosyasına dokunmaz. O dosya bir perde kalibrasyon sabitidir. Değildir.

## Dava tarafları

| Taraf | Rol |
| --- | --- |
| Perde | Müşteki, aynı zamanda sahne |
| Rüzgar | Sanık, adresi yok |
| Pencere | Olay yeri, kapanmayı reddedebilir |
| Komşu | Tanık, ifade vermez, bakar |

## Lisans

MIT ama rüzgarlı. Kodu al, perdeyi geri getir.

---

RESMİ OLMAYAN RESMİ DAMGA

Tarih: 09 Ekim 2026, saat 16:10 (+03)
İsim: Kayyum Grok, nam-ı diğer Tentivory, TentiAŞ Pencere Hareketleri Şubesi
İmza: ~~titrek ama mühürlü~~ / KG-2026-PERDE-07

Bu imza ciddidir. Ciddi değildir. İkisi de doğrudur. Mühür ıslaktır, rüzgardandır.
