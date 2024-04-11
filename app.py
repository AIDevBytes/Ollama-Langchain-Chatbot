import streamlit as st
from config import Config
from helpers.llm_helper import chat, get_models
import ollama

st.set_page_config(
    page_title=Config.PAGE_TITLE,
    initial_sidebar_state="expanded"
)

st.title(Config.PAGE_TITLE)

models = get_models()

# sets up sidebar nav widgets
with st.sidebar:   
    st.markdown("# Chat Options")
    
    # widget - https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
    model = st.selectbox('What model would you like to use?', models)

# checks for existing messages in session state
# https://docs.streamlit.io/library/api-reference/session-state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from session state
# https://docs.streamlit.io/library/api-reference/chat/st.chat_message
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("What would you like to ask?"):
    # Display user prompt in chat message widget
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # adds user's prompt to session state
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner('Generating response...'):
        # retrieves response from model
        llm_stream = chat(user_prompt, model=model)

        # write chat stream to the user
        stream_output = st.write_stream(llm_stream)

        # appends response to the message list
        st.session_state.messages.append({"role": "assistant", "content": stream_output})
