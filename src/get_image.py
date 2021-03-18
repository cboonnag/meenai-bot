from flask import Flask, render_template, make_response
from flask import request, abort 
from config import * 

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage

import requests 
import json 
import os 
import time 

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

def get_image():
    message_id = "ID"
    message_content = line_bot_api.get_message_content(message_id)

    with open(file_path, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)




if __name__ == '__main__':
    get_image()