
import streamlit as st  
from dotenv import load_dotenv
from pathlib import Path  
from streamlit_extras.switch_page_button import switch_page

project_root = Path(__file__).resolve().parent
load_dotenv(project_root / ".env")

st.set_page_config(page_title="Arsh says Thanks!", page_icon="./favicons/end.png", initial_sidebar_state="collapsed")

st.markdown(
"""
<style>
    [data-testid="collapsedControl"] {
        display: none
    },
    #MainMenu {visibility: hidden;}
</style>
""",
    unsafe_allow_html=True,
)
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.image("emoji/happy.png", width=205)

with col2:
    st.header("You did it, "+st.session_state["name"]+"!", divider="grey")
    st.subheader("Thanks for participating. You can collect free swags from our table.")
    st.code("Pace University Career Services: \n [-] https://careerservices.pace.edu/")
    st.code("More on AI Prompt Injection: \n [-] https://youtu.be/fP6vRNkNEt0")
    

st.write("")
st.write("")

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)

left, center, right = st.columns([0.42, 0.4, 0.3])
with center:
    portfolio= "http://arshdeepsingh.me"
    st.write("#SeidenbergCommunityDay2024")
    st.caption('built with :blue_heart: by [arsh](%s)' %portfolio)
