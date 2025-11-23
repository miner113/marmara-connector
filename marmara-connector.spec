# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['src/mainApp.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/ui/images/*.png', 'ui/images'),
        ('src/ui/images/*.ico', 'ui/images'),
        ('src/ui/images/*.gif', 'ui/images'),
        ('src/language', 'language'),
        ('src/styles', 'styles'),
        ('src/ui/generated', 'ui/generated')
    ],
    hiddenimports=['PyQt5', 'QtAwesome', 'src.ui.generated.resources_rc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MarmaraConnector',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='src/ui/images/icon.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='MarmaraConnector',
)
