from playwright.sync_api import sync_playwright, Page, Playwright, Browser
from bs4 import BeautifulSoup
from chatGPT import chatGPT

def get_page_contents(browser: Browser, url: str) -> Page:
    # TODO: Handle PDFs, LinkedIn, and sites with better web scraping protection
    page = browser.new_page()
    page.goto(url)
    # Wait for page to load
    page.wait_for_function('document.readyState === "complete"')
    soup = BeautifulSoup(page.content(), "html.parser") # TODO: Get rid of some of the bad spacing that results
    page.close()
    return soup.get_text().replace("\\n", " ").strip()

if __name__ == "__main__":
    # Load each row from my_links.txt into a list
    with open("my_links.txt", "r") as f:
        links = f.readlines()
    
    # Ask the user for a list of URLs and store them
    if "TEMPLATE" not in links and len(links) == 0:
        links = []
        links.append(input("Enter your full name: "))
        links.extend(input("Enter a list of your professional URLs (put a space between each link): ").split())
        
        # Write the URLs to my_links.txt
        with open("my_links.txt", "w+") as f:
            for url in links:
                f.write(url)

    # Start playwright and open a browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        gpt = chatGPT(p, browser)

        prompts = []
        for i, link in enumerate(links):
            if i == 0:
                prompts.append(f"My name is {link}")
            else:
                # Make a request to the URL and get the HTML
                # Parse the HTML in BeautifulSoup and extract
                # the human readable content on the page
                # Add the content to the prompts list
                page_contents = get_page_contents(browser, link)
                prompts.append(page_contents)

        # Send the prompts to gpt
        gpt.send_prompts(prompts)

        # Prompt user to close browser
        gpt.wait_for_chat_close()

        browser.close()

