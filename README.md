# bravais
Plots 2D Bravais lattices.

## Table of Contents
* [General info](#general-info)
* [Screenshot](#screenshot)
* [Technologies](#technologies)
* [Examples](#examples)
* [How to Use](#how-to-use)

## General Info
Uses the magnitudes of two primitive vectors and the angle between them to generate a scatter plot of the 2D bravais lattice in matplotlib.

## Screenshot


## Technologies
Project was created with:
* Python 3.6

## Examples
    from bravais import bravais

    bravais.Bravais2D()

## How to Use
Just import bravais and run the Bravais2D class.  
Here are all the arguments for Bravais2D:
* a: (float) The magnitude of the first primitive vector (default is 1.0).
* b: (float) The magnitude of the second primitive vector (default is 1.0).
* angle: (float) The angle between the two primitive vectors; can't be 0 or 180 degrees (default is 90.0).
* degrees: (bool) If true, angle is in degrees and if False, angle is in radians (default is True).
* centered: (bool) True if the lattice is a centered rectangular (default is False).
* numpoints: (int) The number of desired points to plot and must be a square number larger than 4; will be the number of 'non-centered' points if centered rectangular lattice (default is 25).
