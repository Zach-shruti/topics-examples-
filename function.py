#calculator
def add(a,b):
    return(a+ b)
    
def sub(a,b):
    return(a-b)
    
def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a//b)
opera = input("choose operature to perform\"+,-,*,/\" ")
num_1 = int(input("chose 1st number: "))
num_2 = int(input("chose 2nd number: "))

if opera == "+":
    print(f" the sum of {num_1} and {num_2} is " , add(num_1 ,num_2))

elif opera == "-":
    print(f"the sub of {num_1} and {num_2} is " , sub(num_1,num_2))

elif opera == "*":
    print(f"the multiply for {num_1} and {num_2} is", multiply(num_1,num_2))

elif opera == "/":
    print(f"the division for {num_1}  and {num_2} is" ,divide(num_1,num_2))

# to print even number from list
def get_even(numbers):
     even_nums = [num for num in numbers if not num % 2]
     return even_nums

print(get_even([1, 2, 3, 4, 5, 6]))

# to reverse a string
def reverse_string(input_string):
    return input_string[::-1]
print("Original string:", original_string)
print("Reversed string:", reversed_string)

# to print percentage
def calculate_percentage(part, whole):
    percentage = (part / whole) * 100
    return percentage
   
print("Total Marks:", total_marks)
print("Obtained Marks:", obtained_marks)
print("Percentage Obtained:", percentage_obtained)

# for recurssion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  
