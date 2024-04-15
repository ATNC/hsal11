# Project Title

This project is a Python-based Elasticsearch autocomplete system. It includes scripts for creating an Elasticsearch index, indexing a file's contents into Elasticsearch, and searching for a word in the indexed data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- pip
- Elasticsearch

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages using pip:

```shell
pip install -r requirements.txt
```

## Usage

### Creating an Elasticsearch Index

You can create an Elasticsearch index using the `create_autocomplete_index.py` script. The script takes the following arguments:

- `--host`: Elasticsearch host (default is 'localhost')
- `--port`: Elasticsearch port (default is 9200)
- `--index`: Index name (default is 'autocomplete')

```shell
python app/create_autocomplete_index.py --host localhost --port 9200 --index autocomplete
```

### Indexing a File's Contents into Elasticsearch

You can index a file's contents into Elasticsearch using the `index_file_to_es.py` script. The script takes the following arguments:

- `--host`: Elasticsearch host (default is 'localhost')
- `--port`: Elasticsearch port (default is 9200)
- `--index`: Name of the Elasticsearch index (default is 'autocomplete')
- `file_path`: Path to the file to index

```shell
python app/index_file_to_es.py --host localhost --port 9200 --index autocomplete file_path
```

### Searching for a Word in the Indexed Data

You can search for a word in the indexed data using the `search.py` script. The script takes the following arguments:

- `word`: The word to search for
- `--host`: Elasticsearch host (default is 'localhost')
- `--port`: Elasticsearch port (default is 9200)
- `--index`: Name of the Elasticsearch index (default is 'autocomplete')

```shell
python app/search.py word --host localhost --port 9200 --index autocomplete
```
