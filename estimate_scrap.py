from bs4 import BeautifulSoup

# Replace 'your_html_code' with the HTML code you provided
your_html_code = """

"""

# Parse the HTML code
soup = BeautifulSoup(your_html_code, 'html.parser')

# Find all <p> elements containing the "Estimate" data
estimate_elements = soup.find_all('p', class_='text-dark')

# Iterate through the elements and extract the "Estimate" values
for estimate_p in estimate_elements:
    estimate_text = estimate_p.get_text()
    estimate_start = estimate_text.find('Estimate') + len('Estimate')
    estimate_end = estimate_text.find('Sold')
    estimate_value = estimate_text[estimate_start:estimate_end].strip()
    print(estimate_value)
