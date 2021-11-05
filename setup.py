import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='ABIRCLON',  
     version='0.1',
     scripts=['ABIRCLON'] ,
     author="ABIR HOSSAIN",
     author_email="abirhossain200019@gmail.com",
     description="this is a Facbook friend list id cloner",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ABIRHOSSAIN10/FB-Cloner",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2.7",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
