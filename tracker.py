import tkinter as tk
from tkinter import font
import pyautogui as pag
import keyboard


class MousePos_Trac:
    xOffest = -60
    yOffset = +30
    tk_width = 120
    tk_height = 30
    
    def __init__(self):
        self.root = tk.Tk()

        self.sc_width = self.root.winfo_screenwidth()#Return the number of pixels of the width of the screen of this widget in pixel.
        self.sc_heigth = self.root.winfo_screenheight()#Return the number of pixels of the height of the screen of this widget in pixel.

        self.tk_width = MousePos_Trac.tk_width
        self.tk_height = MousePos_Trac.tk_height

        self.xOffest = MousePos_Trac.xOffest
        self.yOffset = MousePos_Trac.yOffset


        self.text = tk.Label(self.root)
        self.text.pack()

        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.3)
        self.root.overrideredirect(True)

        self.FollowMouse()

        self.root.mainloop()

    def FollowMouse(self):
        mouseX, mouseY = pag.position()

        _mouseX = max(0, min(mouseX+self.xOffest, self.sc_width-self.tk_width))#Clamping the tkinter window x-dimension
        _mouseY = min(mouseY+self.yOffset, self.sc_heigth-self.tk_height)#Clamping the tkinter window y-dimension

        self.root.geometry(f"{self.tk_width}x{self.tk_height}+{_mouseX}+{_mouseY}")
        self.text.pack()
        self.text.config(text=f"{mouseX}, {mouseY}", font = font.Font(family="Consolas", weight='bold'))

        if keyboard.is_pressed('q'):
            self.root.destroy()
        
        self.root.after(10, self.FollowMouse)


def main():
    trac = MousePos_Trac()


if __name__ == '__main__':
    main()