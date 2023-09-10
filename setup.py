from __future__ import annotations

import os
import sys

from setuptools import find_packages, setup

dependencies = [
    "aiofiles==23.1.0",  # Async IO for files
    "anyio==3.7.0",
    "blspy==2.0.2",  # Signature library
    "boto3==1.26.161",  # AWS S3 for DL s3 plugin
    "chikvdf==1.0.11",  # timelord and vdf verification
    "chikbip158==1.2",  # bip158-style wallet filters
    "chikpos==2.0.2",  # proof of space
    "klvm==0.9.7",
    "klvm_tools==0.4.6",  # Currying, Program.to, other conveniences
    "chik_rs==0.2.10",
    "klvm-tools-rs==0.1.34",  # Rust implementation of klvm_tools' compiler
    "aiohttp==3.8.4",  # HTTP server for full node rpc
    "aiosqlite==0.19.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==4.0.2",  # Binary data management library
    "colorama==0.4.6",  # Colorizes terminal output
    "colorlog==6.7.0",  # Adds color to logs
    "concurrent-log-handler==0.9.24",  # Concurrently log and rotate logs
    "cryptography==41.0.1",  # Python cryptography library for TLS - keyring conflict
    "filelock==3.12.2",  # For reading and writing config multiprocess and multithread safely  (non-reentrant locks)
    "keyring==23.13.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "PyYAML==6.0",  # Used for config file format
    "setproctitle==1.3.2",  # Gives the chik processes readable names
    "sortedcontainers==2.4.0",  # For maintaining sorted mempools
    "click==8.1.3",  # For the CLI
    "dnspython==2.3.0",  # Query DNS seeds
    "watchdog==2.2.0",  # Filesystem event watching - watches keyring.yaml
    "dnslib==0.9.23",  # dns lib
    "typing-extensions==4.6.3",  # typing backports like Protocol and TypedDict
    "zstd==1.5.5.1",
    "packaging==23.1",
    "psutil==5.9.4",
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "build",
    # >=7.2.4 for https://github.com/nedbat/coveragepy/issues/1604
    "coverage>=7.2.4",
    "diff-cover",
    "pre-commit",
    "py3createtorrent",
    "pylint",
    "pytest",
    "pytest-asyncio>=0.18.1",  # require attribute 'fixture'
    "pytest-cov",
    "pytest-monitor; sys_platform == 'linux'",
    "pytest-xdist",
    "twine",
    "isort",
    "flake8",
    "mypy==1.4.1",
    "black==23.3.0",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
    "pyinstaller==5.13.0",
    "types-aiofiles",
    "types-cryptography",
    "types-pkg_resources",
    "types-pyyaml",
    "types-setuptools",
]

legacy_keyring_dependencies = [
    "keyrings.cryptfile==1.3.9",
]

kwargs = dict(
    name="chik-blockchain",
    author="Mariano Sorgente",
    author_email="admin@chiknetwork.com",
    description="Chik blockchain full node, farmer, timelord, and wallet.",
    url="https://chiknetwork.com/",
    license="Apache License",
    python_requires=">=3.8.1, <4",
    keywords="chik blockchain node",
    install_requires=dependencies,
    extras_require=dict(
        dev=dev_dependencies,
        upnp=upnp_dependencies,
        legacy_keyring=legacy_keyring_dependencies,
    ),
    packages=find_packages(include=["build_scripts", "chik", "chik.*", "mozilla-ca"]),
    entry_points={
        "console_scripts": [
            "chik = chik.cmds.chik:main",
            "chik_daemon = chik.daemon.server:main",
            "chik_wallet = chik.server.start_wallet:main",
            "chik_full_node = chik.server.start_full_node:main",
            "chik_harvester = chik.server.start_harvester:main",
            "chik_farmer = chik.server.start_farmer:main",
            "chik_introducer = chik.server.start_introducer:main",
            "chik_crawler = chik.seeder.start_crawler:main",
            "chik_seeder = chik.seeder.dns_server:main",
            "chik_timelord = chik.server.start_timelord:main",
            "chik_timelord_launcher = chik.timelord.timelord_launcher:main",
            "chik_full_node_simulator = chik.simulator.start_simulator:main",
            "chik_data_layer = chik.server.start_data_layer:main",
            "chik_data_layer_http = chik.data_layer.data_layer_server:main",
            "chik_data_layer_s3_plugin = chik.data_layer.s3_plugin_service:run_server",
        ]
    },
    package_data={
        "chik": ["pyinstaller.spec"],
        "": ["*.clsp", "*.clsp.hex", "*.klvm", "*.clib", "py.typed"],
        "chik.util": ["initial-*.yaml", "english.txt"],
        "chik.ssl": ["chik_ca.crt", "chik_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    project_urls={
        "Source": "https://github.com/Chik-Network/chik-blockchain/",
        "Changelog": "https://github.com/Chik-Network/chik-blockchain/blob/main/CHANGELOG.md",
    },
)

if "setup_file" in sys.modules:
    # include dev deps in regular deps when run in snyk
    dependencies.extend(dev_dependencies)

if len(os.environ.get("CHIK_SKIP_SETUP", "")) < 1:
    setup(**kwargs)  # type: ignore
