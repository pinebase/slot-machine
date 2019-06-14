
# Program Name:		Slot Machine
# Program Author:	Scott Forsberg
# Creation Date:	2019-03-04
# Class:		CSE 110
# Python Version:	3.7.1



# import graphics library
from graphics import *

#import random library
import random

# draw the window
win = GraphWin("Slot Machine",600,600)

# set window background to white
win.configure(background='white')



# define a rectangle tile object slot1
slot1 = Rectangle(Point(15,15),Point(195,195))

# draw the tile object slot1
slot1.draw(win)

# clone tile object slot1 into slot2
slot2 = slot1.clone()

# draw the tile object slot2
slot2.draw(win)

# move tile object slot2 to new location
slot2.move(195, 0)

# clone tile object slot2 into slot3
slot3 = slot2.clone()

# draw the tile object slot3
slot3.draw(win)

# move tile object slot3 to new location
slot3.move(195, 0)


# circle function
def circle(slot):
    # define circle object, inheriting the center point (h,k) from current slot object
    c = Circle(slot.getCenter(),40)

    # set background to red
    c.setFill("red")

    # return the circle object
    return c


# triangle function
def triangle(slot):

    # define positional parameters 
    upperCenterXTR = slot.getCenter().getX()
    upperCenterYTR = slot.getCenter().getY() - 40

    bottomRightXTR = slot.getCenter().getX() + 40
    bottomRightYTR = slot.getCenter().getY() + 40

    bottomLeftXTR = slot.getCenter().getX() - 40
    bottomLeftYTR = slot.getCenter().getY() + 40

    # define triangle polygon object
    tr = Polygon(Point(upperCenterXTR,upperCenterYTR),Point(bottomRightXTR,bottomRightYTR),Point(bottomLeftXTR,bottomLeftYTR))

    # set background to blue
    tr.setFill('blue')

    # return the triangle object   
    return tr


# square function
def square(slot):

    # define positional parameters    
    upperLeftXSQ = slot.getCenter().getX() + 40
    upperLeftYSQ = slot.getCenter().getY() + 40

    bottomRightXSQ = slot.getCenter().getX() - 40
    bottomRightYSQ = slot.getCenter().getY() - 40
    
    # define square polygon object
    sq = Rectangle(Point(upperLeftXSQ,upperLeftYSQ), Point(bottomRightXSQ,bottomRightYSQ))

    # set background to yellow
    sq.setFill('yellow')

    # return the square object    
    return sq



# diamond function
def diamond(slot):

    # define positional parameters 
    upperCenterXTR = slot.getCenter().getX()
    upperCenterYTR = slot.getCenter().getY() - 40

    bottomRightXTR = slot.getCenter().getX() + 40
    bottomRightYTR = slot.getCenter().getY()

    bottomLeftXTR = slot.getCenter().getX() - 40
    bottomLeftYTR = slot.getCenter().getY()

    bottomCenterXTR = slot.getCenter().getX()
    bottomCenterYTR = slot.getCenter().getY() + 40


    # define polygon object
    tr = Polygon(Point(upperCenterXTR,upperCenterYTR),Point(bottomLeftXTR,bottomLeftYTR),Point(bottomCenterXTR,bottomCenterYTR),Point(bottomRightXTR,bottomRightYTR))

    # set background
    tr.setFill('purple')

    # return the object   
    return tr


# diamond function
def oval(slot):

    # define positional parameters 
    upperLeftXSQ = slot.getCenter().getX() + 40
    upperLeftYSQ = slot.getCenter().getY() + 20

    bottomRightXSQ = slot.getCenter().getX() - 40
    bottomRightYSQ = slot.getCenter().getY() - 20

    # define polygon object
    tr = Oval(Point(upperLeftXSQ,upperLeftYSQ), Point(bottomRightXSQ,bottomRightYSQ))

    # set background
    tr.setFill('orange')

    # return the object   
    return tr


