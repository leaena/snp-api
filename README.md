#SNP-API
###The only SNPedia wrapper you'll ever need
###(maybe, if you needed one to begin with)
#####(I like to call it snip-appy, btw)
This little program will cure all that ails you. Or at least allow you to be an awesome armchair geneticist! What started out as a way to scrape information from [SNPedia.com](http://snpedia.com/) for a client project turned into a side hobby of trying to see how much information I could pull using a handrolled API.

The little server is written in Python/[Flask](http://flask.pocoo.org/) and it makes extensive use of the beautiful (and aptly named) [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) web scraper. Each specified endpoint returns a JSON object. More endpoints may be added in the future, this is very much a work in progress.

##Installation:
Clone the repository, create a virtual environment in the directory, and start using it:
```
git clone git@github.com:leaena/snp-api.git
cd snpedia-api
virtualenv venv --distribute
source venv/bin/activate
```

Then, install the required packages:
```
pip install -r requirements.txt
```

You're good to go. Start it with:
```
gunicorn server:app
```

##Getting Started:

Everything you know to use SNP-API (it's pretty straight-forward there are only two endpoints currently).

To get info on an RSID from the web version use /snp/api/{rsid}:
```
curl -i http:/127.0.0.1:5000/snp/api/rs15793179
```
The response:
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 107
Server: Werkzeug/0.9.4 Python/2.7.5
Date: Sun, 26 Jan 2014 21:40:50 GMT

{
  "chromosome": "6",
  "position": "20347038",
  "rsid": "rs15793179",
  "trait": "A non-human snp."
}
```

And for a specific base pair with and rsid use /snp/api/{rsid}/{basepair}:
```
curl -i http://127.0.0.1:5000/snp/api/rs15793179/AA
```
The response:
```
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 132
Server: Werkzeug/0.9.4 Python/2.7.5
Date: Sun, 26 Jan 2014 22:28:18 GMT

{
  "chromosome": "6",
  "genotype": "AA",
  "position": "20347038",
  "rsid": "rs15793179",
  "trait": "normal, for chickens"
}
```

_As an aside, capitalization doesn't matter!_

##TODOS:

* More elegant way of handling general errors.
* Find a way to notify if the specific base pair doesn't have an SNPedia entry yet.
* Include more query types?
  * Include a search wrapper to find rsids by trait?
* Hookup directly to 23andme API?
* Heroku deploy? is that necessary?
