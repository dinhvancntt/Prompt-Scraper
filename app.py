import os
import socket
import webbrowser
from flask import Flask, render_template, request
from scraper import scrape_adobe_stock_prompts, save_prompts_to_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    max_prompts = request.form.get('max_prompts')
    search_terms = request.form.get('search_terms')
    url = request.form.get('url')  # Get the URL from the form
    aspect_ratio = request.form.get('aspect_ratio', '16:9')  # Default to 16:9 if not provided
    prompts = scrape_adobe_stock_prompts(search_terms, max_prompts, aspect_ratio, url)
    save_prompts_to_file(prompts)
    return render_template('index.html', prompts=prompts)

def find_free_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

if __name__ == '__main__':
    port = find_free_port()
    url = f"http://127.0.0.1:{port}"
    webbrowser.open(url)
    app.run(port=port, debug=True)

