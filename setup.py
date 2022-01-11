#!/usr/bin/env python
# coding: utf-8
with open("README.md", "r") as f:
	long_description = f.read()
import setuptools
setuptools.setup(name='jupyter_MyVimscript_kernel',
    vevimion='0.0.1',
    description='Minimalistic Vimscript kernel for Jupyter',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='nufeng',
    author_email='18478162@qq.com',
    license='MIT',
    url='https://github.com/nufeng1999/jupyter-MyVimscript-kernel/',
    download_url='https://github.com/nufeng1999/jupyter-MyVimscript-kernel/releases/tag/0.0.1',
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    scripts=['jupyter_MyVimscript_kernel/install_MyVimscript_kernel'],
    keywords=['jupyter', 'notebook', 'kernel', 'vimscript','vim','VimL'],
    include_package_data=True
    )
