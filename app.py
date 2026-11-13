import streamlit as st

st.title("My Streamlit App")

st.write("Welcome to my Streamlit app!")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("This is the first column.")

with col2:
    st.header("Column 2")
    st.write("This is the second column.")  


st.button("Click me!")
st.text_input("Enter your name:")
st.slider("Select a value:", 0, 100, 50)
st.checkbox("Check me!")
st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.selectbox("Select an item:", ["Item 1", "Item 2", "Item 3"])
st.multiselect("Select multiple items:", ["Item A", "Item B", "Item C"])
st.text_area("Enter your message:")

