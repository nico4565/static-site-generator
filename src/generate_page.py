import os
from extract_title import extract_title 
from markdown_to_html import markdown_to_html_node

def generate_page_recurs(dir_path_content, template_path, dest_dir_path, basepath):
    print(f'Generating pages recursuvely from {dir_path_content} to {dest_dir_path} using {template_path}')
    print(os.listdir(dir_path_content))
    for item in os.listdir(dir_path_content):
        origin_path = os.path.join(dir_path_content, item)

        if os.path.isfile(origin_path):
            dest_path = os.path.join(dest_dir_path, "index.html")
            generate_page(origin_path,template_path,dest_path, basepath)
        elif os.path.isdir(origin_path):
            dest_path = os.path.join(dest_dir_path, item)
            generate_page_recurs(origin_path,template_path,dest_path,basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown = ""
    template = ""
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    
    content_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}", content_html)
    
    template = template.replace("href=\"/",f"href=\"{basepath}")
    template = template.replace("src=\"/",f"src=\"{basepath}")
    
    dir_name = os.path.dirname(dest_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(dest_path, "w") as file:
        file.write(template)
    print(f'End')