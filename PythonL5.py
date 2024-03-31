
#Bai 1
sum = 0
for i in range(101):
    if i % 3 == 0:
        sum+=i
print(sum)

#Bai 2
num = 0
for i in range(51):
    if i%2 == 0:
        print("cac so chan trong 0-50:",i)
        num+=1
print("So so chan trong 0-50:",num)

#Bai 3
i = int(input("Nhap so: "))
if i == 0:
    print("i la 0")
elif i == 1:
    print("i la 1")
elif i%2!=0 and i%3!=0 and i%5!=0 and i%7 and i>1:
    print("i la so nguyen to")
else:
    print("i khong phai la so nguyen to")




