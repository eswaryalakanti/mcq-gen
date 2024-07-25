from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Eswar Yalakanti',
    author_email='yalakantieswar@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2","langchain-openai","langchain_community"],
    packages=find_packages()
)