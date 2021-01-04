#!/bin/bash
rm -rf rlpyt-stubs/*
git fetch upstream
git rebase -Xours --no-keep-empty --empty=drop upstream/master
git pull
git cherry-pick -Xtheirs caee25c741ca28b193dd7675a3065fa8a29dbdf5
rm -rf rlpyt-stubs/*
stubgen -o rlpyt-stubs -p rlpyt
mv rlpyt-stubs/rlpyt/* rlpyt-stubs
git add rlpyt-stubs
git cherry-pick -Xtheirs 47682338eed8c6b94c75bb19f10244788506d3b2