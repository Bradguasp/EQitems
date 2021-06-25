import urllib.request
from item import Item

def pullHtmlFromUrl(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()

    return mystr

def main ():
    itmestring = pullHtmlFromUrl("https://wiki.project1999.com/Special:ClassSlotEquip/Necromancer/Arms/AllItems")
    itmes = itmestring.split("<tr>")
    print(itmes[2])



main()