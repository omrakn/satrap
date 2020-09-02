# Spatial Analyst of Transportation Performance -- SATRAP

SATRAP quantifies and illustrates the centrality and accessibility metrics of a road network. The software is designed as an independent GIS software that can calculate transportation performance metrics with an all-round open-source approach. Users can obtain, analyze and visualize open source spatial data without handling any technical difficulties with SATRAP. It targets policy makers and researchers who want to analyze a road network's geometric and topologic properties with its easy-to-use interface.

# To Start SATRAP

The software must be opened from an environment having the required libraries. Conda package management system which comes bundled with the Anaconda Python distribution provided by Continuum Analytics (https://www.anaconda.com/products/individual) has been used to control the versions of used libraries. A conda environment that has required libraries can easily be created by using the environment file (pygis.yml) in this repository with the following command in Anaconda Command Prompt or cmd:

>conda env create -f pygis.yml

After the environment is created, the following command must be executed to use the environment:

>conda activate pygis

After these processes, satrap.py can be opened via prompt screen from pygis environment.

>python satrap.py

# License

SATRAP is distributed under the MIT license, a permissive open-source (free software) license.
