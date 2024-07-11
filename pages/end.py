
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

col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.image("emoji/happy.png", width=205)

with col2:
    st.header("Thanks for participating!", divider="grey")
    st.subheader("Results coming up on the big screen...")
    st.code("Learn more about AI Prompt Injection: \n [-] https://youtu.be/fP6vRNkNEt0")
    st.code("Pace University Career Services: \n [-] https://careerservices.pace.edu/")
    st.code("Have a cool AI Project Idea? Drop a Message: \n [-] https://www.linkedin.com/in/ar33h/ ")

st.write("")
st.write("")

left, center, right = st.columns([0.42, 0.3, 0.3])
with center:
    portfolio= "http://arshdeepsingh.me"
    st.caption('built with :blue_heart: by [arsh](%s)' %portfolio)
