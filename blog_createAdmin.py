import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_admin(self):
        user = "admin"
        pwd = "admin"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[1]/table/tbody/tr[2]/td[1]/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys("testadmin")
        elem = driver.find_element_by_id("id_password1")
        elem.send_keys("testpassword")
        elem = driver.find_element_by_id("id_password2")
        elem.send_keys("testpassword")
        elem = driver.find_element_by_xpath("//*[@id=\"user_form\"]/div/div/input[1]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"user_form\"]/div/div/input[1]").click()
        driver.get("http://127.0.0.1:8000/admin/auth/user/")
        assert "Created Admin"
        time.sleep(1)
        elem = driver.find_element_by_id("searchbar")
        elem.send_keys("testadmin")
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-search\"]/div/input[2]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"result_list\"]/tbody/tr/td[1]/input").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/label/select/option[2]").click()
        elem = driver.find_element_by_xpath("//*[@id=\"changelist-form\"]/div[1]/button").click()
        assert "Deleted Admin"
        elem = driver.find_element_by_xpath("//*[@id=\"content\"]/form/div/input[4]").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


