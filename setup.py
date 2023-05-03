from setuptools import setup, find_packages

setup(
    name='mycli',
    version='0.0.0',
    author='NeoZ',
    author_email='neoz.blockchain@gmail.com',
    description='A CLI tool for converting Book PDFs into mp3 Audio files',
    packages=find_packages(),
    install_requires=[
        'click',
        'gTTS',
        'PyPDF2',
        'pathlib'
    ],
    entry_points={
        'console_scripts': [
            'mycli=mycli.cli:main',
        ],
    },
    include_package_data=True,
    package_data={'': ['LICENSE', 'README.rst']},
    data_files=[
        ()
    ]
)
