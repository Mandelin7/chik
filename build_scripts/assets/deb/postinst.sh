#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/chik/resources/app.asar.unpacked/daemon/chik /usr/bin/chik || true
ln -s /opt/chik/chik-blockchain /usr/bin/chik-blockchain || true
