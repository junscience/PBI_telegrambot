import subprocess
from setuptools import setup, find_packages

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='PBI_telegrambot',
    version='0.0.1',
    author='junscience',
    description='Embedding app for classification',
    install_requires=requirements,
    packages=find_packages(),
    scripts=['telegram_bot.py'],
    entry_points={
        'console_scripts':[
            'PBI_telegrambot=telegram_bot:main'
        ]
    }
)
