# print even numbers
x = int(input("Enter a number: "))
i = 1
even_numbers = []
odd_numbers = []

while i <= x:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
    i += 1

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# armstrong number
n = int(input ("choose number"))
copy_n  = n
rev = 0
unit = len(str(copy_n))
while(copy_n >0):
    digit = n%10
    rev = (rev + digit^unit)
    copy_n= copy_n//10
if n == rev:
    print("Armstrong ")
else:
    print ("not a Armstrong ")

# print prime number
n = int(input("choose a number"))
factor = 0
i = 1
composite = 0
while(i <= n):
    if(n%i)==0:
        factor = factor + 1
    i = i + 1
if (factor == 2):
    print(n," is a prime number")
else:
    composite += 1

# print pattern
n = int(input('Enter number of rows : '))
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1

#reverse a string
original_string = input("Enter a string: ")
reversed_string = ""

index = len(original_string)

while index > 0:
    index -= 1
    reversed_string += original_string[index]

print("Original string:", original_string)
print("Reversed string:", reversed_string)

