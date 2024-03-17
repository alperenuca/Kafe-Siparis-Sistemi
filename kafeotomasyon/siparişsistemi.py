class kafemenu:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, ad, fiyat):
        self.urunler[ad] = fiyat

    def urun_cikar(self, ad):
        del self.urunler[ad]

    def menuyu_ac(self):
        print("Menü:")
        for urun, fiyat in self.urunler.items():
            print(f"{urun}: {fiyat:.2f} TL")

class Siparis:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, menu, ad, miktar):
        if ad in menu.urunler:
            if ad in self.urunler:
                self.urunler[ad] += miktar
            else:
                self.urunler[ad] = miktar
            print(f"{miktar} adet {ad} siparişe eklendi.")
        else:
            print("Hatalı ürün ismi.")

    def urun_cikar(self, ad, miktar):
        if ad in self.urunler:
            if miktar >= self.urunler[ad]:
                del self.urunler[ad]
            else:
                self.urunler[ad] -= miktar
            print(f"{miktar} adet {ad} siparişten çıkarıldı.")
        else:
            print("Hatalı ürün seçimi.")

    def siparisi_goster(self):
        print("Sepetiniz:")
        for urun, miktar in self.urunler.items():
            print(f"{urun}: {miktar}")

def main():
    menu = kafemenu()
    menu.urun_ekle("Türk Kahvesi", 60)
    menu.urun_ekle("Americano", 65)
    menu.urun_ekle("Milkshake", 130)
    menu.urun_ekle("Latte", 80)
    menu.urun_ekle("Flat White", 90)
    menu.urun_ekle("Cortado", 105)
    menu.urun_ekle("Su", 30)

    siparis = Siparis()

    while True:
        print("Hoş Geldiniz ! ")
        print("a. Menüyü Aç")
        print("b. Ürün ekle ")
        print("c. Ürün çıkar ")
        print("d. Siparişi görüntüle ")
        print("e. Siparişi onayla ")
        secim = input("Yapmak istediğiniz işlemi seçiniz : ")

        if secim == "a":
            menu.menuyu_ac()
        elif secim == "b":
            urun = input("Alacağınız ürünün adını giriniz : ")
            miktar = int(input("Kaç adet alacaksnız ? : "))
            siparis.urun_ekle(menu, urun, miktar)
        elif secim == "c":
            urun = input("Çıkartmak istediğiniz ürünün adını giriniz : ")
            miktar = int(input("Kaç adet çıkartacaksınız ? : "))
            siparis.urun_cikar(urun, miktar)
        elif secim == "d":
            siparis.siparisi_goster()
        elif secim == "e":
            print("Siparişiniz iletilmiştir, en kısa sürede servis edilecektir. İyi günler dileriz :) ")
            break
        else:
            print("Bir aksilik oluştu.Lütfen yapmak istediğiniz işlemi yeniden seçiniz. ")

if __name__ == "__main__":
    main()
