import os
from datasets import load_dataset
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

import requests
from requests.adapters import HTTPAdapter, Retry
from tqdm.auto import tqdm

batch_size = 100
endpoint_url = "http://localhost:8000"
s = requests.Session()

documents = load_dataset('jamescalam/langchain-docs', split='train')

def get_docs(documents):
    documents = [{
        'id': doc['id'],
        'text': doc['text'],
        'metadata': {'url': doc['source']}
    } for doc in documents]

    return documents

# we setup a retry strategy to retry on 5xx errors
retries = Retry(
    total=5,  # number of retries before raising error
    backoff_factor=0.1,
    status_forcelist=[500, 502, 503, 504]
)
s.mount('http://', HTTPAdapter(max_retries=retries))
documents = get_docs(documents)
for i in tqdm(range(0, len(documents), batch_size)):
    i_end = min(len(documents), i+batch_size)
    # make post request that allows up to 5 retries
    res = s.post(
        f"{endpoint_url}/upsert",
        headers=headers,
        json={
            "documents": documents[i:i_end]
        }
    )