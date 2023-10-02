import streamlit as st
import tools as flexin

st.set_page_config(
    page_title="Sound Tube Converter",
    #page_icon="media\\favicon.ico",
    layout="centered",
    initial_sidebar_state="collapsed",
)

with st.form(key = "form", clear_on_submit=True):
    
    st.code("📹 transforming YouTube videos into wav format 🎵", language="python")
    
    url = st.text_input(label="url", key="url", label_visibility="collapsed",type="default", placeholder="🔗 url here")

    if st.form_submit_button(label="💾 download", type="secondary", use_container_width=True):

        st.progress(value=100, text="loading")

        st.code(f"▶️ {flexin.Video(url).title().title()}")

        col1, col2 = st.columns(2)

        with col1:

            st.image(image=flexin.Video(url).thumbnail(), use_column_width=True)

        with col2:

            st.code(f"🧑‍💻 {flexin.Video(url).author()}")

            st.code(f"📊 {flexin.Video(url).views()} | 📅 {flexin.Video(url).date()}")
            
            st.progress(value=100, text="download completed")

            done = flexin.Video(url).download()

            print(done)

baseboard = """
    <center>© 2023 flexin®️ - all rights reserved.</center>
"""

st.write(baseboard, unsafe_allow_html=True)