import datetime

Kullanıcılar = {"Tolga":"ugurlu1234"}

Envanter = {'kuşkonmaz': [10,5], 'brokoli': [15,6], 'havuç': [18,7], 'elmalar': [20,5], 'muz':
[10, 8], 'meyve': [30,3], 'yumurta': [50,2], 'karışık meyve suyu': [0,18], 'balık çubukları':
[25,12], 'dondurma': [32,6], 'elma suyu': [40,7], 'portakal suyu': [30,8], 'üzüm suyu':
[10,9]}

Sepet = []

def EnvanteriGöster():
    a = 1
    for key in Envanter.keys():
        print(a,".",key,"fiyat =",Envanter[key][0],"$","stok =",Envanter[key][1])
        a += 1 


def Kontrol(Kullanıcı_Adı,Şifre):

    for key in Kullanıcılar.keys():
        if(Kullanıcı_Adı == key and Şifre == Kullanıcılar[key]):
            print("Giriş Başarılı")
            break

def SepetBoşmu():
    return len(Sepet) == 0        

def SepettenElemanKaldır(ürün):
    Sepet.pop(ürün - 1)

def SepetiGöster():
    toplam = 0
    if(SepetBoşmu()):
        print("Sepet şu an Boş")    
    else:
        a = 1
        print("Sepetiniz Şunları İçeriyor: ")
        for i in Sepet:
            print(a,".",i[0],"fiyatı = ",i[1],"₺","miktar = ",i[3]/i[1],"toplam = ",i[3],"₺")
            toplam = toplam + (i[3]/i[1])*i[1]
            a += 1
        print("Toplam = ",toplam,"₺")         

def SepetMenüsü():
    print("Bir Seçenek Seçiniz: ")
    print("\t1.Tutarı Güncelleyin\n\t2.Bir Öğeyi Kaldırın\n\t3.Satın Al\n\t4.Ana Menüye Dön")
    seçim = int(input("Seçiminiz: "))

    if seçim == 1:
         print("Tutarınız Güncellendi")
         toplam = 0
         for i in Sepet:
             toplam += i[3]
         print("Mevcut Tutarınız = ",toplam)
         SepetMenüsü()
    elif seçim == 2:
        ürün = int(input("Kaldırmak İstediğiniz Ürünü Seçin: "))
        if(SepetBoşmu()):
            print("Sepetiniz Zaten Boş")
        else:
            SepettenElemanKaldır(ürün)
            SepetiGöster()
            SepetMenüsü()
    elif(seçim == 3):
        ürün = input("Satın Almak istediğiniz ürün ismini giriniz: ")
        ÜrünEkleme(ürün)
    else:
        print("Ana menüye Dönülüyor..")
        Hizmet()

def Hizmet():
    
    print(" 1. Ürün Ara\n","2. Sepete Git\n","3. Satın Al\n","4. Oturum Kapat\n","5. Çıkış Yap\n")

    seçim = int(input("Seçiminiz: "))

    if(seçim < 0 or seçim > 5):
        print("Lütfen Geçerli Bir Hizmet Numarası Giriniz !!")
        Hizmet()
    else:
        if(seçim == 1):
            ürün = input("Ne arıyorsunuz ? : ")
            ÜrünAra(ürün)
        elif(seçim == 2):
            SepetiGöster()
            SepetMenüsü()
        elif(seçim == 3):
            EnvanteriGöster()
            ürün = input("Satın Almak istediğiniz ürün ismini giriniz: ")
            ÜrünEkleme(ürün)
        elif(seçim == 4):
            print("Oturum Kapatıldı...")
        else:
            print("Makbuzunuz İşleniyor...\n")

    return seçim        

def ÜrünEkleme(ürün):
    if(ürün == "0"):
        print("Ana Menüye Dönülüyor")
        Hizmet()
    else:
        miktar = int(input("Miktarı girin: "))
        if(Envanter[ürün][1] == 0):
            print("Üzgünüz eklemek istediğiniz ürün tükenti lütfen başka bir ürün girin")
        elif (miktar > Envanter[ürün][1]):
            print("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
            ÜrünEkleme(ürün)
        else:
            print("Ürün Sepetinize Eklendi")
            Sepet.append([ürün,Envanter[ürün][0],Envanter[ürün][1],miktar*Envanter[ürün][0]])
            Envanter[ürün][1] -= miktar
            SepetMenüsü()


def ÜrünAra(ürün):
    liste = []
    ürünsayısı = 0
    numara = 0
    for key in Envanter.keys():
        if ürün in key:
            ürünsayısı += 1
            liste.append([key,Envanter[key][0]])

    if(ürünsayısı != 0):
        print(ürünsayısı," benzer ürün bulundu:\n")
        for i in liste:
            numara += 1
            print(numara,".",i[0]," ",i[1],"₺")
        eklenecekürün = input("Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):")
        if(eklenecekürün == "0"):
            Hizmet()
        else:
            a = True
            for i in liste:
                if eklenecekürün in i:
                    a = False
                    ÜrünEkleme(eklenecekürün)
                    print(eklenecekürün,"Sepetinize Eklendi")
                    print("Ana Menüye Dönülüyor..")
                    Hizmet()
                    break   
            if a:
                print("Lütfen Geçerli Bir Ürün ismi girin !")
                ÜrünAra(ürün)

    else:
        ürünismi = input("Aramanız hiçbir öğeyle eşleşmedi. Lütfen başka bir şey deneyin (Ana menü için 0 girin): ")
        if(ürünismi == "0"):
            Hizmet()
        else:
            ÜrünAra(ürünismi)    


while(True):

    print("**** Neos Akademi Market’e Hoşgeldin Coder! ****\n")

    print("Lütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın.. (Kullanıcı bilgini data'dan kontrol et)\n")

    sart = True

    while(sart):

        Kullanıcı_Adı = input("Kullanıcı Adı: ")

        Şifre = input("Şifre: ")

        for key in Kullanıcılar.keys():
            if(Kullanıcı_Adı == key and Şifre == Kullanıcılar[key]):
                print("Giriş Başarılı")
                sart = False
        if(sart):
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")

    print("Hoşgeldiniz",Kullanıcı_Adı,"Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.\n")
    print("Lütfen aşağıdaki hizmetlerden birini seçin")

    a = Hizmet()

    while(True):
        if a == 5 or a == 4:
            break
        else:
            Hizmet()    

    if a != 4:
        print("****** Neos Akademi Gamer Market ********")
        print("*************************************")
        print("\t\t0850 855 85 85\n\t\tneosakademi.com")
        SepetiGöster()
        tarih = datetime.datetime.now()
        print(tarih)
        print("Online Market’imizi kullandığınız için teşekkür ederiz!")