import random
import string

while True:


    try:
        uzunluk = int(input("(8 - 20) karakter uzunluğunda şifre için uzunluk belirleyiniz: "))

        if 8 <= uzunluk <= 20:
         break

        else:
            print("Lütfen Doğru bir aralık giriniz: /")

    except ValueError:
        print("Lütfen doğru bir şeyler gir")

#harf için
harf=string.ascii_letters
#rakam için
rakam=string.digits
#özel karakterler için
ozel=string.punctuation

# %60 harf, %40 rakam ve özel karakter olacak şekilde şifreyi oluşturmak ıstıyoruz 🧠
# % 60 lık harf kısmı
harfSayısı=round((0.6)*uzunluk)
# %40 kalan diğer kısım
dıgerSayı=uzunluk-harfSayısı

Sıfre = ''.join(random.choices(harf, k=harfSayısı) +
                   random.choices(rakam +ozel, k=dıgerSayı))


# Şifreyi oluşturuyorum
Sıfre= ''.join(random.sample(Sıfre, len(Sıfre)))

print("Oluşturduğum şifrem--> ", Sıfre)
print("Biryerlere kaydetmeyi unutmayın🤌🏻")

















