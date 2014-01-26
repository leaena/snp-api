from snpapi import app, scrape
from flask import jsonify, abort, make_response

@app.route('/')
def index():
  abort(404)

# gives all options for an rsid
@app.route('/snp/api/<rsid>', methods = ['GET'])
def get_snps(rsid):
  # get chromosome, position, trait options
  result = scrape.genotype(rsid)
  return jsonify( {'nan': '1'} )

# gives specific options for an rsid based on a persons basepair
@app.route('/snp/api/<rsid>/<bpair>', methods = ['GET'])
def get_trait(rsid, bpair):
  # get chromosome, position, trait
  pair = '(' + bpair[0] + ';' + bpair[1] + ')'
  result = scrape.snp(rsid, pair)
  return jsonify( result )

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'not found' } ), 404)