import streamlit as st
from PIL import Image

icon = Image.open("UV_icon1.png")
st.set_page_config(
    page_title = "Code",
    page_icon = icon,
)

code = '''import matplotlib.pyplot as plt
import streamlit as st
import cv2
import pyautogui as pg
from PIL import Image
import numpy as np
from io import StringIO

icon = Image.open("UV_icon1.png")
st.set_page_config(
    page_title = "Sketcher",
    page_icon = icon,
)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Sketchers")
st.header("A program to convert any Image to a Pencil Sketch using Python")
st.markdown("**_A project under UV_**")

def fun():
    while True:
        plt.figure(figsize=(14,8))
        plt.subplot(1,2,1)
        plt.title("original image",size = 18)
        plt.imshow(image1)
        plt.axis('off')
        plt.subplot(1,2,2)
        plt.title("sketch",size=18)
        rgb_sketch = cv2.cvtColor(sketch,cv2.COLOR_BGR2RGB)
        plt.imshow(rgb_sketch)
        plt.axis('off')
        ax = plt.show()
        st.pyplot(ax)
        break

# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload your image below", type=['jpg', 'png'])

# Checking the Format of the page
if uploadFile is not None:
    
    im = Image.open(uploadFile)
    image1 = np.array(im)

    st.subheader("Original Image")
    st.image(image1)
    
    grey = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey)

    #appliying gaussian blur 
    blur_img = cv2.GaussianBlur(invert_img,(111,111),0)
    inblur_img = cv2.bitwise_not(blur_img)
    sketch = cv2.divide(grey,inblur_img,scale = 255.0)
    final_img = cv2.cvtColor(sketch,cv2.COLOR_BGR2RGB)

    st.snow()

    st.subheader("Sketched Image")
    st.image(final_img)
    
    st.subheader("Comparison")
    fun()

    st.success('Successfully Sketched the Image', icon = "✅")
    st.text("You can download the Image by clicking OK in the Confirm box")
    
    feedback = st.slider('Rate this Project', 0,5,1)
    st.write(f"I'm giving {feedback} star for this project !")

    st.text("Thank you for visiting this project..Hope it will be useful for you")

    res = pg.confirm('Do you want to download the sketch ?')
    if res == "OK":
       cv2.imwrite('sketch.png',sketch)
       print("Image downloaded successfully !")'''
st.code(code,language='python')