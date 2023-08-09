import os
import calendar
#how many times number 4 is in the list
x1 =[1,3,4,5,2,7,4]
x2=x1.count(4)
print (x2)


#Contain vowels or not
count =0
vowels ={"a","e","i","o","u"}
x3 = input("enter Your string here")
for characters in x3:
    if characters.lower() in vowels:
        count=count+1

if (count>=1):
    print("your strin contain vowels and its number is " + str(count))
else:
    print("your string dont contain characters")


#calculate the area of the circle
radius =int(input("enter the radius of the circle"))
area = ((radius**2)*(3.14159))
print("the area of the circle is "+str(area))

#Access the enviroment OS

current_path =os.getcwd()
operating_system=os.name
home_directory=os.path.expanduser("~")
print ("the current path is ",current_path)
print ("the current operating system is ",operating_system)
print ("the home directory is  ",home_directory)


#calender
year =int(input("enter the year you want"))
month=int(input("enter the month you want"))

print (calendar.month(year,month))