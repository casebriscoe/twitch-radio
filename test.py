import subprocess
import threading
import time
import requests
import os

import streamlink

from stream_data import StreamData, StreamProcManager
from twitch_api import get_followed_twitch_streams
from keys import evan_oauth_token, rlee_user_id, radio_access_token, radio_client_id

proc_manager = StreamProcManager(evan_oauth_token)

proc = None
while True:    
    streams = get_followed_twitch_streams(radio_client_id, rlee_user_id, radio_access_token)
    for i, stream in enumerate(streams):
        print(i)
        print(stream.quick_info_str())
    
    result = int(input("Chat pick a stream:"))
    if result == -1:
        print("bye bye")
        break
    elif result == -2:
        print("Ending current stream")
        proc_manager.close_stream()
        continue
    choice = streams[result]
    
    confirmation = input(f"Play {choice.stream_title}? (y/n)")
    if confirmation.lower() == "y":
        proc = proc_manager.start_stream(choice)
