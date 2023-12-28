import time

from pages.standard_page import StandardPage


def test_amount_simple_numbers(app):
    standard_page = StandardPage(app)
    result = standard_page.amount_numbers(5, 155)
    assert result == 160, "Opps"


def test_change_theme(app):
    standard_page = StandardPage(app)
    standard_page.open_menu()
    time.sleep(3)
    setting_page = standard_page.open_page('settings')
    time.sleep(3)
    selected_state = setting_page.change_themes('system')
    time.sleep(3)
    setting_page.click_back_button()
    assert selected_state == 1, "Opps, settings was not applied!"
