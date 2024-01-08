import matplotlib.pyplot as plt
import numpy as np
import interpolation as ip

# Example usage:
# For function f(x) = 1 / (1 + 25 * x * x)
x = [ -1.0 , -0.6, -0.2, 0.2, 0.6, 1.0]
y = [ 0.038461, 0.1, 0.5, 0.5, 0.1, 0.038461]

# Drawing original function
def f(x):
   return (1 / (1+25*x*x))

x3 = np.linspace(-1,1,1000) # For function

plt.plot(x3,f(x3),'r',label='original function')

x_interpolate = np.arange(-1.0,1,0.01)

# Drawing x and y axes
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Linear Spline Interpolation of Given Data')
plt.xlabel('x')
plt.ylabel('y') 
plt.grid(True)

# Plot the interpolated value
plt.plot(x_interpolate, ip.y_interpolate(x,y,x_interpolate), 'bo', label='interpolated')
plt.legend()
plt.show()
