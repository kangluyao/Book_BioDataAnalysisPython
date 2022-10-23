# 2.1 Installing python
sudo apt-get install python3
# 2.2 Installing packages
sudo pip3 install scipy
## update exiting packages
sudo pip3 install --upgrade scipy

# Packages used throughout this book include
pip3 install scipy
pip3 install os
pip3 install numpy
pip3 install matplotlib
pip3 install global-land-mask
pip3 install pandas
# python -m pip install xxxx

# 2.5 Writing and running scripts
import numpy
import os
from matplotlib import pyplot

# evaluate the sine function on a regular X-grid
x = numpy.linspace(0,10,100)
y = numpy.sin(x)

# plot the sine function using pyplots
fig = pyplot.figure(figsize=(4, 3))
pyplot.plot(x, y, c = '#00507a', linewidth = 2, label = 'sin')

# add title & axis labels
pyplot.title("Sine function")
pyplot.xlabel("x")
pyplot.ylabel("sin(x)")

# save the plot to a PDF file
os.makedirs("figures", exist_ok = True)
pyplot.savefig("figures/script_example_sine_plot.pdf", bbox_inches = "tight")
pyplot.close()

# “call” the script in your terminal
python path_to_my_script.py
