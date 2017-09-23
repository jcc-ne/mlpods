#!/bin/sh

cp ../funpod.py .
docker build -t test_pod ./
rm funpod.py
