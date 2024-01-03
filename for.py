#even number
user = int(input("enter number: "))
num = 0
for i in range(user):
    if i%2 == 0:
        print(i)
    else:
        num += 1
 
 # star pattern            
n = int(input("enter the number: "))    
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

#multiplication table
user = int(input("enter number: "))
for i in range(1, 11):
    result = user * i
    print(f"{user} * {i} = {result}")

#vowel
word = input("Enter a word: " )
for chart in word:
    if chart.lower() in 'aeiou':
        print(chart)

#fibonnacci series
a, b = 0, 1
num = int(input("enter number"))
print(a, b, end=' ')
for i in range(num):
    c = a + b
    print(c, end=' ')
    a = b
    b = c