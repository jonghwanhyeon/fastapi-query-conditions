from setuptools import setup, find_packages

with open('README.md', 'r') as input_file:
    long_description = input_file.read()

setup(
    name='fastapi-query-conditions',
    version='1.0.1',
    description='FastAPI-Query-Conditions is a dependency that parses a query string into conditions using operators enclosed in square brackets',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jonghwanhyeon/fastapi-query-conditions',
    author='Jonghwan Hyeon',
    author_email='jonghwanhyeon93@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Home Automation',
    ],
    keywords=['fastapi', 'query', 'querystring', 'condition'],
    packages=find_packages(),
    install_requires=['fastapi'],
)