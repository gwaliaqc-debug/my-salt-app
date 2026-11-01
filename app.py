import streamlit as st

st.title("My Nani's Secret ®")
st.subheader("Proprietary Batch Formulation Portal")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    user = st.text_input("User ID")
    pas = st.text_input("Secret Password", type="password")
    if st.button("Authenticate Portal"):
        if user == "nani" and pas == "secret":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid ID or Password!")
else:
    st.success(" Login Successful! Welcome to Ayush Consultancy.")
    salt_type = salt_type = st.selectbox("Select Salt Type:", ["Nani Namak", "Buknu", "Sheetal Namak"])
    weight = st.number_input("Enter Total Weight (kg):", min_value=1.0, value=100.0)
    
    if salt_type == "Nani Namak":
        st.write(f"• सादा नमक: {weight * 0.45} kg")
        st.write(f"• सेंधा नमक: {weight * 0.25} kg")
        st.write(f"• जीरा: {weight * 0.05} kg")
    elif salt_type == "Buknu":
        st.write(f"• बेस साल्ट मिक्स: {weight * 0.50} kg")
        st.write(f"• हरड़ पाउडर: {weight * 0.15} kg")
        st.write(f"• नौशादर (FSSAI Safe): {weight * 0.005} kg")
    elif salt_type == "Sheetal Namak":
        st.write(f"• सेंधा नमक बेस: {weight * 0.50} kg")
        st.write(f"• पुदीना पाउडर: {weight * 0.12} kg")
