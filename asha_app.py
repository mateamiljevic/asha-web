import streamlit as st
from PIL import Image
import base64


st.set_page_config(layout="wide")


##HEADING
image = Image.open('data/ASHAFMLOGO2.png')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(image)

with col3:
    st.write(' ')

st.write("  ")

##ASHA FM COUNTDOWN
video_file = open('data/COUNTDOWN.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



st.write("  ")


##DESCRIPTION/BACKGROUND FORMAT
st.markdown("""
<style>
body {
    background-color: #f2f2f2;
}
.mid-font {
    font-size:13px;
    font-weight: thin;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:35px;
    font-weight: bold;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

##DESCRIPTION/BACKGROUND TEXT
col1, col2, col3 = st.columns(3)
with col1:
    image = Image.open('data/WHATISASHA.png')
    st.image(image)
    st.write("  ")
    image = Image.open('data/desc1.png')
    st.image(image)
    st.write("  ")
    image = Image.open('data/THESOUND.png')
    st.image(image)
    st.write("  ")
    image = Image.open('data/desc2.png')
    st.image(image)


with col2:
    image = Image.open('data/PLATFORM.png')
    st.image(image)
    st.write("  ")
    image = Image.open('data/desc3.png')
    st.image(image)

with col3:
    image = Image.open('data/CIRCLE.png')
    st.image(image)
    st.write("  ")
    image = Image.open('data/desc4.png')
    st.image(image)


st.write("  ")
st.write("  ")

col1, col2, col3 = st.columns(3)
with col1:
    st.write("  ")

with col2:
    image = Image.open('data/desc5.png')
    st.image(image)
    st.markdown('<a href="mailto:info@asha.fm"><p class="mid-font">C O N T A C T </p></a>', unsafe_allow_html=True)

with col3:
   st.write("  ")
