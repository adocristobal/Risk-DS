# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Andrea Dominique O. Cristobal
Data Science Training
September 3, 2020
"""

from matplotlib import pyplot as plt
import numpy as np
import os
os.getcwd()
os.chdir("/Users/mbp15/Documents/Learning/Risk-DS/Python Class/PythonEssentials/MatplotlibIntro")


# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    
    A= np.random.normal(loc=0, scale=1, size=(n,n))
    row_mean= A.mean(axis=1)
    var_mean= np.var(row_mean)
    
    return var_mean
    raise NotImplementedError("Problem 1 Incomplete")
    
var_of_means(4)


def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    
    x= np.arange(100,1100,100)
    y= np.array([var_of_means(i) for i in x])
    
    return plt.plot(x,y)
    plt.show()
    
    raise NotImplementedError("Problem 1 Incomplete")

prob1()


# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    
    x= np.linspace(-2*np.pi,2*np.pi)
    
    return plt.plot(x,np.cos(x)), plt.plot(x,np.sin(x)), plt.plot(x,np.arctan(x))
    plt.show()
    
    raise NotImplementedError("Problem 2 Incomplete")
    
prob2()


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    
    #Continuous Graph
    x= np.linspace(-2,6)
    y= 1/(x-1)
    
    #Discontinuous Graph
    x1= np.linspace(-2,1,endpoint=False) #discontinuous at 1
    x2= np.linspace(6,1, endpoint=False) #flip to use endpoint option
    
    y1= 1/(x1-1)
    y2= 1/(x2-1)
    
    
    #return plt.plot(x,y,'m--')
    return plt.plot(x1,y1,'m--',linewidth=4), plt.plot(x2,y2,'m--',linewidth=4)
    plt.show()
    
    raise NotImplementedError("Problem 3 Incomplete")

prob3()

# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    
    x= np.linspace(0,2*np.pi)
    
    #Set limits for x and y axis
    plt.axis([0,2*np.pi,-2,2])
    
    #Overall Title
    plt.suptitle("Variations of sin(x)")
    
    ax1= plt.subplot(221)
    ax1.plot(x,np.sin(x),'g',lw=1)
    ax1.set_title('sin(x)')
    
    ax2= plt.subplot(222)
    ax2.plot(x,np.sin(2*x),'r--',lw=1)
    ax2.set_title('sin(2x)')    
    
    ax3= plt.subplot(223)
    ax3.plot(x,2*np.sin(x),'b--',lw=1)                    
    ax3.set_title('2sin(x)')   
    
    ax4= plt.subplot(224)
    ax4.plot(x,2*np.sin(2*x),'m:',lw=1)
    ax4.set_title('2sin(2x)')  
    
    return ax1,ax2,ax3,ax4
    plt.show()
    plt.tight_layout()
    raise NotImplementedError("Problem 4 Incomplete")

prob4()


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    
    fars= np.load('FARS.npy')
    x= fars[:,1]
    y= fars[:,2]
    z= fars[:,0]
    
    plt.suptitle("FARS Data")
    fars_sc= plt.subplot(211)
    fars_sc.plot(x,y,"k,",markersize=0.5)
    fars_sc.set_xlabel("Longitude")
    fars_sc.set_ylabel("Latitude")
    fars_sc.set_aspect("equal") 
    
    fars_hist = plt.subplot(212)
    fars_hist.hist(z,bins=np.arange(0,25,1))
    fars_hist.set_xlabel("Hours of the Day")
    
    plt.suptitle('Car Crash Incidents 2010-2014', fontsize=11)
    plt.subplots_adjust(hspace=0.6)
    
    return fars_sc, fars_hist
    plt.show()

    raise NotImplementedError("Problem 5 Incomplete")

prob5()


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.linspace(-2*np.pi, 2*np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X)*np.sin(Y))/(X*Y)
    
    # Plot the heat map of f
    sub1= plt.subplot(211,aspect='equal')
    plt.pcolormesh(X, Y, Z, cmap="Greens")
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    plt.colorbar()
    
    # Plot a contour map of f
    sub2= plt.subplot(212,aspect='equal')
    plt.contour(X, Y, Z, 20, cmap="Purples")
    plt.colorbar()
    
    plt.suptitle("sin(x)sin(y)/xy",fontsize=13)
    plt.subplots_adjust(hspace=0.4)
    plt.show()
    
    return sub1,sub2
    raise NotImplementedError("Problem 6 Incomplete")
    
prob6()
