from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
assert opts.headless # без графического интерфейса.
browser = Firefox(options=opts)
browser.get('https//google.com')
