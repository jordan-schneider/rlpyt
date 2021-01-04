#!/bin/bash

# TODO(joschnei): This creates a few git commits even if there are no stub changes. Create a temp
# branch to try all of this, and then merge the tmp into the actual, which should noop if there
# aren't any changes.

git fetch upstream
git rebase -Xours --no-keep-empty --empty=drop upstream/master
git pull
git cherry-pick -Xtheirs caee25c741ca28b193dd7675a3065fa8a29dbdf5
rm -rf rlpyt-stubs/*
stubgen -o rlpyt-stubs -p rlpyt
mv rlpyt-stubs/rlpyt/* rlpyt-stubs
git add rlpyt-stubs
git commit -m "Updates stubs"
git cherry-pick -Xtheirs 47682338eed8c6b94c75bb19f10244788506d3b2