import streamlit as st

# Initialize page state
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Sidebar navigation
st.sidebar.title("Mental Health Support")
menu = st.sidebar.radio("Navigate", ["Home", "Chatbot", "Motivational Story", "Talk with Character", "Virtual Hugs", "Positivity Challenge", "Bubble Game"])
if menu != "Home":
    st.session_state['page'] = menu

# --- Load correct module ---
if st.session_state['page'] == 'home':
    st.title("Mental Health Dashboard 💖")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💬 Chatbot"):
            st.session_state['page'] = "Chatbot"
        if st.button("🧸 Virtual Hugs"):
            st.session_state['page'] = "Virtual Hugs"
    
    with col2:
        if st.button("📖 Motivational Story"):
            st.session_state['page'] = "Motivational Story"
        if st.button("🎉 Positivity Challenge"):
            st.session_state['page'] = "Positivity Challenge"
    
    with col3:
        if st.button("🎭 Talk with Character"):
            st.session_state['page'] = "Talk with Character"
        if st.button("🫧 Bubble Game"):
            st.session_state['page'] = "Bubble Game"

# --- Import modules like anchor behavior ---
if st.session_state['page'] == "Chatbot":
    import chatbot as page
    page.run()

elif st.session_state['page'] == "Motivational Story":
    import story as page
    page.run()

elif st.session_state['page'] == "Talk with Character":
    import character as page
    page.run()

elif st.session_state['page'] == "Virtual Hugs":
    import hug as page
    page.run()

elif st.session_state['page'] == "Positivity Challenge":
    import challenge as page
    page.run()

elif st.session_state['page'] == "Bubble Game":
    import bubble as page
    page.run()
