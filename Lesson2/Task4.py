n = int(input("Введите число"))
def fizz_buzz(n):
    Fizz_Buzz(n)
    for i in range(1,n+1):
     if i % 3==0 and i % 5==0:
            print("Fizz_Buzz")
     elif i % 3==0:
            print("Fizz")
     elif i % 5==0:
            print("Buzz")


