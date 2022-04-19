from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import requests
from transliterate import translit
import random
import time
from fake_user_agent_generator import new_user_agent

with open("birthday_dates.txt", mode="r") as file:
    birthday_dates_list = file.read().splitlines()

with open("names.txt", mode="r") as file:
    names_list = file.read().splitlines()

with open("surnames.txt", mode="r") as file:
    surnames_list = file.read().splitlines()

def mail_registration():
    name = random.choice(names_list)
    surname = random.choice(surnames_list)
    birthday_date = random.choice(birthday_dates_list)
    translit_name = translit(name, language_code='ru', reversed=True)
    translit_surname = translit(surname, language_code='ru', reversed=True)
    username = f"""{translit_name.replace("'", "").lower()}{translit_surname.replace("'", "").lower()}{birthday_date[0:4]}{birthday_date[5:7]}{birthday_date[8:10]}"""
    password = f"""{birthday_date[0:4]}{translit_name.replace("'", "").lower()}"""

    option = webdriver.ChromeOptions()
    option.add_argument("--proxy-server=x97.iproxy.online:14172")
    # option.headless = True
    # option.add_argument("window-size=1280,800")
    option.add_argument(f"user-agent={new_user_agent()}")
    browser = webdriver.Chrome(options=option)
    browser.set_window_size(300, 500)
    browser.set_window_position(0, 0)
    print("STEP 0.0. Go to change ip link")
    browser.get('https://iproxy.online/api-rt/changeip/xB13RyTfpf/xX816BC8KBAPAG876WM3K')
    time.sleep(5)
    print("STEP 0.1. IP changed")
    browser.close()
    browser = webdriver.Chrome(options=option)
    browser.set_window_size(300, 500)
    browser.set_window_position(0, 0)
    browser.get('https://signup.live.com/signup')
    time_sleep_value = 1.5

    # Setup login

    new_email_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/" \
                             "div[1]/fieldset/div[2]/div/div[3]/a"
    login_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/div[1]/" \
                        "fieldset/div[1]/div[3]/div[2]/div/input"
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, new_email_button_xpath)))
    browser.find_element(by=By.XPATH, value=new_email_button_xpath).click()
    browser.find_element(by=By.XPATH, value=login_input_xpath).send_keys(f"{username}")

    print("STEP 1. Setup login")

    # Go to the next step of registration

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]"
                                            "/div/div/form/div/div[1]/div[2]/div/div/div/div[3]/input").click()

    # print("Go to the next step of registration")

    # Setup password

    password_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[3]/" \
                           "div/input[2]"
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, password_input_xpath)))
    browser.find_element(by=By.XPATH, value=password_input_xpath).send_keys(f"{password}")

    print("STEP 2. Setup password")

    # Go to the next step of registration

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div[7]/div/div/div[2]/input").click()

    # print("Go to the next step of registration")

    # Write surname

    surname_input_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[1]/" \
                          "div[3]/div[1]/input"
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, surname_input_xpath)))
    browser.find_element(by=By.XPATH, value=surname_input_xpath).send_keys(f"{surname}")

    print("STEP 3. Write surname")

    # Write name

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div[1]/div[3]/div[2]/input").send_keys(f"{name}")

    print("STEP 4. Write name")

    # Go to the next step of registration

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div[2]/div/div/div[2]/input").click()

    # print("Go to the next step of registration")

    # Chose country

    chose_country_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div/" \
                          "div[3]/div/select/option[222]"
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, chose_country_xpath)))
    browser.find_element(by=By.XPATH, value=chose_country_xpath).click()

    print("STEP 5. Chose country")

    # Chose month of birthday

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div/div[4]/div[3]/div[2]/select/option[7]").click()

    # print("Chose month of birthday")

    # Chose day of birthday

    choose_day_of_birthday_button_xpath = "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/" \
                                          "form/div/div[4]/div[3]/div[1]/select/option[12]"
    browser.find_element(by=By.XPATH, value=choose_day_of_birthday_button_xpath).click()

    print("STEP 6. Chose day of birthday")

    # Write year

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div/div[4]/div[3]/div[3]/input").send_keys("1998")

    print("STEP 7. Write year")

    # Go to the next step of registration

    browser.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/"
                                            "div/div/form/div/div[6]/div/div/div[2]/input").click()

    # print("STEP 8. Go to the next step of registration")

    # Send captcha info to ANYCAPTCHA.COM

    WebDriverWait(browser, 15).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "enforcementFrame")))

    ANYCAPTCHA_KEY = "57bfe232d721460dafd93e549a0650ae"
    anycaptcha_post_params = {
        "clientKey": ANYCAPTCHA_KEY,
        "task": {
            "type": "FunCaptchaTaskProxyless",
            "websitePublicKey": "B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",
            "websiteURL": browser.current_url,
        }
    }

    post_captcha_response = requests.post(url="https://api.anycaptcha.com/createTask", json=anycaptcha_post_params)
    captcha_request_id = post_captcha_response.json()["taskId"]

    anycaptcha_get_params = {
        "clientKey": ANYCAPTCHA_KEY,
        "taskId": captcha_request_id,
    }

    print("STEP 8. Send captcha info to ANYCAPTCHA.COM")

    # Get captcha info from ANYCAPTCHA.COM

    get_captcha_response = requests.post(url="https://api.anycaptcha.com/getTaskResult", json=anycaptcha_get_params)

    captcha_token = get_captcha_response.json()["solution"]["token"]
    script = """parent.postMessage(JSON.stringify({ eventId: "challenge-complete", payload: { sessionToken: '""" \
             + captcha_token + """' } }), "*")"""

    print("STEP 9. Get captcha info from ANYCAPTCHA.COM")

    # browser.switch_to.frame("enforcementFrame")
    browser.execute_script(script)
    print("STEP 10. browser.switch_to.frame('enforcementFrame')")

    # Go to the next step of registration (don't exit from system)
    remain_button_xpath = "/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/" \
                          "div[3]/div[2]/div/div/div[2]/input"
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, remain_button_xpath)))
    # browser.find_element(by=By.XPATH, value=remain_button_xpath).click()
    # print("Go to the next step of registration (don't exit from system)")

    with open("created_mails.txt", mode="a") as file:
        file.write(f"{name}:{surname}:{birthday_date}:{username}@outlook.com:{password}\n")

    print(f"{name}:{surname}:{birthday_date}:{username}@outlook.com:{password}")
    browser.close()

def registration_loop():
    try:
        mail_registration()
    except:
        registration_loop()
    else:
        registration_loop()
    finally:
        registration_loop()

while True:
    registration_loop()
