#copy a list
#car list
cars=['BMW','Ferrari','Audi','Toyota']

#copying the car list
cars2=cars.copy()

#print the list
print('Original list:',cars)

#print the copied list
print('copied List:',cars2)

# Dictionary 
months={'January':1,'February':2, 'March':3,'April':4}

# iterate  keys through for loop
for m in months.keys():
    print('keys:',m)

# iterate values
for n in months.values():
    print('values:',n)
    
# tuple creation
weather=('Spring','Summer','Fall')

# declaring the variables
a='Spring'
b='Bat'

#find the matching element
if(a in weather):
    print('a=',a ,'is in the tuple:weather')
else:
    print(a,' is not in the tuple:weather')
if(b not in weather):
    print('b is not in weather')
else:
    print('b is in weather')
