import streamlit as st
import random

# Page config
def run():
    st.set_page_config(page_title="🌞 Daily Positivity Challenge", layout="centered")

    # Title
    st.title("🌞 Daily Positivity Challenge")

    # List of positive challenges
    challenges = [
        "Write 3 things you're grateful for.",
        "Take a 10-minute walk.",
        "Compliment yourself in the mirror.",
        "Drink a full glass of water.",
        "Write a kind message to a friend.",
        "Listen to your favorite happy song.",
        "Do a 1-minute breathing exercise.",
        "Write down one goal for today.",
        "Stretch for 2 minutes.",
        "Give yourself a smile 😊"
    ]

    # Show a random challenge
    challenge = random.choice(challenges)
    st.info(challenge)

    # Optional: Button to get a new challenge
    if st.button("🔄 New Challenge"):
        st.rerun()