#import libraries
import cv2
import matplotlib.pyplot as plt
import pyautogui as pg
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import webbrowser
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

win = Tk()

# Set the window size
win.title("sketcher")
win.geometry("1100x550")
style = ttk.Style()
style.theme_use('clam')
Label(win, text= "A project created by us to convert a normal image into a sketch..hope y'all liked it", font=('calibri 18 bold')).place(x=140,y=80)

#get image file from computer
def click_fun():
   # Create a Label Text
   #root = Tk()
   win.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("images",".jpg .png .jpeg"),("all files","*.*")))
   user_path = win.filename
   img = cv2.imread(user_path)
   #converting rgb image to grayscale
   grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   invert_img = cv2.bitwise_not(grey)


  #appliying gaussian blur 
   blur_img = cv2.GaussianBlur(invert_img,(111,111),0)
   inblur_img = cv2.bitwise_not(blur_img)
   sketch = cv2.divide(grey,inblur_img,scale = 255.0)

   img2 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

  #display the output
   while True:
       plt.figure(figsize=(14,8))
       plt.subplot(1,2,1)
       plt.title("original image",size = 18)
       plt.imshow(img2)
       plt.axis('off')
       plt.subplot(1,2,2)
       plt.title("sketch",size=18)
       rgb_sketch = cv2.cvtColor(sketch,cv2.COLOR_BGR2RGB)
       plt.imshow(rgb_sketch)
       plt.axis('off')
       ax = plt.show()
       st.pyplot(ax)
       break

   #message box
   res = pg.confirm('Do you want to download the sketch ?')
   if res == "OK":
       cv2.imwrite('sketch.png',sketch)
       print("Image downloaded successfully !")

# Create a Label widget
label = Label(win, text="Sketcher", font=('mistral', 22),fg = "red")
label.pack(pady=40)

# Create a Tkinter button
ttk.Button(win, text="choose file from computer", command=click_fun).pack()

def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
#link to Naveen's github account
link = Label(win, text="Naveen",font=('mistral', 20), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("https://github.com/0EnIgma1"))

#link to Arjun's github account
link = Label(win, text="Arjun",font=('mistral', 20), fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e:
callback("https://github.com/arjunprakash027"))

win.mainloop()


