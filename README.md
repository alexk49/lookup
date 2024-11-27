# Lookup - Command Line Dictionary

Simple, portable command line Dictionary that uses standard library python to query the [Free Dictionary API](https://dictionaryapi.dev/). Results are printed out to the terminal.

## Usage

All examples assume the script is being used on in a Linux environment, and that the script has been marked as executable:

```
chmod +x lookup.py
```

Alternatively, depending on your preference or need, you can invoke python directly when running:

```
python lookup.py

python3 lookup.py
```

## Example usage

To get just the first definition back from a word run either:

```
./lookup.py -w [word-to-lookup]

./lookup.p --word [word-to-lookup]
```

For example, running:

```
./lookup.py -w happy
```

Will print out:

```
happy: noun

1. A happy event, thing, person, etc.
```

You can also get synonyms for your given word with the -syn switch:

```
./lookup.py -w happy -syn

./lookup.py -w happy -thesaurus

./lookup.py -w happy --synonyms
```

Will print out to the console:

```
happy: noun

1. A happy event, thing, person, etc.
synonyms: happify,cheerful,content,delighted,elated,exultant,glad,joyful,jubilant,merry,orgasmic,fortunate,lucky,propitious
```

If you want to get back the full record for the word, which includes different variations of usage and all synonyms then run either:

```
./lookup.py -w [word-to-lookup] -f

./lookup.py --word [word-to-lookup] --full
```

For example, running:

```
./lookup.py -w happy -f
```

Will print out the below:

```
happy has 4 different meanings

happy has 1 definitions as a noun:
1. A happy event, thing, person, etc.

happy has 1 definitions as a noun:
1. Preceded by the: happy people as a group.

happy has 2 definitions as a verb:
1. Often followed by up: to become happy; to brighten up, to cheer up.
2. Often followed by up: to make happy; to brighten, to cheer, to enliven.

happy has 6 definitions as a adjective:
1. Having a feeling arising from a consciousness of well-being or of enjoyment; enjoying good of any kind, such as comfort, peace, or tranquillity; blissful, contented, joyous.
example usage: Music makes me feel happy.
2. Experiencing the effect of favourable fortune; favored by fortune or luck; fortunate, lucky, propitious.
3. Content, satisfied (with or to do something); having no objection (to something).
example usage: Are you happy to pay me back by the end of the week?
4. (Of acts, speech, etc.) Appropriate, apt, felicitous.
example usage: a happy coincidence
5. (in combination) Favoring or inclined to use.
example usage: slaphappy, trigger-happy
6. (of people, often followed by "at" or "in") Dexterous, ready, skilful.
synonyms: happify,cheerful,content,delighted,elated,exultant,glad,joyful,jubilant,merry,orgasmic,fortunate,lucky,propitious
```

## Dataset

Lookup uses the excellent [Free Dictionary API](https://dictionaryapi.dev/), which uses [wikitionary](https://en.wiktionary.org) as its dataset.

## Todo

Set up to work with other datasets:

* Collins Dictionary API, which requires setting up an API Key- https://www.collinsdictionary.com/collins-api
Wordnet

* Wordnet - which can be used fully offline once dataset has been downloaded but likely would require more than standard library python to use - https://wordnet.princeton.edu/
