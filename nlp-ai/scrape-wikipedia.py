import requests
from bs4 import BeautifulSoup
import re

def extract_text_from_wikipedia(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ''
    for paragraph in paragraphs:
        text += re.sub(r'\[\d+\]', '', paragraph.get_text())
    return text

def write_to_txt(article_urls, output_file):
    with open(output_file, mode='w', encoding='utf-8') as file:
        for url in article_urls:
            text = extract_text_from_wikipedia(url)
            file.write(f'{text}\n\n')

article_urls = [
    'https://en.wikipedia.org/wiki/Python_(programming_language)',
    'https://en.wikipedia.org/wiki/Artificial_intelligence',
    'https://en.wikipedia.org/wiki/Arsenal_F.C.',
    'https://en.wikipedia.org/wiki/Premier_League',
    'https://en.wikipedia.org/wiki/Thierry_Henry',
    'https://en.wikipedia.org/wiki/What_Happens_in_Vegas',
    'https://en.wikipedia.org/wiki/Boston_Legal',
    'https://en.wikipedia.org/wiki/Puma_(brand)',
    'https://en.wikipedia.org/wiki/Donald_Trump',
    'https://en.wikipedia.org/wiki/Michael_Jackson',
    'https://en.wikipedia.org/wiki/LangChain',
    'https://en.wikipedia.org/wiki/Big_Five_personality_traits',
    'https://en.wikipedia.org/wiki/Bruce_Springsteen',
    'https://en.wikipedia.org/wiki/Ferrari',
    'https://en.wikipedia.org/wiki/Toronto',
    'https://en.wikipedia.org/wiki/Eiffel_Tower',
    'https://en.wikipedia.org/wiki/Electricity',
    'https://en.wikipedia.org/wiki/The_Office_(American_TV_series)',
    'https://en.wikipedia.org/wiki/Canada',
    'https://en.wikipedia.org/wiki/United_States',
    'https://en.wikipedia.org/wiki/England',
    'https://en.wikipedia.org/wiki/Tree',
    'https://en.wikipedia.org/wiki/Vertical_farming',
    'https://en.wikipedia.org/wiki/Port_Perry',
    'https://en.wikipedia.org/wiki/James_Bond',
    'https://en.wikipedia.org/wiki/Max_Payne'
]
output_file = 'wikipedia_articles.txt'
write_to_txt(article_urls, output_file)
