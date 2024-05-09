import ast
import os


class CodeExtractor:
    def __init__(self, repository_path):
        self.repository_path = repository_path

    def extract_code_blocks(self):
        code_blocks = []
        for root, dirs, files in os.walk(self.repository_path):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        content = f.read()
                        try:
                            tree = ast.parse(content)
                            for node in ast.walk(tree):
                                if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                                    # Extracting functions and classes with their line numbers
                                    code_segment = ast.unparse(node)
                                    code_blocks.append({
                                        'file_path': file_path,
                                        'code_segment': code_segment,
                                        'start_line': node.lineno,
                                        'end_line': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno,
                                        'type': type(node).__name__
                                    })
                                elif isinstance(node, ast.Expr) and hasattr(node, 'lineno'):
                                    # Handling top-level expressions
                                    code_segment = ast.get_source_segment(
                                        content, node)
                                    code_blocks.append({
                                        'file_path': file_path,
                                        'code_segment': code_segment,
                                        'start_line': node.lineno,
                                        'end_line': node.end_lineno if hasattr(node, 'end_lineno') else node.lineno,
                                        'type': type(node).__name__
                                    })
                        except SyntaxError:
                            print(f"Syntax Error in file: {
                                  file_path}")  # Log the error
        return code_blocks
