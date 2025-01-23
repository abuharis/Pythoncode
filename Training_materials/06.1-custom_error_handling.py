"""
In Python, you can create custom exception handlers by defining a new exception class that inherits from the built-in Exception class. 
Here's how you can create a custom exception called WebsiteNotFound and handle it properly.
"""

#Step 1: Define the Custom Exception
class WebsiteNotFound(Exception):
    """Custom exception for website not found errors."""
    def __init__(self, website_url, message="Website not found"):
        self.website_url = website_url
        self.message = f"{message}: {website_url}"
        super().__init__(self.message)


#Step 2: Use the Custom Exception in Your Code
def check_website(website_url):
    # Simulate website checking (in reality, you can make HTTP requests)
    known_websites = ["https://google.com", "https://github.com"]
    
    if website_url not in known_websites:
        raise WebsiteNotFound(website_url)

    return f"Website {website_url} is available."

#Step 3: Handle the Exception Gracefully
try:
    check_website("https://example.com")
except WebsiteNotFound as e:
    print(f"Handling Exception: {e}")


#Step 4: Raising the Exception Manually
def visit_website(url):
    if not url.startswith("https"):
        raise WebsiteNotFound(url, "Invalid URL format")

try:
    visit_website("http://unsecure-website.com")
except WebsiteNotFound as e:
    print(e)

