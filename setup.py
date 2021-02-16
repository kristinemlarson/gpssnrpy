from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension

ext1 = Extension(name='gpssnrpy.gpssnr',
        sources=['gpssnrpy/gpssnr.f'], 
        f2py_options=['--verbose'],
        )


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy","scipy","wget","matplotlib"]

setup(
    name="gpssnrpy",
    version="0.0.3",
    author="Kristine Larson",
    author_email="kristinem.larson@gmail.com",
    description="A GPS/SNR translation software package1 ",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/kristinemlarson/gpssnrpy/",
    packages=find_packages(),
    include_package_data=True,
    entry_points ={
        'console_scripts': [
            'gpssnr = gpssnrpy.gpssnr_cl:main', 
            'download_rinex = gpssnrpy.download_rinex:main', 
            'download_orbits = gpssnrpy.download_orbits:main',
            ],
        },
    install_requires=requirements,
    ext_modules = [ext1],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
