from bs4 import BeautifulSoup
import re

with open('vqvztaifwefiyncv.txt', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
final_text = soup.get_text()
final_text = ''.join(soup.findAll(text=True))
clean_text = re.sub("<[^>]*>\t\n", "", final_text)

print(final_text)