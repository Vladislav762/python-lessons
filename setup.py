from cx_Freeze import setup, Executable

executables = [Executable('main.py')]

setup(name='hello_world',
      version='0.0.1',
      description='project',
      executables=executables)