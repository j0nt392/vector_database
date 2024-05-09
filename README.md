# Vector database for querying code-files and structures.

2024-05-09
- Query vectorspace with code or/and queries, receive code and metadata (linenumber, filepath).
- Persist the database with pickle
- Summarize a chosen file
- Walk through a repository and create embeddings out of the code using AST. The AST extracts Classes, Func, and Expressions.

Classes:
VectorDatabase, adds embeddings, searches in the database, as well as saves and loads persistent data. 
Embeddings creates the embeddings used both for querying and adding new embeddings using davinci-002.
CodeSummarizer uses gpt3.5 to read files and summarize them. 
Utils contains the AST_parser, it analyzes code and extracts classes functions and expressions. 
CLI is the commandline interface which implements all of the above to be used from the terminal. 

So far using only OpenAI API-calls with davinci-002 for encoding embeddings and a test_repository with a small codefile. 
