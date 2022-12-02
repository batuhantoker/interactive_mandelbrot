import matplotlib.pyplot as plt

# Create a figure and a subplot
fig, ax = plt.subplots()

# Set the axis limits
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Set the number of iterations
n_iter = 100

# Create a grid of complex numbers
reals = np.linspace(-2, 2, 1000)
imags = np.linspace(-2, 2, 1000)
c = np.array([complex(r, i) for i in imags for r in reals])

# Compute the Mandelbrot set
z = np.zeros_like(c, dtype=np.complex64)
output = np.zeros(c.shape, dtype=int)
for i in range(n_iter):
    z = z**2 + c
    done = np.abs(z) > 2
    c[done], z[done] = 2, 2
    output[done] = i

# Plot the Mandelbrot set
ax.imshow(output, extent=[-2, 2, -2, 2])

# Define a callback function for the scroll event
def on_scroll(event):
    # Get the current x and y limits of the plot
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Compute the new x and y limits based on the scroll event
    xrange = xlim[1] - xlim[0]
    yrange = ylim[1] - ylim[0]
    x_center = (xlim[1] + xlim[0]) / 2
    y_center = (ylim[1] + ylim[0]) / 2
    x_new_center = x_center - event.step * xrange * 0.1
    y_new_center = y_center - event.step * yrange * 0.1
    xlim = (x_new_center - xrange/2, x_new_center + xrange/2)
    ylim = (y_new_center - yrange/2, y_new_center + yrange/2)

    # Update the x and y limits of the plot
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    plt.draw()

# Connect the scroll event to the callback function
fig.canvas.mpl_connect('scroll_event', on_scroll)

# Show the plot
plt.show()
