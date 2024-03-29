# plot2

python3 main.py OPTIONS

Take a parametrically defined curve in the Argand plane and transform
it with a C -> C function.

Plot original curve in blue; transformed in red; origin marked blue.

# Example

python3 main.py -x 1 -y t -f '1 / t'

![The locus of points 1/(1 + it).](circle.png)

# Will be promted for if absent:
	-x	function of t
	-y	function of t
	-f	function of x + iy, but written as function of t

# Defaults are hard-coded in main.py:
	-s	starting value for t
	-e	end value for t
	-r	step value for t
	-z	zoom
	-g	grid spacing in units, not pixels
	  
# Other notes

The math and cmath libraries are available without the need to name
them explicitly.
