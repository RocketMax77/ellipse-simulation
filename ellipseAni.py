'''The *Geometric deriviation of an ellipse* pretty dope
stuff imo'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pyinputplus as pyip

def ellipseFunc(majorAxis, minorAxis, x, upperLower=False):
    '''The function of an ellipse'''
    output = np.sqrt(minorAxis**2 - (minorAxis**2 * x**2)/majorAxis**2)
    if upperLower == True:
        output *= -1
    return output

#data
print("Note: The major axis needs to be greater than the foci dist")
majorAxis = pyip.inputFloat(prompt='Type half the length of the major axis here: ')
fociDist = pyip.inputFloat(prompt='Input foci dist here: ')
minorAxis = np.sqrt(majorAxis**2 - fociDist**2)
xVals = list(np.arange(-1*majorAxis, majorAxis, 0.01))
xVals.reverse()
yVals = [ellipseFunc(majorAxis, minorAxis, x) for x in xVals]
xVals2 = list(np.arange(-1*majorAxis, majorAxis, 0.01))
yVals += [ellipseFunc(majorAxis, minorAxis, x, True) for x in xVals2]
xVals += xVals2
numFrames = len(yVals)


#Ploting mangos
fig, ax = plt.subplots()
plt.style.use('seaborn-v0_8')
plt.grid(True)
ellipse = ax.plot(xVals[0], yVals[0], color='black')[0] #The actual ellipse
mesage = """The sum of the distances from every point on the parabola
to each foci is equal to the major axis!"""
lineF1 = ax.plot(-1*fociDist, 0, color='red', label=mesage)[0] #Foci one
lineF2 = ax.plot(fociDist, 0, color='red')[0] #Foci two
lineTV1 = ax.plot(xVals[0], 0, linestyle='dashed')[0] #Vertial line to show right triangles
foci1 = ax.scatter(-1*fociDist, 0, color='darkorange', s=80, label='Foci')
foci2 = ax.scatter(fociDist, 0, color='darkorange', s=80)
ax.set(xlim=[((-1*majorAxis)-2), (majorAxis+2)], ylim=[((-1*majorAxis)-2), (majorAxis+2)])

#animates the plot
def animateElipse(frame):
    '''A function that animates the plot'''
    
    x = xVals[:frame]
    y = yVals[:frame]
    ellipse.set_xdata(x)
    ellipse.set_ydata(y)

    xF1 = [-1*fociDist, xVals[frame]]
    yF1 = [0, yVals[frame]]
    xF2 = [fociDist, xVals[frame]]
    yF2 = [0, yVals[frame]]
    lineF1.set_xdata(xF1)
    lineF1.set_ydata(yF1)
    lineF2.set_xdata(xF2)
    lineF2.set_ydata(yF2)

    xlineTV1 = [xVals[frame], xVals[frame]]
    ylineTV1 = [0, yVals[frame]]
    lineTV1.set_xdata(xlineTV1)
    lineTV1.set_ydata(ylineTV1)

    return (ellipse, lineF1, lineF2, lineTV1, foci1)

animated = animation.FuncAnimation(fig=fig, func=animateElipse, frames=numFrames, interval=10,)
plt.legend()
plt.show()







