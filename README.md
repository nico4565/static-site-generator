# Static Site Generator 🚀


I built a Python-based static site generator that turns Markdown files into a fully functional HTML website. This project helped me understand how tools like Hugo, Jekyll, and Gatsby work under the hood—by building one from scratch!


**Features at a glance:**
- Convert Markdown content into HTML pages  
- Use a custom HTML template for styling  
- Copy static assets (CSS, images) automatically  
- Serve a fully functional site locally  


---


## Overview


This project takes Markdown content and transforms it into static HTML pages, ready to be served by any web server. The focus was on learning the fundamentals of parsing, templating, and generating a complete site with Python.


## Architecture



/content (Markdown files) ──┐                                                                                                                                                            
├──▶ SSG (Python) ──▶ /public (HTML files)                                                                                                                                               
template.html ──────────────┘



## How It Works


1. **Clean Build** – Clears the `/public` directory to ensure a fresh build  
2. **Copy Static Assets** – Moves images, CSS, and other static files to `/public`  
3. **Parse Markdown** – Reads each Markdown file from `/content`  
4. **Convert to HTML** – Transforms Markdown into HTML using a custom parsing pipeline:  
   - Splits content into blocks (paragraphs, headings, lists, etc.)  
   - Converts blocks into an `HTMLNode` tree structure  
   - Processes inline elements (bold, italic, links) via intermediate `TextNode` objects  
5. **Apply Template** – Injects generated HTML into `template.html`  
6. **Write Output** – Saves final HTML files to `/public`  


## Usage


```bash
# Generate the site
python src/main.py


# Serve locally
python -m http.server 8888 --directory public

Then open http://localhost:8888
 in your browser.

Project Structure
├── content/        # Markdown source files
├── public/         # Generated HTML output
├── src/            # Python source code
└── template.html   # HTML template

##What I Learned

- How to parse Markdown and convert it to structured HTML

- How to design a simple templating system in Python

- How static site generators work under the hood

- How to organize multi-file Python projects for clarity and scalability

This repository is a great starting point for anyone wanting to understand the mechanics of static site generation and practice Python in a real-world project.
