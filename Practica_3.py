from tkinter import Button
from mlp import MLP
from entry import Entry
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton, MouseEvent
data=[]
fig, ax = plt.subplots()
plt.xlim([-5,5])
plt.ylim([-5,5])

def onclick(event):
    if event.inaxes != ax:
        return
    if event.button is MouseButton.LEFT:
        #identificar como dar sobles click
        if event.xdata ==None or event.ydata ==None:
            return
        else:
            data.append(Entry(event.xdata,event.ydata,0))
            ax.scatter(x=event.xdata,y=event.ydata,color='tab:cyan')
            plt.draw()
    elif event.button is MouseButton.RIGHT:
        if event.xdata ==None or event.ydata ==None:
            return
        data.append(Entry(event.xdata,event.ydata,1))
        ax.scatter(x=event.xdata,y=event.ydata,color='tab:pink')
        plt.draw()
    # if event.button is MouseButton.LEFT:
    #     print("Here")
    #     if event.xdata ==None or event.ydata ==None:
    #         return
    #     data.append(Entry(event.xdata,event.ydata,2))
    #     ax.scatter(x=event.xdata,y=event.ydata,color='tab:yellow')
    #     plt.draw()

def run():
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()
    mlp_=MLP()


if __name__ =='__main__':
    run()