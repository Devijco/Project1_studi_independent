import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog

f = open('files/catalog.json')
data_json = json.load(f)

books = []
magazines = []
dvd = []
cd = []

for item in data_json:
    if item['source'] == 'book':
        books.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                issbn=item['issbn'],
                authors=item['authors'],
                dds_number=item['dds_number']
            )
        )
    elif item['source'] == 'magazine':
        magazines.append(
            Magazine(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                volume=item['volume'],
                issue=item['issue'],
            )
        )
    elif item['source'] == 'dvd':
        dvd.append(
            Dvd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                actors=['actors'],
                directors=['directors'],
                genre=['genre']
            )
        )
    elif item['source'] == 'cd':
        cd.append(
            Cd(
                title=item['title'],
                subject=item['subject'],
                upc=item['upc'],
                artist=['artist'],
            )
        )

catalog_all = [books, magazines, dvd, cd]
input_search = 'test'
result = Catalog(catalog_all).search(input_search)

for index, result in enumerate(result):
    print(f'result ke {index+1} | {result}')
