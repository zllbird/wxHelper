from .core import MsgManager

def new_instance():
    newInstance = MsgManager()
    return newInstance

instance = new_instance()

run = instance.startWeChat()