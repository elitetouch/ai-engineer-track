#Application to check for word count  and convert to lower case and upper case with a click of a button using streamlit

import streamlit as st


st.title("WORD CHECKER")
# Ask the user to input a word.

check = st.radio(
  
    ["***Character Count***", "***Word Count***"],
    captions=[
        "Count the number of characters in the text.",
        "Count the number of words in the text.",
    ],
)



txt = st.text_area(
    "Text to analyze",
    "",
)



st.write(f"You wrote {len(txt)} characters.")

txt = st.text_area(
    "Text to analyze",
    "",
)

st.write(f"You wrote {len(txt)} characters.")

operation = st.radio(
    "Select An operation to be done on the text",
    ["***All Uppercase***","***All Lowercase***","***Title Case***","***Reverse Text***","***Word Search***"],
    captions=[
        "Convert the text to all uppercase letters.",
        "Convert the text to all lowercase letters.",
        "Convert the text to title case.",
        "Reverse the text.",
        "Search for a word in the text.",
    ],
)

