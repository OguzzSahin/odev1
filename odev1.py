# Python veri tiplerinden bazıları aşağidaki gibidir.

# Metin tipi veriler =str
#Örnek: a = "Merhaba"

# Sayı tipi veriler = int, float, complex
# Örnek int=1 , float=1,1 , complex= -1 = x^2 (X burada complex bir sayıdır)

# Dizi tipi veriler = list, tuple, range
# Örnek
# list = [1,2,3,4,5] (örneğimiz bir liste olup sonradan içerdiği üyeler tekil olarak değiştirilebilir)
# Tuple = (1,2,3,4,5) (örneğimiz bir demet olup içeridiği üyeler değiştirilemez)
# Range(6) (örneğimiz bir liste veya demette alınmasını istediğimiz üye sayısını belirtir. 0 dan başlar 6. üyeyi dahil etmez.)

# Sözlük tipi veriler = dict
# Örnek {kitap adı : olasılıksız , yazar : adam fawer , baskı no : 2}
#(sözlük tipi veriler içlerinde belirli bir veriyi başka bir veri ile eşler)

#Set tipi veriler = set, frozenset
# set = {1,2,3} (setler belirlenmiş bir düzene sahip değildir ve her seferinde farklı bir sıra ile yazılabilirler ve tekrarlanan değer içeremezler)
# frozenset => x = [1,2,3]
# y = frozenset(x) (forzenset'ler de setler gibidir ancak değiştirilemezler)

#Bool tipi veriler
# print(10>9), numerik bir veri tipi olup çıktısı "True" olarak bir bool tipi veri olacaktır
# a="elma" - b="armut" print(a==b) str tipi bir veri olup çıktısı "False" olarak bool tipi veri olacaktır

# Binary tipi veriler = bytes, bytearray, memoryview
# bu veri tipi hakkında örnek verebilecek bilgim bulunmuyor

#Nonetype tipi veriler
# bu veri tipi hakkında örnek verebilecek bilgim bulunmuyor


# Kodlama.io sitesinde kullanılmış olabilecek veri tipleri:
# str= ödev açıklamalarında kullanılan veri tipidir
# int= kurs tamamlanma oranını bildiren kutucukta kullanılan veri tipidir
# list= profil ikonunun üzerine geldiğimizde profili düzenle, üyelikleri yönet vb. seçeneklerin çıkmasını sağlayan veri tipidir
# range = kodlama.io/courses linkinde kullanıcıya kaç kurs gösterileceğine karar verirken kullanılan veri tipidir



eğitmen = ("Tümü","Engin Demirog", "Halit Enes Kalayci")
Kurslar = ("kurs1","kurs2","kurs3","kurs4","kurs5","kurs6")

if eğitmen == "Halit Enes Kalayci":
    print(Kurslar(range(4,7)))
elif eğitmen == "Engin Demirog":    
    print(Kurslar(range(0,4)))
else: 
    print(Kurslar)

    # sitenin kullanıcı giriş ekranlarında, kurs tamamlama oranları yazdırılırken ve 
    # şifre değişim ekranlarında new password ve confirm password alanları karşılaştırılırken de şart blokları kullanılmaktadır.



