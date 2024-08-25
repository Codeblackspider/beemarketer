import sys
import requests
from bs4 import BeautifulSoup
import re
import validators
from PIL import Image
import io
import htmlmin
from urllib.parse import urljoin

# Define the title with blue and green gradient style
title = r"""
    ____               __  ___           __        __  _
   / __ )___  ___     /  |/  /___ ______/ /_____  / /_(_)___  ____ _
  / __  / _ \/ _ \   / /|_/ / __ `/ ___/ //_/ _ \/ __/ / __ \/ __ `/
 / /_/ /  __/  __/  / /  / / /_/ / /  / ,< /  __/ /_/ / / / / /_/ / 
/_____/\___/\___/  /_/  /_/\__,_/_/  /_/|_|\___/\__/_/_/ /_/\__, /  
                                                           /____/
"""

# Gradient colors for blue and green
def gradient_text(text, colors):
    gradient_colors = colors
    result = ""
    for i, char in enumerate(text):
        color = gradient_colors[i % len(gradient_colors)]
        result += f"\033[38;5;{color}m{char}\033[0m"
    return result

# Function to print the title with a blue and green gradient effect
def print_gradient_title_and_prompt():
    gradient_colors_title = ["21", "26", "30", "34", "36", "32"]  # Blue to Green gradient
    
    print(gradient_text(title, gradient_colors_title))
    print("\n\033[36mVisit our website: https://www.fontbees.store\033[0m")
    print("\033[33mWarning: This tool is for educational purposes only.\033[0m\n")
    print_options()

def print_options():
    green_color = "\033[38;5;76m"  # #43e701 (Green)
    orange_color = "\033[38;5;208m"  # #ff9002 (Orange)
    yellow_color = "\033[33m"  # Yellow color code
    purple_color = "\033[35m"  # Purple color code
    reset_color = "\033[0m"
    
    options = [
        "1. Keyword Density Analyzer",
        "2. Web Scraper for Competitor Analysis",
        "3. Simple Web Crawler for Link Analysis",
        "4. Content Generator (Basic)",
        "5. Email Validator",
        "6. Basic Web Traffic Estimator",
        "7. Website Screenshot Tool",
        "8. Simple Sitemap Generator",
        "9. Content Diff Checker",
        "10. On-Page SEO Checker",
        "11. Broken Link Checker",
        "12. HTML Minifier",
        "13. Basic Image Optimizer",
        "0. Exit"
    ]
    
    print(f"\033[33mSelect an option (0-13):\033[0m")
    for option in options:
        number, text = option.split('. ', 1)
        print(f"{orange_color}{number}{reset_color}. {green_color}{text}{reset_color}")

def main():
    while True:
        print_gradient_title_and_prompt()
        choice = input("\033[34mSelect an option (0-13): \033[0m").strip()

        if choice == '1':
            keyword_density_analyzer()
        elif choice == '2':
            web_scraper_competitor_analysis()
        elif choice == '3':
            simple_web_crawler()
        elif choice == '4':
            content_generator()
        elif choice == '5':
            email_validator()
        elif choice == '6':
            basic_web_traffic_estimator()
        elif choice == '7':
            website_screenshot_tool()
        elif choice == '8':
            simple_sitemap_generator()
        elif choice == '9':
            content_diff_checker()
        elif choice == '10':
            on_page_seo_checker()
        elif choice == '11':
            broken_link_checker()
        elif choice == '12':
            html_minifier()
        elif choice == '13':
            basic_image_optimizer()
        elif choice == '0':
            print("\033[35mExiting...\033[0m")
            sys.exit()
        else:
            print("\033[31mInvalid option. Please try again.\033[0m")

def back_to_menu():
    input("\033[38;5;76mPress Enter to return to the menu...\033[0m")

def keyword_density_analyzer():
    url = input("\033[34mEnter the URL to analyze: \033[0m")
    response = requests.get(url)
    text = BeautifulSoup(response.text, 'html.parser').get_text()
    
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    keyword_count = {}
    
    for word in words:
        if word not in keyword_count:
            keyword_count[word] = 1
        else:
            keyword_count[word] += 1
    
    print("\033[35mKeyword Density:\033[0m")
    for word, count in keyword_count.items():
        print(f"{word}: {count / word_count:.2%}")
    
    back_to_menu()

