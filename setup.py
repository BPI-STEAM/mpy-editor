#!/usr/bin/env python

from distutils.core import setup

setup(name='mpy-editor',
      version="%d.%d.%d" % (1, 0, 7),
      description='Simple! Easy! Quick! Start your micropython code!',
      author='Juwan',
      author_email='junhuanchen@qq.com',
      url='https://github.com/junhuanchen/mpy-editor',
      download_url='https://codeload.github.com/junhuanchen/mpy-editor/zip/master',
      install_requires=['pyserial', 'Pillow', 'Pygments'],
      packages=['mpy'],
      package_data={'mpy': ['img//*.gif','img//*.png']},
      scripts=['editor'],
      keywords=['micropython', 'editor', 'simple', 'easy', 'quick'],
      classifiers=[],
      entry_points={"console_scripts": ["editor=mpy.editor:run"]},
)
