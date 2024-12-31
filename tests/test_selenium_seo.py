import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium_seo import SeleniumSEO

class TestSeleniumSEO(unittest.TestCase):
    def setUp(self):
        """Set up a shared WebDriver instance before each test."""
        self.driver = webdriver.Chrome()
        url = "https://www.selenium.dev"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def test_seo(self):
        seo = SeleniumSEO(self.driver)
        keywords = seo.process_keywords()
        assert len(keywords) > 0

    def test_set_tags(self):
        seo = SeleniumSEO(self.driver)
        tags = ['p']
        seo.set_tags(tags)
        assert seo.get_tags() == tags

    def test_set_ignore_words(self):
        seo = SeleniumSEO(self.driver)
        ignore_words = ['the']
        seo.set_ignore_words(ignore_words)
        assert seo.get_ignore_words() == ignore_words

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()