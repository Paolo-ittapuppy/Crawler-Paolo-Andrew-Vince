import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import tokenizer
import json

uniquePages = []
longestPage = tuple() #two tuple, first is page and second is length
wordCounts = dict()
icsSubDomains = []

jsonDict = {}
jsonDict["UPages"] = uniquePages
jsonDict["LPage"] = longestPage
jsonDict["wCount"] = wordCounts
jsonDict["sDomains"] = icsSubDomains

def storeData():
    uniquePages = list(set(uniquePages))
    data = open('data.json', 'w')
    json.dump(jsonDict, data)
    data.close

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content

    #error in page
    if resp.status != 200:
        return list()
    
    #too big
    if len(resp.raw_response.content) > 1_200_000:
        return list()
    
    #duplicate check, dupe url set

    #maybe more checks?

    webPage = BeautifulSoup(resp.raw_response.content, "html.parser")
    text = tokenizer.tokenize(webPage.text)
    freq = tokenizer.computeWordFrequencies(text)

    #too much repitition
    if len(freq.keys)/len(text) < .2:
        return list()

    #return a list of all urls 
    newUrls = []
    for url in webPage.findAll('a'):
        newUrls.append(url.get('href'))
    #maybe add deleting duplicates here?
    return newUrls



#returns true if the given url has a robot text file 
def RobotTXT_exist(url):
    return True

def readRobot(url):
    return

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if parsed.scheme not in set(["http", "https"]):
            return False
        
        if not re.match(r".*(.ics.uci.edu/|.ics.uci.edu/|.informatics.uci.edu/|.stat.uci.edu/|)", parsed.netloc):
            return False

        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
