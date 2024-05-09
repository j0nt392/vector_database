# Vector database for querying code-files and structures.

2024-05-09
- Query vectorspace with code or/and queries, receive code and metadata (linenumber, filepath).
- Persist the database with pickle
- Summarize a chosen file
- Walk through a repository and create embeddings out of the code using AST. The AST extracts Classes, Func, and Expressions. 

So far using only OpenAI API-calls with davinci-002 for encoding embeddings and a test_repository with a small codefile. 
