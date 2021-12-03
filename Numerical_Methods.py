import matplotlib.pyplot as plt
from tkinter import *

"""
Euler method
n - Iteration, h - Step, (x, y) - Cauchy problem
"""

xlist = []
ylist = []
yCorList = []
def Euler():
    n=10
    h=0.1
    x=0
    y=-1
    xlist.append(x)
    ylist.append(y)
    yCorList.append(CorrectFunction(x))
    result = "\nEuler method\n"
    result += "%7s\t%7s\t%7s\t%7s\n" % ("x", "y", "y*", "y*-y")

    result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    for i in range(n-1):
            y += h * Function(x, y)
            x += h
            xlist.append(x)
            ylist.append(y)
            yCorList.append(CorrectFunction(x))
     
            result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    return result #solution


'''
 Improved Euler - Cauchy method
'''
ylist2 = []
def EulerK():
    n=10
    h=0.1
    x=0
    y=-1
    ylist2.append(y)
    result = "\nEuler - Cauchy method\n"
    result += "%7s\t%7s\t%7s\t%7s\n" % ("x", "y", "y*", "y*-y")

    result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
    for i in range(n-1):
            yTemp = y + h * Function(x, y)
            yPrev = y
            xPrev = x
            x += h
            for j in range(3):
                if (j == 0 ): 
                    y = yPrev + h * (Function(xPrev, yPrev)+Function(x, yTemp))/2
                else:
                    y = yPrev + h * (Function(xPrev, yPrev)+Function(x, y))/2            
            ylist2.append(y)              
           
            result += "%7f %7f %7f %7f\n" % (x, y, CorrectFunction(x), CorrectFunction(x) - y)
                
    return result #solution:


yRunge = []
yR = []
deltaY = []
def Runge():
    #Runge rules
    h = 2*0.1
    n = 5
    x=0
    y=-1
    yR.append(y)

    for i in range(n-1):
        yTemp = y + h * Function(x, y)
        yPrev = y
        xPrev = x
        x += h
        for j in range(3):
            if (j == 0 ): 
                y = yPrev + h * (Function(xPrev, yPrev)+Function(x, yTemp))/2
            else:
                y = yPrev + h * (Function(xPrev, yPrev)+Function(x, y))/2
        yR.append(y)

    i = 0
    for k in range(n*2):
        if ( k%2 == 0):
            deltaY.append((ylist2[k]-yR[i])/(2**2-1))
            i += 1

    i = 0
    for k in range(n*2):
        if ((k%2)==0):
            yRunge.append( ylist2[k] + deltaY[i] )
            i += 1
        else:
            if(k==(n*2-1)):
                yRunge.append( ylist2[k] + ((deltaY[i-1])/2) )
                break              
            yRunge.append( ylist2[k] + ((deltaY[i-1] + deltaY[i])/2) )
                    

    result = "\nRunge rules\n"
    x = 0
    h = 0.1
    for elem in yRunge:
        result += "%7f  %7f\n" % (elem, CorrectFunction(x) - elem)
        x += h
    return result

"""
Given 1st order ODE: y'=f(x,y)
"""
def Function(x, y):
    return (-3 * y * x + 8 * y - x**2)/(x**2 - 5 * x + 6)


"""
Analytical solution:
"""
def CorrectFunction(x):
    return (-(1/4) * x**4 + (2/3) * x**3 + 12)/((x-2)*(x-2)*(x-3))



def ShowGUI(text):
    w = 500
    h = 300
    root = Tk()
    #root.geometry('600x400')
    root.title("Numerical Methods")

    frame1=Frame(root)
    lbl=Label(frame1,text=text)
    frame1.pack()
    lbl.pack(side='top')

    #plotting
    plt.plot(xlist, ylist,    "bo-", label='Euler method')
    plt.plot(xlist, yCorList, "r-o", label="Analytical solution")
    plt.plot(xlist, ylist2,   "gD",  label="Improved Euler (Euler - Cauchy) method")
    plt.plot(xlist, yRunge,   "y.--",label="Runge rules")
    plt.xlabel('X') 
    plt.ylabel('Y') 
    plt.title('') 
    plt.grid(True) 
    plt.legend()
    plt.show() 
    
    root.mainloop()

ShowGUI(Euler()+EulerK()+Runge())