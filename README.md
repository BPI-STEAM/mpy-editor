# mpy-editor

Simple! Easy! Quick! Start your micropython code!

# uasge

## Open mpy-editor.

## Connect your hardware.

## Run micropython code.

## Look running results.

## save or load your file.

# pyinstaller

1. create editor.spec

pyinstaller -w -F editor.py -i logo.ico

2. modify editor.spec

in 9 line editor.spec add `datas=[('img', 'img')],`

3. create editor.exe

pyinstaller -w -F editor.spec -i logo.ico
