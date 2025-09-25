from os.path import dirname, join

from setuptools import find_packages, setup

from channels_valkey import __version__

# We use the README as the long_description
readme = open(join(dirname(__file__), "README.rst")).read()

crypto_requires = ["cryptography>=1.3.0"]

test_requires = crypto_requires + [
    "pytest",
    "pytest-asyncio",
    "async-timeout",
    "pytest-timeout",
]


setup(
    name="channels_valkey",
    version=__version__,
    url="http://github.com/20252KNUCSECapstoneDesign1Class2Team5/channels_valkey/",
    author="Yunseong Ha",
    author_email="gci28267@gmail.com",
    description="Valkey-backed ASGI channel layer implementation, Based on django/channel_redis",
    long_description=readme,
    license="BSD",
    zip_safe=False,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "valkey",
        "msgpack~=1.0",
        "asgiref>=3.9.1,<4",
        "channels>=4.2.2",
    ],
    extras_require={"cryptography": crypto_requires, "tests": test_requires},
)
