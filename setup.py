import setuptools 

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
   
setuptools.setup(
    name="kinliuren",
    version="0.0.0.1",
    author="Ken Tang",
    author_email="kinyeah@gmail.com",
    install_requires=[            
      ],
	description="Qimendunjia (奇門遁甲) is one of the three greatest Chinese Divination systems ever.",
	long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kentang2017/kinqimen",
	packages=setuptools.find_packages(),
	package_data = {},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)