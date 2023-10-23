from app import app
from flask import render_template
import redis
from datetime import datetime as dt

r = redis.StrictRedis(host='localhost', port=6379, db=1)

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
    if not r.exists('counter'):
        r.set('counter',0)
        r.expire('counter', 24*60*60 - dt.now().hour*60*60 - dt.now().minute*60 - dt.now().second)
    r.incr('counter',1)
    a = int(r.get('counter'))
    return f"Количество запросов = {a}\n" + f"Время до перезапуска в секундах {r.ttl('counter')}"

