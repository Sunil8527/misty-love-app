import streamlit as st
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Set page config
st.set_page_config(page_title="Hey! Misty ❤️", page_icon="💌")

# Title
st.title("Hey! Misty, let's begin the story 💖")
st.markdown("Answer these with your heart...")

# Form for questions
with st.form("misty_form"):
    q1 = st.text_area("1. What was the first thought that came to your mind when you saw me?")
    q2 = st.text_area("2. What comes to your mind whenever you see me?")
    q3 = st.text_area("3. How long do you want to live with me?")
    q4 = st.text_area("4. What is the most beautiful thing in me?")
    q5 = st.text_area("5. Is there anything you want me to change?")
    q6 = st.text_area("6. What is the most beautiful thing you want to do with me?")

    submitted = st.form_submit_button("Submit 💌")

if submitted:
    # Prepare text for image
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answers = [
        f"1. {q1}",
        f"2. {q2}",
        f"3. {q3}",
        f"4. {q4}",
        f"5. {q5}",
        f"6. {q6}",
        f"\nSubmitted on: {timestamp}"
    ]
    full_text = "\n\n".join(answers)

    # Create image
    img = Image.new('RGB', (1000, 1400), color=(255, 240, 245))  # Light pink
    draw = ImageDraw.Draw(img)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", size=28)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(full_text, width=80)
    draw.text((50, 50), wrapped_text, fill=(0, 0, 0), font=font)

    # Save image
    os.makedirs("responses", exist_ok=True)
    filename = f"responses/misty_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpeg"
    img.save(filename)

    st.success("Your answers were saved beautifully as a love note 💕")
    st.image(filename, caption="Saved Response 💌", use_column_width=True)
