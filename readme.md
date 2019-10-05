## AirQuality

Air Quality is a simple web application which presents the air quality
in Poland. 

## Usage 

The 1.0 version will present the user with a map which will display
each voivodeship of Poland in a different color, based on the average
value of Air Quality calculated for that region.

For this purpose, helper methods (get_average and set_color) have
been implemented. 

The get_average method takes on 4 predefined parameters, which 
are the geographical latitude and longitute of each voivodeship.
For the purpose of simplification of this implementation, each 
v-ship is treated as a rectangle. The average of Air Quality Index
values is then calculated for the area specified.

The set_color method takes on 2 predefined arguments, one of which
is the output of the get_average method for a specific v-ship, 
and the other one the code of each v-ship. This is used to 
determine the region of the map which needs to be colored. 

The codes for each v-ship can be found below:

2 - Lower Silesian (Dolnoslaskie)
4 - Kuyavian-Pomeranian (Kujawsko-Pomorskie)
6 - Lublin (Lubelskie)
8 - Lubusz (Lubuskie)
10 - Lodz (Lodzkie)
12 - Lesser Poland (Malopolskie)
14 - Masovian (Mazowieckie)
16 - Opole (Opolskie)
18 - Podkarpackie (Podkarpackie)
20 - Podlaskie (Podlaskie)
22 - Pomeranian (Pomorskie)
24 - Silesian (Slaskie)
26 - Swietokrzyskie (Swietokrzyskie)
28 - Warmian-Masurian (Warminsko-Mazurskie)
30 - Greater Poland (Wielkopolskie)
32 - West Pomeranian (Zachodniopomorskie) 