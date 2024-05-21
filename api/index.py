import os
import socket
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
    aspect_ratio = request.form.get('aspect_ratio', '16:9')  # Default to 16:9 if not provided
    prompts = scrape_adobe_stock_prompts(search_terms, max_prompts, aspect_ratio)
    save_prompts_to_file(prompts)
    return render_template('index.html', prompts=prompts)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)