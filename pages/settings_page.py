from pages.base_page import BasePage


class SettingPage(BasePage):
    EXPANDER_THEME = "AppThemeExpander"
    LIGHT_THEME = "LightThemeRadioButton"
    DARK_THEME = "DarkThemeRadioButton"
    SYSTEM_THEME = "SystemThemeRadioButton"
    BACK_BUTTON = "BackButton"

    def change_themes(self, type_them):
        types = {"light": self.LIGHT_THEME,
                 "dark": self.DARK_THEME,
                 "system": self.SYSTEM_THEME}
        self.windows_app.child_window(auto_id=self.EXPANDER_THEME).click_input()
        self.windows_app.child_window(class_name="RadioButton", auto_id=types[type_them]).click()
        select_state = self.windows_app.child_window(class_name="RadioButton", auto_id=types[type_them]).is_selected()
        return select_state

    def click_back_button(self):
        self.windows_app.child_window(auto_id=self.BACK_BUTTON).click_input()
