import subprocess

from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/v1.0/reviews',methods=['GET'])
def hello_world():
    spider_name = "review"
    
    if "output.json" in os.listdir('.'):
        os.remove('output.json')

    if 'page' in request.args:
        page = request.args['page']
    if 'url' in request.args:
        url = request.args['url']
    subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "output.json","-a","page={}".format(page),"-a","url={}".format(url)])
    with open("output.json","r+") as items_file:
        return items_file.read()

if __name__ == '__main__':
    app.run(debug=True)