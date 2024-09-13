import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import random
import time
import requests
import streamlit.components.v1 as components

st.set_page_config(page_title="Registration | HackLLM", page_icon="./favicons/app.png", initial_sidebar_state="collapsed")

st.header('HackLLM | Career Services, Pace University', divider="grey")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.write("Outsmart the AI chatbot by creating clever prompts and make it uncover each level's password. The bot will level up each time you succeed. Think you can defeat it? Let's find out.")

col1, col2 = st.columns([0.7, 0.3])
with col1:
    with st.form("register_form", clear_on_submit=False):
        st.write("Register now & start hacking!")
        first_name = st.text_input('First Name: ')
        st.session_state["name"] = first_name
        last_name = st.text_input('Last Name: ')
        email = st.text_input('Email', '@pace.edu')
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            if (first_name=="") or (last_name=="") or (email==""):
                st.warning("You need to fill all fields!")
            else:
                
                gformRegis = "https://docs.google.com/forms/d/e/1FAIpQLSfRWYmlQU55Vycf78aFYmCRhThtr70jOodcFAohlyBVtTvlAg/formResponse?&submit=Submit?usp=pp_url&entry.1526997065="+first_name+"&entry.1479648773="+last_name+"&entry.1469978627="+email
                
                registerPost = requests.post(gformRegis)
                if (registerPost.status_code == 200):
                    st.toast("Loading Challenge...", icon="✅")
                    time.sleep(3)
                    switch_page("level1")
                else:
                    st.toast("Server Error...", icon="❓")

with col2:
    st.image("emoji/point.png", width=205)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)

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



#-------------------Caching Passwords----------------------
#List of 173 passwords

# Novice
# Learner
# Apprentice
# Competent
# Champion
# Expert
# Master
# Legendary
# Divine
# Ubermensch

passwords = [
    "Scarlet", "Stellar", "Whiskers", "Lagoon", "Harmony", "Thunder", "Willow",
    "Blossom", "Saffron", "Velvet", "Serene", "Twilight", "Mosaic", "Breeze",
    "Pebbles", "Jade", "Radiant", "Glimmer", "Flamingo", "Nimbus", "Marigold",
    "Wander", "Aurora", "Luminary", "Misty", "Tropic", "Ember", "Enigma",
    "Zephyr", "Poppies", "Mirage", "Tundra", "Quasar", "Aquatic", "Zinnia",
    "Symphony", "Glitter", "Bliss", "Whisper", "Coral", "Opal", "Cascade",
    "Gossamer", "Azure", "Jubilee", "Reverie", "Solace", "Elysian", "Puzzle",
    "Lemon", "Helmet", "Breeze", "Ticket", "Turtle", "Wallet", "Orange",
    "Bakery", "Circus", "Hammer", "Juggle", "Zipper", "Muffin", "Cherry",
    "Planet", "Rocket", "Father", "Camera", "Castle", "Ginger", "Basket",
    "Forest", "Dolphin", "Friend", "Guitar", "Icebox", "Jaguar", "Lizard",
    "Mosaic", "Needle", "Outlet", "Pirate", "Rabbit", "Singer", "Travel",
    "Walnut", "Window", "Yellow", "Anchor", "Bumble", "Candle", "Dancer",
    "Fabric", "Goblet", "Hammer", "Insect", "Jacket", "Kitchen", "Locket",
    "Marvel", "Nimble", "Oyster", "Parrot", "Quiver", "Racket", "Saddle",
    "Thumbs", "Umbrella", "Velvet", "Waffle", "Zenith", "Banana", "Basket",
    "Circle", "Doctor", "Engine", "Farmer", "Guitar", "Hiccup", "Insect",
    "Jigsaw", "Kettle", "Ladder", "Market", "Noodle", "Pancake", "Rabbit",
    "Snakes", "Tomato", "Unicorn", "Violet", "Window", "Yacht", "Zebra",
    "Breeze", "Carpet", "Dancer", "Empire", "Feather", "Grapes", "Helmet",
    "Inning", "Jacket", "Kitten", "Lizard", "Mantis", "Number", "Outlet",
    "Parrot", "Quiver", "Ransom", "Saddle", "Tangle", "Uptake", "Vortex",
    "Wrench", "Yellow", "Zodiac", "Bangle", "Candle", "Dimple", "Eagle",
    "Frugal", "Garden", "Hobbit", "Icicle", "Jungle", "Kettle", "Lively",
    "Master", "Nectar", "Onyx", "Pirate", "Quiver"
]

@st.cache_data
def randPass():
    selectedPasswords = (random.sample(passwords, 4))
    return selectedPasswords

st.session_state["keys"] = randPass()

