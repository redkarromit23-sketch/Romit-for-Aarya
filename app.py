import streamlit as st
import time

# Page Config
st.set_page_config(page_title="A Message for You", page_icon="✨")

# --- Header Section ---
st.title("To Aarya,")
st.subheader("I wrote some code because words alone weren't enough.")

# --- The "Effort" Visual ---
# This shows a progress bar to simulate the 'loading' of your memories
progress_text = "Scanning my favorite memories..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
st.success("Memories Loaded.")

# --- Interactive Content ---
tab1, tab2, tab3 = st.tabs(["Our Timeline", "The Small Things", "A Final Word"])

with tab1:
    st.write("### How we grew...")
    # You can list dates or specific milestones here
    st.info("2021: The day we first met at Sandip sir's tuition.")
    st.info("2022: The year which I will cherish throughout my whole life.")

with tab2:
    st.write("### Why I still care")
    st.write("It’s not just the big moments. It’s:")
    st.write("- The way you used to look into my eyes.")
    st.write("- Those quiet moments when we were just together.")
    st.write("- How you always knew what I was thinking.")
    st.write("- तुझ्यासाठी मी अजूनही ते jhumke's सांभाळून ठेवले आहे, जे मी तुला दाखवलेले, मला ते तुला द्यायचे आहे आणि ते मी तुलाच देईन.")

with tab3:
    st.write("### The Truth")
    if st.button('Click to reveal'):
        st.balloons() # This creates a cool animation on screen
        st.markdown("#### I'm still in love with you, आणि मी तुझ्यावर जीवापाड प्रेम करतो!.")
        st.write("I've spent a lot of time thinking about us. I built this to show you that I'm willing to put in the work to show you how much you mean to me.\n I hope this makes you smile, even just a little bit. I care about you more than words can say. - Romit")

        import streamlit as st

# Setup
st.set_page_config(page_title="For You", page_icon="❤️")

# Secret Access (Only she knows the date)
auth = st.text_input("Enter our relationship date (DDMMYYYY) to unlock:", type="password")

if auth == "12052023": # <--- CHANGE THIS to your actual date
    st.balloons()
    st.title("Hi Aarya,")
    st.write("I built this from scratch because I wanted to show you I'm still all in.")
    
    # Emotional Hook
    st.header("The moments I keep thinking about...")
    st.info("That time we stayed up until 4 AM just talking.")
    st.info("The way you look when you're actually focused on a book.")

    # The Response Form
    st.divider()
    st.subheader("Send a message back to me?")
    with st.form("response_form"):
        msg = st.text_area("What's on your mind?")
        submitted = st.form_submit_button("Send to Romit")
        if submitted:
            st.success("Message received. I'm listening.")
            # Note: For a real email to land in your inbox, we'd use 'Formsubmit.co' 
            # but for now, this shows her you care about her reaction.

else:
    st.warning("Waiting for the right key...")