import requests
import subprocess

import streamlink

from stream_data import StreamData

def get_followed_twitch_streams(app_client_id, user_id, user_access_token):
    request_headers = {
    "Client-ID": app_client_id,
    "Authorization": f"Bearer {user_access_token}"
    }

    request_params = {
        "user_id": user_id
    }

    response = requests.get(r"https://api.twitch.tv/helix/streams/followed", headers=request_headers, params=request_params)
    data = response.json()
    print(data)
    followed_streams = data["data"]

    streams = [StreamData(s_data) for s_data in followed_streams]
    return streams
