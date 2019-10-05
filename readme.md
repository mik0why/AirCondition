## AirQuality

Air Quality is a simple web application which presents the air quality of each voivodeship in Poland. 

## About

The current version (1.1) displays a map of Poland with each voivodeship having a color corresponding to the value of Air Quality calculated for that region. The AQ value is obtained from Air Quality Data Platform's API (aqicn.org).

## Usage 

The main.py function is invoked with two parameters which specify
	* frequency - how often should the map get updated (default: 50)
	* runtime -  how long should the application run for (default: 3600)
The values are interpreted as seconds.


