# Date: Nov 22, 2019

from bs4 import BeautifulSoup
import requests
import csv
import re

def getBudget(link):
	url = f'https://www.imdb.com/{link}'
	budget_source = requests.get(url).text
	budget_soup = BeautifulSoup(budget_source, 'lxml')

	country = budget_soup.find('div', id= 'titleDetails').findNext('h4', text = 'Country:').findNext('a').text

	cw_gross = budget_soup.find('h3', text = 'Company Credits').find_previous('div').text
	cwg_pattern = re.compile(r'\d{1,3}\,?\d{0,3}\,?\d{0,3}\,?\d{0,3}')
	cwg_match = cwg_pattern.search(cw_gross).group()

	if budget_soup.find('h3', class_ = 'subheading', text = 'Box Office').findNext('div').h4.text == 'Budget:':
		pro_budget = budget_soup.find('h3', class_ = 'subheading', text = 'Box Office').findNext('div').text
		budget_pattern = re.compile(r'\d{0,3}\,\d{0,3}\,?\d{0,3}')
		budget_match = budget_pattern.search(pro_budget).group()
		return country, budget_match, cwg_match
	else:
		pro_budget = None
		return country, pro_budget, cwg_match

csv_file = open('imdb_top_250.csv', 'a')
csv_writer = csv.writer(csv_file, lineterminator = '\r')
csv_writer.writerow(['Title', 'Year', 'Director', 'Country', 'Genre', 'Runtime','Certificate', 'IMDb Rating', 'Metascore', 'Votes', 'Budget', 'Gross'])

for i in range (1, 250, 50):
	url = f'https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start={i}&ref_=adv_nxt'
	source = requests.get(url).text
	soup  = BeautifulSoup(source, 'lxml')

	for article in soup.find_all('div', class_ = 'lister-item-content'):
		try: 
			title = article.a.text
		except:
			title = None

		try:	
			year = article.find('span', class_ = 'lister-item-year').text[-5:-1]
		except:
			year = None
			
		try:
			runtime = article.p.find('span', class_ = 'runtime').text[:3]
		except:
			runtime = None

		try:
			certificate = article.find('p', class_ = 'text-muted').find('span', class_ = 'certificate').text
		except:
			certificate = None
		try: 
			genre = article.find('p', class_ = 'text-muted').find('span', class_ = 'genre').text
			genre = str(genre).strip()
		except:
			genre = None

		try:
			imdb_rating = article.find('div', class_ = 'ratings-bar').find('div', class_ = 'ratings-imdb-rating').strong.text
		except:
			imdb_rating = None

		try:	
			metascore = article.find('div', class_ = 'ratings-bar').find('div', class_ = 'ratings-metascore').span.text
		except:
			metascore = None

		try:
			director = article.find('p', class_ = '').a.text
		except:
			director = None

		try:
			votes = article.find('p', class_ = 'sort-num_votes-visible').find('span', {'name': 'nv'})['data-value']
		except:
			votes = None
		
		try:
			link = article.h3.a['href']
		except:
			link = None
		else:
			country, budget, gross = getBudget(link)
			
		csv_writer.writerow([title, year, director, country, genre, runtime, certificate, imdb_rating, metascore, votes, budget, gross])

csv_file.close()