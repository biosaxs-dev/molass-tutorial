import json, pathlib

notebooks = list(pathlib.Path('chapters').rglob('*.ipynb'))
print(f"Total notebooks: {len(notebooks)}\n")

executed_count = 0
empty_count = 0
partial_count = 0

for nb_path in sorted(notebooks):
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    if not code_cells:
        status = "📄 no code"
        empty_count += 1
    else:
        cells_with_outputs = sum(1 for c in code_cells if c.get('outputs'))
        if cells_with_outputs == 0:
            status = "❌ 0 outputs"
        elif cells_with_outputs == len(code_cells):
            status = f"✅ {cells_with_outputs}/{len(code_cells)}"
            executed_count += 1
        else:
            status = f"⚠️  {cells_with_outputs}/{len(code_cells)}"
            partial_count += 1
            executed_count += 1
    
    print(f"{status:15} {nb_path}")

print(f"\nSummary:")
print(f"  Fully/partially executed: {executed_count}")
print(f"  No code cells: {empty_count}")
print(f"  Not executed: {len(notebooks) - executed_count - empty_count}")
