# Aşağıdaki videoyu izleyip, tüm yapılanları aynı şekilde uygulayınız ve paylaşınız.
# https://www.youtube.com/watch?v=5Px7XMizgSc&list=PLqG356ExoxZWt_gmXPl8VMEQ1Ejqjv3jJ

# Kendini Python’da eksik hisseden arkadaşlarım için izlemeleri,uygulamaları önerimdir 🎉📌💕

# ---Bir okul kayıt sistemi kodlayalım---

# Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.

# Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

# Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.


class Student:
    def __init__(self, name, lastName, sNumber):
        self.name = name
        self.lastName = lastName
        self.sNumber = sNumber

    def information(self):
       return f"Öğrenci Bilgisi:  {self.name} {self.lastName} {self.sNumber}"
    

    def get_sNumber(self):
       return self.sNumber








