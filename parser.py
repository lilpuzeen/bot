import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice

# todo: импортнуть problem_number
# todo: добавить --headless
class GetProblem:
    def __init__(self):
        self.number = problem_number
        self.PATH = "/Users/armantovmasyan/PycharmProjects/bot/chromedriver"

    def construct(self):
        global curr_url, prob_maindiv_exact_num
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
            maindiv = driver.find_element_by_class_name("prob_maindiv")
            pbody = maindiv.find_element_by_class_name("pbody")
            problem_photo = pbody.screenshot(f"Problem{prob_maindiv_exact_num}.png")
            driver.quit()
            return f"Problem{prob_maindiv_exact_num}.png"
        except Exception as e:
            print(e)
            print(e.__traceback__)
            driver.quit()
            return "Ошибка!!!"

    def getimage(self): # TODO анализ на наличие фотографий, иначе return None. Возможно raise TypeError по NoneType-у
        driver = webdriver.Chrome(self.PATH)
        driver.get(curr_url)
        maindiv = driver.find_element_by_class_name("prob_maindiv")
        pbody = maindiv.find_element_by_class_name("pbody")
        img = pbody.find_elements_by_tag_name("img")
        img[0].screenshot(f"Problem{prob_maindiv_exact_num}_picture.png")
        return f"Problem{prob_maindiv_exact_num}_picture.png"

    def getsolution(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(curr_url)
        maindiv = driver.find_element_by_class_name("prob_maindiv")
        solution = maindiv.find_element_by_id(f"sol{prob_maindiv_exact_num}")
        solution.screenshot(f"Problem{prob_maindiv_exact_num}_solution.png")
        return f"Problem{prob_maindiv_exact_num}_solution.png"


# if __name__ == '__main__':
#     a = GetProblem()
#     a.construct()
#     a.getimage()
#     a.getsolution()