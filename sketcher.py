import matplotlib.pyplot as plt
import streamlit as st
import cv2
from PIL import Image
import numpy as np
from io import StringIO

icon = Image.open("UV_icon1.png")
st.set_page_config(
    page_title = "Sketcher",
    page_icon = icon,
    layout = "centered"
)
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Sketcher")
st.header("A program to convert any Image to various Sketchs and filters using Python")
st.markdown("**_A project under UV_**")

def fun(image1,image2):
    while True:
        plt.figure(figsize=(14,8))
        plt.subplot(1,2,1)
        plt.title("original image",size = 18)
        plt.imshow(image1)
        plt.axis('off')
        plt.subplot(1,2,2)
        plt.title("sketch",size=18)
        image2 = cv2.cvtColor(image2,cv2.COLOR_BGR2RGB)
        plt.imshow(image2)
        plt.axis('off')
        ax = plt.show()
        st.pyplot(ax)
        break

def gray(image):
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray_img

#def oil_paint(image):
    #oil_img = cv2.xphoto.oilPainting(image,7,1)
    #return oil_img

def watercol(image):
    water_img = cv2.stylization(image,sigma_s = 60, sigma_r = 0.3)#0.2 or 0.3
    return water_img

def negative(image):
    neg_img = 255 - image
    return neg_img

def sketch(image):
    grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(grey)
    #appliying gaussian blur 
    blur_img = cv2.GaussianBlur(invert_img,(111,111),0)
    inblur_img = cv2.bitwise_not(blur_img)
    sketch = cv2.divide(grey,inblur_img,scale = 255.0)
    final_img = cv2.cvtColor(sketch,cv2.COLOR_BGR2RGB)
    return final_img

def sobel_edge(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(img_gray,(3,3), 0)
    sobelx = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
    return sobelxy

def canny_edge(image,threshold1, threshold2):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(img_gray,(3,3), 0, 0)
    edges = cv2.Canny(image=blur_img, threshold1=threshold1, threshold2=threshold2)
    return edges

def cartoon(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
    k = 7
    data = np.float32(image).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(image.shape)
    return result

# Uploading the File to the Page
uploadFile = st.file_uploader(label="Upload your image below", type=['jpg', 'png'])

option = st.selectbox('Sketch the image into :',('Pencil sketch','Gray','Watercolor','Negative','Canny Edge','Cartoon'))
# Checking the Format of the page
if uploadFile is not None:
    im = Image.open(uploadFile)
    image1 = np.array(im)
    st.subheader("Original Image")
    st.image(image1)
    st.subheader("Converted Image")

    if option == 'Gray':
        out_img = gray(image1)
    elif option == 'Pencil sketch':
        out_img = sketch(image1)
    elif option == 'Oil Painting':
        out_img = oil_paint(image1)
    elif option == 'Watercolor':
        out_img = watercol(image1)
    elif option == 'Negative':
        out_img = negative(image1) 
    elif option == 'Cartoon':
        out_img = cartoon(image1)   
    elif option == 'Canny Edge':
        values = st.slider("Select the Range of Thresholds",0,255,(25,75))
        st.text(values)
        threshold1, threshold2 = values
        out_img = canny_edge(image1, threshold1, threshold2)
 
    st.image(out_img)

    st.subheader("Comparison")
    fun(image1,out_img)

    st.text("")

    st.success('Successfully Sketched the Image', icon = "✅")
    #st.text("You can download the Image by clicking OK in the Confirm box")
    st.text("")
    st.text("")
    feedback = st.slider('Rate this Project', 0,5,1)
    st.write(f"I'm giving {feedback} star for this project !")

    st.text("Thank you for visiting this project..Hope it will be useful for you")

    for j in range(0,4):
        st.text("")
    st.subheader("Wanna join / become MEMBER of our society UV...")
    st.write("Follow the LINK [UV](https://theuvofearth.wixsite.com/stage1)")
    
    for i in range(0,5):
        st.text("")
    st.write("[GitHub](https://github.com/0EnIgma1) <> [LinkedIn](https://www.linkedin.com/in/naveen-kumar-s-921990210/)")

    #res = pg.confirm('Do you want to download the sketch ?')
    #if res == "OK":
       #cv2.imwrite('sketch.png',sketch)
       #print("Image downloaded successfully !")

    
        



   
