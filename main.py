import streamlit as st
from datetime import date
from PIL import Image

# Title and banner
st.set_page_config(page_title="Eid-ul-Adha Mubarak!", layout="centered")
st.title("🌙 Eid-ul-Adha Mubarak!")
st.markdown("## 🤲 May Allah bless you with peace and happiness.")

# Show Eid image
st.markdown("### 🕌 Eid Celebration")
img = Image.open("eid_mubarak2.jpg")
resized_img = img.resize((400, 300))  # (width, height)
st.image(resized_img, caption="Eid-Ul-Adha Mubarak!")

# Date
today = date.today()
st.markdown(f"**📅 Today's Date:** {today.strftime('%A, %d %B %Y')}")

# Fun interaction
st.markdown("### 🐐 Sacrifice Reminder")
if st.button("Click to Sacrifice (Virtually!)"):
    st.success("🐐 Baaa! Qurbani Accepted! May your sacrifices be rewarded.")
    st.balloons()

# Add user message
user_message = st.text_input("💬 Send a message to your friends and family:")
if user_message:
    st.markdown(f"✉️ **Your Eid Message:** _{user_message}_")

# Footer
st.markdown("---")
st.markdown("🎉 Made with ❤️ using Streamlit | Designed by Muhammad Maaz")


