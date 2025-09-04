from collections import defaultdict
import random
import statistics as ist

############################################ Veri ##########################################
kitaplar = [
    {"isim": "Veri Bilimi 101", "yazar": "Ali", "tur": "Bilim", "satis": 1200, "yil": 2021},
    {"isim": "Python ile Yapay Zeka", "yazar": "Ayşe", "tur": "Bilim", "satis": 950, "yil": 2020},
    {"isim": "İstatistik Temelleri", "yazar": "Ali", "tur": "Akademik", "satis": 700, "yil": 2019},
    {"isim": "Makine Öğrenmesi", "yazar": "Can", "tur": "Bilim", "satis": 1800, "yil": 2022},
    {"isim": "Veri Görselleştirme", "yazar": "Deniz", "tur": "Sanat", "satis": 400, "yil": 2018},
    {"isim": "Matematiksel Modelleme", "yazar": "Ali", "tur": "Akademik", "satis": 1500, "yil": 2021},
    {"isim": "Bilgi Toplumu", "yazar": "Ayşe", "tur": "Sosyal", "satis": 600, "yil": 2022}
]

############################################ Fonksiyonlar ##########################################

def en_cok_satan(kitaplar):
    return max(kitaplar, key=lambda a: a["satis"])

cokitap = en_cok_satan(kitaplar)
print("\nEn çok satan kitap:\n")
print(f"İsim: {cokitap['isim']}, Yazar: {cokitap['yazar']}, Tür: {cokitap['tur']}, Satış: {cokitap['satis']}, Yıl: {cokitap['yil']}")



def yazar_satislari(kitaplar):
    toplam = defaultdict(int)
    for kitap in kitaplar:
        toplam[kitap["yazar"]] += kitap["satis"]
    return dict(toplam)


print("\nYazarların toplam satışları:\n")
for yazar, satis in yazar_satislari(kitaplar).items():
    print(f"{yazar}: {satis}")

####################################### List ve Küme İşlemleri ###############################

def analiz(kitaplar):
    turler = {kitap["tur"] for kitap in kitaplar}
    cok_satan_kitaplar = [kitap["isim"] for kitap in kitaplar if kitap["satis"] > 1000]
    return turler, cok_satan_kitaplar

turler, cok_satan_kitaplar = analiz(kitaplar)

print("Kitap türleri:", turler)
print("1000'den fazla satışı olan kitaplar:", cok_satan_kitaplar)

############################### Lambda / Filter / Map / Sorted ##############################

k_2020_sonra = list(filter(lambda b: b["yil"] > 2020, kitaplar))
print("2020'den sonra çıkan kitaplar:", [b["isim"] for b in k_2020_sonra])


artirilmis = list(map(lambda c: c["satis"]*1.10, kitaplar))
print("Satışları %10 artırılmış liste:", artirilmis)


satis_sirali = sorted(kitaplar, key=lambda d: d["satis"], reverse=True)
print("Kitapların azalan sırada satış miktarı:", [e["isim"] for e in satis_sirali])

#################################### İstatistiksel Analiz #######################################


ortalama_satis = ist.mean([f["satis"] for f in kitaplar])
print("Ortalama satış adedi:", round(ortalama_satis,2))

tur_satislari = defaultdict(int)
for g in kitaplar:
    tur_satislari[g["tur"]] += g["satis"]
en_cok_satan_tur = max(tur_satislari, key=tur_satislari.get)
print("En çok satış yapan tür:", en_cok_satan_tur)

# Satışların standart sapması
standart_sapma = ist.stdev([h["satis"] for h in kitaplar])
print("Satışların standart sapması:", round(standart_sapma,2))

##############################  Train/Test Simülasyon ###########################################

random.shuffle(kitaplar)
train_size = int(len(kitaplar)*0.7)
train = kitaplar[:train_size]
test = kitaplar[train_size:]

# Train seti: yazarların ortalama satışları
yazar_toplam_train = defaultdict(list)
for k in train:
    yazar_toplam_train[k["yazar"]].append(k["satis"])
yazar_ortalama_train = {yazar: sum(s)/len(s) for yazar, s in yazar_toplam_train.items()}

# Test seti: ortalamanın üzerinde satış yapan kitaplar
test_ustu_satis = [k["isim"] for k in test if k["satis"] > yazar_ortalama_train.get(k["yazar"], 0)]

print("\nTrain/Test Simülasyonu\n")
print("Train seti:", [k["isim"] for k in train])
print("Test seti:", [k["isim"] for k in test])
print("Train seti yazar ortalamaları:", yazar_ortalama_train)
print("Test setinde ortalamanın üzerinde satış yapan kitaplar:", test_ustu_satis)

#################################### Karşılaştırmalı Yorum ##########################################
print("\n## Karşılaştırmalı Yorum ## \n")
train_ortalama = ist.mean([k["satis"] for k in train])
test_ortalama = ist.mean([k["satis"] for k in test])
print(f"Train ortalaması: {train_ortalama}, Test ortalaması: {test_ortalama}")
if test_ortalama > train_ortalama:
    print("Test seti ortalama satış olarak train setinden yüksek.")
elif test_ortalama < train_ortalama:
    print("Test seti ortalama satış olarak train setinden düşük.")
else:
    print("Train ve Test seti ortalama satışları eşit.")

