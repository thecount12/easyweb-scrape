easyweb-scrape
==============

Web Scraping for Email and other contact information

Requires BeautifulSoup

----

Web scraping is a messy science. Most people stay clear from it for the 
following reasons. 

1. Websites constantly change. 
2. Every website is essentially different
3. Not standards. Wouldn't it be nice if the standard for contact was in XML
4. Degradation of DOM.
5. Flash driven sites
6. contact info embedded in images or other media
7. extracting name and email: nearly impossible
  * Names most often don't follow an email tag
  * Not on the same line or same couple of lines
  * Hard to distinguish example (dolphin, razor, Peter) words or names

----

This script is designed to scrape a list of urls: 
```
http://foo.com
http://bar.com 
http://hop.com
etc...
```
1. Build an array of all urls from a domain 
2. Stay within the domain name
3. Search for email addresses

 
