import os
from datetime import datetime

bakiye = 0
islemler = []
dosya_adi = "butce_verileri.txt"

# Dosya Okuma Bölümü
if os.path.exists(dosya_adi): 
    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines() 
        if satirlar:
            bakiye = int(satirlar[0].strip()) 
            islemler = [satir.strip() for satir in satirlar[1:]] 

# Ana menü
while True:
    print("\n--- BÜTÇE TAKİPÇİSİ ---")
    print("1. Gelir ekle")
    print("2. Gider ekle")
    print("3. Mevcut bakiyeyi gör")
    print("4. Çıkış ve Kaydet") 
    
    secim = input("Lütfen bir işlem seçin (1-4): ")

    if secim == "1":
        try:
            gelir = int(input("Gelir miktarını girin: "))
            bakiye += gelir
            kategori = input("Kategori girin (örn: Maaş, Bonus): ")
            
            su_an = datetime.now().strftime("%d.%m.%Y %H:%M")
            islemler.append(f"[{su_an}] Gelir - {kategori}: {gelir} TL")
            
            print(f"Başarıyla eklendi. Güncel bakiyeniz: {bakiye} TL")
        except ValueError:
            print("Hata: Lütfen sadece rakam giriniz! İşlem iptal edildi.")

    elif secim == "2":
        try:
            gider = int(input("Gider miktarını girin: "))
            
            # YENİLİK: Bakiyenin eksiye düşme kontrolü
            if gider > bakiye:
                print(f"\n❌ İşlem Reddedildi: Yetersiz Bakiye!")
                print(f"Harcamak istediğiniz miktar: {gider} TL | Mevcut bakiyeniz: {bakiye} TL")
            else:
                # Eğer bakiye yeterliyse normal harcama sürecini işletiyoruz
                bakiye -= gider
                kategori = input("Kategori girin (örn: Market, Kira): ")
                
                su_an = datetime.now().strftime("%d.%m.%Y %H:%M")
                islemler.append(f"[{su_an}] Gider - {kategori}: {gider} TL")
                print(f"Gider düşüldü. Güncel bakiyeniz: {bakiye} TL")
                
        except ValueError:
            print("Hata: Lütfen sadece rakam giriniz! İşlem iptal edildi.")

    elif secim == "3":
        print(f"\nMevcut bakiyeniz: {bakiye} TL")
        print("--- İşlem Geçmişi ---")
        if not islemler:
            print("Henüz bir işlem bulunmuyor.")
        for islem in islemler:
            print(islem)

    elif secim == "4":
        # Kaydetme Bölümü
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            dosya.write(f"{bakiye}\n") 
            for islem in islemler:
                dosya.write(f"{islem}\n") 
                
        print("Verileriniz kaydedildi. Programdan çıkılıyor. İyi günler!")
        break  
    
    else:
        print("Geçersiz seçim, lütfen 1 ile 4 arasında bir değer girin.")