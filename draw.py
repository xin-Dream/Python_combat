import numpy as np
import matplotlib.pyplot as plt

def draw1():
    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)
    width = 0.35
    p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

    plt.ylabel('Scores')
    plt.title('Scores by group and gender')
    plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Men', 'Women'))
    plt.show()

def drawsin():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    z = np.cos(x ** 2)
    
    plt.plot(x, y, 'r-',label="$sinx$", linewidth=2)
    plt.plot(x, z, 'b--',label="$cosx$")
    
    plt.xlabel("Times")
    plt.ylabel("Volt")
    plt.legend()
    plt.show()
    
    

if __name__ == "__main__":
    drawsin()