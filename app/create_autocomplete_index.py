import argparse
from elasticsearch import Elasticsearch, exceptions


def create_autocomplete_index(es_instance, index_name):
    settings = {
        'settings': {
            'analysis': {
                'analyzer': {
                    'short_analyzer': {
                        'type': 'custom',
                        'tokenizer': 'standard',
                        'filter': [
                            'lowercase',
                            'stop',
                            'short_edge_ngram_filter'
                        ]
                    },
                    'long_analyzer': {
                        'type': 'custom',
                        'tokenizer': 'standard',
                        'filter': [
                            'lowercase',
                            'stop',
                            'long_edge_ngram_filter'
                        ]
                    }
                },
                'filter': {
                    'short_edge_ngram_filter': {
                        'type': 'edge_ngram',
                        'min_gram': 2,
                        'max_gram': 5
                    },
                    'long_edge_ngram_filter': {
                        'type': 'edge_ngram',
                        'min_gram': 3,
                        'max_gram': 15
                    }
                }
            }
        },
        'mappings': {
            'properties': {
                'word': {
                    'type': 'text',
                    'fields': {
                        'short': {
                            'type': 'text',
                            'analyzer': 'short_analyzer'
                        },
                        'long': {
                            'type': 'text',
                            'analyzer': 'long_analyzer'
                        }
                    }
                }
            }
        }
    }

    try:
        es_instance.indices.create(index=index_name, body=settings)
        print(f'Index "{index_name}" created successfully.')
    except exceptions.RequestError as e:
        print(f'Error creating index: {e}')


def main():
    parser = argparse.ArgumentParser(description='Create Elasticsearch "autocomplete" index.')
    parser.add_argument('--host', type=str, default='localhost', help='Elasticsearch host')
    parser.add_argument('--port', type=int, default=9200, help='Elasticsearch port')
    parser.add_argument('--index', type=str, default='autocomplete', help='Index name')

    args = parser.parse_args()

    es = Elasticsearch(
        [{'host': args.host, 'port': args.port, 'scheme': 'http'}],
    )
    create_autocomplete_index(es, args.index)


if __name__ == '__main__':
    main()
