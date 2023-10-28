from bs4 import BeautifulSoup

# Sample HTML code
html_code = '''

'''

# Parse the HTML code
soup = BeautifulSoup(html_code, 'html.parser')

# Find all <p> elements with class "text-dark"
p_elements = soup.find_all('p', class_='text-dark')

# Iterate through the <p> elements and extract the "sold" data or print 0 if not found
for p in p_elements:
    sold_tag = p.find('span', class_='sold')
    if sold_tag:
        sold_data = sold_tag.get_text()
    else:
        sold_data = "0"
    print(sold_data)
