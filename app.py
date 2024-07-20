import streamlit as st
import requests
import shutil

st.set_page_config(
    page_title="Image Sphere",
    page_icon="icon.png",
    menu_items={
        "About":"Welcome to ImageSphere, your ultimate source for high-quality, random images across various captivating categories. Dive into our vast collection and find the perfect image to inspire your creativity."
    }
)

st.write("<h2 style='color:#E98C3A;'>Your Gateway to Stunning Random Images.</h2>",unsafe_allow_html=True)

category=st.radio(label="Choose a Category", options=["Nature","Wildlife","City","Technology","Food","Still Life","Abstract","Others"],)

btn=st.button("Generate")
if btn:
    if category=="Others":
        category=""
    elif(category=="Still Life"):
        category="still_life"
    try:
        api_url = 'https://api.api-ninjas.com/v1/randomimage?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6', 'Accept': 'image/jpg'}, stream=True)
        if response.status_code == requests.codes.ok:
            with open('img.jpg', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
        
        with open("img.jpg","rb+") as bin_data:
            st.download_button("Download Image",bin_data.read(),"imgsphere.jpg")
        st.image("img.jpg")
    except:
        st.error("Some Error Occured")