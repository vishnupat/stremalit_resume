import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Vishnu Vadhan P | Data Analyst",
    page_icon=":bar_chart:",
    layout="wide"
)

# --- STYLES ---
st.markdown("""
    <style>
    /* Styles the IMAGE itself */
    div[data-testid="stImage"] img {
        border-radius: 50%;
        max-height: 250px;
        display: block;
        margin-left: 33.332%;
        margin-right: 33.332%;
    }

    /* Center the title (h1) */
    h1 {
        text-align: center;
    }

    /* Center and style the subtitle (h3) */
    h3 {
        text-align: center;
        color: #777;
    }

    /* Center 'About Me' header (h2) */
    h2 {
        text-align: center;
    }

   .icon-button {
            display: inline-block;
            margin: 20px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #f0f0f0;
            text-align: center;
            line-height: 60px;
            transition: background-color 0.3s ease;
            box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
        }

        .icon-button:hover {
            background-color: #e0e0e0;
        }

        .icon-button i {
            font-size: 28px;
            color: #333;
        }

        .icon-container {
            text-align: center;
            margin-top: 30px;
        }



    </style>
    """, unsafe_allow_html=True)

prof_image =Image.open("assets/profile.jpg")

# --- HERO SECTION ---
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    # IMPORTANT: This file must be in the SAME folder as your script.
    st.image(prof_image)
    st.title('Vishnu Vadhan P')
    st.subheader('Results-Oriented Data Analyst')

st.write("---") # Adds a horizontal divider

# --- ABOUT ME ---
st.subheader("About Me")

st.write("""
A results-oriented Data Analyst with over 4.5 years of experience specializing in financial analysis, data visualization, and process automation. Proficient in transforming complex data into actionable strategies using a robust technical skillset including SQL, Python (leveraging libraries such as Pandas, NumPy, Matplotlib, and Seaborn), Power BI, and Advanced Excel. Experienced in version control with Git and GitHub. Possesses significant experience across diverse sectors including Technology, Media, and Telecom (TMT), manufacturing, retail, and healthcare.

Key competencies include developing comprehensive MIS solutions, creating robust financial models, forecasting, and establishing KPI frameworks. Proven ability to drive efficiency, demonstrated by successfully automating data ingestion and transformation processes to cut project durations by over 55%. Holds an MBA in Finance and in recognized for creative problem-solving and a collaborative work ethic.
""")

st.write("---") # Adds a horizontal divider


st.markdown("<h4 style='text-align: center;'>Connect with Me</h4>", unsafe_allow_html=True)

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
""", unsafe_allow_html=True)

st.markdown("""
<div class="icon-container">
    <a href="https://www.linkedin.com/in/vishnuvardhanpatnana" target="_blank" class="icon-button">
        <i class="fab fa-linkedin-in"></i>
    </a>
    <a href="https://github.com/your-username" target="_blank" class="icon-button">
        <i class="fab fa-github"></i>
    </a>
</div>
""", unsafe_allow_html=True)
