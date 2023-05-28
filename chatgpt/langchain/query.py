import requests
import os

endpoint_url = "http://localhost:8000"
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
queries = [
    {'query': "What is the LLMChain in LangChain?"},
    {'query': "How do I use Pinecone in LangChain?"},
    {'query': "What is the difference between Knowledge Graph memory and buffer memory for "+
     "conversational memory?"}
]

res = requests.post(
    f"{endpoint_url}/query",
    headers=headers,
    json={
        'queries': queries
    }
)
print(res)

for query_result in res.json()['results']:
    query = query_result['query']
    answers = []
    scores = []
    for result in query_result['results']:
        answers.append(result['text'])
        scores.append(round(result['score'], 2))
    print("-"*70+"\n"+query+"\n\n"+"\n".join([f"{s}: {a}" for a, s in zip(answers, scores)])+"\n"+"-"*70+"\n\n")