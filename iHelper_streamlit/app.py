import Main as Main
import Presentation as Presentation
import Application as Application
import streamlit as st

PAGES = {
    "MAIN": Main,
    "INFO": Presentation,
    "APPLICATION": Application
}
page_names = ["MAIN","INFO", "APPLICATION"]

selection = st.sidebar.radio("NAVIGATION", list(PAGES.keys()))
page = PAGES[selection]
page.app()

with st.sidebar.expander("CODE OF CONDUCT ⚠️"):
                st.write("""
            WE DO NOT WELCOME☝️\n- Hate: content that expresses, incites, or promotes hate based on identity.\n- Harassment: content that intends to harass, threaten, or bully an individual.\n - Violence: content that promotes or glorifies violence or celebrates the suffering or humiliation of others.\n - Self-harm: content that promotes, encourages, or depicts acts of self-harm, such as suicide, cutting, and eating disorders.\n - Sexual: content meant to arouse sexual excitement, such as the description of sexual activity, or that promotes sexual services (excluding sex education and wellness).\n - Political: content attempting to influence the political process or to be used for campaigning purposes.\n - Spam: unsolicited bulk content.\n - Deception: content that is false or misleading, such as attempting to defraud individuals or spread disinformation.\n - Malware: content that attempts to generate ransomware, keyloggers, viruses, or other software intended to impose some level of harm.
            """)


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)








        


