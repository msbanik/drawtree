import setuptools

setuptools.setup(
    name="drawtree",
    version="0.1.1",
    url="https://github.com/msbanik/drawtree.git",

    author="Madhusudan Banik",
    author_email="msbanik@gmail.com",

    description="Draw binary tree in plain text",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],
    license='MIT',
    keywords='tree draw ascii',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
