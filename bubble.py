import streamlit as st
import time

def run():
    st.title("🫧 Bubble Game – Release Your Emotions")

    # User inputs their emotion
    feeling = st.text_input("Type what you're feeling right now:")

    # List of negative and positive keywords
    negative_feelings = ["sad", "depression", "angry", "lonely", "anxious", "tired", "upset", "worthless"]
    positive_feelings = ["happy", "excited", "joy", "peace", "grateful", "hopeful", "motivated"]

    if feeling:
        st.write("Analyzing your emotion...")

        if any(word in feeling.lower() for word in negative_feelings):
            st.warning("We sense you're carrying something heavy 💔")

            # Bubble image (you can replace this with a local file or a URL image)
            st.image("https://i.imgur.com/t9NwN6P.png", caption="This is your emotion bubble. Pop it to feel better!", width=300)

            if st.button("🫧 Pop the Bubble"):
                with st.spinner("Draining your emotions..."):
                    time.sleep(2)
                st.success("Your emotional bubble is popped! Breathe in... and out... You're doing great 💖")
                st.balloons()

        elif any(word in feeling.lower() for word in positive_feelings):
            st.success("That's beautiful to hear! Keep shining 🌟")
            st.image("https://i.imgur.com/rX1cZxK.png", caption="Positive vibes bubble!", width=300)
            st.snow()

        else:
            st.info("That's a unique feeling! Let's pop a custom bubble for it.")
            if st.button("🫧 Pop Custom Bubble"):
                st.success("Sending you comfort and strength 🌈")
                st.image("https://i.imgur.com/NmN5M1I.png", caption="Peaceful release bubble", width=300)
