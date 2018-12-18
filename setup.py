"""
Setup for Platform Tour XBlock.
"""

import os

from setuptools import setup


def package_data(pkg, roots):
    """
    Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.
    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))
    return {pkg: data}


setup(
    name='xblock-platform-tour',
    version='1.0.2',
    description=('This xblock makes it easy for instructors to build a custom tour'
                 ' of the platform and their specific course.'),
    license='AGPL v3',
    packages=[
        'platformtour',
    ],
    install_requires=[
        'XBlock',
        'xblock-utils',
        'django',
    ],
    dependency_links=[
        'https://github.com/edx/xblock-utils/tarball/c39bf653e4f27fb3798662ef64cde99f57603f79#egg=xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'platformtour = platformtour:PlatformTourXBlock',
        ]
    },
    package_data=package_data(
        'platformtour',
        [
            'static',
            'public',
            'templates',
        ],
    ),
)
