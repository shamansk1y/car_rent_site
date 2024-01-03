from fake_useragent import UserAgent
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

ua = UserAgent()
headers = {'User-Agent': ua.random}

service = Service()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=service, options=chrome_options)

page = 1
work = True
data = []

while work:
    main_url = f'https://concreteplayground.com/melbourne/bars?paged={page}'
    driver.get(main_url)
    time.sleep(3)
    html = driver.page_source
    if html:
        soup = BS(html, 'html.parser')
        next_page_link = soup.find('a', class_='next')
        main_div = soup.find('ul', 'items')
        li_list = main_div.find_all('li', 'item')

        for item in li_list:
            title_el = item.find('p', 'name')

            if title_el:
                title = title_el.find('a').text.strip()
                link = title_el.find('a')['href']

                driver.get(link)
                time.sleep(3)
                html = driver.page_source
                soup = BS(html, 'html.parser')

                main_div = soup.find('div', 'articletitlebox')
                section_content = main_div.find('section', 'article-details clearfix')
                next_div = section_content.find('div', 'section-content')
                if next_div:
                    address_parts = next_div.contents[0].rsplit(',', 1)
                    address = address_parts[0].strip()
                    suburb = next_div.find('a').text.strip()

                div_pub = soup.find('div', 'published')
                date = div_pub.find('span', 'created_at').text

                div_style = soup.find('li', 'infoitem')
                if div_style:
                    find_style_element = div_style.find('h3', class_='title')
                    if find_style_element and find_style_element.text == 'STYLE':
                        subinfo_items = div_style.find_all('li')
                        style = ', '.join([item.text.strip() for item in subinfo_items])
                    else:
                        style = ''
                else:
                    style = ''

                find_url = soup.find('section', class_='email places')
                if find_url:
                    url = find_url.find('a')['href']

                data.append({
                    'Title': title,
                    'Address': address,
                    'Suburb': suburb,
                    'Date': date,
                    'Style': style,
                    'URL': url
                })

        if next_page_link:
            print('Страница найдена')
            page += 1
        else:
            print('Страница не найдена')
            work = False

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('bars_data.xlsx', index=False)

driver.quit()
