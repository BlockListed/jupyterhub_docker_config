#!/bin/bash
set -e

VERSION=4.0.2

BASE=quay.io/jupyter/base-notebook:hub-$VERSION

echo "Building for hub version: ${VERSION}"

docker buildx build --build-arg "BASE=${BASE}" -t "jupyter-notebook:${VERSION}" .
