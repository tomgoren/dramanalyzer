# dramanalyzer
A utility to analyze https://nikolas.github.io/github-drama/

## Overview
This utility goes over every link in the above mentioned document and tries to
assemble some statistics for the commenters in the threads.

## Getting started

* Create a virtualenv for the project
* Get the drama data source: `git submodule update --init --recursive`
* Install dependencies: `pip install -r requirements.txt`
* Run the utility: `./main.py`

## Known issues
Initial version includes a variety of inefficiencies, and tends to hammer the
GitHub API.
