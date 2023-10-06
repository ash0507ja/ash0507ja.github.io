from flask import Flask
from flask import render_template, request,jsonify

import requests
import urllib
import os

# url = requests.get(r'https://raw.githubusercontent.com/mochidukiyukimi/yuki-youtube-instance/main/instance.txt').text.rstrip()
url = os.getenv('TRACER')

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/bbs')
def bbs():
  verify = request.args.get('verify')
  channel = request.args.get('channel')
  view = f'https://yuki-math-blog-xiv6.onrender.com/bbs/api?verify={verify}&channel={channel}&t=0'
  res = requests.get(view, cookies={"yuki": "True"}).text
  return res

@app.route('/send', methods=['POST'])
def send():
  name = request.form['name']
  seed = request.form['seed']
  message = request.form['message']
  channel = request.form['channel']
  post = f'https://yuki-math-blog-xiv6.onrender.com/bbs/result?channel={channel}&message={message}&name={name}&seed={seed}'
  requests.get(post, cookies={"yuki": "True"})
  return ''

@app.route('/use')
def use():
  return render_template('use.html')
  
# 404 - Not Found
@app.errorhandler(404)
def not_found(error):
  return render_template('error/404.html'), 404

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
