# mpy-editor

Simple! Easy! Quick! Start your micropython code!

# uasge

1. download editor.exe

double click it.

2. pip insrall mpy-editor

run `pip insrall mpy-editor` in your cmd(shell), then input `editor` run it.

```shell
pip insrall mpy-editor

editor
```

## Open mpy-editor.

## Connect your hardware.

## Run micropython code.

## Look running results.

## save or load your file.

# pyinstaller

1. create editor.spec

pyinstaller -w -F editor.py -i logo.ico

2. modify editor.spec

in 9 line editor.spec add `datas=[('mpy\\img','img')],`

3. create editor.exe

pyinstaller -w -F editor.spec -i logo.ico

# uplaod pypi

```shell
python setup.py sdist build
```

```shell
# pip install twine
twine upload dist/*
```

