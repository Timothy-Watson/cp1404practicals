"""
CP1404 Practical
Using the wikipedia API
"""
from wikipedia import page
from wikipedia import DisambiguationError
from wikipedia import PageError


def main():
    title = input("Enter page title: ")
    while title != "":
        try:
            wiki_page = page(title, auto_suggest=False)
            print(wiki_page.title)
            print(wiki_page.summary)
            print(wiki_page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')
        title = input("Enter page title: ")
    print("Thank you.")


main()
