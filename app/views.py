from app import app
from flask import render_template

v_count = 0 

# Приветсвеная старничка
@app.route('/')
def index():
    return "Hello, World!"

# Выдача файла с прошлой домашки
@app.route('/hw3')
def test():
    return render_template("Web.html")

# Счётчик
@app.route('/counter')
def counter():
    global v_count
    v_count += 1
    return f"Количество запросов = {v_count}"
