from setuptools import setup, find_packages

setup(
    name="Entrancify",
    author="Pranjal Khadka",
    author_email="pranzalkhadka1@gmail.com",
    version="0.1",
    description="An educational platform for CSIT Entrance Examination aspirants.",
    long_description="""Entrancify serves as a platform empowering CSIT Entrance Examination aspirants
                        to make informed decisions through data-driven insights, aiding them in selecting 
                        the most suitable college for their academic journey.""",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'streamlit'
    ],
)