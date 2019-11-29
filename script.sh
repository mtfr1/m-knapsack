#!/bin/bash
for file in instances/*
do
	python mkp.py < $file
done
