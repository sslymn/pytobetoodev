
#DEĞİŞKENLER

baslik = "HABERİNİZ OLSUN"   #haber, değişken
#print(baslik)   #print, fonksiyon: o an yaptığımız işin doğruluğunu görme adına

vade = 12
faizOrani = 1.47
print(baslik)
print(type(baslik))     #str
print(type(vade))       #int
print(type(faizOrani))  #float

mesaj = "Hoşgeldin"
musteriAdi = "Engin"
musteriSoyadi = "Demiroğ"
print(mesaj+musteriAdi+musteriSoyadi)   # + bir operator ve bu şekilde olursa HoşgeldinEnginDemiroğ sonucu oluşur.
print(mesaj+" "+musteriAdi+" "+musteriSoyadi) # Hoşgeldin Engin Demiroğ



#ŞART BLOKLARI

dolarDun = 7.65
dolarBugun = 7.75

if dolarDun > dolarBugun:
    print("Azalış Oku")

elif dolarDun < dolarBugun:      #elseyi şarta bağlamak için elif
    print("Artış Oku")

else:
    print("Eşittir Oku")

print("Bitti")




#LİSTELER

krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))   #içerisine yazdığımız lsitenin kaç elemandan oluştuğu

krediler[0] = "Çabuk kredi"   #değiştirebiliriz
print(krediler)

#Döngüler


krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]

for kredi in krediler:   # kredi burada takma ad buna alias denir
    print(kredi)


for i in range(10):  # 0-dan başlar ama 10 dahil değil.
    print(i)


for i in range(len(krediler)):
    print(i)

for i in range(3,10):
    print(i)

for i in range (0,10,2): # 0 dan başla 10 dahil değil 2şer arttır.
    print(i)


#Fonksiyonlar
    

def kredileriListele():
    krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:   # kredi burada takma ad buna alias denir
     print("<option>"+kredi+"<option>")

kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()
kredileriListele()



print("İLK SAYFA")
for kredi in krediler:   # kredi burada takma ad buna alias denir
    print("<option>"+kredi+"<option>")

krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]



print("İKİNCİ SAYFA")
for kredi in krediler:   # kredi burada takma ad buna alias denir
    print("<option>"+kredi+"<option>")

krediler = ["Hızlı Kredi","Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]


print("ÜÇÜNCÜ SAYFA")

for kredi in krediler:   # kredi burada takma ad buna alias denir
    print("<option>"+kredi+"<option>")

