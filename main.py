
def IslemHesapla(sayi1,islem,sayi2):
    if islem == '+' :
        print("{} + {} : {} ".format(sayi1,sayi2 , (sayi1+sayi2)))
    elif islem == '-':
        print("{} - {} : {} ".format(sayi1, sayi2, (sayi1 - sayi2)))
    elif islem == '*':
        print("{} * {} : {} ".format(sayi1, sayi2, (sayi1 * sayi2)))
    elif islem == '/':
        print("{} / {} : {} ".format(sayi1, sayi2, (sayi1 / sayi2)))
    else :
        print("Hatalı Tekrar Deneyiniz ! ")

def ProgramSonlandırma():
    print("\n")
    while 1:
        cevap = input("Programa Devam Etmek İçin 'D' Tusuna Basınız , Çıkmak İçin 'Y' Tuşuna Basınız : ")
        cevap = cevap.upper()
        if cevap == 'D':
            sayi1= int(input("1.Sayıyı Giriniz : "))
            islem = input("İşlemi giriniz : ")
            sayi2 = int(input("2. Sayıyı Giriniz : "))
            IslemHesapla(sayi1,islem,sayi2)
            ProgramSonlandırma()

        elif cevap == 'Y':
            print("Programdan Başarıyla Çıktınız.")
            break
        else:
            print("Hatalı Tuşlama Yaptınız.")

print(*"Hesap Makinesine Hoşgeldiniz" , sep='-')

while 1 :
    sayi1 = int(input("1.Sayıyı Giriniz : "))
    islem = input("İşlemi giriniz : ")
    sayi2 = int(input("2. Sayıyı Giriniz : "))
    IslemHesapla(sayi1,islem,sayi2)
    ProgramSonlandırma()
    break