# pentagon function
def pentagon(slot):

    # define positional parameters 
    upperCenterXTR = slot.getCenter().getX()
    upperCenterYTR = slot.getCenter().getY() - 40

    bottomRightXTR = slot.getCenter().getX() + 40
    bottomRightYTR = slot.getCenter().getY() - 5

    bottomLeftXTR = slot.getCenter().getX() - 40
    bottomLeftYTR = slot.getCenter().getY() - 5

    bottomCenterXTR = slot.getCenter().getX() - 22
    bottomCenterYTR = slot.getCenter().getY() + 40

    bottomCenterLXTR = slot.getCenter().getX() + 22
    bottomCenterLYTR = slot.getCenter().getY() + 40



    # define polygon object
    tr = Polygon(Point(upperCenterXTR,upperCenterYTR),Point(bottomLeftXTR,bottomLeftYTR),Point(bottomCenterXTR,bottomCenterYTR),Point(bottomCenterLXTR,bottomCenterLYTR),Point(bottomRightXTR,bottomRightYTR))

    # set background
    tr.setFill('green')

    # return the object   
    return tr


# put slot objects into list
slots = [slot1,slot2,slot3]



# function to return random shape
def randShape():
    return random.randrange(6)


# function to load the play button
def buttonLoad(upperLeftX,upperLeftY,bottomRightX,bottomRightY):

    r =  Rectangle(Point(upperLeftX,upperLeftY), Point(bottomRightX,bottomRightY))
    r.draw(win)

    # define positional parameters  
    centerX = (upperLeftX + bottomRightX) / 2
    centerY =(upperLeftY + bottomRightY) / 2

    # enter play label  
    label = Text(Point(centerX,centerY), "Play")
    label.setSize(18)
    label.draw(win)

# load the play button
buttonLoad(210,210,390,270)

# define dictionaries
rendered_shapes = {}
rendered_messages = {}
winning_shapes = {}


# funcition to loaed the shapes
def playLoad():

    # check winner message dicitonary for previous entry, and undraw if found
    if 'winner' in rendered_messages:
        rendered_messages['winner'].undraw()

    # reset current tile number
    current_tile=0

    # iterate through tile slot objects
    for slot in slots:

        # select shape 0-2
        shape = randShape()

        # tiles 1-3
        current_tile = current_tile + 1

        # undraw previous shape for the current tile
        if current_tile in rendered_shapes:
            rendered_shapes[current_tile].undraw()

        # check if circle 0  
        if shape == 0:
            # create circle object
            current_shape = circle(slot)
            # create shape variable
            winning_shape = 'circle'

        # check if square 1  
        if shape == 1:
            # create triangle object
            current_shape = square(slot)
            # create shape variable
            winning_shape = 'square'

        # check if triangle 2              
        if shape == 2:
            # create triangle object
            current_shape = triangle(slot)
            # create shape variable
            winning_shape = 'triangle'

        # check if diamond 3              
        if shape == 3:
            # create diamond object
            current_shape = diamond(slot)
            # create shape variable
            winning_shape = 'diamond'

        # check if oval 4              
        if shape == 4:
            # create oval object
            current_shape = oval(slot)
            # create shape variable
            winning_shape = 'oval'

        # check if pentagon 5              
        if shape == 5:
            # create pentagon object
            current_shape = pentagon(slot)
            # create shape variable
            winning_shape = 'pentagon'






            
        # dictionary keys 1,2,3

        # update shape objects dictionary with key being current tile 
        rendered_shapes[current_tile] = current_shape

        # update winning shapes tracker dictionary with key being current tile 
        winning_shapes[current_tile] = winning_shape

        # draw the current shape
        current_shape.draw(win)


    # if all the generate shapes for last load were same
    if winning_shapes[1] == winning_shapes[2] == winning_shapes[3]:
        
        # create winner message
        winner_message = Text(Point(300,370), "Winner!")

        winner_message.setSize(30)
        rendered_messages['winner'] = winner_message
        winner_message.draw(win)
        

        
          


# check if true
while True:

    # get mous x,y coords
    p = win.getMouse()
    #test click position
    #print("You clicked", p.getX(), p.getY())

    # if clicked within play button
    if p.getX() > 210 and p.getX() < 390:

        if p.getY() > 210 and p.getY() < 270:       

            # load the shapes
            playLoad()


