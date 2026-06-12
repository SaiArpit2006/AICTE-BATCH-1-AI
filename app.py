import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


# ======================
# PAGE
# ======================

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="🚀",
    layout="wide"
)


# ======================
# GEMINI
# ======================

load_dotenv()

genai.configure(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# ======================
# CSS
# ======================

st.markdown("""
<style>

.stApp{

background:
linear-gradient(
135deg,
#050816,
#0A1028,
#130A33
);

color:white;

}


/* TITLE */

.title{

text-align:center;

font-size:60px;

font-weight:900;

color:#00E5FF;

text-shadow:
0 0 25px cyan;

}


.sub{

text-align:center;

font-size:18px;

color:#AAB7FF;

margin-bottom:40px;

}


/* INPUT */

.stTextInput input,
.stTextArea textarea{

background:
rgba(
15,
15,
40,
0.9
)!important;

color:white!important;

border:

1px solid cyan!important;

border-radius:14px!important;

}


/* BUTTON */

.stButton button{

width:100%;

height:65px;

border:none;

border-radius:16px;

font-size:20px;

font-weight:700;

background:

linear-gradient(
90deg,
#00E5FF,
#8A2BE2
);

color:white;

box-shadow:

0 0 35px
rgba(
0,
255,
255,
0.4
);

}


/* OUTPUT */

.result{

background:

rgba(
15,
15,
35,
0.9
);

padding:40px;

border-radius:22px;

border:

1px solid cyan;

box-shadow:

0 0 40px
rgba(
0,
255,
255,
0.2
);

}

</style>
""",
unsafe_allow_html=True
)


# ======================
# HEADER
# ======================

st.markdown("""
<div class='title'>
🚀 AI Resume & Portfolio Builder
</div>

<div class='sub'>
Create • Resume • Cover Letter • Portfolio
</div>
""",
unsafe_allow_html=True
)


# ======================
# INPUT
# ======================

c1,c2=st.columns(2)

with c1:

    name=st.text_input(
        "👤 Name"
    )

    education=st.text_input(
        "🎓 Education"
    )

    goal=st.text_input(
        "🎯 Career Goal"
    )


with c2:

    skills=st.text_area(
        "💻 Skills"
    )

    projects=st.text_area(
        "🚀 Projects"
    )


# ======================
# GENERATE
# ======================

if st.button(
    "✨ Generate Professional Profile"
):

    prompt=f"""

Create:

1 Professional Resume

2 Cover Letter

3 Portfolio Summary


Name:
{name}

Education:
{education}

Skills:
{skills}

Projects:
{projects}

Career Goal:
{goal}


Make output:

ATS Friendly

Modern

Professional

"""


    try:

        with st.spinner(
            "Generating..."
        ):

            response=model.generate_content(
                prompt
            )

        st.success(
            "Generated Successfully ✅"
        )

        st.markdown(

f"""
<div class='result'>

{response.text}

</div>
""",

unsafe_allow_html=True

)

        st.metric(
            "AI Engine",
            "Gemini"
        )

        st.info(
"""
Generated:

✅ Resume

✅ Cover Letter

✅ Portfolio
"""
)

    except Exception as e:

        st.error(
f"""
Error:

{e}
"""
)