import streamlit as st

# Page configuration
def run():
    st.set_page_config(page_title="Virtual Hug", page_icon="🤗", layout="centered")

    # App title
    st.title("🤗 Virtual Hug Station")

    # Description
    st.write("Sometimes, all we need is a warm hug. 💙")
    st.write("Upload a video from your loved ones or receive a cozy virtual hug from us!")

    # File uploader for user video (optional)
    hug_video = st.file_uploader("Upload a video from your loved one (MP4 only)", type=["mp4"])

    # Display based on upload
    if hug_video:
        st.success("💖 Here's your personalized virtual hug:")
        st.video(hug_video)
    else:
        st.info("💖 No upload found. Here's a warm virtual hug from us:")
        st.image("virtual hug.gif", width=900)  # Make sure this file exists in the same folder
        st.markdown("**You're not alone. We're here with you.** 💙")