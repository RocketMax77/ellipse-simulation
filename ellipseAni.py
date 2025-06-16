'''This code is meant to help show the geometric deriviation
of the ellipse using math and matplotlib'''

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
majorAxis = pyip.inputFloat(prompt='Type the major axis here: ')
fociDist = pyip.inputFloat(prompt='Input foci dist here: ')
minorAxis = np.sqrt(majorAxis**2 - fociDist**2)
xVals = list(np.arange(-1*majorAxis, majorAxis, 0.01))
xVals.reverse()
yVals = [ellipseFunc(majorAxis, minorAxis, x) for x in xVals]
xVals2 = list(np.arange(-1*majorAxis, majorAxis, 0.01))
yVals2 = [ellipseFunc(majorAxis, minorAxis, x, True) for x in xVals]
xVals += xVals2
yVals += yVals2
numFrames = len(xVals)


#Ploting mangos
fig, ax = plt.subplots()
plt.style.use('seaborn-v0_8')
plt.grid(True)
ellipse = ax.plot(xVals[0], yVals[0], color='black')[0]
lineF1 = ax.plot(-1*fociDist, 0, color='red')[0]
lineF2 = ax.plot(fociDist, 0, color='red')[0]
lineTV1 = ax.plot(xVals[0], 0, linestyle='dashed')[0]
ax.set(xlim=[-6,6], ylim=[-6,6])

#animates the plot
def animateElipse(frame):
    '''A helper function that animates the plot'''
    
    x = xVals[:frame]
    y = yVals[:frame]
    ellipse.set_xdata(x)
    ellipse.set_ydata(y)

    xline = [-1*fociDist, xVals[frame]]
    yline = [0, yVals[frame]]
    xline2 = [fociDist, xVals[frame]]
    yline2 = [0, yVals[frame]]
    lineF1.set_xdata(xline)
    lineF1.set_ydata(yline)
    lineF2.set_xdata(xline2)
    lineF2.set_ydata(yline2)

    xlineTV1 = [xVals[frame], xVals[frame]]
    ylineTV1 = [0, yVals[frame]]
    lineTV1.set_xdata(xlineTV1)
    lineTV1.set_ydata(ylineTV1)


    return (ellipse, lineF1, lineF2, lineTV1)

animated = animation.FuncAnimation(fig=fig, func=animateElipse, frames=numFrames, interval=20,)
plt.show()







