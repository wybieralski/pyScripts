import bs4 as bs
import urllib.request
import csv
import re
import sys

def count_buttonz():
    """ Function counting how many buttons is given website containing """
    files_with_websites=sys.argv[1]
    counted_websites=sys.argv[2]
    with open (files_with_websites) as file:
        readfile=csv.reader(file)
        address=file.readlines()
        counter = 0
        addresses=[]
        for row in address:
            counter =0
            sauce = urllib.request.urlopen(row)
            soup = bs.BeautifulSoup(sauce,'lxml')
            for btn in soup.find_all('a',{'class' : 'btn'}):
                counter+=1
            for button_tag in soup.find_all('button'):
                counter+=1
            for button_tag in soup.find_all('input'):
                counter+=1
            addresses.append([row,counter])
        with open(counted_websites,'w',newline='') as f:
                fieldnames = ['address','number_of_buttons']
                fieldnameswriter = csv.DictWriter(f,fieldnames=fieldnames)
                writer = csv.writer(f)
                fieldnameswriter.writeheader()
                for address in addresses:
                    writer.writerow(address)
count_buttonz()