import time
# from main import PROBLEMS, problem_number
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

problem_number = 3

class GetProblem:
    def __init__(self):
        self.number = problem_number
        self.PATH = "/Users/armantovmasyan/PycharmProjects/bot/chromedriver"

    def construct(self):
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

            for prob in problems:
                prob_text = prob.find_element_by_class_name("pbody")
                for p in prob_text:
                    myP = p.find_elements_by_tag_name("p")
                    for secP in myP:
                        print(secP, end="\n")
        except Exception:
            driver.quit()
            print("Ошибка!")


if __name__ == '__main__':
    a = GetProblem()
    a.construct()
