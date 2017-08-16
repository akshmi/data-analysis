from setuptools import setup, find packages 
setup(
name='data_analysis',
version='0.0.1',
url='https://github.com/akshmi/data-analysis',
author='Akash'
license='BSD'
packages=find_packages(),
install_requires=['Pyqt5',
'pandas',
'sqlalchemy',
'nltk',
'numpy',
'jupyter',
'python-twitter'],
entry_points={},
extras_require={'dev':['flake',]},
)

