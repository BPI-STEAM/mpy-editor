# mpy-editor [Chinese](README.md)

Simple! Easy! Quick! Start your micropython code!

## uasge

### 1. into [releases](https://github.com/junhuanchen/mpy-editor/releases)download editor.exe.

double click it.

### 2. pip insrall mpy-editor

![](readme/01.png)

run `pip insrall mpy-editor` in your cmd(shell), then input `editor` run it.

```shell
pip insrall mpy-editor
editor
```

## Open mpy-editor.

When opened, the current list of devices is displayed. Hardware has not been inserted yet.

![](readme/02.png)

## Connect your hardware.

Connect to your hardware and the port number of the current hardware will appear.

![](readme/03.png)

Click 'COM5' as shown in the figure to connect successfully.

![](readme/05.png)

## Run micropython code.

Click the button(Run) code, as shown in figure of the built-in code `print(' hello world!')`.

![](readme/07.png)

## Look running results.

![](readme/09.png)

## save or load your file.

![](readme/11.png)

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
twine upload dist/* --verbose
```

