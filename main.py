import streamlit as st 
from openai import OpenAI
from utils import *

st.title("AI Assistant")

password = st.text_input("Enter password to use ChatGPT", type="password")

checkbox_visible = False
if password != st.secrets["APP_PW"]:
    checkbox_visible = True

want_use_chatgpt = st.checkbox("**Use ChatGPT** (consumes tokens)", value=False, disabled=checkbox_visible)

use_chatgpt = False
if password == "keyrus":
    use_chatgpt = want_use_chatgpt

####################################################
####################### INIT #######################
####################################################

# Load config file
config = load_config()
avatars = load_avatars(config)

# st.write(config)

if use_chatgpt:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4o-mini"

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

####################################################
##################### SIDE BAR #####################
####################################################

with st.sidebar:
    with st.expander(":pencil: **Email credentials** 🤫"):
        email_login = st.text_input("Login:",value="")
        email_password = st.text_input("Password:",value="", type="password")
    
    with st.container(border=True):
        st.title("GPT personality")
        selected_persona = st.selectbox(
            "What personality do you want you GPT to have?",
            list(config["AI personalities"].keys()),
            index=None,
            placeholder="Select personality",
        )

        if selected_persona:
            persona = config["AI personalities"][selected_persona]
            st.image(avatars[selected_persona])
            st.markdown(persona)
        if not selected_persona:
            if use_chatgpt:
                selected_persona = "ChatGPT"
                persona = config["AI personalities"][selected_persona]
            else:
                selected_persona = "RobotGPT"

####################################################
#################### MAIN VIEW #####################
####################################################

# Display chat message from history on app rerun 
for message in st.session_state.messages:
    # st.write(message)
    with st.chat_message(message["role"],avatar=avatars[message["persona"]]):
        st.markdown(message["content"])

        
# React to user input
if prompt := st.chat_input():
    # Display user message in chat container
    with st.chat_message("user",avatar=avatars["User"]):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role":"user","persona":"User","content":prompt})

    if use_chatgpt:
        # Display assistant response in chat message container
        with st.chat_message("assistant",avatar=avatars[selected_persona]):
            ai_response = client.responses.create(
                    model=st.session_state["openai_model"],
                    instructions=persona if selected_persona else None,
                    input=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    stream=False,
                    )
            response = st.write_stream([words for words in ai_response.output_text])
        st.session_state.messages.append({"role": "assistant","persona":selected_persona, "content": response})
    
    if not use_chatgpt:
        # Display assistant response in chat message container
        with st.chat_message("assistant",avatar=avatars[selected_persona]):
            response = st.write_stream(response_generator(config,selected_persona))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant","persona":selected_persona, "content": response})

# Clear the chat history
if st.session_state.messages:
    st.button("Clear chat history", on_click=clear_chat_history)

