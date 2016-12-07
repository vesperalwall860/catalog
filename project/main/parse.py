import urllib2
import bs4
from bs4 import BeautifulSoup

url = 'http://modelistam.com.ua/mulitikoptery/professionalinye-c-765/?page' + \
      '=2&sort=products_sort_order'

response = urllib2.urlopen(url)
html = response.read()

soup = BeautifulSoup(html, 'lxml')

products = []

goods_table = soup.find(id="spisok_tovarov")
goods_trs = goods_table.find_all('tr')

# remove the table header
del goods_trs[0]

for tr in goods_trs:
    tds = tr.find_all('td')

    url = tds[0].find('a').get('href')
    img = tds[0].find('img').get('src')
    name = tds[1].find('a').string

    price_divs = tds[2].find_all('div')

    # delete extra block
    del price_divs[-1]

    for div in price_divs:
        div_id = div.get('id')
        if div_id == 'productSpecialPrice' or div_id == 'productprice':
            price = div.find('span').string

    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    description = soup.find(id="ins2")
    uls = description.find_all('ul')

    chars = {
        'title': [],
        'ul': []
    }

    for ul in uls:
        p = ul.previous_sibling

        if p:
            while not isinstance(p, bs4.Tag):
                p = p.previous_sibling

            if p.name != 'p':
                break

            if p.string:
                if p.find('strong'):
                    chars['title'].append(p.find('strong').string)
                else:
                    chars['title'].append(p.string)

                chars['ul'].append(ul)

    imgs = []

    product_id = soup.find("input", {"name": "products_id"}).get("value")
    url = 'http://modelistam.com.ua/gallery.php?products_id=' + product_id

    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')

    content = soup.find(id="content")

    links = content.find_all('a')

    for link in links:
        imgs.append(link.get('href'))

    product = {
        'url': url,
        'name': name,
        'price': price,
        'chars': chars,
        'imgs': imgs,
    }

    products.append(product)

    print(product)