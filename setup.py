from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='fundamentalista', 
version='0.0.2', 
url='https://github.com/victoracoelho/fundamentalista', 
license='MIT License', 
author='Victor Coelho', 
long_description=readme, 
long_description_content_type="text/markdown", 
author_email='victoracoelho22@gmail.com', 
keywords='Análise Fundamentalista', 
description='Coletor de dados financeiros de empresas listadas na B3 VISITE: https://github.com/victoracoelho/fundamentalista', 
packages=['fundamentalista'], 
install_requires=['pandas', 'lxml'])
