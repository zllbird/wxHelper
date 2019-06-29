import itchat
from itchat.content import *
from xml.etree import ElementTree as ET
from .mongohelper import insert_msg
from .mongohelper import insert_contact

class MsgManager(object):

    def __init__(self):
        self.msgDict = {}

    def logincallback(self):
        # 初始化信息
        pass

    @itchat.msg_register(INCOME_MSG)
    def _(self, msg):
        self.removeMsgHelper(msg)
        self.groupMsgHelper(msg)
        self.msgDict[msg.MsgId] = msg
        return

    # 将想要撤回的消息发送给文件助手
    def removeMsgHelper(self, msg):
        if msg.MsgType == 10002:
            root = ET.fromstring(msg.content)
            print(root)
            for element in root.iter("msgid"):
                # 判断消息类型，如果是文本则发送文本给主账号，谁想撤回什么文本。
                revokeMsg = self.msgDict[element.text]
                # 如果是图片 语音，则告诉主账号撤回了一张图片，则提示，图片已保存，语音也提示图片已保存。
                # 如果是表情，应该属于文本管理吧。
                # 如果是其他，则只提示谁撤回了什么消息。
                # msg.user.send("居然想撤回消息：%s" % revokeMsg.text)
                print(revokeMsg)
                if revokeMsg is not None:
                    if revokeMsg.type == 'Text':
                        # codeClass.teacher.send("%s 居然想撤回消息。撤回的消息是：%s" % (msg.user.NickName, revokeMsg.text))
                        itchat.send_msg("%s 居然想撤回消息。撤回的消息是：%s" % (msg.user.NickName, revokeMsg.text),
                                        toUserName='filehelper')
                    elif revokeMsg.type == 'Picture':
                        revokeMsg.download(revokeMsg.fileName)
                        itchat.send_image(fileDir=revokeMsg.fileName)
                        itchat.send("%s 居然想撤回这张图片。" % msg.user.NickName,
                                        toUserName='filehelper')
                    elif revokeMsg.type == 'Recording':
                        revokeMsg.download(revokeMsg.fileName)
                        itchat.send_video(fileDir=revokeMsg.fileName)
                        itchat.send("%s 居然想撤回这段留言。" % msg.user.NickName,
                                        toUserName='filehelper')

    @itchat.msg_register(FRIENDS)
    def add_friend(self, msg):
        msg.user.verify()
        msg.user.send('我是诸隆隆，很高兴认识你!这是程序自动通过的验证，有可能我没看到消息，所以请留言，我会在第一时间看到消息后回复')

    # @itchat.msg_register(TEXT, isGroupChat=True)
    # def text_reply(msg):
    #     if msg.isAt:
    #         msg.user.send(u'@%s\u2005I received: %s' % (
    #             msg.actualNickName, msg.text))
    # @itchat.msg_register(TEXT, isGroupChat=True)
    # def teacherCallClass(self, msg):
    #     if msg.isAt:
    #         msg.user.send(u'@%s\u2005 ,收到！正在处理，请稍后' % msg.actualNickName)
            # tulingResponse(msg)

    # def tulingResponse(self, msg):
    #     reText = http.postTuling(msg)
    #     msg.user.send(u'@%s\u2005 ,%s' % (msg.actualNickName, reText))

    def groupMsgHelper(self, msg):
        if msg.type == 'Text' and msg.text == '群发':
            friends = itchat.get_friends()
            for friend in friends:
                print(friend)
                friend.send("%s , 儿童节快乐！！！，保持一个不老的心哦。" % friend.RemarkName)

    def groupMsgHelperBySex(self, msg):
        if msg.type == 'Text' and msg.text == '群发':
            friends = itchat.get_friends()
            for friend in friends:
                if friend.sex == 1:
                    friend.send("小哥哥， 小哥哥 ， %s , 儿童节快乐！！！ 永远年轻，永远热血。" % friend.RemarkName)
                elif friend.sex == 2:
                    friend.send("小姐姐， 小姐姐 ， %s , 儿童节快乐！！！ 永远18岁哦。" % friend.RemarkName)
                else:
                    friend.send("%s , 儿童节快乐！！！ " % friend.RemarkName)

    def startWeChat(self):
        # itchat.login(loginCallback=self.logincallback)
        itchat.auto_login(enableCmdQR=True, loginCallback=self.logincallback())
        itchat.run()
