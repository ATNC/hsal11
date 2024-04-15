import argparse
from elasticsearch import Elasticsearch

ALLOW_TYPOS = 3
LONG_WORD_LENGTH = 7


def get_minimum_should_match(word: str) -> str:
    minimum_should_match = 100
    if len(word) >= LONG_WORD_LENGTH:
        minimum_should_match = int(
            (len(word) - ALLOW_TYPOS) / len(word) * 100
        )

    return f'{minimum_should_match}%'


def get_query(word: str) -> dict:
    minimum_should_match = get_minimum_should_match(word)
    base_match = {
        'word.short': {
            'query': word,
            'fuzziness': 'AUTO',
            'minimum_should_match': minimum_should_match
        }
    }
    if len(word) >= LONG_WORD_LENGTH:
        base_match = {
            'word.long': {
                'query': word,
                'minimum_should_match': minimum_should_match
            }
        }
    query = {
        '_source': ['word'],
        'query': {
            'bool': {
                'should': [
                    {
                        'match': base_match
                    }
                ],
                'minimum_should_match': 1
            }
        }
    }
    print(query)
    return query


def search_word(es, index, word):
    query = get_query(word)

    # Execute the search
    response = es.search(index=index, body=query)
    return response['hits']['hits']


def main():
    parser = argparse.ArgumentParser(description='Index the contents of a file into Elasticsearch for autocomplete.')
    parser.add_argument('word', type=str, help='The word to search for.')
    parser.add_argument('--host', type=str, default='localhost', help='Elasticsearch host')
    parser.add_argument('--port', type=int, default=9200, help='Elasticsearch port')
    parser.add_argument('--index', type=str, default='autocomplete', help='Name of the Elasticsearch index')

    args = parser.parse_args()

    es = Elasticsearch(
        [{'host': args.host, 'port': args.port, 'scheme': 'http'}],
    )

    words = search_word(es, args.index, args.word)
    for word in words:
        print(word['_source']['word'])


if __name__ == '__main__':
    main()
