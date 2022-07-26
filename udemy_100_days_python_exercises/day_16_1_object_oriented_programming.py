#Procedural programming = early paradigm of programming,
# where code is considered as sequence of instructions to be executed

#split larger task into smaller piece, each of those pieces can be worked on by separate teams, 
# and can be reused if we need same functionality in the future
#makes code scalable for use in large scale projects


#An Object has :
#1. attributes i.e. what it has
#2. Methods i.e. what it can do 

#ex : Waiter
#attributes : is holding plate = True; tables_responsible [4,5,6]
#methods : take_order(table, order): #takes order to chef; take_payment(amount):#add money to restaurant


#note:
#attribute is just word for variable associated with a modelled object i.e. like waiter, is attached to a particular object.
#same for "method". it is a function, h/e it is a function that a particular modeled object can do. ie we need a waiter object to take an order and payment
#these are not free floating variables or functions.

#so essentially object is a way of combingin some pieces of data (attriubtes) and functionality (methods) in one same thing.

#we can generate multiple versions of the same object. 
# these are OBJECTS. we use the CLASS as a blueprint. 
# the versions generated are called an OBJECT.

#CONSTRUCTING OBJECTS AND ACCESSING THEIR ATTRIBUTES AND METHODS

#car = CarBlueprint()
#object    #class
#class (CarBlueprint()) is written in Pascal case (vs camel_case) to distinguis it from variable and function names in python.

from turtle import Turtle, Screen 

timmy = turtle.Turtle() #parentheses construct /initialise an object from class blueprint and saved into object turtle
print(timmy)

#OBJECT ATTRIBUTES

 #to access attributes, syntax of code is following :
 #car.speed 
 #car = object, full stop separates object from attribute we want to access 

my_screen = Screen ()
print(my_screen.canvheight) #canvas height is attribute associated with Screen class and tf object we created based on Screen class blueprint

 #OBJECT METHODS
 #car.stop()
my_screen.exitonclick()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)

