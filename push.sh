#!/bin/bash

mdbook clean
python3 build.py

git add .
git commit -m "$1"
git push origin master
