import argparse
from elasticsearch import Elasticsearch, helpers


def index_file_contents(es_instance, index_name, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        actions = (
            {
                '_index': index_name,
                '_source': {
                    'word': line.strip(),
                }
            }
            for line in file if line.strip()
        )
        helpers.bulk(es_instance, actions)


def main():
    parser = argparse.ArgumentParser(description='Index the contents of a file into Elasticsearch for autocomplete.')
    parser.add_argument('--host', type=str, default='localhost', help='Elasticsearch host')
    parser.add_argument('--port', type=int, default=9200, help='Elasticsearch port')
    parser.add_argument('--index', type=str, default='autocomplete', help='Name of the Elasticsearch index')
    parser.add_argument('file_path', type=str, help='Path to the file to index')

    args = parser.parse_args()

    es = Elasticsearch(
        [{'host': args.host, 'port': args.port, 'scheme': 'http'}],
    )

    index_file_contents(es, args.index, args.file_path)
    print(f'File "{args.file_path}" indexed successfully into "{args.index}".')


if __name__ == '__main__':
    main()
