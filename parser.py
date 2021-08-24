import time
# from main import PROBLEMS, problem_number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import choice


problem_number = 9


class GetProblem:  # TODO сделать отдельный метод под получение фотографий, чтобы легче воспользоваться в мэйне
    def __init__(self):
        self.number = problem_number
        self.PATH = "/Users/armantovmasyan/PycharmProjects/bot/chromedriver"

    def construct(self):
        global curr_url
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
            curr_url = driver.current_url()
            problems = problem_list.find_elements_by_class_name("prob_maindiv")
            prob_maindiv = choice(problems)
            prob_maindiv_text = prob_maindiv.text
            prob_maindiv_exact_num = prob_maindiv_text.split()[3]
            prob_maindiv_img = prob_maindiv.find_elements_by_tag_name("img")
            print(prob_maindiv_exact_num)
            print(prob_maindiv_text)
            print("Done!")
            driver.quit()
        except Exception as e:
            print(e)
            driver.quit()
            print("Ошибка!!!")

    def getimage(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(curr_url)
        # TODO сделать поиск по id, и в left_margin найти фотки. return фотки в скриншотах, чтобы бот отправил



if __name__ == '__main__':
    a = GetProblem()
    a.construct()
