# let's creat a age checker for driving !!!!
age = 18
name = input("enter your name : ")
user_age = int (input("enter your age: "))
if user_age > age :
    print("name are an adult")
    print("you can drive !!!")
else :
    print("you are minor you can't drive")

#  let creat a grade checker !!!!
markes = int(input("enter your score in exam: "))
if 90 <= markes <= 100:
    print("Grade = A ")
elif 80 <= markes < 90:
    print("Grade = B ") 
elif 70 <= markes < 80:
    print("Grade = C ")
elif 60 <= markes < 70:
    print("Grade = D ")
else:
    print("Grade = E ")

# calculator
num_1 = int(input("enter first number: "))
num_2 = int(input("enter second number: "))
oper = input("chose operator +,-,/,*: ")
result = 0
if oper == "+":
    result = num_1 + num_2
elif oper == "-":
    result = num_1 - num_2
elif oper == "/":
    result = num_1 / num_2
elif oper == "*":
    result = num_1 * num_2

print(f"The result of {num_1} {oper} {num_2} is:{result}")

# pallindrome
a = input("enter number: ")
copy_a = a[::-1]
if a == copy_a:
    print("is a palindrome")
else:
    print("is not a palindrome")
    
# guess number game
secret_number = 7  
guess = int(input("Guess the number (between 1 and 10): "))
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
else:
    print(" Try again next time.")
