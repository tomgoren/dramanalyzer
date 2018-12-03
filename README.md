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

## Example
Generated (and sorted) output displaying the top 50 "contributors":
```
Username            Comment count
ghost               106
davidfowl           94
markrendle          68
meh                 61
mikeal              48
jasnell             42
puffnfresh          40
DanielRuf           37
myrne               36
ForbesLindesay      35
benaadams           34
JohnMH              34
NickCraver          31
andrewmcwatters     29
sheerun             28
benjamingr          28
Rycochet            27
gulbanana           24
joepie91            24
et304383            24
erisdev             24
fxn                 24
moxie0              24
Fishrock123         23
jamiebuilds         23
poettering          23
PinpointTownes      22
ashleygwilliams     22
FransBouma          21
mikesherov          21
to-json             21
isaacs              20
JsonFreeman         20
jebrosmund          20
ipsumx              20
abritinthebay       20
domenic             20
ambv                19
kodypeterson        19
chrisjsmith         19
jpsnover            19
MartinJohns         17
friism              17
N3X15               17
leecollings         17
rotemdan            17
RByers              17
mythz               16
aredridel           16
```
