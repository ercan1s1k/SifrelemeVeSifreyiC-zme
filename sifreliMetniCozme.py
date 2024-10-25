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

def parcalari_duzenle(parcalar, sifrelenmis_metin):
    sifrelenmis_parcalar = [sifrelenmis_metin[i:i+8] for i in range(0, len(sifrelenmis_metin), 8)]
    return sorted(sifrelenmis_parcalar, key=lambda x: parcalar.index(x))

def ikili_kodu_metne_donustur(ikili_kod):
    metin = ''.join(chr(int(ikili_kod[i:i+8], 2)) for i in range(0, len(ikili_kod), 8))
    return metin

def coz(sifrelenmis_metin, uzunluk=8):
    ikili_kod = metni_ikili_kodla(gunluk)  # Orijinal metnin ikili kodunu al
    parcalar = parcalara_ayir(ikili_kod, uzunluk)
    duzenlenmis_parcalar = parcalari_duzenle(parcalar, sifrelenmis_metin)
    cozulen_ikili_kod = ''.join(duzenlenmis_parcalar)
    orijinal_metin = ikili_kodu_metne_donustur(cozulen_ikili_kod)
    return orijinal_metin

# Günlük şifreleme
gunluk = "Bugün harika bir gündü."
sifrelenmis_gunluk = sifrele(gunluk)
print("Şifrelenmiş Günlük: ", sifrelenmis_gunluk)

# Günlük çözme
cozulen_gunluk = coz(sifrelenmis_gunluk)
print("Çözülmüş Günlük: ", cozulen_gunluk)
