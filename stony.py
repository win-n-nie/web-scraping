import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.stonybrook.edu/commcms/dining/locations/index.php')

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

loc_name = soup.find_all('p', class_="zigzagsnippetheading")
loc_name
output_loc_name = []
###make loop
for name in loc_name: ###var could be anything
    print(name.text)
    data = name.text
    data = data.strip()
    data
    data = data.replace('\n','')
    output_loc_name.append(data)
len(loc_name)

df = pd.DataFrame({'locations':loc_name})
df.to_csv('/Users/wendyarias/Documents/GitHub/web-scraping/data/locations.csv')