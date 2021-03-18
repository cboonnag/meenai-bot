from flask import Flask, render_template, make_response
from flask import request, abort 
from config import * 

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError 
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, LocationMessage

from message.general import *
from detect_intent import detectIntentText

#CRUD
from CRUD.crowdsource import insertData

import requests 
import json 
import os 
import time 

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@app.route("/")
def home():
    return "HOME"

@handler.add(MessageEvent, message = TextMessage)
def handle_text(event):
    user_id = event.source.user_id
    user_message = event.message.text
    user_intent = detectIntentText(user_message, user_id)

    if user_intent == "greeting":        
        greeting_msg = greetingMessage()
        objective_msg = objectiveMessage()
        getname_msg = getName()

        line_bot_api.reply_message(
            event.reply_token,
            [greeting_msg, objective_msg, getname_msg]
            )
            
    elif user_message in ["ร้านกาแฟ/ร้านขนม","ร้านอาหาร","พื้นที่สาธารณะ","พื้นที่จำกัดเฉพาะกลุ่ม"]:
        if user_message == "ร้านกาแฟ/ร้านขนม":
            room_cat = "1"
        elif user_message == "ร้านอาหาร":
            room_cat = "2"
        elif user_message == "พื้นที่สาธารณะ":
            room_cat = "3"
        elif user_message == "พื้นที่จำกัดเฉพาะกลุ่ม":
            room_cat = "4"

        insertData(TimeStamp = event.timestamp , UserId = event.source.user_id, MsgType = "category", Col1 = room_cat, Col2 = user_message, Col3 = "NONE")
        
        thankyou_msg = thankyou()
        line_bot_api.reply_message(
            event.reply_token,
            thankyou_msg
            )
        
    elif user_message in ["ส่งเพิ่ม","เดี๋ยวไว้มาส่งใหม่"]:
        end_msg = endMessage()

        line_bot_api.reply_message(
            event.reply_token,
            end_msg
            )

    elif user_intent == "location-name":

        insertData(TimeStamp = event.timestamp , UserId = event.source.user_id, MsgType = "name", Col1 = user_message, Col2 = "NONE", Col3 = "NONE")

        getimage_msg = getImage()    
        line_bot_api.reply_message(
            event.reply_token,
            getimage_msg
            )
    elif user_intent == "end":
        end_msg = endSticker()
        line_bot_api.reply_message(
            event.reply_token,
            end_msg
            )
    else:
        default_msg = defaultMessage()

        line_bot_api.reply_message(
            event.reply_token,
            default_msg
            )

@handler.add(MessageEvent, message = LocationMessage)
def handle_location(event):
    lat = str(event.message.latitude) 
    lon = str(event.message.longitude) 

    try:
        title = event.message.title
    except:
        title = "NONE"

    insertData(TimeStamp = event.timestamp , UserId = event.source.user_id, MsgType = "location", Col1 = lat,  Col2 =  lon, Col3 = title)

    getcategory_msg = getCategory()
    line_bot_api.reply_message(
        event.reply_token,
        getcategory_msg
        )

@handler.add(MessageEvent, message = ImageMessage)
def handle_image(event):

    insertData(TimeStamp = event.timestamp , UserId = event.source.user_id, MsgType = "image", Col1 = event.message.id,  Col2 = "NONE", Col3 = "NONE")

    getlocation_msg = getLocation()
    line_bot_api.reply_message(
        event.reply_token,
        getlocation_msg
        )

@handler.default()
def default(event):      
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
        )

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = int(os.environ.get('PORT',8080)))