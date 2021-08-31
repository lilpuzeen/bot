import time
# from main import PROBLEMS, problem_number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import choice
from PIL import Image

problem_number = 9


class GetProblem:
    def __init__(self):
        self.number = problem_number
        self.PATH = "/Users/armantovmasyan/PycharmProjects/bot/chromedriver"

    def construct(self):
        global curr_url
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(self.PATH)
        driver.get("https://math-ege.sdamgia.ru/?redir=1")
        time.sleep(3)
        problem = driver.find_element_by_name(f"prob{self.number}")
        problem.send_keys(99)
        button = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/main/section[4]/form/div/div[2]/div/button[1]")
        button.click()
        try:
            problem_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "prob_list"))
            )
            problems = problem_list.find_elements_by_class_name("prob_maindiv")
            prob_maindiv = choice(problems)
            prob_maindiv_text = prob_maindiv.text
            prob_maindiv_exact_num = prob_maindiv_text.split()[3]
            driver.find_element_by_link_text(f"{prob_maindiv_exact_num}").click()
            driver.implicitly_wait(10)
            curr_url = driver.current_url
            in_prob_text = prob_maindiv.find_element_by_class_name("pbody")
            myphoto = Image.open(in_prob_text.screenshot_as_png(f"Problem{prob_maindiv_exact_num}"))
            # print(prob_maindiv_exact_num)
            # print(prob_maindiv_text)
            # print("Done!")
            driver.quit()
        except Exception as e:
            print(e)
            print(e.__traceback__)
            driver.quit()
            print("Ошибка!!!")

    def getimage(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(curr_url)

        # TODO сделать поиск по id задания (prob_maindiv_exact_num), и в left_margin найти фотки. return фотки в screenshot_as_png, чтобы бот отправил
        # TODO анализ на наличие фотографий, иначе return None. Возможно raise TypeError по NoneType-у


if __name__ == '__main__':
    a = GetProblem()
    a.construct()
