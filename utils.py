import streamlit as st
import random
import time
import yaml
from PIL import Image

@st.cache_data
def load_config(file_path="config.yaml"):
    with open(file_path,encoding="utf-8") as f:
        return yaml.safe_load(f)

@st.cache_data
def load_avatars(config):
    avatars = {}
    for name, path in config["Avatars"].items():
        avatars[name] = Image.open(path)
    return avatars


def response_generator(config,persona):
    response = random.choice(config["random responses"][persona])

    for word in response.split():
        yield word + " "
        time.sleep(0.1)

def clear_chat_history(key="messages"):
    del st.session_state[key]

