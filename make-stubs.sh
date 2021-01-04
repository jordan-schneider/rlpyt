#!/bin/bash
rm -rf rlpyt-stubs/*
stubgen -o rlpyt-stubs -p rlpyt
mv rlpyt-stubs/rlpyt/* rlpyt-stubs
git cherry-pick caee25c741ca28b193dd7675a3065fa8a29dbdf5