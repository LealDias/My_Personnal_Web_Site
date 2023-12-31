
import streamlit as st
import requests
from PIL import Image
import json

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# Local CSS

def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_json = "https://lottie.host/65854a92-9354-4343-968a-9988621275bf/AcDiAs4hj5.json"

image_contact_form = Image.open("images/GitProfile.PNG")
image_kaggle = Image.open("images/KaggleProfile.PNG")


# --------- HEADER SECTION ---------- #

with st.container():
    
    text_column , image_column = st.columns((5.5, 3))

    with text_column:
      st.subheader("Hi, My name is Diego :wave:")
      st.title("A Data Analyst and Developer from Brazil")
      st.write("I'm a technology worker looking foward to help companies increase their efficiency and power by using powerfull technologies🚀")
      st.write("As a professional, I work with integrity and quality, always looking foward to client's satisfaction, and through innovation I believe we can solve problems and improve people's life🏅")
      st.write("One curiosity about me is that a love custom motorcycles, and even better, I love riding custom motorcycles🏍️! LoL")
      st.write("Check out my linkedin profile, so you can see my projects and experience as well! Feel free to get in touch from there! You're more than welcome!👋🇼‌🇪‌🇱‌🇨‌🇴‌🇲‌🇪‌🙋")
      st.write("[Linkedin Profile >](https://github.com/LealDias)")

    with image_column:
      image_html = f'<img src="https://media.licdn.com/dms/image/D4D03AQFhhrGQkdgbAA/profile-displayphoto-shrink_400_400/0/1696733482141?e=1703116800&v=beta&t=AMfuO3ZXOe0Y7DAvjAcE2pZHDcAHRWaZzHvS8dzGFII" alt="Image" style="border-radius: 100%; width: 400px; height: 400px; float: center; position: sticky; top: 0; right:50">'
      st.markdown(image_html, unsafe_allow_html=True)
      #st.image(image_html)

# ------- WHAT I DO ------- #

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
        """
        Dedicated Python Developer with a strong foundation in data analysis and data science. Computer Engineering graduate with a passion for technology and software engineering. Seeking opportunities to contribute technical expertise in a dynamic environment.

        - Proficient in Python programming with expertise in data analysis, data manipulation, and data visualization.
        - Skilled in creating data-driven solutions, utilizing libraries like NumPy, Pandas, and Matplotlib.
        - Experienced in collaborating with cross-functional teams to deliver impactful projects.
        - Adaptable problem-solver with a continuous learning mindset and a drive for excellence.

        Skills:
        -------
        - Programming Languages: Python (NumPy, Pandas, Matplotlib), SQL.
        - Data Analysis: Data Cleaning, Exploratory Data Analysis (EDA).
        - Machine Learning: Regression, Classification, Clustering.
        - Data Visualization: Matplotlib, Data Dashboarding.
        - Tools & Frameworks: Jupyter Notebook, Git, VS Code.

        """
        )

with right_column:
# Create a Lottie animation using lottie-web
  iframe_html = f'<iframe src="https://lottie.host/?file=65854a92-9354-4343-968a-9988621275bf/AcDiAs4hj5.json" title="Lottie Animation" frameborder="0" style="width:100%; height:500px;"></iframe>'
  st.write(iframe_html, unsafe_allow_html=True)

# ------- PROJECTS --------- #

with st.container():
  st.write("---")
  st.header("My Projects")
  st.write("##")
  image_column, text_column = st.columns((1, 2))

  with image_column:
    st.image(image_contact_form)

  with text_column:
    st.subheader("My GitHub Portfolios")
    st.write(

        """

        On my github page I have many projects from simple web pages to data analysis and data science models. See below the link that will redirect you to my profile. Be welcome!


    """)
    st.markdown("[Check it out...](https://github.com/LealDias)")


with st.container():
  st.write("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(image_kaggle)

  with text_column:
    st.subheader("My Kaggle Profile")
    st.write(

        """

        On my Kaggle's profile you'll see my achievements on data analyis and data science. I'm still bulding up and soon I'll have more to show!


    """)
    st.markdown("[See my Kaggle's link...](https://www.kaggle.com/diegoleal)")

# ------- CONTACTS --------- #

with st.container():
  st.write("---")
  st.write("Get In Touch With Me!")
  st.write("##")

  contact_form = """
    <form action="https://formsubmit.co/lealexpertsecurity@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" placeholder="Your Name" required>
      <input type="email" placeholder="Your E-mail" required>
      <textarea name="message" placeholder="Your message here"></textarea>
      <button type="submit">Send</button>
    </form>
  """

left_column, right_column = st.columns(2)

with left_column:
  st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
# Create a Lottie animation using lottie-web
  iframe_html = f'<iframe src="https://lottie.host/?file=7465c052-e14b-41a0-88e8-b251580d7258/cRfMrhXVNW.json" title="Lottie Animation" frameborder="0" style="width:100%; height:400px; top:0; position: relative"></iframe>'
  st.write(iframe_html, unsafe_allow_html=True)
