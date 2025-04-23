from time import sleep
from mcpi import minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("Now the chat is python!")
while True:
    chat = str(mc.events.pollChatPosts())[32:-2]
    try:
        sleep(0.01)
        exec(chat.replace("print", "mc.postToChat").replace("; ", "\n"))
    except Exception as e:
        mc.postToChat(e)
