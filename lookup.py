import argparse
import json
import sys
from urllib.request import Request, urlopen


class Lookup:

    def __init__(self, word):

        self.word = word

        self.free_dictionary_api_root = (
            "https://api.dictionaryapi.dev/api/v2/entries/en"
        )

        self.free_dictionary_api_word_url = (
            f"{self.free_dictionary_api_root}/{self.word}"
        )

    def get_word_data_from_free_dict(self, url):

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"
        }
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

    def print_all_definitions_from_free_dict(self, response):
        meanings = response[0]["meanings"]

        num_of_meanings = len(meanings)

        print(f"{self.word} has {num_of_meanings} different meanings")

        for meaning in meanings:

            part_of_speech = meaning["partOfSpeech"]
            num_definitions = len(meaning["definitions"])

            print(
                f"\n{self.word} has {num_definitions} definitions as a {part_of_speech}: "
            )

            definitions = meaning["definitions"]

            self.print_word_definitions_from_free_dict(definitions)

    def print_word_definitions_from_free_dict(self, definitions: list):
        for index, definition in enumerate(definitions):
            print(f"{index + 1}. {definition['definition']}")

            try:
                print(f"example usage: {definition['example']}")
            except KeyError:
                pass

    def print_main_definition_from_free_dict(self, response):
        """
        Just get first meaning in response
        """
        meaning = response[0]["meanings"][0]

        part_of_speech = meaning["partOfSpeech"]
        print(f"{self.word}: {part_of_speech}\n")

        definitions = meaning["definitions"]

        self.print_word_definitions_from_free_dict(definitions)


def set_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-q",
        "--quick",
        action="store_true",
        help="When passed only first meaning is printed.",
    )
    parser.add_argument(
        "-f",
        "--full",
        action="store_true",
        help="When passed the full definition for every possible meaning is printed out.",
    )
    parser.add_argument("-w", "--word", type=str, help="Pass the word to look up.")
    return parser


def main():
    parser = set_args()

    args = parser.parse_args()

    word = args.word

    if word is None:
        print("no word has been passed to look up, exiting program")
        parser.print_help()
        sys.exit(1)

    lookup = Lookup(word)

    response = lookup.get_word_data_from_free_dict(lookup.free_dictionary_api_word_url)

    if args.full:
        lookup.print_all_definitions_from_free_dict(response)
    else:
        lookup.print_main_definition_from_free_dict(response)


if __name__ == "__main__":
    main()
