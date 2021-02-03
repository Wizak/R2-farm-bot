# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['bot.py'],
            pathex=['D:\\Develops\\R2-farm-bot'],
            binaries=[],
            datas=[
                ('D:\\Develops\\R2-farm-bot\\Interface\\R2-Logo.ico', 'Interface'), 
                ('D:\\Develops\\R2-farm-bot\\Mark\\Bord.png', 'Mark'),
                ('D:\\Develops\\R2-farm-bot\\Mark\\Hp.png', 'Mark'),
                ('D:\\Develops\\R2-farm-bot\\Mark\\Screenshot.png', 'Mark')],
            hiddenimports=[],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)
exe = EXE(pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            [],
            name='R2bot',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=False,
            icon='D:\\Develops\\R2-farm-bot\\Interface\\R2-Logo.ico')