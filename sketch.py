#import libraries
import cv2
import matplotlib.pyplot as plt
import pyautogui as pg

#reading image
user_path = input("Enter the image path :")
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
    plt.show()
    break

#message box
res = pg.confirm('Do you want to download the sketch ?')
if res == "OK":
    cv2.imwrite('sketch.png',sketch)
    print("Image downloaded successfully !")