"""
Program to aid maths assesment on mensuration and are/length of arcs and sectors

window function must be sepearate to math function
and variables in window function being used by math function must be made global
math.pow(x, y) function input must be float
must close all windows before opening new ones as radius variable is generic and may result in error or
variable with incorrect value
"""
import math
import tkinter as tk
import time

#specify inputs
radius = 0
slantedHeight = 0
height = 0
baseArea = 0
degrees = 0
radians = 0
radianInput = 0
degreesInput = 0
a = 0
b = 0
c = 0
sectorAngle = 0
circumference = 0
circleArea = 0
output = 0
pi = float(math.pi)
radiusEntry = 0
#preset username and password
username = "classB"
password = "assignment"
access = "false"
#Security Function

def attemptUser():
    userAttempt = userInput.get()
    if userAttempt == username:
        security.destroy()
        newWindow()
    else:
        checkUser.config(text="Incorrect")

def openWindow2():
    #convert radians to degrees
    window2Con = tk.Tk()
    global radianInput
    global degreeButton
    radianInput = tk.Entry(window2Con)
    degreeButton = tk.Button(window2Con, text="Degrees =", command=radiansToDegrees)
    radianInput.pack()
    degreeButton.pack()
    window2Con.mainloop()

def radiansToDegrees():
    radians = radianInput.get()
    degreeFinal = int(radians) * (180 / math.pi)
    degreeButton.config(text="Degrees = " + str(degreeFinal)) 

def openWindow3():
    #convert degrees to radians
    window3Con = tk.Tk()
    global degreeInput
    global radianButton
    degreeInput = tk.Entry(window3Con)
    radianButton = tk.Button(window3Con, text="Radians =", command=degreesToRadians)
    degreeInput.pack()
    radianButton.pack()
    window3Con.mainloop()

def degreesToRadians():
    degrees = degreeInput.get()
    radianFinal = int(degrees) * (pi / 180)
    radianButton.config(text="Radians = " + str(radianFinal))

def attemptPass():
    global access
    passAttempt = passEntry.get()
    if passAttempt == password:
        checkPass.config(text="Correct")
        access = "true"
        window2.destroy()
        
    else:
        checkPass.config(text="incorrect")

def newWindow():
    #must be global as function will change value of variable
    global passEntry, window2
    window2 = tk.Tk()
    passEntry = tk.Entry(window2, show="*")
    #must be global as function will change value of variable
    global checkPass
    checkPass = tk.Button(window2, text="Login", command=attemptPass)
    passEntry.pack()
    checkPass.pack()
    window2.mainloop()

def security():
    global userInput, checkUser, security
    security = tk.Tk()
    checkUser = tk.Button(security, text="Enter Username: ", command=attemptUser)
    userInput = tk.Entry(security, text="Enter Username: ")
    userInput.pack()
    checkUser.pack()
    security.mainloop()

def instructions():
    ins = tk.Tk()
    instructions = tk.Label(ins, text="WARNING - Close each function window before opening the next")
    instructions.pack()
    ins.mainloop()

def coneSA():
    #sureface area of a cone
    global answer, radiusEntry, sHeightEntry
    windowConeSA = tk.Tk()
    radiusEntryLabel = tk.Label(windowConeSA, text="Radius:")
    radiusEntry = tk.Entry(windowConeSA)
    sHeightEntryLabel = tk.Label(windowConeSA, text="Enter slanted height")
    sHeightEntry = tk.Entry(windowConeSA)
    slantedHeight = sHeightEntry.get()
    answer = tk.Button(windowConeSA, text="Answer", command=CSAout)
    radiusEntryLabel.pack()
    radiusEntry.pack()
    sHeightEntryLabel.pack()
    sHeightEntry.pack()
    answer.pack()
    windowConeSA.mainloop()
    
def CSAout():
    slantedHeight = float(sHeightEntry.get())
    radius = float(radiusEntry.get())
    radius2 = math.pow(radius, 2)
    output = pi * radius2 + pi * radius * slantedHeight
    answer.config(text="Answer = " + str(output))

