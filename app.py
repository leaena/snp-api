#!/usr/bin/python
from flask import Flask, jsonify, abort, make_response
from bs4 import BeautifulSoup

app = Flask(__name__)

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# gives all options for an rsid
@app.route('/')
def index():
  abort(404)
@app.route('/snp/api/<rsid>', methods = ['GET'])
def get_snps():
  # get chromosome, position, trait options
  return jsonify( { 'tasks': tasks } )

# gives specific options for an rsid based on a persons basepairf
@app.route('/snp/api/<rsid>/<bpair>', methods = ['GET'])
def get_trait(rsid, bpair):
    # get chromosome, position, trait
    soup = BeautifulSoup(html_doc)
    print(soup.prettify())
    pair = '(' + bpair[0] + ';' + bpair[1] + ')'
    return jsonify( { 'trait': pair , 'rsid': rsid} )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)