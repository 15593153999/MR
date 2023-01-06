import time

from pynput import mouse, keyboard

m_keyboard = keyboard.Controller() 
qty = int(input("轰炸次数:"))
content = input("轰炸内容：")
time_Span = int(input("开始轰炸时间(s):"))
frequency = float(input("轰炸频率(0.1-0.5):"))
print ("选择轰炸区域", time_Span, "秒后开始轰炸") 
time.sleep(time_Span)
for i in range(qty):
    m_keyboard.type(content)
    m_keyboard.press(keyboard.Key.enter) 
    m_keyboard.release(keyboard.Key.enter) 
    time.sleep(frequency)
