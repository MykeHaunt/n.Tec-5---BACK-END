# backend.spec
# -*- mode: python -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Collect any dynamic modules (e.g. python‑can plugins)
hidden_imports = collect_submodules('can')

# If you have static config files or templates, list them here:
datas = [
    # ('config/*.yaml', 'config'),
    # ('migrations/*.sql', 'migrations'),
]

a = Analysis(
    ['backend.py'],           # <-- replace with your entry script
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ntec5-backend',
    debug=False,
    strip=False,
    upx=True,
    console=True,            # set False if you want no console window on Windows
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='ntec5-backend'
)