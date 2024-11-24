import json
from urllib.request import Request, urlopen


class Lookup:

    def __init__(self, word):

        self.free_dictionary_api_root = "https://api.dictionaryapi.dev/api/v2/entries/en"

        self.free_dictionary_api_word_url = f"{self.free_dictionary_api_root}/{word}"

    def get_word_data(self, url):

        headers = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"}
        request = Request(url, headers=headers)

        try:
            with urlopen(request, timeout=10) as response:
                body = response.read()
                word_data = json.loads(body)
        except Exception as err:
            print(f"error making request to {url}: {err}")
        finally:
            response.close()
        return word_data


def main():

    word = "happy"

    lookup = Lookup(word)

    json = lookup.get_word_data(lookup.free_dictionary_api_word_url)

    print(json)
    

if __name__ == "__main__":
    main()

