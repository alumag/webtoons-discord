from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='WebtoonHooks',
    version='1.0',
    packages=['WebtoonHooks'],
    install_requires=required,
    url='https://github.com/MissLummie/webtoons-discord',
    license='',
    author='Aluma Gelbard',
    author_email='violetaluma@hotmail.com',
    description='Send discord webhooks with all the daily releases from webtoon'
)
