import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-1995460195813-2022344747728-JkIJDI9QkkrNeJ02C91HhGIs"
 
post_message(myToken,"#coin-alarm","hi! i'm DABOK")