def CVout():
    radius = float(radiusEntry.get())
    radius2 = math.pow(radius, 2)
    height = heightEntry.get()
    output = (1 / 3) * pi * radius2 * int(height)
    answer.config(text="Answer = " + str(output))
    
def coneV():
    #volume of a cone
    global radiusEntry, heightEntry, answer
    coneV = tk.Tk()
    radiusEntryLabel = tk.Label(coneV, text="Radius:")
    radiusEntry = tk.Entry(coneV)
    heightEntryLabel = tk.Label(coneV, text="Height:")
    heightEntry = tk.Entry(coneV)
    answer = tk.Button(coneV, text="Answer", command=CVout)

    radiusEntryLabel.pack()
    radiusEntry.pack()
    heightEntryLabel.pack()
    heightEntry.pack()
    answer.pack()
    coneV.mainloop()

def sphereA():
    #area of a sphere
    sphereA = tk.Tk()
    global radiusEntry, answer
    radiusEntryLabel = tk.Label(sphereA, text="Radius:")
    radiusEntry = tk.Entry(sphereA)
    answer = tk.Button(sphereA, text="Answer", command=SAout)
    radiusEntryLabel.pack()
    radiusEntry.pack()
    answer.pack()
    sphereA.mainloop()
    

def SAout():
    radius = float(radiusEntry.get())
    radius2 = math.pow(radius, 2)
    output = 4 * pi * radius2
    answer.config(text="Answer = " + str(output))

def sphereV():
    #volume of a sphere
    sphereV = tk.Tk()
    global answer, radius3, radiusEntry
    radiusEntryLabel = tk.Label(sphereV, text="Radius:")
    radiusEntry = tk.Entry(sphereV)
    answer = tk.Button(sphereV, text="Answer", command=SVout)
    radiusEntryLabel.pack()
    radiusEntry.pack()
    answer.pack()
    sphereV.mainloop()
    

def SVout():
    radius = float(radiusEntry.get())
    radius3 = math.pow(radius, 3)
    output = (4 / 3) * pi * radius3
    answer.config(text="Answer = " + str(output))
    
    

def pyramidV():
    #volume of a pyramid
    global answer, baseWidthEntry, baseHeightEntry, heightEntry
    pyramidV = tk.Tk()
    baseWidthLabel = tk.Label(pyramidV, text="Base Width:")
    baseWidthEntry = tk.Entry(pyramidV)
    baseHeightLabel = tk.Label(pyramidV, text="Base Height:")
    baseHeightEntry = tk.Entry(pyramidV)
    heightLabel = tk.Label(pyramidV, text="Height:")
    heightEntry = tk.Entry(pyramidV)
    answer = tk.Button(pyramidV, text="Answer", command=PVout)

    baseWidthLabel.pack()
    baseWidthEntry.pack()
    baseHeightLabel.pack()
    baseHeightEntry.pack()
    heightLabel.pack()
    heightEntry.pack()
    answer.pack()
    pyramidV.mainloop()
    

def PVout():
    baseArea = float(baseHeightEntry.get()) * float(baseWidthEntry.get())
    height = float(heightEntry.get())
    output = baseArea * height * (1 / 3)
    answer.config(text="Answer = " + str(output))

def circleA():
    #area of a circle
    global answer, radiusEntry
    circleA = tk.Tk()
    radiusLabel = tk.Label(circleA, text="Radius:")
    radiusEntry = tk.Entry(circleA)
    answer = tk.Button(circleA, text="Answer", command=CAout)
    radiusLabel.pack()
    radiusEntry.pack()
    answer.pack()

def CAout():
    radius = float(radiusEntry.get())
    radius2 = math.pow(radius, 2)
    output = pi * radius2
    answer.config(text="Answer = " + str(output))
    

