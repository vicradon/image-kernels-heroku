import streamlit as st 
import cv2
import matplotlib.pyplot as plt
import numpy as np
from sympy import Matrix,Identity
import base64


#default page layout
st.set_page_config(
    page_title="Filter Demonstration",
    page_icon="🐍",
    layout="wide",
) 

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
   
add_bg_from_local('bg.jpg') 

st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

/* breakline for header color        */
div[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.00);
    background: rgb(255, 255, 255, 0);
}
/style>
"""
, unsafe_allow_html=True)
    
st.markdown("<h1 style='text-align: center;'>Image Kernels :</h1>", unsafe_allow_html=True)
st.markdown("***")

col1, col2, col3 = st.columns([0.5,1,1])

with col1:
    upload_img = st.file_uploader(label='Upload image : ')

if upload_img:
    
    with col1:
        select = st.selectbox(label='Select filter: ', 
                          options=['Default','blur image','Gray Scale','Sharpen Image','Sepia','Apply your own filter'])
        
        if select == 'blur image':
            filter_ = np.around([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]], 4)
            M = Matrix(filter_)
            st.write("The applied Image kernel:",M*Identity(3).as_explicit())
        if select == 'Gray Scale':
            st.markdown('To convert a colored image having RGB channels to grayscale ( $ I_g $) , the weighted formula below can be used; ')
            st.markdown('$ I_g = 0.2989 \\times I_R + 0.5870 \\times I_G + 0.1140 \\times I_B $')
        if select == 'Sharpen Image':
            filter_ = np.around([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], 4)
            M = Matrix(filter_)
            st.write("The applied Image kernel:",M*Identity(3).as_explicit())
        if select == 'Sepia':
            filter_ = np.around([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]], 4)
            M = Matrix(filter_)
            st.write("The applied Image kernel:",M*Identity(3).as_explicit())
        
        if select == 'Apply your own filter':
            input_ = st.text_input(label='Enter the values for your filter kernel row-wise:')
            if input_ != '':
                input_array = np.array(input_.split(','),dtype=float).reshape(3,3)
                I = Matrix(input_array)
                st.write("The applied Image kernel:",(I*Identity(3)).as_explicit())
                
        
    with col2:
        img = plt.imread(upload_img)
        st.image(img,use_column_width = True)
    with col3 :
        if select == 'Default':
            pass
        elif select == 'blur image':
            Blur_Effect_Img = cv2.GaussianBlur(img, (35, 35), 0)
            st.image(Blur_Effect_Img, use_column_width = True)
        elif select == 'Gray Scale':
            bw_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            st.image(bw_img, use_column_width = True)
        elif select == 'Sharpen Image':
            Sharpen_Kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            Sharpen_Effect_Img = cv2.filter2D(src=img, kernel=Sharpen_Kernel, ddepth=-1)
            st.image(Sharpen_Effect_Img, use_column_width = True,clamp=True)
        elif select == 'Sepia':
            sepia_Kernel = np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
            sepia_Effect_Img = cv2.filter2D(src=img, kernel=sepia_Kernel, ddepth=-1)
            st.image(sepia_Effect_Img, use_column_width = True,clamp=True)
        elif select == 'Apply your own filter':
            try:    
                custom_kernel = input_array
                custom_img = cv2.filter2D(src=img, kernel=custom_kernel, ddepth=-1)
                st.image(custom_img,use_column_width = True)
            except:
                pass
        st.markdown("built by : [Ejelonu Benedict](https://www.linkedin.com/in/benedict-ositadinma-ejelonu-367a6218a)")
