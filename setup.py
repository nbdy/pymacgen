from setuptools import setup, find_packages

setup(
    long_description=open("README.rst", "r").read(),
    name="pymacgen",
    version="0.42",
    description="generate mac addresses",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/pymacgen",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="mac generator oui",
    packages=find_packages(),
    include_package_data=True,
    entry_points={'console_scripts': ['pymacgen = pymacgen.__main__:main']},
    install_requires=open("requirements.txt").readlines()
)
