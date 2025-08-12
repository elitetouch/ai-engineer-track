#Application to check for word count  and convert to lower case and upper case with a click of a button using streamlit

import streamlit as st


st.title("WORD CHECKER")
# Ask the user to input a word.



txt = st.text_area(
    "Text to analyze",
    "",
)

st.write(f"You wrote {len(txt)} characters.")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")

