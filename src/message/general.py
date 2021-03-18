from linebot.models import ImagemapSendMessage, BaseSize, MessageImagemapAction, ImagemapArea
from linebot.models import TextSendMessage, StickerSendMessage
from linebot.models import QuickReply, QuickReplyButton, MessageAction, LocationAction, CameraAction, CameraRollAction

import random 
import json 

def getMessage():
    
    with open("./message/message.json") as f: 
        message = json.load(f)
        f.close()
    return message

def greetingMessage():
    msg = getMessage()
    greeting_text = msg["greeting"][0]

    text_message = TextSendMessage(text= greeting_text)
    return text_message

def objectiveMessage():
    msg = getMessage()
    objective_text = msg["objective"][0]

    text_message = TextSendMessage(text= objective_text)
    return text_message

def getImage():
    msg = getMessage()
    getimage_text = msg["get_image"][0]

    text_message = TextSendMessage(text=getimage_text,
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=CameraAction(label="เปิดกล้อง")),
                                QuickReplyButton(action=CameraRollAction(label="ส่งภาพที่ถ่ายไว้")),
                            ]))
    return text_message

def getLocation():
    msg = getMessage()
    getlocation_text = msg["get_location"][0]

    text_message = TextSendMessage(text=getlocation_text,
                            quick_reply=QuickReply(items=[
                                QuickReplyButton(action=LocationAction(label="พิกัดปัจจุบัน"))
                            ]))
    return text_message

def getName():
    msg = getMessage()
    getname_text = msg["get_name"][0]

    text_message = TextSendMessage(text=getname_text)
    return text_message

def getCategory():
    msg = getMessage()
    getcategory_text = msg["get_category"][0]

    text_message = TextSendMessage(text=getcategory_text,
                            quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="ร้านกาแฟ/ร้านขนม", text="ร้านกาแฟ/ร้านขนม")),
                                   QuickReplyButton(action=MessageAction(label="ร้านอาหาร", text = "ร้านอาหาร")),
                                   QuickReplyButton(action=MessageAction(label="พื้นที่สาธารณะ", text = "พื้นที่สาธารณะ")),
                                   QuickReplyButton(action=MessageAction(label="พื้นที่จำกัดเฉพาะกลุ่ม", text = "พื้นที่จำกัดเฉพาะกลุ่ม"))
                               ]))
    return text_message

def thankyou():
    msg = getMessage()
    thankyou_text = msg["thankyou"][0]

    text_message = TextSendMessage(text=thankyou_text,
                            quick_reply=QuickReply(items=[
                                   QuickReplyButton(action=MessageAction(label="ส่งเพิ่ม", text = "ส่งเพิ่ม")),
                                   QuickReplyButton(action=MessageAction(label="เดี๋ยวไว้มาส่งใหม่", text = "เดี๋ยวไว้มาส่งใหม่"))
                               ]))
    return text_message

def endMessage():
    msg = getMessage()
    end_text = msg["end"][0]
    text_message = TextSendMessage(text= end_text)
    return text_message

def endSticker():
    sticker_list = []
    sticker_list.append( StickerSendMessage(package_id = "11537", sticker_id = "52002734") )
    sticker_list.append( StickerSendMessage(package_id = "11537", sticker_id = "52002740") )
    sticker_list.append( StickerSendMessage(package_id = "11537", sticker_id = "52002738") )
    
    sticker_message = sticker_list[ random.randint(0, len(sticker_list) - 1)]
    
    return sticker_message 

def defaultMessage():
    text_message = TextSendMessage(text = "ฟังก์ชั่นดังกล่าวยังไม่เปิดให้บริการ \nขออภัยด้วยน้า เค้ากำลังเรียนรู้อยู่")
    return text_message