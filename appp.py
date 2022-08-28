from flask import Flask, jsonify, request, render_template
import db
from bson import ObjectId
import json
from urllib.parse import urlparse

app = Flask(__name__)

URL = {}

def urlchecker(url):
    if "http://" not in url:
        url = "http://" + url
    parsed = urlparse(url).netloc
    return parsed

def checker(url):
    keys = []
    values = []
    url = urlchecker(url)
    if 'www.' in url:
        url = url.replace('www.', '')
    #print(url)
    sourcedict = db.db.sources.find()
    
    for key in sourcedict[0]:
        keys.append(key)
    #print(keys)
    for value in sourcedict[0].values():
        values.append(value)
    #print(values)
    sourcedict = dict(zip(keys, values))
    #print(sourcedict)
    for key in sourcedict.keys():
        if key == url:
            return sourcedict[key]
        else:
            pass


@app.route('/test')
def my_form():
    return render_template('main.html')


@app.route('/test', methods=['POST'])
def my_form_post():
    global URL
    URL = request.form['text']
    data = checker(URL)
    return final_render(URL)

def final_render(url=URL):  #returns the final render
    info = checker(URL)
    title = info[0]
    score = info[1]
    description = info[2]
    return render_template('post_input.html',description=description, title=title, score=score)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
