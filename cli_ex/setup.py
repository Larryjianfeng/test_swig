from setuptools import setup, find_packages

setup(
    name='cli_ex',
    packages=find_packages(),
    version='0.2',
    description='test',
    author='larry',
    url='www.google.com',
    setup_requires=[
        'setuptools>=18.0'],
    entry_points={'console_scripts': ['ss=cli_ex:ex']})
