''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''

import turtle
print("===== Python Packages & Core Package =====")
''' Python Packages/Modules: Core, File, External'''
# Core Packages -> https://docs.python.org/3/library/


# CORE
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(150)
# turtle.done()


print("--"*30)
my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()


# with - Context Manager
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
print("DONE")
