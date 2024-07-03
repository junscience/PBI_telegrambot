import subprocess
from setuptools import setup, find_packages

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='',
    version='0.0.1',
    author='junscience',
    description='Embedding app for classification',
    install_requires=requirements,
    packages=find_packages(),
    scripts=['telegram_bot.py']
)
