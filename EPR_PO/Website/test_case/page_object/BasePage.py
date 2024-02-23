class Page:
    def __init__(self, driver):
        self.baseurl = 'http://www.mobin.love:10001/#'
        self.driver = driver

    def open(self, url):
        url_ = self.baseurl + url
        print('test page is %s' % url_)
        self.driver.get(url_)
        assert self.driver.current_url == url_, 'did not land on %s' % url_

    def base_find_element(self, locator):
        return self.driver.find_element(*locator)

    def base_click(self, locator):
        self.base_find_element(locator).click()

    def base_input(self, locator, value):
        self.base_find_element(locator).send_keys(value)

    def base_clear(self, locator):
        self.base_find_element(locator).clear()
