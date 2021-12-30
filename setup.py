from setuptools import setup

setup(name='jupyter_MyVimscript_kernel',
      vevimion='0.0.1',
      description='Minimalistic Vimscript kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifievim=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyVimscript-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyVimscript-kernel/tarball/0.0.1',
      packages=['jupyter_MyVimscript_kernel'],
      scripts=['jupyter_MyVimscript_kernel/install_MyVimscript_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'vimscript','vim','VimL'],
      include_package_data=True
      )
