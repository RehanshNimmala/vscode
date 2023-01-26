#declaring int datatype - single line comment
number = 123
print(number)

name = 'Naveen'  #declared string datastype - inline comment
print(name)

#declaring tuple datatype
tuple = ("naveen",700,"Reyansh",1234)
print(tuple)
print(tuple[0])

#declaring list datatype
list = ["reyansh",1,2,3]
print(list)
print(list[1])

#declaring dictionary datatype
dict={
    "carName":"Toyota",
    "miles":100
}
print(dict)
dict['colour'] = "White"
print(dict)

#multiline comment
'''
if else program used to find 
the grades of students
'''

grade = 67

if grade >= 80 :
    print("Your grade is A")
elif grade  >= 60 and grade < 80 :
    print("Your grade is B")
else :
    print("Your grade is C")

# FOR Loop example

listOfCars = ["BMW","Ford","Tesla"]
for x in listOfCars:
    print(x)

#While loop example

value = 6
while value > 0:
    value = value-1
    if value == 3:
        continue
    elif value == 2:
        pass
    print(value)