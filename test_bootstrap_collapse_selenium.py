from Collapse import Collapse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_collapsible_panel&stacked=h')
driver.switch_to.frame(driver.find_element_by_id('iframeResult'))
WebDriverWait(driver, 5).until(lambda s: s.find_element_by_class_name('panel').is_displayed())

container = Collapse.CollapsibleContainer(driver.find_element_by_class_name('panel'), By.TAG_NAME, "a", By.CLASS_NAME, "panel-collapse")
container.open_inner_container()
container.close_inner_container()
