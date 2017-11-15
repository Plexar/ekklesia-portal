#!/bin/sh
# lock packages and creates a requirements file with pinned versions and hashes
pipenv lock -r > pypi2nix_source_deps_with_hash
# strip hashes
awk '{ print $1 }' pypi2nix_source_deps_with_hash > pypi2nix_source_deps
# create requirements.nix from intermediary pypi2nix_source_deps
pypi2nix -V 3.6 -r pypi2nix_source_deps -E postgresql -E libffi
