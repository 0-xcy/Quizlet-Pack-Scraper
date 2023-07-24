# Quizlet Pack Link & Pack Scraper
> Scrape over 850 packs/min

Requirements: 
- Mitm Proxy (Mobile)
- Quizlet App
- Quizlet Account

------------------
**Pack Link Scraping:** 

1. Go to Quizlet.com on **Incognito** and navigate to a Subject directory.
2. Load the raw subject pack listings as follows: ```https://quizlet.com/subjects/arts-and-humanities-flashcards-f567c560-t01?page=1```
3. Multiple pages can be loaded on each line with differing pages: ```page=1, page=2, page=3```
4. Run the ```rawpackscrape.py``` file and find the generated links in the ```rawpacklist.txt``` file.
5. Transfer the list of generated links to the ```packlist.txt``` file and continue below. 

------------------
**Pack Data Scraping:** 
1. Download the Repo and in the local directory, run ```pip install -r requirements.txt```
2. Start Mitm Proxy and log into the Quizlet on IOS/Android
3. Load a random Quizlet Pack and wait for a ```GET``` request to the link: ```https://api.quizlet.com/3.9/```
4. Copy the ```__cf_bm=``` Token value and paste it in ```line 7``` of the ```scrape.py``` file.
5. Copy the ```authorization``` Token value (Should be formatted as: Bearer ABC123) and paste it in ```Line 6``` of the ```scrape.py``` file.
6. Load ```packlist.txt``` with the generated link list from ```rawpackscrape.txt``` (if you haven't already done so)
7. Run ```scrape.py```
8. Files should output to ```/scrapedpacks``` directory in JSON format
```````````````````
This is for educational purposes only. Abuse of this tool is not prohibited. 
