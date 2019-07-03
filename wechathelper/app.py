import itchat
from itchat.content import *
import helper
# import time
# current_milli_time = lambda: int(round(time.time() * 1000))

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('我是诸隆隆，很高兴认识你!这是程序自动通过的验证，有可能我没看到消息，所以请留言，我会在第一时间看到消息后回复')


@itchat.msg_register(INCOME_MSG, isGroupChat=True)
def text_reply(msg):
    print(msg)
    if msg.actualNickName == "诸隆隆":
        if msg.type == 'Picture':
            downinfo = msg.download(fileName=msg.fileName)
            imageMsg = {
                'fileName': msg.fileName,
            }
            helper.save_image(imageMsg)
            print(downinfo)
        elif msg.type == 'Text':
            txtMsg = {
                'text': msg.text
            }
            helper.save_text(txtMsg)

@itchat.msg_register(TEXT, isGroupChat=False)
def actionText(msg):
    if msg.text == '来张图':
        imageMsg = helper.find_image_to_friend()
        print(imageMsg)
        for item in imageMsg:
            print(item)
            msg.user.send_image(fileDir=item['fileName'])
    elif msg.text == '来个段子':
        txtMsg = helper.find_text_to_friend()
        for item in txtMsg:
            msg.user.send_msg(item['text'])

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=False)
    itchat.run()