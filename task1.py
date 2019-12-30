# Попросить пользователя ввести текст. В результате вывести процент букв в верхнем
# регистре (заглавные) и в нижнем регистре (прописные).

text = "Hello my name is Kanat, and I study in Maker's course."
big = 0
small = 0
for x in text:
    if 'a'<= x <= 'z':
        small += 1
    elif 'A' <= x <= 'Z':
        big += 1
print(big, small)
all = big + small
capital = round(big *100/all)       
Little = round(100 - capital)
print(f"The big letter is : {capital} %")
print(f"The small letter is: {Little} %")
   
