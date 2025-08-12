from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Deepak',
    install_requirements=['openai','langchain','streamlit','python_dotenv','PyPDF'],
    packages=find_packages()
)