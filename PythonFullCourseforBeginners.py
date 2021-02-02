# 03/02/2021 01:33
# WELCOME TO PythonFullCourseforBeginners.py

# I have learned and master this from:
# Learn Python - Full Course for Beginners [Tutorial]
# https://www.youtube.com/watch?v=rfscVS0vtbw

#--------------------------------------------------------------
#
# Needs improvement:
#
# 15. IF STATEMENTS & COMPARISONS (01:54:07)
# 19. BUILDING A GUESSING GAME (02:20:02)
# 23. BUILD A TRANSLATOR (02:52:41)
# 25. TRY EXCEPT (03:04:17)
# 32. INHERITANCE (03:28:13) *****REVIEW THIS*****
#--------------------------------------------------------------


# DIRECTORY:
# 1. INSTALLING PYTHON & PYCHARM (00:01:47 TS)
# 2. SETUP & HELLO WORLD (00:06:41 TS)
# 3. DRAWING A SHAPE (00:10:24 TS)
# 4. VARIABLES  & DATA TYPES (00:15:07 TS)
# 5. WORKING WITH STRINGS (00:24:04 TS)
# 6. WORKING WITH NUMBERS (00:38:21 TS)
# 7. GETTING INPUT FROM USERS (00:48:26 TS)
# 8. BUILDING A BASIC CALCULATOR (00:52:39 TS)
# 9. MAD LIBS GAME (00:58:28 TS)
# 10. LISTS (01:03:10 TS)
# 11. LIST FUNCTIONS (01:10:44 TS)
# 12. TUPLES (01:18:57 TS)
# 13. FUNCTIONS (01:24:16 TS)
# 14. RETURN STATEMENT (01:34:12 TS)
# 15. IF STATEMENTS & COMPARISONS (01:54:07)
# 16. BUILDING A BETTER CALCULATOR (02:00:39)
# 17. DICTIONARIES (02:07:17)
# 18. WHILE LOOP (02:14:15)
# 19. BUILDING A GUESSING GAME (02:20:02)
# 20. FOR LOOP (02:32:45)
# 21. EXPONENT FUNCTION (02:41:20)
# 22. 2D LISTS & NESTED LOOPS (02:47:13)
# 23. BUILD A TRANSLATOR (02:52:41)
# 24. COMMENTS (03:00:18)
# 25. TRY EXCEPT (03:04:17)
# 26. READING FILES (03:12:42)
# 27. WRITING TO FILES (03:21:26)
# 28. MODULES AND PIP (03:28:13 TS)
# 29. CLASSES & OBJETCS  (03:43:55 TS)
# 30. BUILDING A MULTIPLE CHOICE QUIZ (03:57:36)
# 31. OBJECT FUNCTIONS (04:08:28 TS)
# 32. INHERITANCE (04:12:37)

# HELLO WORLD

print("Hello World") # print statement


# Drawing Shapes

print("    /|")
print("   / |")
print("  /  |")
print(" /___|")


print(" /___|")
print("    /|")
print("   / |")
print("  /  |")


# VARIABLES & DATA TYPES

character_name = "Tom"
character_age = 50
is_male = False
print("There once a man named " + character_name + ",")
print("he was " + character_age + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ",")
print("but didn't like being " + character_age + ".")


# WORKING WITH STRINGS

print ("Giraffe Academy")

phrase = "Giraffe Academy"
print (phrase)

phrase = "Giraffe Academy"
print (phrase + " is cool")

phrase = "Giraffe Academy"
print (phrase.lower())               # using simple function

phrase = "Giraffe Academy"
print (phrase.upper())                # function

phrase = "Giraffe Academy"
print (phrase.isupper())

phrase = "Giraffe Academy"
print (phrase.upper().isupper())

phrase = "Giraffe Academy"
print (len(phrase))

phrase = "Giraffe Academy"
print (phrase[0])

phrase = "Giraffe Academy"
print (phrase[3])

phrase = "Giraffe Academy"
print (phrase.index("G"))       	# index function

