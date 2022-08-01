n = int(input("enter an integer: "))

if n % 2 != 0 : #if the reminder when you divide n by 2 is not 0 (odd number) print odd
    print("odd")

elif n % 2 == 0 and n >=2 and n <=5 : # if the reminder when you divide n by 2 is 0 ( even number ) and is between 2 and 5 print small even
    print(" small even")


elif n % 2 == 0 and n >=6 and n <=20 : # if the reminder when you divide n by 2 is 0 ( even number ) and is between 2 and 5 print small even
    print(" medium even")


elif n % 2 == 0 and n >=20 : # if the reminder when you divide n by 2 is 0 ( even number ) and is between 2 and 5 print small even
    print(" big even")