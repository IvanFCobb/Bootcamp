num1 = 42 #- variable declaration - Primitive Numbers
num2 = 2.3 #- variable declaration - Primitive Numbers
boolean = True #- variable declaration - Primitive Boolean
string = 'Hello World' #- variable declaration - Primitive String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # - Composite List - initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #- Composite Dictionary - initialize
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration - Composite Tuple - initialize
print(type(fruit)) # - log statement
print(pizza_toppings[1]) # - log statement
pizza_toppings.append('Mushrooms') # - Composite List - add value
print(person['name']) # - log statement
person['name'] = 'George' #- Composite Dictionary - access value
person['eye_color'] = 'blue' #- Composite Dictionary - access value
print(fruit[2]) # - log statement

if num1 > 45: # - conditional if
    print("It's greater") # - log statement
else: # - conditional if
    print("It's lower") # - log statement

if len(string) < 5: # - conditional if
    print("It's a short word!") # - log statement
elif len(string) > 15: # - conditional if
    print("It's a long word!") # - log statement
else: # - conditional if
    print("Just right!") # - log statement 

for x in range(5): # for loop
    print(x) # - log statement
for x in range(2,5):  # for loop
    print(x) # - log statement
for x in range(2,10,3):  # for loop
    print(x) # - log statement
x = 0 #- variable declaration - Primitive Numbers
while(x < 5): #while loop
    print(x) # - log statement
    x += 1 #- variable declaration - Primitive Numbers

pizza_toppings.pop() # - Composite List - delete value
pizza_toppings.pop(1) # - Composite List - delete value

print(person) # - log statement
person.pop('eye_color')  #- Composite Dictionary - delete value
print(person) # - log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # - conditional if
        continue # for loop continue
    print('After 1st if statement') # - log statement
    if topping == 'Olives': # - conditional if
        break # for loop break

def print_hello_ten_times():
    for num in range(10): # for loop
        print('Hello') # - log statement

print_hello_ten_times() # funtion

def print_hello_x_times(x): # funtion 
    for num in range(x): # for loop
        print('Hello') # - log statement

print_hello_x_times(4) # funtion 

def print_hello_x_or_ten_times(x = 10): # funtion 
    for num in range(x): # for loop
        print('Hello') # - log statement

print_hello_x_or_ten_times() # funtion 
print_hello_x_or_ten_times(4) # funtion 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)