phrase = "Giraffe Academy"
print (phrase.index("a"))

phrase = "Giraffe Academy"
print (phrase.index("Acad"))

phrase = "Giraffe Academy"
print (phrase.replace("Giraffe","Elephant")) # replace function


# find a list of functions in google.
# check google for more python functions

# WORKING WITH NUMBERS

print(3 * (4 + 5))

print(10 % 3)	# modulus operator - "10 mod 3"

my_num = 5
print(my_num)

my_num = 5
print(str(my_num) + " my favorite number")

my_num = -5
print(abs(my_num))  # absolute number - "absolute value"

my_num = -5
print(pow(3, 2))

my_num = -5
print(pow(4, 6))	# power function

my_num = -5
print(max(4, 6))

my_num = -5
print(min(4, 6))

my_num = -5
print(round(3.7))


from math import *

my_num = -5
print(floor(3.7))


my_num = -5
print(ceil(3.7))


from math import *

my_num = -5
print(sqrt(36))

# check for more math functions in google.

# GETTING INPUT FROM USERS

name = input("Enter your name: ")
print("Hello " + name + "!")
------
Enter your name: Mike
Hello Mike!

name = input("Enter your name: ")
name = input("Enter your last name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old.")
------
Enter your name: John
Enter your last name: Snow
Enter your age: 35
Hello Snow! You are 35 years old.


# BUILDING A BASIC CALCULATOR

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result)


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result)


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)


# MAD LIBS GAME

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


# LISTS

friends = ["Kevin", "Karen", "Jim"]
print(friends[0])

friends = ["Kevin", "Karen", "Jim"]
print(friends[-1])


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:3])


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[1:5])


friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends[1] = "Mike"
print(friends[1])



# LIST FUNCTIONS

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)		# friends.extend
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.append("Creed")			# friends.append
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly")		# friends.insert
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.remove("Jim")			# friends.remove
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.clear()				# friends.clear
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()		# friends.pop
print(friends)		# removed last element from the list



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends.index("Kevin"))



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends.index("Oscar"))



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print(friends.count("Jim"))



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.sort()
print(friends)


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers.sort()
print(lucky_numbers)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
lucky_numbers.reverse()
print(lucky_numbers)



lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()

print(friends2)



# TUPLES

coordinates = (4, 5)	# TUPLES is immutable, cannot be change

print(coordinates[0])


coordinates = [(4, 5), (6, 7), (80, 34)]
coordinates[1] = 10
print(coordinates[1])



# FUNCTIONS

def sayhi():
    print("Hello User")


sayhi()



def sayhi():
    print("Hello User")


print("Top")
sayhi()
print("Bottom")



def say_hi(name):
    print("Hello " + name)


say_hi("Mike")
say_hi("Steve")



def say_hi(name, age):
    print("Hello " + name + ", you are " + age)


say_hi("Mike", "35")
say_hi("Steve", "70")



def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Mike", 35)
say_hi("Steve", 70)




# RETURN STATEMENT

def cube(num):
    return num*num*num


print (cube(3))


def cube(num):
    return num*num*num


print (cube(4))



def cube(num):
    return num*num*num


result = cube (4)
print (result)


# IF STATEMENTS

is_male = True

if is_male:
    print("You are a male")


is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")


    
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
   
    
    
is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")    
    
    
    
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")
    
    
    
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")    




is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")



is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are either not male or not tall or both")




is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")



# IF STATEMENTS & COMPARISONS

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))



# BUILDING A BETTER CALCULATOR

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 -  num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")



# DICTIONARIES

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])



monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])	#[]



monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Dec"))	# get function




December

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Luv")




monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Luv", "Not a valid key"))





# WHILE LOOP

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")





# BUILDING A GUESSING GAME

- use of WHILE LOOP
- use of IF STATEMENTS

secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You win!")




secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")





secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")




# FOR LOOP

for letter in "Giraffe Academy":
    print(letter)



friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)



