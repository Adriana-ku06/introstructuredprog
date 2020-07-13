#Adriana ku exercise 26
from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
tall=input() #undeclared tall variable
print("How much do you weigh?", end=' ')#first error missing closing parentheses
weight = input()

print(f"So, you're {age} old, {tall} height  and {weight} heavy.")#variable declaration error



script, filename = argv #error. import from argv

txt = open(filename)#variable write error

print(f"Here's your file {filename}:")
print(txt.read())#variable write error is txt

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())#function call error is "." no " _"


print("Let's practice everything.")#error two, single quotes in a print
print("You \d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")#error three, line break and single quotes

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")#error 4 missing closing quote
print(poem)
print("--------------")#error 5, a start quote is required


five = 10 - 2 + 3 - 6 #error 6 sign without variable to subtract
print(f"This should be five: {five}") 
def secret_formula (started): #error 8, missing ":" in the function declaration
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100 # error 9, missing division operation symbols
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)##variable write error
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 ##variable write error
dogs = 15


if people < cats:
    print ("Too many cats! The world is doomed!") #Error 10, parenthesis in missing print 

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs: ##error 11, missing ":" in the declaration
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:#error 12, missing ":" in the function declaration
    print("People are less than or equal to dogs.") #error 8, missing " in the function declaration

if people == dogs: #error 13, missing "==" in the function declaration
    print("People are dogs.")
    