def triangleA():
    global sideAentry, angleBentry, sideCentry, answer
    #area of a triangle
    triangleA = tk.Tk()
    info = tk.Label(triangleA, text="In triangle ABC where angle is at ABC,")
    sideAlabel = tk.Label(triangleA, text="Length A =")
    sideAentry = tk.Entry(triangleA)
    angleBlabel = tk.Label(triangleA, text="Angle B =")
    angleBentry = tk.Entry(triangleA)
    sideClabel = tk.Label(triangleA, text="Length C =")
    sideCentry = tk.Entry(triangleA)
    answer = tk.Button(triangleA, text="Answer", command=TAout)
    sideAlabel.pack()
    sideAentry.pack()
    angleBlabel.pack()
    angleBentry.pack()
    sideClabel.pack()
    sideCentry.pack()
    answer.pack()
    triangleA.mainloop()

def TAout():
    a = float(sideAentry.get())
    b = float(angleBentry.get()) * (pi / 180)
    c = float(sideCentry.get()) 
    SinC = float(math.sin(b))
    output = (1 / 2) * a * c * SinC
    answer.config(text="Answer = " + str(output))
    

def arcLength():
    #length of an arc
    global radiusEntry, sectorEntry, answer
    arcLength = tk.Tk()
    radiusLabel = tk.Label(arcLength, text="Radius:")
    radiusEntry = tk.Entry(arcLength)
    sectorLabel = tk.Label(arcLength, text="Sector angle:")
    sectorEntry = tk.Entry(arcLength)
    answer = tk.Button(arcLength, text="Answer", command=ALout)
    radiusLabel.pack()
    radiusEntry.pack()
    sectorLabel.pack()
    sectorEntry.pack()
    answer.pack()

def ALout():
    radius = float(radiusEntry.get())
    circumference = radius * 2
    sector = float(sectorEntry.get()) / 360.0
    output = pi * circumference * sector
    answer.config(text="Answer = " + str(output))

def sectorArea():
    #area of a sector
    global radiusEntry, sectorEntry, answer
    sectorArea = tk.Tk()
    radiusLabel = tk.Label(sectorArea, text="Radius:")
    radiusEntry = tk.Entry(sectorArea)
    sectorLabel = tk.Label(sectorArea, text="Sector angle:")
    sectorEntry = tk.Entry(sectorArea)
    answer = tk.Button(sectorArea, text="Answer", command=SectAout)
    radiusLabel.pack()
    radiusEntry.pack()
    sectorLabel.pack()
    sectorEntry.pack()
    answer.pack()
    sectorArea.mainloop()
    

def SectAout():
    radius = float(radiusEntry.get())
    radius2 = math.pow(radius, 2)
    sector = float(sectorEntry.get()) / 360
    output = pi * radius2 * sector
    answer.config(text="Answer = " + str(output))

#opening window

security()
if access == "true":
    instructions()
    
    window = tk.Tk()
    radianDegreeChoice = tk.Button(window, text="Radians to Degrees", command=openWindow2)
    degreeRadianChoice = tk.Button(window, text="Degrees to Radians", command=openWindow3)
    choice = tk.Label(window, text="What would you like to work out?")
    coneSurfaceArea = tk.Button(window, text="Surface area of a cone", command=coneSA)
    coneVolume = tk.Button(window, text="Volume of a cone", command=coneV)
    sphereArea = tk.Button(window, text="Area of a Sphere", command=sphereA)
    sphereVolume = tk.Button(window, text="Volume of a sphere", command=sphereV)
    pyramidVolume = tk.Button(window, text="Volume of a pyramid", command=pyramidV)
    circleArea = tk.Button(window, text="Area of a circle", command=circleA)
    triangleArea = tk.Button(window, text="Area of a triangle", command=triangleA)
    arcLength = tk.Button(window, text="Length of an arc", command=arcLength)
    sectorArea = tk.Button(window, text="Area of a sector", command=sectorArea)
    choice.pack()
    radianDegreeChoice.pack()
    degreeRadianChoice.pack()
    coneSurfaceArea.pack()
    coneVolume.pack()
    sphereArea.pack()
    sphereVolume.pack()
    pyramidVolume.pack()
    circleArea.pack()
    triangleArea.pack()
    arcLength.pack()
    sectorArea.pack()
    window.mainloop()
    

