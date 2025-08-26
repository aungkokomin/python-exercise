from pathlib import Path
data_dir = Path('data'); data_dir.mkdir(exist_ok=True) # Ensure the data directory exists

Path('data/hello.txt').write_text('hello\nworld\n', encoding='utf-8')
content = Path('data/hello.txt').read_text(encoding='utf-8')
print(content.splitlines())