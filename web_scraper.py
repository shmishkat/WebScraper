from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://bdnews24.com/sport/').text
soup = BeautifulSoup(source, 'lxml')
firstTitle = 0
#firstTitle checks the first headline beacuse the first headline is in h3 tag and rest of the headlines are in h2 tag.


csv_file = open('bdnews24-sports.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Description', 'Image Link'])

for article in soup.find_all('div', class_='text')[:10]:
    try:
        if firstTitle == 0:
            hline = article.h3.a.text
        else:
            hline = article.h2.a.text
        desc = article.p.span.text
        img = article.find('img')['src']
        firstTitle += 1
    except Exception as e:
        print("Not found")

    print('Headline :',hline)
    print('Description :',desc)
    print('Imagelink :',img)

    csv_writer.writerow([hline,desc,img])
csv_file.close()