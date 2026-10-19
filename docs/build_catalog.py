"""Refresh local source catalogs without executing project code or reading secrets."""
import ast, os, re
from pathlib import Path
from urllib.parse import quote
BASE=Path(__file__).resolve().parent
WORK=BASE.parent
DOWNLOADS=Path.home()/'Downloads'
ROOTS={
 'phase-1':DOWNLOADS/'kaggle_upload', 'phase-2':DOWNLOADS/'phase2',
 'phase-3':DOWNLOADS/'Phase3-main','phase-4':DOWNLOADS/'Phase4-main',
 'phase-5':DOWNLOADS/'Phase5-main','application':DOWNLOADS/'BiomedicalVerifier',
 'workspace':WORK,
}
SKIP={'.git','.venv','venv','node_modules','__pycache__','.next','vendor','site-packages','documentation','data','models','checkpoints','.cache'}
EXT={'.py','.js','.mjs','.cjs','.ts','.tsx','.jsx','.css','.html','.sh','.command','.ipynb','.yaml','.yml','.toml'}
def scan(root):
 for directory, dirs, files in os.walk(root):
  dirs[:]=sorted(d for d in dirs if d not in SKIP and not d.startswith('.'))
  for name in sorted(files):
   p=Path(directory)/name
   if p.suffix not in EXT or p.is_symlink() or p.stat().st_size>2_000_000: continue
   yield p

def detail(p):
 if p.suffix=='.py':
  try:
   tree=ast.parse(p.read_text(errors='replace'))
   symbols=[n.name for n in tree.body if isinstance(n,(ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef))]
   doc=ast.get_docstring(tree)
   text=(' '.join(doc.split())[:220] if doc else 'Python module; see defined symbols and source.')
   return text, ', '.join('`'+s+'`' for s in symbols) or 'No top-level functions/classes.'
  except SyntaxError: return 'Python source could not be parsed by the documentation interpreter; inspect before running.', 'Not extracted.'
 if p.suffix=='.ipynb': return 'Research notebook; execution state and embedded outputs were not inspected.', 'Notebook'
 if p.suffix in {'.command','.sh'}: return 'Shell entry point; inspect paths and arguments before running.', 'Shell'
 if p.suffix in {'.yaml','.yml','.toml'}: return 'Configuration file; values are intentionally not copied into this catalog.', 'Configuration'
 return 'Frontend/source asset; follow the source link for implementation.', p.suffix.lstrip('.')

def main():
 catalog=BASE/'catalog';catalog.mkdir(exist_ok=True)
 count=0;summary=[]
 for key,root in ROOTS.items():
  paths=list(scan(root)) if root.exists() else []
  lines=[f'# {key}: source file catalog','',f'Source root: `{root}`','', 'Generated from local files. Inclusion does not imply a file is active, tested, or production-ready. Backups and historical experiments are included when present. Descriptions are module docstrings or structural summaries, not an audit of correctness.','']
  for p in paths:
   desc,symbols=detail(p);rel=p.relative_to(root)
   lines += [f'## `{rel}`','',f'[Open source]({quote(str(p),safe="/")})','',desc.replace('<','&lt;'),'',f'**Top-level definitions/type:** {symbols}','']
  (catalog/f'{key}.md').write_text('\n'.join(lines))
  summary.append(f'| [{key}](catalog/{key}.md) | {len(paths)} | `{root}` |')
  count+=len(paths)
 (BASE/'FILE_INDEX.md').write_text('# Source file index\n\nGenerated on 2026-10-19 from the local project folders.\n\n| Component | Source/config files | Root |\n|---|---:|---|\n'+'\n'.join(summary)+f'\n\nTotal: **{count} files**.\n\nScope: Python, JavaScript/TypeScript, HTML/CSS, shell launchers, notebooks and YAML/TOML configuration. Excludes virtual environments, third-party vendor folders, Git internals, data/model/checkpoint directories, files above 2 MB, and generated build directories. This is a source catalog, not a backup of every filesystem file. JSON datasets, secrets, credentials, and notebook contents are not reproduced. Source links point to this Mac; documentation links are relative.\n\nRefresh with `python3 documentation/build_catalog.py` from the workspace root.\n')
 print(f'Cataloged {count} files across {len(ROOTS)} roots')
if __name__=='__main__':main()
