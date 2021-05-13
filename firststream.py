# -*- coding: utf-8 -*-
"""FirstStream.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qJ3ByrC_uT74mGx1S_MY0-oTjTvjaJCN
"""
import pyqrcode
import streamlit as st

def generateQRcode(txt, color):
    url = pyqrcode.create(txt)
    url.png('QR-Code.png', scale = 28, module_color = (66, 245, 242))
    return url

st.title('My First StreamLit Project - Testing my Sugarboooooo')
st.write()
