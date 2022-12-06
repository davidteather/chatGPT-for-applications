from playwright.sync_api import sync_playwright, Page
import os
import json

'''
    This class is used to interact with chatGPT on the website
'''
class chatGPT:
    '''
        Constructor for the chatGPT class
    '''
    def __init__(self, p, browser):
        self.p = p
        self.browser = browser
        self.start_chat()

    def start_chat(self):
        self.chat_page: Page = self.browser.new_page()
        self.first_prompt = True

        # Attempt to load cookies from cookies.json into page
        if os.path.exists("cookies.json"):
            with open("cookies.json", "r") as f:
                cookies = json.load(f)
                self.chat_page.context.add_cookies(cookies['cookies'])

        self.chat_page.goto("https://chat.openai.com/chat")

        # If the url is not the chat page, then the user is not logged in
        if self.chat_page.url == "https://chat.openai.com/auth/login":
            input("Please log in to chatGPT and press enter to continue")
            # Save the cookies to a file to use later
            cookies = self.chat_page.context.cookies()
            with open("cookies.json", "w+") as f:
                # Dump json to the file
                json.dump({"cookies": cookies}, f)

        # Click past the introduction
        for i in range(2):
            # Click button that says next in innerText
            self.chat_page.click("text=Next")
        self.chat_page.click("text=Done")
            

    def send_prompts(self, prompts: list):
        # Send each prompt to the chatGPT chat
        for prompt in prompts:
            # Type into a textarea element
            self.chat_page.fill("textarea", prompt)

            if not self.first_prompt:
                self.chat_page.wait_for_selector(self.btn_selector, timeout=300000)
            
            # TODO: Probably can just hit enter on the textarea, but still need a way to detect when the chat is done
            btn_selector_1 = "#__next > div > div.flex.flex-1.flex-col.md\:pl-52.h-full > main > div.Thread__PositionForm-sc-15plnpr-3.kWvvEa > form > div > div.PromptTextarea__LastItemActions-sc-4snkpf-3.gRmLdg > button"
            btn = self.chat_page.query_selector(btn_selector_1)
            self.btn_selector = btn_selector_1
            if btn is None:
                btn_selector_2 = "#__next > div > div.flex.flex-1.flex-col.md\:pl-52.h-full > main > div.sc-15plnpr-3.jqdtxi > form > div > div.sc-4snkpf-0.iLrIMi > button"
                btn = self.chat_page.query_selector(btn_selector_2)
                self.btn_selector = btn_selector_2

            btn.click()

            self.first_prompt = False

    def wait_for_chat_close(self):
        input("Hit enter to close the browser")
        self.chat_page.close()