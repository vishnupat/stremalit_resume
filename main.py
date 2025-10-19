import streamlit as st

# --- PAGE CONFIGURATION ---
# This should be the first Streamlit command

st.markdown (
    """ <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* 2. APPLY THE FONT GLOBALLY */
        html, body, h1,h2,h3 {
        font-family: 'Montserrat', sans-serif;
    }
    </style>""", unsafe_allow_html=True
)

st.set_page_config(
    page_title="Vishnu Vardhan P",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# --- HIDE STREAMLIT STYLE ---
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            .stAppDeployButton {display: none;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- NAVIGATION BAR ---
pages = {
        "Analyze Me":[
            st.Page('summary.py',title='About Me', icon="👤"),
            st.Page('professional_summary.py', title ='Profession Summary', icon="📄"),
            st.Page('Work_History.py', title='Work History',icon="💼"),
            st.Page('software_and_tools.py',title ='Software and Tools', icon = "⚙️"),
            st.Page('Education.py', title = 'Education', icon="🎓")
            ] ,

        "Projects": [
            st.Page('Funda_pro.py',title='Funda Pro', icon="💡"),
            st.Page('Data_visualisation.py',title='Data Visualisation', icon="📊"),
            st.Page('AI_&_ML.py', title='AI & ML',icon="🤖")]
            
        }

# The 'position="sidebar"' puts the navigation controls in the sidebar,
# after the toggle we added above.
nav = st.navigation(pages, position='sidebar')
nav.run()