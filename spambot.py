import pyautogui
import time

print("PYTHON SPAM BOT created by Rodrigo Hernandez\n")

# Preparing bot
seconds = 10
while seconds > 0:
	print(f"[*] In {seconds} seconds the bot starts to spam [*]\n")
	time.sleep(1)
	seconds = seconds - 1

# Bot spams
for i in range(1, 100):
	pyautogui.typewrite("Message to send")
	pyautogui.press("enter")
	print(f"> Message number {i} sent\n")
