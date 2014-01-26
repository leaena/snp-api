from bs4 import BeautifulSoup
import urllib

def genotype(rsid):
  if rsid[0] == 'I' or rsid[0] == 'i':
    return { 'error': 'Cannot find indicators, must use rs #s'}
  soup = BeautifulSoup(urllib.urlopen('http://snpedia.com/index.php/Special:Browse/' + rsid).read())
  trows = soup('table')[1].find_all('th')
  if len(trows) < 2:
    return { 'error': 'RSID not found.' }
  for i in range(len(trows)):
    print trows[i].get_text()

def snp(pair, rsid):
  if rsid[0] == 'I' or rsid[0] == 'i':
    return { 'error': 'Cannot find indicators, must use rs #s'}
  soup = BeautifulSoup(urllib.urlopen('http://snpedia.com/index.php/Special:Browse/' + rsid + pair).read())
  trows = soup('table')[1].find_all('tr')
  if len(trows) < 2:
    return { 'error': 'That base pair does not have a trait associated with it.' }
  chromosome = trows[6].find_all('span')[0].get_text().split()[0]
  position = ''.join(trows[2].find_all('span')[0].get_text().split()[0].split(','))
  expression = trows[8].find_all('span')[0].get_text().split(u"\u00A0")[0]
  result = {
    'chromosome': chromosome,
    'position': position,
    'expression': expression,
    'rsid': rsid,
    'genotype': bpair
    }