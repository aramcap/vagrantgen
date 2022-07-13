from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
   name = 'vagrantgen',
   version = '0.5',
   description = 'Vagrantfile generator',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author = 'Adrian Ramos',
   url = 'https://github.com/aramcap/vagrantgen',
   license = 'LICENSE',
   py_modules = ['vagrantgen'],
   packages = find_packages(),
   install_requires = ['importlib_resources', 'pyyaml'],
   package_data = {
    '': ['*']
   },
   classifiers=[
      "Environment :: Console",
      "Development Status :: 4 - Beta",
      "Programming Language :: Python :: 3",
   ],
   entry_points = '''[console_scripts]
   vagrantgen=vagrantgen:main
   '''
)
