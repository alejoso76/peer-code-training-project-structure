from libraries.common import log_message, capture_page_screenshot, browser
from config import OUTPUT_FOLDER
from libraries.mundialitis.mundialitis import Mundialitis


class Process:
    def __init__(self, credentials: dict):
        log_message("Initialization")
        # Login, download files to start proccess, conect to google drive, mail, etc
        # * Customize browser
        prefs = {
            'profile.default_content_setting_values.notifications': 2,
            # Browser popups
            'profile.default_content_settings.popups': 0,
            # Upgrades default download directory to the one that is set after
            'directory_upgrade': True,
            'download.default_directory': OUTPUT_FOLDER,

            # For pdf tab and prompt to save or open file
            'plugins.always_opens_pdf_externally': True,
            'download.prompt_for_download': False,
            # "chrome.prefs": {
            #     'Chromedriver.required_version': '97.0.4692.71'
            # }
        }
        # Blank browser
        # chrome esta molestando
        browser.open_available_browser(
            preferences=prefs, browser_selection=['firefox'])

        # browser.open_available_browser(
        #     preferences=prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()
        mundialitis = Mundialitis(browser, credentials['Mundialitis'])
        mundialitis.login()
        self.mundialitis = mundialitis

    def start(self):
        log_message("Start - Create New Lobby")
        self.mundialitis.create_lobby()
        log_message("Finish - Create New Lobby")

        log_message("Start - Register New User")
        self.mundialitis.register_new_user()
        log_message("Finish - Register New User")

        log_message("Start - Join Lobby")
        self.mundialitis.join_lobby('user')
        log_message("Finish - Join Lobby")

        log_message("Start - Login with first user")
        self.mundialitis.login()
        log_message("Finish - Login with first user")

        log_message("Start - Join Lobby with first user")
        self.mundialitis.join_lobby('creator')
        log_message("Finish - Join Lobby with first user")

        log_message("Start - Start game with first user")
        self.mundialitis.start_game()
        log_message("Finish - Start game with first user")

        log_message("Start - Play game with first user")
        self.mundialitis.play_game()
        log_message("Finish - Play game with first user")

    def finish(self):
        log_message("DW Process Finished")
        # Good practice: close browser manually
        browser.close_browser()
