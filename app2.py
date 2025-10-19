import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

# --- PAGE SETUP ---
st.set_page_config(page_title="Happy Birthday, Kayyycyy!", page_icon="🎂", layout="wide")
st.balloons()
# --- HELPER FUNCTIONS ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_json(path):
    import json
    with open(path, "r") as f:
        data = json.load(f)
    return data

# --- LOAD ANIMATIONS ---
lottie_confetti = load_json(r"animations\confetti.json")
lottie_dance = load_json(r"animations\dance.json")  # Add a dance/fun animation!
#lottie_party = load_json("party.json")  # Another animation if available

# --- HEADER ---
st.html("<h1><center><b>HAPPY BIRTHDAY, KAYYYCYY 🎂</b></center></h1>")
st.html("""<h3><center><b>
OR GC! OR Cocunut Barfi OR truth - just, Dayaan! Whatever you are HAPPY BIRTHDAY!</b></center></h3>
""")

with st.expander("Before you begin"):
    st.warning("IK ki kitna nerdy wish and all! BUTT I am in office with office laptop, with no creativity, no teammates (sab chuthi pe) and the thought ki kal tera bday hai so excuse me!!!")

# Fancy Confetti
cols = st.columns([1,1])
with cols[0]:
    st_lottie(lottie_confetti, height=180, key="confetti")
with cols[1]:
    st_lottie(lottie_dance, height=180, key="confetti1")

st.divider()

# --- YEARLY JOURNEY (Timeline) ---
st.header("🌈 What a Journey this year!")
st.markdown("""## ACL Recovery  | Exceling in design | Back to Dancing | New Relationship | New Job  
        - Bhaiii sahabb you crushed your 25..!
        """)
st.image(r"Data\kc.jpg", width=180)
with st.expander("# You really came from this ----> this ????"):
    cols = st.columns([1, 1])
    with cols[0]:
        st.image(r"Data\uthh jaa.jpeg", caption="[10 min aur, mai gir gayii, fighting over waking upss!]! 😴", width=500)
    with cols[1]:
        st.image(r"Data\utth gayi.png", caption="Waking up at your sleeping time ✨", width=500)
#st_lottie(lottie_dance, height=120, key="dance")
st.divider()

# --- BINGO ---
st.header("🎲 Kayycyy Bingo I miss!! (well not really 🙃 - maybe just 4th one)")
bingo_items = [ "DRAMA QUEEN moment", "Quote: 'Mai firse gir gayi every morning!'",
    "Coffee dilemma", "Quote Specially: Pizaa & Busss", "Bhai vo Red Flag updates !", "Quote: Galti teri hai (always 😢)!", "Reel Shoot karna hai!", "Quote: Bataaaaaaaa... nth time", "Quote: Gubgubit for random animals !?!"]
cols = st.columns(3)
for i, item in enumerate(bingo_items):
    with cols[i % 3]:
        st.text(item)
st.divider()
# --- POLAROID FAREWELL ---
st.header("🎊 To Another Beautiful Year Ahead 🎊")
st.markdown("""
You’ve crushed it so far and the new adventures are just beginning. \n
IK kaafi busy chal raha filhaal, different phases of Life I guess. \n
But yaar it's a long success journey and you're on the right path so **ENJOYYYY**!\n
Always be that `bohot sahii insaan` \n
Dont foget to **TAKE FREQUENT BREAKS**. \n
May your **coffee be strong**, your relationships even stronger!  \n
**Proud of you always** — till i forget: "WHO'S THIS?" 😉  \n
""")
st.image(r"Data\bye.png", width=320)

st.divider()

# --- Quiz ---
st.header("Birthday gift might be a little late you can keep guessing...!")
options = ["Potty karne waala poster !",
            "Thengaa because again 'WHO's THIS ??", 
            "Survival power for your stressfull day-week-life :(", 
            "God, just another ring!"]


user_ans = st.radio("", options)
if user_ans == options[2]:
    st_lottie(lottie_dance, height=100, key="party")
elif user_ans == options[0]:
    st.error("LOLOLOLOL SUREEEEE")
elif user_ans == options[1]:
    st.success("SAHI JAWAAAAB AAPKO MILTE HAI 10 crore (points bas)")
elif user_ans == options[3]:
    st.error("Sudhaar jaa madam! logo ko sachai pata chal jaayegi rings ki!")
else:
    pass
# --- TODO (Playful Reminder) ---
st.subheader("HAVE THE BEST DAY Ma'am and REMEMBER! 🎁")
reminders = [
    "Get that appointment ✅",
    "Call your new phsyio ☎️",
    "Keep the drama alive 🎭",
]
st.markdown("\n".join([f"- {r}" for r in reminders]))
st.image(r"Data\kick.png", width=220)
st.divider()

# --- CELEBRATION FOOTER ---
st.markdown("- param-mitra (HUH!) Idiot Insaan!")
st.text("Baloon waala bug nai fix karna - limited efforts 😂")

