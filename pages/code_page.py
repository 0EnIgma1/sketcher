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

def info():
    print("To unlock full code, Become a Member of UV")
    print("Good luck")'''
st.code(code,language='python')