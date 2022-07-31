#Dosya Açma ve Yazma İşlemleri

"""
Dosyalarımızı açmak ve dosyalarımıza yazmak için "w" kipini kullanıyoruz. "w" kipi, eğer oluşturmak istediğimiz dizinde
öyle bir dosya yoksa dosya oluşturuyor. Eğer öyle bir dosya varsa dosyayı silip tekrar oluşturuyor. Yani eğer açmak
istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa "w" kipi dosyadaki bilgileri silip tekrar oluşturacaktır.
"""

open("Bilgiler.txt","w") #Bilgiler adlı txt dosyası oluşturduk
file=open("Bilgiler.txt","w") #oluşturduğumuz dosyaya değişken atadık
file.close() #dosyayı kapattık

file1=open("C:/udemy/Python/examples/Bilgiler1.txt","w",encoding="utf-8") 
#dosyanın uzantısını yazarak işlem yapabiliriz.
#encoding="utf-8" işlemini, programın türkçe karakterleri desteklemesi için ekledik

file1.write("merhaba dünya çoşkun")

"""
Dosyalarımızı düzenlemek için "a" kipini kullanıyoruz. "a" kipi, eğer oluşturmak istediğimiz dizinde
öyle bir dosya yoksa dosya oluşturuyor. Eğer öyle bir dosya varsa dosyaya girdiğimiz verileri ekliyor. Yani eğer açmak
istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa "a" kipi dosyadaki bilgilere bizim gireceğimiz bilgileri ekliyor.
"""
file1=open("C:/udemy/Python/examples/Bilgiler1.txt","a",encoding="utf-8")
file1.write("\nekleme yapıldı")
file1.write("\nikinci ekleme yapıldı")#\n ile ekleyeceğimiz yazıyı mevcut dosyadaki yazının bir alt satırına geçerek ekler. kullanmazsak aynı satıra yazar
#dosyaya python'da kodlamadan manuel olarak eklediğimiz metin, python'u çalıştırınca silindi. sadece python'da yer alan metinler kaldı

