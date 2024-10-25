import random

def metni_ikili_kodla(metin):
    ikili_kod = ''.join(format(ord(char), '08b') for char in metin)
    return ikili_kod

def parcalara_ayir(ikili_kod, uzunluk):
    return [ikili_kod[i:i+uzunluk] for i in range(0, len(ikili_kod), uzunluk)]

def parcalari_karistir(parcalar):
    random.shuffle(parcalar)
    return ''.join(parcalar)

def sifrele(metin, uzunluk=8):
    ikili_kod = metni_ikili_kodla(metin)
    parcalar = parcalara_ayir(ikili_kod, uzunluk)
    sifrelenmis_metin = parcalari_karistir(parcalar)
    return sifrelenmis_metin

gunluk = "Bugün harika bir gündü."
sifrelenmis_gunluk = sifrele(gunluk)
print(sifrelenmis_gunluk)
