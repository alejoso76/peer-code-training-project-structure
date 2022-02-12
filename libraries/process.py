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
            'download.prompt_for_download': False
        }
        # Blank browser
        browser.open_available_browser(preferences=prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()
        mundialitis = Mundialitis(browser, credentials['Mundialitis'])
        mundialitis.login()

    def start(self):
        log_message("Macro Step 1")
        log_message("Macro Step 2")
        log_message("Macro Step 3")

    def finish(self):
        capture_page_screenshot(OUTPUT_FOLDER, 'Mundialitis_Login')
        log_message("DW Process Finished")
        # Good practice: close browser manually
        browser.close_browser()