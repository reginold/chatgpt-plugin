# App Quickstart
- 1. `cd /path/chatgpt-plugin`
- 2. `pip install poetry`
- 3. `conda create -n py310 python=3.10`
- 4. `conda activate py310`
- 5. `poetry env use python3.10`
- 6. `poetry install`
- 7. ```
      export DATASTORE=pinecone
      export BEARER_TOKEN=
      export OPENAI_API_KEY=
      export PINECONE_API_KEY=
      export PINECONE_ENVIRONMENT=
      export PINECONE_INDEX=
      ```
- 8. Run the app with:
     `poetry run start`