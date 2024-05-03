import streamlit as st
import google.generativeai as genai

st.title("💬 SMenAI !!! Generative Data Science Chatbot")

# f = open("keys/gemini.txt")
# key = f.read()
# genai.configure(api_key=key)


api_token = st.secrets['api_token_access']


# Given a Data Science topic help the user understand it.You also answer any followup question as well.If a question is not related to data science,the response should be, 'That is beyond my knowledge.'

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are a helpful Data Science AI Teaching Assistant. Your name is "Smen" devoloped by Soumen.
                              
                              Given a topic that is related to Data Science whatever come , You assist all queries and if it's not related to computer science the tell 'This is beyond my knowledge.'""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message('user').write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    st.session_state["chat_history"] = chat.history
