import streamlit as st


st.title("KUDA BANK Application")


balance = 1000

# Show options
st.write("### Options:")
option = st.selectbox("Please choose an option:", 
                      ["Select an option", "1. Check Balance", "2. Buy Airtime", "3. Pay Bill", "4. Exit"])

if option == "1. Check Balance":
    st.write("Checking balance...")
    st.success(f"Your balance is N{balance}")

elif option == "2. Buy Airtime":
    airtime = st.number_input("Enter the amount of airtime to buy:", min_value=0, step=100)
    if st.button("Buy Airtime"):
        st.success(f"You are buying airtime worth N{airtime}")
        st.info(f"Your new balance is N{balance + airtime}")

elif option == "3. Pay Bill":
    bill = st.number_input("Enter the amount to pay:", min_value=0, step=100)
    if st.button("Pay Bill"):
        st.success(f"You are paying a bill of N{bill}")
        st.info(f"Your remaining balance is N{balance - bill}")

elif option == "4. Exit":
    st.write("Thank you for using the USSD application. Goodbye!")
