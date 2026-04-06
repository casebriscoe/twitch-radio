
import subprocess

import streamlink

class StreamData:
    def __init__(self, json):
        self.raw_json = json
        self.streamer_name = json["user_name"]
        self.viewer_count = json["viewer_count"]
        self.stream_game = json["game_name"]
        self.stream_title = json["title"]
        self.url = f"twitch.tv/{self.streamer_name}"

    def quick_info_str(self):
        return f"""{self.streamer_name}
    {self.stream_game}
    {self.viewer_count} viewers"""

class StreamProcManager:
    def __init__(self, oauth_token):
        self.proc = None
        self.auth = oauth_token
        
    def start_stream(self, stream: StreamData):
        self.close_stream()
        
        session = streamlink.Streamlink()
        session.set_option("twitch-api-header", {"Authorization=OAuth", self.auth})
        streams = session.streams(stream.url)
        stream_url = streams["audio_only"].to_url()

        self.proc = subprocess.Popen(["ffplay", "-nodisp", stream_url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    def close_stream(self):
        if self.proc is not None:
            self.proc.terminate()
            
        self.proc = None

    def __del__(self):
        self.close_stream()        
