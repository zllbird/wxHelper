import itchat, time
from itchat.content import *
from xml.etree import ElementTree as ET
from httpdemo import http

msgList = []
msgDict = {}

class CodeClass(object):
    def __init__(self):
        self.teacher = None

codeClass = CodeClass()

@itchat.msg_register(INCOME_MSG)
def _(msg):
    removeMsgHelper(msg)
    groupMsgHelper(msg)
    msgDict[msg.MsgId] = msg
    return

def removeMsgHelper(msg):
    if msg.MsgType == 10002:
        root = ET.fromstring(msg.content)
        print(root)
        for element in root.iter("msgid"):
            # 判断消息类型，如果是文本则发送文本给主账号，谁想撤回什么文本。
            revokeMsg = msgDict[element.text]
            # 如果是图片 语音，则告诉主账号撤回了一张图片，则提示，图片已保存，语音也提示图片已保存。
            # 如果是表情，应该属于文本管理吧。
            # 如果是其他，则只提示谁撤回了什么消息。
            # msg.user.send("居然想撤回消息：%s" % revokeMsg.text)
            print(revokeMsg)
            if revokeMsg is not None:
                if revokeMsg.type == 'Text':
                    itchat.send_msg("%s 居然想撤回消息。撤回的消息是：%s" % (msg.user.NickName, revokeMsg.text), toUserName='filehelper')
                    # codeClass.teacher.send("%s 居然想撤回消息。撤回的消息是：%s" % (msg.user.NickName, revokeMsg.text))
                elif revokeMsg.type == 'Picture':
                    revokeMsg.download(revokeMsg.fileName)
                    codeClass.teacher.send_image(fileDir=revokeMsg.fileName)
                    codeClass.teacher.send("%s 居然想撤回这张图片。" % msg.user.NickName)
                elif revokeMsg.type == 'Recording':
                    revokeMsg.download(revokeMsg.fileName)
                    codeClass.teacher.send_video(fileDir=revokeMsg.fileName)
                    codeClass.teacher.send("%s 居然想撤回这段留言。" % msg.user.NickName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     if msg.isAt:
#         msg.user.send(u'@%s\u2005I received: %s' % (
#             msg.actualNickName, msg.text))
@itchat.msg_register(TEXT,isGroupChat=True)
def teacherCallClass(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005 ,收到！正在处理，请稍后'% msg.actualNickName)
        tulingResponse(msg)

def tulingResponse(msg):
    reText = http.postTuling(msg)
    msg.user.send(u'@%s\u2005 ,%s' % (msg.actualNickName, reText))

def groupMsgHelper(msg):
    if msg.type == 'Text' and msg.text == '群发':
        friends = itchat.get_friends()
        contacts = itchat.get_contact()
        for friend in friends:
            print(friend)
            # friend.send("%s , 儿童节快乐！！！，保持一个不老的心哦。" % friend.RemarkName)
        for contact in contacts:
            print(contact)

def groupMsgHelperBySex(msg):
    if msg.type == 'Text' and msg.text == '群发':
        friends = itchat.get_friends()
        for friend in friends:
            if friend.sex == 1:
                friend.send("小哥哥， 小哥哥 ， %s , 儿童节快乐！！！ 永远年轻，永远热血。" % friend.RemarkName)
            elif friend.sex == 2:
                friend.send("小姐姐， 小姐姐 ， %s , 儿童节快乐！！！ 永远18岁哦。" % friend.RemarkName)
            else:
                friend.send("%s , 儿童节快乐！！！ " % friend.RemarkName)

def loginCallback():
    Zhu = itchat.search_friends(nickName='诸隆隆')
    codeClass.teacher = Zhu[0]
    print(Zhu[0])
    initInfo = itchat.web_init()
    print(initInfo)
    # for friend in friends:
    #     print(friend)

if __name__ == '__main__':
    itchat.auto_login(True, loginCallback=loginCallback)
    itchat.run(True)


