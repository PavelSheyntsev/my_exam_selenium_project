import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from loguru import logger

from base.base_class import Base


class MacBookProPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # highlight elements

    def highlight(self, element):
        driver = self.driver
        effect_time = 0.3
        colors = ["red", "skyblue", "lightgreen"]
        border = 4

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        for color in colors:
            apply_style("border: {0}px solid {1};".format(border, color))
            time.sleep(effect_time)
        apply_style(original_style)

    # locators

    XPATH_RAM = "//*[@id='page-side']/form/fieldset[2]/div/div/label[2]"
    XPATH_BRAND = "//*[@id='page-side']/form/fieldset[3]/div/div/label"
    XPATH_MANUFACTURER = "//*[@id='page-side']/form/fieldset[4]/div/div/label[1]"
    XPATH_PROCESSOR = "//*[@id='page-side']/form/fieldset[5]/div/div/label[1]"
    XPATH_CORES = "//*[@id='page-side']/form/fieldset[6]/div/div/label[1]"
    XPATH_MEMORY = "//*[@id='page-side']/form/fieldset[10]/div/div/label[2]"
    XPATH_COLOR = "//*[@id='page-side']/form/fieldset[11]/div/div/label[2]"
    XPATH_TO_POUND = "//*[@id='catalog']/div/div/a"

    # getters

    def get_ram(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_RAM)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_brand(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_BRAND)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_manufacturer(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_MANUFACTURER)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_processor(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_PROCESSOR)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_processor_cores(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_CORES)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_processor_memory(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_MEMORY)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_processor_color(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_COLOR)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def get_pound(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.XPATH_TO_POUND)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    # actions

    def click_ram_checkbox(self):
        self.highlight(self.get_ram())
        self.get_ram().click()
        logger.info("Click RAM checkbox")

    def click_brand_checkbox(self):
        self.highlight(self.get_brand())
        self.get_brand().click()
        logger.info("Click brand checkbox")

    def click_manufacturer_checkbox(self):
        self.highlight(self.get_manufacturer())
        self.get_manufacturer().click()
        logger.info("Click manufacturer checkbox")

    def click_processor_checkbox(self):
        self.highlight(self.get_processor())
        self.get_processor().click()
        logger.info("Click processor checkbox")

    def click_processor_cores_checkbox(self):
        self.highlight(self.get_processor_cores())
        self.get_processor_cores().click()
        logger.info("Click processor_cores checkbox")

    def click_processor_memory_checkbox(self):
        self.highlight(self.get_processor_memory())
        self.get_processor_memory().click()
        logger.info("Click processor_memory checkbox")

    def click_processor_color_checkbox(self):
        self.highlight(self.get_processor_color())
        self.get_processor_color().click()
        logger.info("Click processor_color checkbox")

    def click_to_pound(self):
        self.driver.refresh()  # избегаем StaleElementReferenceException
        self.highlight(self.get_pound())
        self.get_pound().click()
        logger.info("Click buy button")

    # methods

    def select_options(self):
        self.get_current_url()
        self.click_ram_checkbox()
        self.click_brand_checkbox()
        self.click_manufacturer_checkbox()
        self.click_processor_checkbox()
        self.click_processor_cores_checkbox()
        self.click_processor_memory_checkbox()
        self.click_processor_color_checkbox()
        self.click_to_pound()
        self.assert_url("https://pitergsm.ru/catalog/tablets-and-laptops/mac/macbook-pro/macbook-pro-16-2021/13270/")
        self.get_screenshot()
