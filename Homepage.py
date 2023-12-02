import streamlit as st

st.set_page_config(
    page_title="My Music Webpage",
    page_icon=":musical_notes:",
    layout="wide",
)

st.title("Introduction")
st.sidebar.success("Select a page above.")

with st.container():
    st.header("Hi I am Sheldone R. Dacuya :wave:")
    st.subheader("A BSCpE Student In SURIGAO DEL NORTE STATE UNIVERSITY 🏫")


with st.container():
    st.markdown("<h1 style='text-align: right;'>Homepage</h1>", unsafe_allow_html=True)
    st.markdown("------")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            The lead guitarist is the sonic architect of a band, crafting expressive solos, contributing unique style, 
            and playing a pivotal role in defining the character and identity of the musical ensemble.

            If you want to learn how to become a lead guitarist in your band, kindly watch his tutorial
            """
        )
        st.write("[youtube tutorial >](https://youtu.be/UMaxzl18EyE?si=Xpydd-8ifpNAhAuS)")

 