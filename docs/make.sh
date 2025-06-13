#!/bin/sh
# Command file for Sphinx documentation

if [ "$SPHINXBUILD" = "" ]; then
    export SPHINXBUILD=sphinx-build
fi
export SOURCEDIR=src
export BUILDDIR=build

if ! [ -x "$(command -v $SPHINXBUILD)" ]; then
    echo.
    echo.The \'sphinx-build\' command was not found. Make sure you have Sphinx
    echo.installed, then set the SPHINXBUILD environment variable to point
    echo.to the full path of the \'sphinx-build\' executable. Alternatively you
    echo.may add the Sphinx directory to PATH.
    echo.
    echo.If you don\'t have Sphinx installed, grab it from
    echo.https://www.sphinx-doc.org/
    exit 1
fi

if [ "$1" = "" ]; then
    $SPHINXBUILD -M help $SOURCEDIR $BUILDDIR $SPHINXOPTS $O
else
    $SPHINXBUILD -M $1 -d $BUILDDIR/.doctrees/$1 -W $SOURCEDIR $BUILDDIR/$1 -T $SPHINXOPTS $O
fi
