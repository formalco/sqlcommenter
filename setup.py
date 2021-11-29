from setuptools import find_packages, setup

setup(
    name='formal-sqlcommenter',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    extras_require={
        'psycopg2': ['psycopg2'],
    },
    author='Formal',
    author_email='hello@joinformal.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
    description='Formal sql commenter',
    license='BSD',
    keywords='postgresql sql database',
    url='https://github.com/formalco/formal-pg-sdk',
)
