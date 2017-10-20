# My solution to the Reaktor orbital challenge in 2016

The challenge was to route a signal from point a to b on earth surface trough given satellite coordinates.
The coordinates are given as latitude, longitude and altitude.
The code will read the starting and ending points and the satellite coordinates from the randomly generated generate.txt file.
The program then transforms the coordinates into cartesian coordinates.
The cartesian coordinates simplify the geomery check to see if two satellites can see each other.
Finally the program performs a breadth first search to find a shortest route and prints it.

Original Problem formulation

> # Reaktor Orbital Challenge
> ## Solve our puzzle for a chance to win an Oculus Rift headset!
>
> To honor the founding of Reaktor Spacelab, we’ve organized a challenge where you can win an Oculus Rift headset. Download this data file, create an algorithm to solve it and submit your answer using the form below. In order to be considered eligible for the prize drawing, you’ll need to submit the correct answer to our puzzle. The challenge ends on the 15th of May 2016.
>
> Your task is to create an algorithm that can route phone calls through space across a network of satellites, much like the Iridium satellite constellation. Due to unfortunate circumstances that took place in the launch, our satellite constellation did not turn out as planned, but instead the satellites are scattered randomly across the globe at altitudes between 300-700km. Your algorithm should return the intermediate hops across satellites needed to transmit a signal from a starting point on the ground to an end point (also on the ground) in valid order (e.g. SAT10,SAT22,SAT7). No signal can travel through Earth, so all hops must be made between satellites that have an unobstructed line of sight between each other. It is possible, albeit very unlikely that a working route cannot be found for a given data file. The route you generate does not need to be the optimal one (i.e. least amount of hops or shortest), but our engineers will appreciate such a solution, as it’ll reduce the overall bandwidth needed.
>
> This CSV formatted randomized data file contains a snapshot with the current position of the satellites in orbit expressed as:
>
> ```
> ID,latitude,longitude,altitude
> ```
> The last line in the file will contain a route between two random points on the Earth surface expressed as:
> ```
> ROUTE,latitude of starting point,longitude of starting point,latitude of end point,longitude of end point
> ```
> The file will also contain a random seed used to generate it, which you will need to submit for verification purposes along with your answer. To make things simple, Earth is assumed to be perfectly round and its radius is 6371km. All altitudes are expressed as kilometers above the surface.
>
> You may use whatever programming language you desire. To take part in the prize drawing, you’ll need to submit your answer and provide the seed value in the data file along with a correct route. Note: headset can only be shipped to countries listed in the official Oculus Rift webstore.
>
> We’re actively looking for talented developers at all our offices (New York, Tokyo & Helsinki), so if you’d like to work with us, we’d love to take a peek at your source code as well!

 https://web.archive.org/web/20160510170247/https://www.reaktor.com/orbital-challenge/