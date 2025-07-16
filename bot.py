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
        print("\n✅ Bot started successfully!")
        print(response.json())
    else:
        print("\n❌ Failed to start bot:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    # Paste your Zoom link and API key below:
    zoom_link = input("Paste your Zoom meeting link: ")
    #api_key = input("Paste your Recall.ai API key: ")
    api_key = "21b00c2b23d444ffbb01ab6f471b51985301d534"
    launch_recallai_bot(zoom_link, api_key)
