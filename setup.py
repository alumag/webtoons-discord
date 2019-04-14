from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='WebtoonHooks',
    version='2.0.1',
    packages=['WebtoonHooks'],
    install_requires=required,
    url='https://github.com/MissLummie/webtoons-discord',
    license='',
    author='Aluma Gelbard',
    author_email='violetaluma@hotmail.com',
    description='Send discord webhooks with all the daily releases from webtoon',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
