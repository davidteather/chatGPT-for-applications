from playwright.sync_api import sync_playwright, Page
import os
import json
import time

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
            
        # Wait for the chat to load
        time.sleep(1)

    def send_prompts(self, prompts: list):
        # Send each prompt to the chatGPT chat
        for prompt in prompts:
            # Type into a textarea element and hit the enter key to submit
            self.chat_page.fill("textarea", prompt)

            # If a prompt is still processing we wait
            while self.chat_page.query_selector(".text-2xl"):
                pass
            self.chat_page.press("textarea", "Enter")

            self.first_prompt = False

    def wait_for_chat_close(self):
        input("Hit enter to close the browser")
        self.chat_page.close()