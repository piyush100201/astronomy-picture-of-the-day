import requests
import streamlit as st


url = "https://api.nasa.gov/planetary/apod?api_key=raoAKLgpxW45PtjV0iJMV5jutgY7XueRHqxee2Ec"
response1 = requests.get(url)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "image.png"

response2 = requests.get(image_url)
with open(image_filepath,"wb") as file:
     file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)



