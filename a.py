# n = int(input("Enter any number: "))

# rev = int(str(n)[::-1])
# print("Reversed number:", rev)

# n = int(input("Enter any number: "))
# def isPrime(n):
#     if n <2:
#         return "Not prime"
#     for i in range(2, n):
#         if n % i == 0:
#             return "Not prime"
#     return "Prime"

# print(isPrime(n))

# str1=input("Enter any string: ")
# def check_palindrome(str1):
#     str2 = str1[::-1]
#     if str1 == str2:
#         print("The string is a palindrome.")
#     else:
#         print("The string is not a palindrome.")
# check_palindrome(str1)

# n = int(input("Enter the number of Fibonacci terms: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# n=int(input("n= "))
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return (n*(n+1))/2

# print("Sum =",int(sum(n)))

# 153 → 1³ + 5³ + 3³ = 153
# n = int(input("Enter any number: "))
# def isArmstrong(n):
#     temp = n
#     digits = len(str(n))
#     sum_of_power = 0
#     while temp > 0:
#         digit = temp % 10
#         sum_of_power += digit ** digits
#         temp //= 10
#     if sum_of_power == n:
#         print(n, "Number is armstrong")
#     else:
#         print(n, "Number is not armstrong")

# isArmstrong(n)