import requests
from bs4 import BeautifulSoup
import os

def scrape_adobe_stock_prompts(search_terms, max_prompts, aspect_ratio):
    url = f'https://stock.adobe.com/search?k={search_terms}'  # Adjust this to the actual URL with search terms
    print(f"Scraping URL: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    prompts = []
    # Select the meta tags with itemprop="name"
    for item in soup.select('meta[itemprop="name"]'):
        prompt = item.get('content', '').strip()
        if prompt:
            prompt += f" --ar {aspect_ratio}"  # Append aspect ratio to the prompt
            prompts.append(prompt)
        if len(prompts) >= int(max_prompts):
            break

    print(f"Scraped {len(prompts)} prompts")
    return prompts

def save_prompts_to_file(prompts):
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, 'prompt.txt')

    with open(file_path, 'w') as file:
        for prompt in prompts:
            file.write(f"{prompt}\n")

    print(f"Saved prompts to {file_path}")