friends = ["Jim", "Karen", "Kevin"]
for index in range(10):
    print(index)



friends = ["Jim", "Karen", "Kevin"]
for index in range(3, 10):
    print(index)



friends = ["Jim", "Karen", "Kevin"]

for index in range(len(friends)):
    print(friends[index])



friends = ["Jim", "Karen", "Kevin"]

for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")





# EXPONENT FUNCTION

print(2**3)




def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3,2))





def raise_to_power(base_num, pow_num):


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3,4))




# 2D LISTS & NESTED LOOPS

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])




number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])



number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    print(row)






number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)





# BUILD A TRANSLATOR

Giraffe Language
vowels -> g




def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))





def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))






def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))





def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation






# COMMENTS

# This program is cool
print("Comments are fun")



# This print out a string
print("Comments are fun")

 		# use of three ''' single quotation as COMMENT
'''
asdfasdfsdfkslkdlk
asdfklksdf
asdfasdf
asdf
asdf
fasdf
'''

# This print out a string

print("Comments are fun")



# TRY EXCEPT

number = int(input("Enter a number: "))
print(number)



try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")




try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")





try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")






try:

    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")



try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")




# READING FILES


# "r" - read file
# "w" - write
# "a" - append (add new information)
# "r+" - read and write

open("employees.txt", "r")



employee_file = open("employees.txt", "r")

print(employee_file.readable())

employee_file.close()





employee_file = open("employees.txt", "w")

print(employee_file.readable())

employee_file.close()






employee_file = open("employees.txt", "r")

print(employee_file.read())

employee_file.close()





employee_file = open("employees.txt", "r")

print(employee_file.readline())


employee_file.close()




employee_file = open("employees.txt", "r")

print(employee_file.readline())
print(employee_file.readline())
employee_file.close()




employee_file = open("employees.txt", "w")

print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

employee_file.close()




employee_file = open("employees.txt", "w")

print(employee_file.readlines())	# .readlines

employee_file.close()



employee_file = open("employees.txt", "w")

print(employee_file.readlines()[1])

employee_file.close()




employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()






# WRITING TO FILES


employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()





employee_file = open("employees.txt", "a")

employee_file.write("Toby - Human Resources")

employee_file.close()






employee_file = open("employees.txt", "a")

employee_file.write("Toby - Human Resources")

employee_file.close()





employee_file = open("employees.txt", "a")	#"a"

employee_file.write("\nKelly - Customer Service")

employee_file.close()




employee_file = open("employees.txt", "w")	#"w"

employee_file.write("\nKelly - Customer Service")

employee_file.close()




employee_file = open("employees1.txt", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()




employee_file = open("index.html.", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()





# MODULES AND PIP

# Note:
'''

# filename useful_tools.py
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Star"]


def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)

'''

import useful_tools

print(useful_tools.roll_dice(10))




# CLASSES & OBJECTS

'''
# Student.py filename
class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
'''


from Student import Student

student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)




from Student import Student

student1 = Student("Jim", "Business", 3.1, False)

print(student1.gpa)



from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Business", 2.5, True)
print(student1.gpa)



from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Business", 2.5, True)
print(student2.gpa)





# BUILDING A MULTIPLE CHOICE QUIZ

# Note:
#- this program was not successful
#- this program was not successful
#- this program was not successful


question_prompts = [
	"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
	"What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
	"What color are apples?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]



from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are apples?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)




from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are apples?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)





# OBJECT FUNCTIONS


'''
# Student.py filename

class Student:

    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
'''


from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())



from Student import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student2.on_honor_roll())



# INHERITANCE

# Note:
#-make ChineseChef.py Class filename
#-make ItalianChef.py Class filename

'''
# Chef.py class filename

class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a bbq ribs")

'''

from Chef import Chef

myChef = Chef()
myChef.make_chicken()


# STOPPED AT (04:14:14)
# STOPPED AT (04:14:14)
# STOPPED AT (04:14:14)
# STOPPED AT (04:14:14)
# STOPPED AT (04:14:14)



