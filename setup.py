from setuptools import find_packages,setup

setup(
    name='Chatbot',
    version='1.0.0',
    author='Varun',
    author_email='darklususnaturae@gmail.com',
    install_requires=[
        'openai',
        'flask',
    ],
    packages=find_packages()
)