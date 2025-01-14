from setuptools import find_packages,setup

setup(
    name='Music Playlist Creator',
    version='1.1.1',
    author='Varun',
    author_email='darklususnaturae@gmail.com',
    install_requires=[
        'openai',
        'flask',
        'requests',
        'setuptools'
    ],
    packages=find_packages()
)