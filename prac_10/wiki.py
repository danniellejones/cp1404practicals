"""
CP1404 | Prac_10 | Dannielle Jones
Use wikipedia python API
Wiki Quick start guide URL: https://wikipedia.readthedocs.io/en/latest/quickstart.html
"""
import wikipedia
from wikipedia import DisambiguationError, PageError

search_phrase = input("Search phrase: ")
while search_phrase != "":
    # Search using search phrase
    wikipedia.search(search_phrase)
    # Print summary and get page
    try:
        summary = wikipedia.summary(search_phrase)
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary: \n{summary}")
        print(f"URL: {page.url}")
    except DisambiguationError as e:
        print("Page is disambiguation page")
        print(e.options)
    except PageError:
        print("Page does not exist")
    search_phrase = input("Search phrase: ")