"""
Dosyalarımızı okumak için "r" kipini kullanıyoruz.
"""
#file1=open("C:/udemy/Python/examples/Bilgiler1.txt","r",encoding="utf-8")
try:
    file=open("C:/udemy/Python/examples/Bilgiler2.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("Dosya Bulunamadı") #okumak istediğimiz dosya mevcut değilse "Dosya Bulunamadı" ekran çıktısını verir

file1=open("C:/udemy/Python/examples/Bilgiler1.txt","r",encoding="utf-8")
#encoding="utf-8 komutunu eklemezsek türkçe karakterlerin gösteriminde problem yaşanır

print(file1) #<_io.TextIOWrapper name='C:/udemy/Python/examples/Bilgiler1.txt' mode='r' encoding='utf-8'> ekran çıktısını verir

for i in file1: #for döngüsü ile dosyadaki bütün satırları yazdırdık
    print(i,end="") #for döngüsü ile print ettiğimizde her satırın sonuna otomatik olarak \n eklediği için ekran çıktısında 2 satır arasında boşluk oluşacak
    #bu boşluğun oluşmaması için print ifadesinin içine end="" yazarak satır sonlarına bir şey eklenmemesini sağlarız

file1.close()

file2=open("C:/udemy/Python/examples/Bilgiler2.txt","r",encoding="utf-8")
icerik=file2.read()
print("\nDosyanın içeriği: ")
print(icerik)
file2.close()
#read fonksiyonu ile dosyanın tamamını okuttuk ve sonrasında da yazdırdık

file3=open("C:/udemy/Python/examples/Bilgiler3.txt","w",encoding="utf-8")

file3.write("ikinci dosya içeriği")
file3.write("\nikinci dosya içeriği2")

file3=open("C:/udemy/Python/examples/Bilgiler3.txt","r",encoding="utf-8")

print(file3.readline())
print(file3.readline())

file3.close()

#readline fonksiyonu ile dosyayı satır bazlı okuduk. 2 tane readline fonksiyonu kullandığımız için ilk 2 satırı ekrana getirecektir.
#readline yerine readlines fonksiyonunu kullansaydık dosyadaki tüm verileri liste şeklinde okuyacaktı

#liste=file2.readlines()
#print(liste) ile dosyadaki verilerin liste şeklinde çıktısını alabiliriz

"""
python'da dosyalarla işlem yaparken bazen dosyayı kapatmayı unutabiliyoruz. 
programla işimiz bittikten sonra dosyanın kendi kendini kapatmasını istiyorsak aşağıdaki blok içinde yazmamız gerekmekte.
    with open(dosya_adı , dosya_kipi) as file:
        Dosya İşlemleri
"""

#DOSYA İŞLEMLERİ

#Dosyaları İleri Geri Sarma

"""Bir önceki derslerde dosya okurken sadece dosyanın en başından başlayarak ilerliyorduk ve okuma işleminin sonunda dosya imleci dosyadaki verilerin en sonuna gidiyordu.
Ancak çoğu zaman dosya imlecini dosyanın herhangi bir yerine götürmek isteyebiliriz. Bunun için Python'daki seek() fonksiyonunu kullanacağız. 
Aynı zamanda dosya imlecinin hangi byte'ta olduğunu gösteren tell() fonksiyonunu kullanacağız.
"""

with open("bilgiler2.txt","r",encoding="utf-8") as file:
    print(file.tell()) #0 çıktısını verecek çünkü imlecin yerini değiştirecek herhangi bir işlem yapmadık.
    file.seek(20)
    print(file.tell()) #20 çıktısını verecek çünkü seek() fonksiyonu ile imlecin 20. byte'a gitmesini istedik.
#"merhaba dünya ben mali kurtulmuş" yazan dosya üzerinden işlem yapalım

with open("bilgiler2.txt","r",encoding="utf-8") as file:
    file.seek(5) #imleci 5. byte'a gönderdik
    icerik=file.read(10) #icerik değişkenine imlecin bulunduğu yerden 10. byte'a kadar okumasını söyledik.
    file.seek(0) #imleci 0. byte'a gönderdik
    icerik2=file.read(6) #içerik değişikenini bulunduğu byte'tan 6. byte'a gönderdik.
    print(icerik) #ba dünya b çıktısını verdi
    print(icerik2) #merhab çıktısını verdi
    """
    file.seek(10)
    icerik3 = file.read(5)
    print(icerik3)
    
    seek() içindeki sayı read() içindeki sayıdan büyük olursa program hata verir
    """

#DOSYALARDA DEĞİŞİKLİK YAPMAK

#"r+" kipi ile dosyaları hem okuyup hem yazabiliyoruz.
with open("bilgiler2.txt","r+",encoding="utf-8") as file4:
    print(file4.read())
    file4.seek(7)
    file4.write(" dosyaya yazma işlemi") #7. byte'tan sonraya belirtilen yazıyı ekledik
    print(file4.read())

#dosyanın sonuna ekleme yapmak için
with open("bilgiler2.txt","a",encoding="utf-8") as file4: #"a" kipi ile işlem yapmamız gerekmekte
    file4.write("\nEklemek yaptık\n") #programı her çalıştırdığımızda mevcut metnin altına "Ekleme yaptık yazacak.
    #değişikliği dosyada yaptığımız için programı kapatıp açsak dahi eklenen veriler dosyada kalacak
with open("bilgiler2.txt","r+",encoding="utf-8") as file4:
    print(file4.read())

#dosyanın başına ekleme yapmak için
with open("bilgiler2.txt","r+",encoding="utf-8") as file4:
    icerik=file4.read()
    icerik="Mehmet Keper\n"+icerik
    print(icerik) #dosyanın başına Mehmet Keper yazısını ekledik

with open("bilgiler2.txt","r+",encoding="utf-8") as file4:
    file4.seek(0)
    file4.write("En birinci") #dosyanın başına ekleme yapmak için diğer bir yol
    icerik = file4.read()
    print(icerik)

#dosyanın ortasına ekleme yapmak

#dosyanın ortasına eleman eklemek için öncelikle dosyayı listeye çevirmeliyiz
#sonrasında da listenin ortasına denk gelen indeksi bularak elemanı eklemek için insert fonksiyonunda kullanabiliriz

with open("bilgiler2.txt","r+",encoding="utf-8") as file4:
    liste=file4.readlines()
    print(liste)
    uzunluk=len(liste)
    print(len(liste))
    liste.insert(int(uzunluk/2),"ortaya ekle\n") #listenin ortasına denk gelen indeksi bulmak için önce uzunluk tanımladık.
    #sonra da uzunluğun yarısını alarak(burda float değer gelebileceği için int() içine yazdık) insert işlemi yaptık
    #buradaki ekleme işlemi python'daki listeye ekleme yapar. bu listeyi dosyaya aktarmak için for döngüsü oluşturmamız gerekir
    for i in liste:
        file4.write(i)
        """
        for döngüsü yerine;
        file4.writelines(liste) 
        komutunu da kullanabiliriz
        """
    print(liste)

with open("bilgiler2.txt", "r+", encoding="utf-8") as file4:
    print(file4.read())






