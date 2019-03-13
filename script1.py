import datetime
now = datetime.datetime.now()
print(now)
print("please enter your name: ")
name = input()
print("Hello " + name)
print("Enter your age: ")
age = int(input())
year_of_age100 = (100- age)+ now.year
print(f"you will be 100 years old in the year {year_of_age100}!")



