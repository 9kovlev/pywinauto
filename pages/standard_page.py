from pywinauto import Application

from pages.base_page import BasePage


class StandardPage(BasePage):

    def amount_numbers(self, num1, num2) -> int:
        self.click_number(num1)
        self.click_plus()
        self.set_numbers(num2)
        self.click_equal()
        return self.get_result()
