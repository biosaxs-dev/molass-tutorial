"""
Check notebook execution status by execution_count (not outputs).
This correctly handles function definition cells which execute but produce no output.
"""
import json, pathlib

notebooks = list(pathlib.Path('chapters').rglob('*.ipynb'))
print(f"Total notebooks: {len(notebooks)}\n")

fully_executed = 0
partially_executed = 0
not_executed = 0
no_code = 0

for nb_path in sorted(notebooks):
    nb = json.loads(nb_path.read_text(encoding='utf-8'))
    all_code_cells = [c for c in nb['cells'] if c['cell_type'] == 'code']
    
    # Filter out empty cells (source is [] or "")
    code_cells = []
    for c in all_code_cells:
        src = c['source']
        if isinstance(src, list):
            src = ''.join(src).strip()
        else:
            src = src.strip()
        if src:  # Non-empty
            code_cells.append(c)
    
    if not code_cells:
        status = "📄 no code"
        no_code += 1
    else:
        executed_cells = sum(1 for c in code_cells if c.get('execution_count') is not None)
        
        if executed_cells == 0:
            status = "❌ 0 executed"
            not_executed += 1
        elif executed_cells == len(code_cells):
            status = f"✅ {executed_cells}/{len(code_cells)}"
            fully_executed += 1
        else:
            status = f"⚠️  {executed_cells}/{len(code_cells)}"
            partially_executed += 1
    
    print(f"{status:15} {nb_path}")

print(f"\nSummary:")
print(f"  Fully executed: {fully_executed}")
print(f"  Partially executed: {partially_executed}")
print(f"  Not executed: {not_executed}")
print(f"  No code cells: {no_code}")
