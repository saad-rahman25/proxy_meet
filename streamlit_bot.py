import streamlit as st
import requests

def launch_recallai_bot(meeting_url, api_key, region="us-west-2"):
    url = f"https://{region}.recall.ai/api/v1/bot"
    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "meeting_url": meeting_url,
        "bot_name": "My RecallAI Bot",
        "recording_config": {
            "transcript": {
                "provider": {
                    "meeting_captions": {}
                }
            }
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        return True, response.json()
    else:
        return False, response.text

st.title("📡 ProxyMeet Meeting Bot Launcher")
st.markdown("Enter your Zoom meeting link and launch the bot to transcribe it.")

zoom_link = st.text_input("🔗 Zoom Meeting Link")
#api_key = st.text_input("🔑 Recall.ai API Key", type="password")
api_key = "21b00c2b23d444ffbb01ab6f471b51985301d534"

if st.button("🚀 Launch Bot"):
    if not zoom_link: #or not api_key:
        st.error("Please provide both the meeting link")
    else:
        with st.spinner("Launching bot..."):
            success, result = launch_recallai_bot(zoom_link, api_key)
        if success:
            st.success("✅ Bot started successfully!")
            st.json(result)
        else:
            st.error("❌ Failed to start bot.")
            st.code(result)
