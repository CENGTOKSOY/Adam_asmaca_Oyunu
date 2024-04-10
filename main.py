import random

# Kelime listesi
kelimeler = ["python", "programlama", "bilgisayar", "klavye", "fare"]

# Rastgele bir kelime seç
secilen_kelime = random.choice(kelimeler)

# Başlangıçta bilinen harfler
tahminler = set()

# Oyun döngüsü
while True:
    # Kelimeyi göster (bilinmeyen harfler alt çizgi ile gösterilir)
    gorunen_kelime = "".join([harf if harf in tahminler else "_" for harf in secilen_kelime])
    print(f"Kelime: {gorunen_kelime}")

    # Kullanıcıdan tahmin al
    tahmin = input("Bir harf tahmin edin: ").lower()

    # Tahmin doğruysa ekle, yanlışsa uyarı ver
    if tahmin in secilen_kelime:
        tahminler.add(tahmin)
        if set(secilen_kelime) <= tahminler:
            print(f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {secilen_kelime}")
            break
    else:
        print("Yanlış harf! Tekrar deneyin.")

print("Oyun bitti. İyi oyunlar!")