def web_scraper_competitor_analysis():
    url = input("\033[34mEnter the competitor's URL to scrape: \033[0m")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("\033[35mTitle:\033[0m", soup.title.string if soup.title else "No title")
    print("\033[35mMeta Description:\033[0m", soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else "No description")
    print("\033[35mHeadings:\033[0m")
    for heading in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        for tag in soup.find_all(heading):
            print(f"{heading}: {tag.get_text()}")
    
    back_to_menu()

def simple_web_crawler():
    url = input("\033[34mEnter the URL to crawl: \033[0m")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("\033[35mLinks found:\033[0m")
    for link in soup.find_all('a', href=True):
        print(urljoin(url, link['href']))
    
    back_to_menu()

def content_generator():
    prompt = input("\033[34mEnter a topic for content generation: \033[0m")
    print(f"\033[35mGenerated content for '{prompt}':\033[0m")
    # Placeholder for actual content generation logic
    print(f"Here is some content about {prompt}.")
    
    back_to_menu()

def email_validator():
    email = input("\033[34mEnter an email address to validate: \033[0m")
    if validators.email(email):
        print("\033[35mValid email address.\033[0m")
    else:
        print("\033[35mInvalid email address.\033[0m")
    
    back_to_menu()

def basic_web_traffic_estimator():
    print("\033[35mBasic web traffic estimator (stub).\033[0m")
    # Placeholder for actual web traffic estimation logic
    
    back_to_menu()

def website_screenshot_tool():
    print("\033[35mWebsite screenshot tool (stub).\033[0m")
    # Placeholder for screenshot functionality
    
    back_to_menu()

def simple_sitemap_generator():
    url = input("\033[34mEnter the URL to generate a sitemap: \033[0m")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("\033[35mSitemap URLs:\033[0m")
    for link in soup.find_all('a', href=True):
        print(urljoin(url, link['href']))
    
    back_to_menu()

def content_diff_checker():
    url1 = input("\033[34mEnter the first URL to compare: \033[0m")
    url2 = input("\033[34mEnter the second URL to compare: \033[0m")
    
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    
    if response1.text == response2.text:
        print("\033[35mContents are the same.\033[0m")
    else:
        print("\033[35mContents differ.\033[0m")
    
    back_to_menu()

def on_page_seo_checker():
    url = input("\033[34mEnter the URL for SEO analysis: \033[0m")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("\033[35mOn-Page SEO Analysis:\033[0m")
    print("\033[35mTitle:\033[0m", soup.title.string if soup.title else "No title")
    print("\033[35mMeta Description:\033[0m", soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else "No description")
    print("\033[35mMeta Keywords:\033[0m", soup.find('meta', {'name': 'keywords'})['content'] if soup.find('meta', {'name': 'keywords'}) else "No keywords")
    
    back_to_menu()

def broken_link_checker():
    url = input("\033[34mEnter the URL to check for broken links: \033[0m")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    broken_links = []
    for link in soup.find_all('a', href=True):
        link_url = urljoin(url, link['href'])
        try:
            resp = requests.head(link_url, allow_redirects=True)
            if resp.status_code != 200:
                broken_links.append(link_url)
        except requests.RequestException:
            broken_links.append(link_url)
    
    print("\033[35mBroken Links:\033[0m")
    for link in broken_links:
        print(link)
    
    back_to_menu()

def html_minifier():
    url = input("\033[34mEnter the URL of the HTML to minify: \033[0m")
    response = requests.get(url)
    minified_html = htmlmin.minify(response.text, remove_comments=True, remove_empty_space=True)
    
    with open("minified.html", "w") as file:
        file.write(minified_html)
    
    print("\033[35mMinified HTML saved to minified.html\033[0m")
    
    back_to_menu()

def basic_image_optimizer():
    url = input("\033[34mEnter the URL of the image to optimize: \033[0m")
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    
    optimized_image = io.BytesIO()
    image.save(optimized_image, format='JPEG', optimize=True, quality=85)
    
    with open("optimized_image.jpg", "wb") as file:
        file.write(optimized_image.getvalue())
    
    print("\033[35mOptimized image saved to optimized_image.jpg\033[0m")
    
    back_to_menu()

if __name__ == "__main__":
    main()
