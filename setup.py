"""Setup for Platform Tour XBlock."""

import os

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

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
    name='platform-tour-xblock',
    version='0.1',
    description='Platform Tour XBlock',   # TODO: write a better description.
    license='AGPL v3',
    packages=[
        'platformtour',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'platformtour = platformtour:PlatformTourXBlock',
        ]
    },
    package_data=package_data("platformtour", ["static", "public"]),
)
