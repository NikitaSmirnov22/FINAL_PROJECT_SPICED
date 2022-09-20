
def app():
    import streamlit as st
    import pandas as pd
    from PIL import Image
    html = '<div class="header"><h1>iHelper ❤️‍🩹👵🏻👨🏼👩🏽‍🦱👶🏻👩🏻‍🦰🧑🏻‍🦰👴🏾</h1></div>'
    st.markdown(html, unsafe_allow_html=True)
    st.success('**The idea behind this project is to provide a customer with high-quality first-aid AI support.\niHelper is capable of dealing with problems of different levels of complexity for any kind of damage(physical or psychological harm) being delivered to an individual.**')
    image = Image.open('kit.jpg')
    st.image(image)
    