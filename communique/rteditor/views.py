from django.shortcuts import render
import re

def view(request):
    return render(request, 'view.html')

def index(request):
    try:
        with open('index.html', 'r') as file:
            html_content = file.read()
        return render(request, 'index.html', {'title': re.search(r'<h1>(.*?)<\/h1>', html_content).group(1), 'content': re.search(r'<p>(.*?)<\/p>', html_content).group(1)})
    except:
        return render(request, 'index.html')

def update(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        with open('index.html', 'r') as file:
            html_content = file.read()
        html_content = re.sub(r'<h1>(.*?)<\/h1>', f'<h1>{title}</h1>', html_content)
        html_content = re.sub(r'<p>(.*?)<\/p>', f'<p>{content}</p>', html_content)
        with open('index.html', 'w') as file:
            file.write(html_content)
    return render(request, 'index.html', {'title': title, 'content': content}) 