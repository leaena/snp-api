from bs4 import BeautifulSoup
import urllib

def getLocations(soup):
  """
  requires a base BeatifulSoup object(with url)
  quick and dirty function to find get the locations of all the table rows and their labels
  """
  results = []
  trows = soup('table')[1].find_all('th')
  if len(trows) < 2:
    return { 'error': 'RSID not found.' }
  for header in trows:
    cleanText = header.get_text().split('\n')[0].replace(u'\xa0', ' ')
    results.append(cleanText)
  print results
  return results

def getData(locations, soup):
  """
  requires the locations array from getLocations and a base BeatifulSoup object(with url)
  pull genotype info based on
  """
  chromeIndex = locations.index('On chromosome')
  positionIndex = locations.index('Chromosome position')
  if 'Summary' in locations:
    traitIndex = locations.index('Summary')
  else:
    traitIndex = locations.index('Trait')
  print traitIndex

  tvalues = soup('table')[1].find_all('td')
  chromosome = tvalues[chromeIndex].find_all('span')[0].get_text().split()[0]
  position = ''.join(tvalues[positionIndex].find_all('span')[0].get_text().split()[0].split(','))
  trait = tvalues[traitIndex].find_all('span')[0].get_text().split(u"\u00A0")[0]
  result = {
    'chromosome': chromosome,
    'position': position,
    'trait': trait
  }
  return result

def genotype(rsid):
  """
  requires an rsid string
  grabs information on an rsid, including location on the chromosome and general traits
  """
  if rsid[0] == 'I' or rsid[0] == 'i':
    return { 'error': 'Cannot find indicators, must use rs #s'}
  soup = BeautifulSoup(urllib.urlopen('http://snpedia.com/index.php/Special:Browse/' + rsid).read())
  trows = soup('table')[1].find_all('tr')
  if len(trows) < 2:
    return { 'error': 'That rsid does not have any data/does not exist.' }
  locations = getLocations(soup)
  genotypeData = getData(locations, soup)
  genotypeData['rsid'] = rsid
  return genotypeData

def snp(rsid, pair):
  """
  requires rsid and pair string
  grabs specific information for an snp with the supplied base pair
  """
  if rsid[0] == 'I' or rsid[0] == 'i':
    return { 'error': 'Cannot find indicators, must use rs #s'}
  formatPair = '(' + pair[0].upper() + ';' + pair[1].upper() + ')'
  soup = BeautifulSoup(urllib.urlopen('http://snpedia.com/index.php/Special:Browse/' + rsid + formatPair).read())
  trows = soup('table')[1].find_all('tr')
  print rsid + formatPair
  if len(trows) < 2:
    return { 'error': 'That base pair does not have a trait associated with it.' }
  locations = getLocations(soup)
  genotypeData = getData(locations, soup)
  genotypeData['rsid'] = rsid
  genotypeData['genotype'] = pair
  return genotypeData