import streamlit as st
#task one
# get user full name
# get user phone number
# get user email address
# get user university
# get user favorite Nigerian food
# get user image
# set the default session state to false
# when the user submits the form, set the session state to true
# then redirect to a new success page displaying the information

# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Page 1: Form
if not st.session_state.submitted:
    st.title("Register Student Form")

    full_name = st.text_input("Enter your full name:")
    phone_number = st.text_input("Enter your phone number:")
    email_address = st.text_input("Enter your email address:")
    university = st.text_input("Enter your university:")
    favorite_food = st.text_input("Enter your favorite Nigerian food:")
    user_image = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

    if st.button("Submit"):
        if not full_name or not phone_number or not email_address or not university or not favorite_food or not user_image:
            st.error("Please fill in all fields.")
        else:
            st.session_state.submitted = True
            st.session_state.data = {
                "name": full_name,
                "phone": phone_number,
                "email": email_address,
                "university": university,
                "food": favorite_food,
                "image": user_image
            }
            st.rerun()  # Refresh the app to show next "page"

# Page 2: Success Page
else:

    # Show success message
    st.success("Form submitted successfully!")
    st.markdown("<h2 style='text-align: center;'>Submitted Information</h2>", unsafe_allow_html=True)

    data = st.session_state.data

    if data["image"] is not None:
        from PIL import Image
        from PIL import ImageDraw

        
        # Load the image
        image = Image.open(data["image"])

        # Resize image to smaller dimensions (e.g., 150x150)
        image = image.resize((150, 150))

        # Create a circular mask
        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)

        # Apply the mask to make the image circular
        circular_image = Image.new("RGBA", image.size)
        circular_image.paste(image, (0, 0), mask=mask)

        # Display the image
        st.image(circular_image, caption="Profile Photo", use_container_width=False)
        

    st.write(f"**Full Name:** {data['name']}")
    st.write(f"**Phone Number:** {data['phone']}")
    st.write(f"**Email Address:** {data['email']}")
    st.write(f"**University:** {data['university']}")
    st.write(f"**Favorite Food:** {data['food']}")

    

    if st.button("Go back to form"):
        st.session_state.submitted = False
        st.rerun()
