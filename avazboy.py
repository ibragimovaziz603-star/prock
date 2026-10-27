import math

# ==========================================
# LEVEL 1: EASY (1-8, 11-12)
# ==========================================

# №1
print("Hello, Python!")

# №2
print("Welcome to Python!")

# №3
name = "Avazbek"
age = 18
city = "Toshkent"
print(name, age, city)

# №4
a = 14
b = 9
print(a + b)

# №5
print(12 + 8 * 2)    # 28
print((12 + 8) * 2)  # 40

# №6
ism = input("Ismingiz: ")
print("Salom, " + ism + "!")

# №7
royxat = ["Red", "Green", "White", "Black"]
print(royxat[0], royxat[3])

# №8
print(type(25), type(3.5), type("25"), type(True))

# №11
n = int(input("Son kiriting: "))
print(n - 1, n + 1)

# №12
c = float(input("Selsiy: "))
print("Farengeyt:", (c * 9 / 5) + 32)


# ==========================================
# LEVEL 2: MODERATE (13, 16-23)
# ==========================================

# №13
r = float(input("Radius: "))
print("Yuza:", math.pi * r**2)

# №16
son = int(input("Son: "))
if son % 2 == 0:
    print("Juft")
else:
    print("Toq")

# №17
x = int(input("Son: "))
if 1 <= x <= 10:
    print("In range")
else:
    print("Out of range")

# №18
a = int(input("1-son: "))
b = int(input("2-son: "))
if a > b:
    print("Birinchi katta")
elif a < b:
    print("Ikkinchi katta")
else:
    print("Teng")

# №19
harf = input("Harf kiriting: ").lower()
if harf in ['a', 'e', 'i', 'o', 'u']:
    print("Unli")
elif harf.isalpha():
    print("Undosh")
else:
    print("Xato kiritish")

# №20
a = "12"
b = "3"
print(a + b)             # "123" (matnlar qo'shildi)
print(int(a) + int(b))   # 15 (sonlar qo'shildi)

# №21
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
if a >= b and a >= c:
    print("1-son eng katta:", a)
elif b >= a and b >= c:
    print("2-son eng katta:", b)
else:
    print("3-son eng katta:", c)

# №22
a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))
if a == b == c:
    print("Hammasi teng")
elif a == b or b == c or a == c:
    print("Ikkitasi teng")
else:
    print("Hammasi har xil")

# №23
yil = int(input("Yil: "))
if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print("Kabisa yili")
else:
    print("Kabisa yili emas")


# ==========================================
# LEVEL 3: CHALLENGING (26-38)
# ==========================================

# №26
n = int(input("Nechta son: "))
if n > 0:
    yigindi = 0
    for i in range(n):
        yigindi += float(input("Son: "))
    print("O'rta arifmetik:", yigindi / n)
else:
    print("Xato: n musbat bo'lishi kerak")

# №27
n = int(input("n: "))
yigindi = 0
for i in range(1, n + 1):
    yigindi += 1 / i
print("Garmonik yig'indi:", yigindi)

# №28
musbat = 0
manfiy = 0
while True:
    son = int(input("Son (0 to'xtatadi): "))
    if son == 0:
        break
    if son > 0:
        musbat += son
    else:
        manfiy += son
print("Musbatlar yig'indisi:", musbat, "Manfiylar yig'indisi:", manfiy)

# №29
for i in range(26):
    kichik = chr(97 + i)
    katta = chr(97 + i - 32)
    print(kichik, ord(kichik), katta, ord(katta))

# №30
n = int(input("n: "))
for i in range(1, n + 1):
    print("*" * i)

# №31
def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print("Eng katta:", maximum(5, 9, 2))

# №32
def yigindi(royxat):
    jami = 0
    for son in royxat:
        jami += son
    return jami
print(yigindi([1, 2, 3, 4]))

# №33
def faktorial(n):
    if n == 0:
        return 1
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija
print(faktorial(5)) # 120

# №34
def harflar(matn):
    katta = 0
    kichik = 0
    for harf in matn:
        if harf.isupper():
            katta += 1
        elif harf.islower():
            kichik += 1
    return katta, kichik
print(harflar("Salom Dunyo"))

# №35
def teskari(matn):
    natija = ""
    for harf in matn:
        natija = harf + natija
    return natija
print(teskari("Python")) # nohtyP

# №36
scores = [12, 8, 15]
scores[1] = 20
for i in range(len(scores)):
    scores[i] = scores[i] * 2
print(scores) # [24, 40, 30]

# №37
songs = ["A", "B", "C", "D", "E"]
print(songs[:3])    # Birinchi 3 ta
print(songs[1:4])   # O'rtadagi 3 ta (yoki 2 ta o'rtadagi)
print(songs[-2:])   # Oxirgi 2 ta

# №38
# copy_list = original -> ikkalasi bitta xotira manzilini ko'rsatadi. Birini o'zgartirsangiz, ikkinchisi ham o'zgaradi.
# copy_list = original[:] -> nusxa oladi. O'zgartirsangiz faqat nusxa o'zgaradi.
original = [1, 2, 3]
nusxa = original[:]
nusxa.append(4)
print(original) # [1, 2, 3]
print(nusxa)    # [1, 2, 3, 4]


# ==========================================
# LEVEL 4: ADVANCED (39-45)
# ==========================================

# №39
royxat = ["aka", "uka", "dada", "ona", "bobo"]
sanoq = 0
for soz in royxat:
    if len(soz) >= 2 and soz[0] == soz[-1]:
        sanoq += 1
print("Mos keladiganlar:", sanoq)

# №40
royxat = [10, 5, 20, 8, 20]
eng_katta1 = float('-inf')
eng_katta2 = float('-inf')
for son in royxat:
    if son > eng_katta1:
        eng_katta2 = eng_katta1
        eng_katta1 = son
    elif son > eng_katta2 and son != eng_katta1:
        eng_katta2 = son
print("1-eng katta:", eng_katta1, "2-eng katta:", eng_katta2)

# №41 (EKUB - Evklid algoritmi)
a = int(input("1-son: "))
b = int(input("2-son: "))
while b != 0:
    a, b = b, a % b
print("EKUB:", a)

# №42
# n ta son ketma-ketligini tekshirish
# (Kodni soddalashtirilgan holda yozamiz)
royxat = [1, 2, 3, 4, 5]
osish = True
kamayish = True
for i in range(len(royxat) - 1):
    if royxat[i] >= royxat[i+1]:
        osish = False
    if royxat[i] <= royxat[i+1]:
        kamayish = False
if osish:
    print("O'suvchi")
elif kamayish:
    print("Kamayuvchi")
else:
    print("Aralash")

# №43
a = float(input("1-tomon: "))
b = float(input("2-tomon: "))
c = float(input("3-tomon: "))
if a + b > c and a + c > b and b + c > a:
    print("Uchburchak")
    if a == b == c:
        print("Teng tomonli")
    elif a == b or b == c or a == c:
        print("Teng yonli")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("To'g'ri burchakli")
else:
    print("Uchburchak emas")

# №44 (Kvadrat tenglama)
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a == 0:
    print("Kvadrat tenglama emas")
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("2 ta ildiz:", x1, x2)
    elif D == 0:
        x = -b / (2*a)
        print("1 ta ildiz:", x)
    else:
        print("Haqiqiy ildiz yo'q")

# №45 (Floyd uchburchagi)
n = int(input("Qatorlar soni: "))
son = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(son, end=" ")
        son += 1
    print()