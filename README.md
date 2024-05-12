# AI-codebuddy that helps review, critique and debug my repositories.

2024-05-12
- Query vectorspace with code or/and queries, receive code and metadata (linenumber, filepath).
- Persist the database with pickle
- Summarize a chosen file
- Walk through a repository and create embeddings out of the code using AST. The AST extracts Classes, Func, and Expressions.
- GPT-3.5-instruct for code_review, with choice to implement or reject changes, also commits changes to repository.

Classes:
- VectorDatabase, adds embeddings, searches in the database, as well as saves and loads persistent data.
- Embeddings creates the embeddings used both for querying and adding new embeddings using davinci-002. 
- CodeSummarizer uses gpt3.5 to read files and summarize them. 
- Utils contains the AST_parser, it analyzes code and extracts classes functions and expressions. 
- CLI is the commandline interface which implements all of the above to be used from the terminal.
- CodeReview handles changing code-files on optimization type (Readability, Refactoring, etc)

The ".index and .metadata" files are the persisted vector-indexes for the vector_database. 

