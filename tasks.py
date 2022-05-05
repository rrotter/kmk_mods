from invoke import task
import os
import re

@task
def init(c, kmk_url='https://github.com/KMKfw/kmk_firmware'):
    if not os.path.isdir('kmk_firmware/.git'):
        c.run(f'git clone {kmk_url}')
    c.run(f'rm -r kmk')
    c.run(f'cp -r kmk_firmware/kmk kmk')

@task
def install(c, install_path, quick=False):
    # print(f'path={install_path} quick={quick}')

    skip_kmk_install = os.path.isdir(f'{install_path}/kmk') and quick
    if not skip_kmk_install:
        c.run(f'rsync -a kmk/ {install_path}/kmk')

    c.run(f'rsync -a kmkx/ {install_path}/kmkx')

    # install top level py files, except tasks.py
    files = list(filter(
      lambda f: re.match('^(?!tasks\.py)(\w+)\.py$',f),
      os.listdir('.')
    ))
    for file in files:
        c.run(f'cp {file} {install_path}/{file}')
