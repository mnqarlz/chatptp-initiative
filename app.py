import streamlit as st
import ollama
from PIL import Image
import io

st.set_page_config(
    page_title="ChatPTP",
    page_icon="🚢",
    layout="centered"  
)

theme = st.get_option("theme.base")

if theme == "dark":
    LOGO_PATH = "public/ptp-logo-light.png"
else:
    LOGO_PATH = "public/ptp-logo.png"

with st.sidebar:
    try:
        st.image(LOGO_PATH, width="stretch")
    except:
        st.title("ChatPTP")

    st.header("⚙️ Settings")
    
    model_choice = st.selectbox(
        "Select AI Model:",
        ("Standard (Llama 3.2)", "Vision (Llava)"),
        index=0
    )

    if "Llava" in model_choice:
        selected_model = "llava"
        enable_vision = True
        st.success("✅ Vision Enabled: You can upload images.")
    else:
        selected_model = "llama3.2"
        enable_vision = False
        st.info("⚡ Standard Mode: Text optimized.")

    st.markdown("---")
    
    if st.button("🗑️ New Conversation", type="primary", width="stretch"):
        st.session_state["messages"] = []
        st.rerun()

    uploaded_file = None
    if enable_vision:
        st.markdown("### 📎 Attachments")
        uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])


st.title("ChatPTP") 
st.caption("🚀 Internal AI Assistant | Port of Tanjung Pelepas")
st.markdown("---") 

def load_internal_data():
    try:
        with open("company_info.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

internal_context = load_internal_data()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    if message["role"] == "assistant":
        avatar_icon = LOGO_PATH
    else:
        avatar_icon = None 
        
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.markdown(message["content"])
        if "image_data" in message:
             st.image(message["image_data"], width=300)

if prompt := st.chat_input("How can I assist you today?"):
    
    with st.chat_message("user"): 
        st.markdown(prompt)
        if uploaded_file:
            st.image(uploaded_file, width=250)
            st.caption("Image attached")

    msg_data = {"role": "user", "content": prompt}
    
    image_path_for_api = None
    if uploaded_file:
        msg_data["image_data"] = uploaded_file.getvalue()
        
        image_path_for_api = "temp_upload.jpg"
        with open(image_path_for_api, "wb") as f:
            f.write(uploaded_file.getbuffer())

    st.session_state["messages"].append(msg_data)

    with st.chat_message("assistant", avatar=LOGO_PATH):
        with st.spinner("Thinking..."):
            try:
                system_prompt = f"""
                You are ChatPTP. Professional, concise, and helpful.
                Use this internal data to answer:
                {internal_context}
                """

                api_msg = {'role': 'user', 'content': f"{system_prompt}\n\nUser Question: {prompt}"}
                
                if image_path_for_api and enable_vision:
                    api_msg['images'] = [image_path_for_api]

                response = ollama.chat(model=selected_model, messages=[api_msg])
                bot_reply = response['message']['content']
                
                st.markdown(bot_reply)
                
                st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

            except Exception as e:
                st.error(f"Error: {e}")
                st.caption("Please ensure Ollama is running.")