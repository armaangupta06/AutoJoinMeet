
import time
from selenium import webdriver
from send_messages import send_Message
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import datetime
import pyautogui


opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
  })
last_bot = ""
current_bot = ""
def make_instance(quit=False):
    global last_bot
    global current_bot
    if quit == False:
        bot = webdriver.Chrome(options=opt, executable_path="/Users/armaangupta/Downloads/chromedriver")
        current_bot = bot
        return current_bot
    elif quit == True:
        if current_bot == "":
            print("No open fields")
            return

        else:
            current_bot.quit()
            print("Quit")
            return

def type_chat(bot, type):
    btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[1]/div[3]/div/div[2]/div[3]")
    time.sleep(1)
    btn.click()
    time.sleep(1)
    pyautogui.write(type)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)



def join_classes(meeting_link = "", quit = False, click = False, type = ""):
    email = "3012624@chclc.org"
    pas = "Ag2624!"
    phonenumber1 = "8568736010"
    phonenumber2 = "8568736000"
    phonenumber3 = "8568733066"
    phonenumber4 = "8567019014"
    if quit == True:
        make_instance(quit=True)
        time.sleep(3)
        return
    else:
        bot = make_instance()


    bot.maximize_window()
    bot.get(
        "https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fmeet.google.com%2F_meet%2Fwhoops%3Fsc%3D232%26alias%3Dmymeetingraheel&_ga=2.262670348.1240836039.1604695943-1869502693.1604695943&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(3)
    email_in = bot.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
    email_in.send_keys(email)
    time.sleep(1)
    next_btn = bot.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
    next_btn.click()
    time.sleep(3)
    pas_in = bot.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    pas_in.send_keys(pas)
    time.sleep(1)
    next1_btn = bot.find_element_by_xpath(
        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
    time.sleep(4)
    time.sleep(1)
    bot.get(meeting_link)
    time.sleep(1)
    try:
        diss_btn = bot.find_element_by_xpath("/html/body/div/div[3]/div/div[2]/div[3]/div/span/span")
        diss_btn.click()
        time.sleep(2)
        join_btn = bot.find_element_by_xpath(
        "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]")
        join_btn.click()
    except NoSuchElementException:
        try:
            time.sleep(1)
            time.sleep(2)
            mute_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div")
            mute_btn.click()
            time.sleep(1)
            time.sleep(2)
            camera_btn = bot.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div")
            camera_btn.click()
            time.sleep(2)
            join_btn = bot.find_element_by_xpath(
            "/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]")
            join_btn.click()
        except NoSuchElementException:
            send_Message("No class today", "8568736010")
            return
    finally:
        #second dismiss button
        try:
            time.sleep(5)
            bot.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/div/span/span").click()
            print("Joined meeting")
        except NoSuchElementException:
            print("Joined meeting")

    if click == True:
        type_chat(bot, "here")
'''
    while True:
        if (justtime == "12:38" or justtime == "11:57" or justtime == "13:06" or justtime == "14:15"):
            send_Message("Class is finished...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
            bot.quit()
            return
            break
        else:
            time.sleep(20)
            now = datetime.datetime.now()
            current_time = now.strftime("%A")
            justtime = now.strftime("%H:%M")

            print(justtime)
'''



