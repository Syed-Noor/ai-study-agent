import streamlit as st
import base64
import os

from agent import run_agent


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Study Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# BACKGROUND IMAGE
# ============================================================

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKGROUND_PATH = os.path.join(BASE_DIR, "background.jpg")

try:
    background_image = get_base64_image(BACKGROUND_PATH)
except (FileNotFoundError, OSError):
    background_image = ""


# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    f"""
    <style>

    /* ================================
       APP BACKGROUND
       ================================ */

    .stApp {{
        background:
            linear-gradient(
                rgba(5, 10, 25, 0.82),
                rgba(5, 10, 25, 0.88)
            ),
            url("data:image/jpeg;base64,{background_image}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}


    /* ================================
       MAIN CONTAINER
       ================================ */

    .main .block-container {{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }}


    /* ================================
       HEADER
       ================================ */

    header {{
        background: transparent !important;
    }}


    /* ================================
       SIDEBAR
       ================================ */

    section[data-testid="stSidebar"] {{
        background: rgba(10, 15, 30, 0.96) !important;
        border-right: 1px solid rgba(255,255,255,0.08);
    }}


    section[data-testid="stSidebar"] > div {{
        padding-top: 1.5rem;
    }}


    /* ================================
       HERO
       ================================ */

    .hero {{
        text-align: center;
        padding: 50px 20px 35px 20px;
    }}

    .hero-icon {{
        font-size: 65px;
        line-height: 1;
        margin-bottom: 20px;

        filter:
            drop-shadow(
                0 0 25px
                rgba(99,102,241,0.7)
            );
    }}

    .hero-title {{
        color: white !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        line-height: 1.2 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}

    .hero-gradient {{
        background:
            linear-gradient(
                90deg,
                #60a5fa,
                #a78bfa,
                #f472b6
            );

        -webkit-background-clip: text;
        background-clip: text;

        -webkit-text-fill-color: transparent;
        color: transparent;
    }}

    .hero-description {{
        max-width: 650px;
        margin: 18px auto 0 auto;

        color:
            rgba(255,255,255,0.70) !important;

        font-size: 15px !important;
        line-height: 1.7 !important;
    }}


    /* ================================
       SIDEBAR LOGO
       ================================ */

    .logo-container {{
        text-align: center;
        padding: 10px 0 25px 0;
    }}

    .logo-icon {{
        font-size: 55px;
        line-height: 1;
        margin-bottom: 10px;
    }}

    .logo-title {{
        color: white !important;
        font-size: 23px !important;
        font-weight: 800 !important;
    }}

    .logo-subtitle {{
        color:
            rgba(255,255,255,0.55) !important;

        font-size: 12px !important;
        margin-top: 6px;
    }}


    /* ================================
       SIDEBAR SECTION
       ================================ */

    .sidebar-section {{
        color:
            rgba(255,255,255,0.45) !important;

        font-size: 11px !important;
        font-weight: 700 !important;

        letter-spacing: 1.5px;
        text-transform: uppercase;

        margin-top: 25px;
        margin-bottom: 12px;
    }}


    /* ================================
       TOOL CARDS
       ================================ */

    .tool-card {{
        background:
            rgba(255,255,255,0.055);

        border:
            1px solid
            rgba(255,255,255,0.08);

        border-radius: 12px;

        padding: 14px;
        margin-bottom: 9px;

        transition:
            all 0.2s ease;
    }}

    .tool-card:hover {{
        background:
            rgba(139,92,246,0.15);

        border-color:
            rgba(139,92,246,0.4);

        transform:
            translateX(3px);
    }}

    .tool-icon {{
        font-size: 20px;
        margin-right: 8px;
    }}

    .tool-name {{
        color: white !important;
        font-weight: 600;
        font-size: 14px;
    }}

    .tool-description {{
        color:
            rgba(255,255,255,0.5) !important;

        font-size: 11px;

        margin-top: 4px;
        margin-left: 32px;
    }}


    /* ================================
       STATUS
       ================================ */

    .status-card {{
        margin-top: 25px;
        padding: 12px;

        border-radius: 12px;

        background:
            rgba(34,197,94,0.08);

        border:
            1px solid
            rgba(34,197,94,0.18);
    }}

    .status-dot {{
        width: 8px;
        height: 8px;

        background: #22c55e;

        border-radius: 50%;

        display: inline-block;

        margin-right: 8px;

        box-shadow:
            0 0 10px #22c55e;
    }}

    .status-text {{
        color: #86efac !important;
        font-size: 12px;
        font-weight: 600;
    }}


    /* ================================
       FEATURE CARDS
       ================================ */

    .feature-card {{
        background:
            rgba(255,255,255,0.055);

        border:
            1px solid
            rgba(255,255,255,0.09);

        border-radius: 16px;

        padding: 22px;

        min-height: 145px;

        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);

        transition:
            all 0.25s ease;
    }}

    .feature-card:hover {{
        transform:
            translateY(-5px);

        background:
            rgba(255,255,255,0.08);

        border-color:
            rgba(139,92,246,0.35);
    }}

    .feature-icon {{
        font-size: 30px;
        margin-bottom: 10px;
    }}

    .feature-title {{
        color: white !important;

        font-size: 15px;
        font-weight: 700;
    }}

    .feature-text {{
        color:
            rgba(255,255,255,0.55) !important;

        font-size: 12px;

        line-height: 1.6;

        margin-top: 7px;
    }}


    /* ================================
       CHAT
       ================================ */

    [data-testid="stChatMessage"] {{
        background:
            rgba(255,255,255,0.055) !important;

        border:
            1px solid
            rgba(255,255,255,0.08);

        border-radius: 18px;

        padding: 15px;

        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);

        margin-bottom: 12px;
    }}

    [data-testid="stChatMessage"] p {{
        color:
            rgba(255,255,255,0.92) !important;

        line-height: 1.7;
    }}


    /* ================================
       CHAT INPUT
       ================================ */

    [data-testid="stChatInput"] {{
        background:
            rgba(15,23,42,0.95) !important;

        border:
            1px solid
            rgba(255,255,255,0.12);

        border-radius: 18px;
    }}

    [data-testid="stChatInput"] textarea {{
        color: white !important;
    }}

    [data-testid="stChatInput"] textarea::placeholder {{
        color:
            rgba(255,255,255,0.4) !important;
    }}


    /* ================================
       BUTTON
       ================================ */

    .stButton > button {{
        width: 100%;

        background:
            rgba(255,255,255,0.06) !important;

        color: white !important;

        border:
            1px solid
            rgba(255,255,255,0.10);

        border-radius: 10px;

        transition:
            all 0.2s ease;
    }}

    .stButton > button:hover {{
        background:
            rgba(139,92,246,0.18) !important;

        border-color:
            rgba(139,92,246,0.7);
    }}


    /* ================================
       DIVIDER
       ================================ */

    hr {{
        border-color:
            rgba(255,255,255,0.08) !important;
    }}


    /* ================================
       SCROLLBAR
       ================================ */

    ::-webkit-scrollbar {{
        width: 6px;
    }}

    ::-webkit-scrollbar-track {{
        background:
            rgba(0,0,0,0.2);
    }}

    ::-webkit-scrollbar-thumb {{
        background:
            rgba(255,255,255,0.20);

        border-radius: 10px;
    }}

    </style>
    """
)


# ============================================================
# DISPLAY CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    if message["role"] == "user":
        avatar = "👤"
    else:
        avatar = "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar,
    ):

        st.markdown(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

user_message = st.chat_input(
    "Ask your AI study agent anything..."
)


# ============================================================
# PROCESS USER MESSAGE
# ============================================================

if user_message:

    # --------------------------------------------------------
    # USER MESSAGE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    with st.chat_message(
        "user",
        avatar="👤",
    ):

        st.markdown(
            user_message
        )


    # --------------------------------------------------------
    # AI RESPONSE
    # --------------------------------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖",
    ):

        with st.spinner(
            "Agent is thinking..."
        ):

            try:

                response = run_agent(
                    user_message
                )

                # Make sure response is a string
                if response is None:
                    response = (
                        "I couldn't generate a response."
                    )
                else:
                    response = str(response)

            except Exception as e:

                response = (
                    "⚠️ **Something went wrong.**\n\n"
                    "Please check your agent configuration "
                    "and API credentials."
                )

                # Print actual error in terminal
                print(
                    "Agent Error:",
                    repr(e)
                )

        st.markdown(
            response
        )


    # --------------------------------------------------------
    # SAVE AI RESPONSE
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )