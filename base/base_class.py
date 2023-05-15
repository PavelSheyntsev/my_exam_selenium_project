import datetime
from loguru import logger


class Base:
    def __init__(self, driver):
        self.driver = driver

    """method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        logger.warning(f'Current url {get_url}')

    """method assert word"""

    def assert_word(self, word, result):
        value_word = word
        assert value_word == result
        logger.warning("Good value word")

    """method make screen"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot {now_date}.png'
        self.driver.save_screenshot(f'C:\\Users\\Pavel\\PycharmProjects\\my_exam_selenium_project\\screens\\{name_screenshot}')

    """method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        logger.warning("Good value url")
