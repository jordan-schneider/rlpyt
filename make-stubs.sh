#!/bin/bash
rm -rf rlpyt-stubs/*
git fetch upstream
git rebase upstream/master
git pull
git cherry-pick caee25c741ca28b193dd7675a3065fa8a29dbdf5
stubgen -o rlpyt-stubs -p rlpyt
mv rlpyt-stubs/rlpyt/* rlpyt-stubs
git cherry-pick 47682338eed8c6b94c75bb19f10244788506d3b2