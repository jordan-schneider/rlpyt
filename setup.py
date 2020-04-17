import setuptools
import os

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}

INSTALL_REQUIRES = [
    'numpy',
    'torch',
]
TEST_REQUIRES = [
    # testing and coverage
    'pytest', 'coverage', 'pytest-cov',
    # unmandatory dependencies of the package itself
    'atari_py', 'opencv-python', 'psutil', 'pyprind', 'gym',
]

setuptools.setup(
    name='rlpyt',
    version='0.1.2',
    packages=setuptools.find_packages(),
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES + INSTALL_REQUIRES,
    },
    package_data=find_stubs('rlpyt-stubs'),

)
