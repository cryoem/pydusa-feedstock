#!/bin/bash

build_dir="${SRC_DIR}/../build_eman"

mkdir -p $build_dir
cd $build_dir

cmake --version
cmake $SRC_DIR

cmake
make
make install
