import webview
import json
import os


def run():
    window = webview.create_window("LuckyCord", "https://discord.com/app", width=1920, height=1080, fullscreen=False)
    webview.start()

run()