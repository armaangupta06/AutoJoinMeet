import os
from discord_mesage import discord_send_messsage


def send_Message(message, *args):


    for arg in args:

        cmd = f"""osascript<<END

            tell application "Messages"

            send "{message}" to buddy "{str(arg)}" of (service 1 whose service type is iMessage)

            end tell

            END"""
        os.system(cmd)


    discord_send_messsage(message)








