from selenium import webdriver
import pyautogui

driver = webdriver.Chrome('./chromedriver')
# driver.implicitly_wait(3)
driver.get('http://nypc2019.s3-website.ap-northeast-2.amazonaws.com/d80c285dad42354e/?subtask=7')

commands = 'LLLLLLLLLLLLLLLLLLLLLLLLUUURRRRRRRRRRUULLLLLLLLLLUURRRRRRRRRRRRRRRUUUUUUUULLDDDDLDLLUULUUURRRRRRDDDDDDDLLLLLLLLLLLLLLRUUUUUUURRDDRDDDRRUURRUUULUUUUULLDLLDDRDRDDRDDRUUDUUDDLULUULULUURRURRDDLDRDDRRRRRUUURUULLDLDLDLLDRRRRRRLLLLLLDDDDLDDLLUUULUULLDDDDDDDRRRRRRRRRRRRRRUUUUUUULLURDRULURUDDR'

pyautogui.PAUSE = 0.01
keys = {
    'U': 'up',
    'D': 'down',
    'L': 'left',
    'R': 'right'
}

for command in commands:
    key = keys[command]
    print(key)
    pyautogui.keyDown(key)
    pyautogui.press(key)
    pyautogui.keyUp(key)
