#Create a variable “x” and assign it the integer value “10”. Create another variable “y” and assign it the float value “20.5”. Write a Python statement to add these two variables and print the result.
x = 10
y = 20.5
print(x+y)

#Question 2
name = 'Pious'
print(len(name))

#Question 3
def calculate_area(length, width):
    return length * width
print(calculate_area(5, 3))

#Question 4
a = 15
b = 4
print(a//b)
print(a%b)

#Question 5
age = 18
if age >= 18 < 65:
    print('adult')
else: 
    print('not adult')    

#Question 6
num1 = 99
num2 = 99
if num1 != num2:
    print('not equals to')
else: 
    print('it is equal to')    

#Question 7
def integer(num):
    return num > 0 and num % 2 == 0
print(integer(8))


#Question 8
x = True
y = False
print(x and y)  
print(x or y)   

#Question 9
def greet(name):
    return ('hello ' + name)
print (greet('pious'))    

#Question 10
def findmax(numbers):
    return max(numbers)
print (findmax([3,8,12,5]))

#Question 11
x = [1, 2, 3]
print(type(x))

# Question 12
numbers = [4, 2, 9, 1]
numbers.sort()
print(numbers)

#Question 13
def calc_discount (price, discount):
    return price - (price*discount/100)
print (calc_discount(300, 10))

#Question 14
age = int(input('age- '))
if age <= 18:
    print('minor')
else:
    print('adult')

#Question 15
def string_statistics(string):
    return len(string), string.upper(), string.lower()
print(string_statistics("Python Programming"))






