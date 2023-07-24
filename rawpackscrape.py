from bs4 import BeautifulSoup
import cloudscraper

scraper = cloudscraper.create_scraper()
output_file = open('rawpacklist.txt', 'w')

with open('raw.txt') as f:
    for line in f:
        packLink = line.strip()
        url = packLink
        payload = {}
    
        response = scraper.get(packLink)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', {'class': 'AssemblyLink AssemblyLink--medium AssemblyLink--title'})
        for link in links:
            href = link.get('href')
            output_file.write(href + '\n')
            print(href)