
def checkNumbeEvenOrOdd(numbers ):
    for num in numbers:
        if (num % 2) == 0:  
           print(f"{num} is even")  
        else:  
           print(f"{num} is odd") 


value = int(input("Enter a numbers value: ")) 
rang =value
numbers = []

for num in range(rang):
    number =int(input("Enter a number: "))
    if(number>10):
       number =int(input("pls ,enter a number less than 10: "))
       numbers.append(number)
    else:
        numbers.append(number)

checkNumbeEvenOrOdd(numbers)



