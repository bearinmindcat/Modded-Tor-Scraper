# Modded-Tor-Scraper

Took inspirtation from this (https://hoxframework.com.hr/?p=473) and (https://www.youtube.com/watch?v=tSovaXhkLzs&pp=ygUiaG93IHRvIHVzZSBmcmVzaG9uaW9ucyB0b3Igc2NyYXBlcg%3D%3D)

I really liked this project and added my own scripts to make it a lot more user friendly for myself, note you can easily edit the code yourself and make any additional changes if you want.

RUN IN ORDER

(RunScraper.py, ahmiascraper.py, TORsearcher.py)

RunScraper.py - just makes sure you have TOR vpn enabled (make sure to run tor.exe and ensure it's running in your taskbar)

ahimascraper.py - you can edit what search querys in here, in this I just have the word "credit card" appended but you can change to whatever you want the searches to cover ie "hacking", "database", "forums", etc

TORsearcher.py - I made changes to the general GUI inside of python IDLE so you can copy paste the file path of the onion sites you want to scrape, I added a script to generate a folder and put a seperate HTML & TXT file when you get tracebacks from the onion sites you visit, and I also added some code that will keep going through the list of onion sites even if you get an untraceable error from an onion link that is broken or isn't working anymore

Good luck and have fun learning!

