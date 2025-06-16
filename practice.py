# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}")
# else:
#     print(f"{num2} is greater than {num1}")   
     
# gender = input("Enter your gender (M/F): ").strip().upper()
# if gender == 'M':
#     print("Good Morning Sir!")
# elif gender == 'F':
#     print("Good Morning Madam!")
# else:
#     print("Invalid input. Please enter M or F.")  

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")    

# name= input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age < 18:
#     print(f"Hello {name}, you are a minor.")
# else:
#     print(f"Hello {name}, you are a valid voter.")    

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 100 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# temperature = float(input("Enter the temperature in Celsius: "))
# if temperature < 0:
#     print("It's freezing cold!")
# elif 0 <= temperature <= 10:
#     print("It's very cold.")
# elif 10 < temperature <= 20:
#     print("It's cold.")
# elif 20 < temperature <= 30:
#     print("It's pleasant.")
# elif 30 < temperature <= 40:
#     print("It's hot.")
# else:
#     print("It's extremely hot!")


# for loop questions

# 1.
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     print("hello world")

# 2.
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#         print(i)

# 3.
# num = int(input("Enter a number: "))
# for i in range(num,0,-1):
#     print(i)

# 4.
# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# 5.
# sum = 0
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     sum += i
# print(f"The sum of all numbers from 1 to {num} is {sum}")    


# 6.
# product = 1
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     product*=i
# print(f"The product of all numbers from 1 to {num} is {product}")    


# 7.
# even = 0
# odd = 0
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         even+=i
#     else:
#         odd+=i
# print(f"The sum of even numbers from 1 to {num} is {even}")
# print(f"The sum of odd numbers from 1 to {num} is {odd}")      
  

# 8.
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num%i == 0:
#         print(i)


# 9.
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum += i 
# if sum == num:
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")    


# 10.
# num = int(input("Enter a number: "))
# count = 2

# for i in range(2, num):
#     if num % i == 0:
#        count += 1
        
# if count == 2:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")


# 11.
# a= "sheriyans"
# b=""
# for i in range(len(a)-1, -1, -1):
#     b+= a[i]
# print(b)  


# # 12.
# a= "amma"
# b=""
# for i in range(len(a)-1, -1, -1):
#     b+= a[i]

# if a == b:
#     print(f"{a} is a palindrome.")
# else:
#     print(f"{a} is not a palindrome.") 
      

# 13.
# str = "P@#yn26at^&i5ve"
# alpha = 0
# num = 0
# symbol = 0
# for char in str:
#     if char.isalpha():
#         alpha += 1
#     elif char.isdigit():
#         num += 1
#     else:
#         symbol += 1
# print(f"Alphabets: {alpha}, Digits: {num}, Symbols: {symbol}")   


# while loop question    # 
# num = int(input("Enter a number: "))
# while num > 0:
#     i= num%10
#     print(i)
#     num = num // 10

# num = int(input("Enter a number: "))
# i=0
# while num > 0:
#     b= num%10
#     i=i*10+b
#     num = num // 10
# print("reversed number is", i  )    


# num = int(input("Enter a number: "))
# a=num
# i=0
# while num > 0:
#     b= num%10
#     i=i*10+b
#     num = num // 10
# if a == i:
#     print(f"{a} is a palindrome.")
# else:
#     print(f"{a} is not a palindrome.")


import random
num = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == num:
        print("Congratulations! You guessed the number correctly.")
    else:
        print(f"Sorry, the correct number was {num}. Better luck next time!")

   