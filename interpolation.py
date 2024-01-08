def y_interpolate(x_values, y_values, x_interpolate_array): 
    """Interpolate the y value for a given x value using linear spline interpolation."""

    if len(x_values) != len(y_values):
        raise ValueError("Number of x values must be equal to the number of y values.")

    n = len(x_values)

    y_interpolate_array = []
    for x_interpolate in x_interpolate_array:
        for i in range(n - 1):
            if x_values[i] <= x_interpolate <= x_values[i + 1]:
                # Linear interpolation formula: y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
                x1, x2 = x_values[i], x_values[i + 1]
                y1, y2 = y_values[i], y_values[i + 1]
                y_interpolate_array.append(y1 + (x_interpolate - x1) * (y2 - y1) / (x2 - x1))

    return y_interpolate_array
