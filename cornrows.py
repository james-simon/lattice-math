import numpy as np

# consider a rectangle with width d and length L
# tilted at an angle theta from vertical
# placed on an infinite unit rectangular lattice of points.
# calculate the maximal length L the rectangle can have without overlapping any lattice points.
def max_length(d, theta, max_length=1000, eps=1e-5):

    theta = theta % np.pi
    if theta > np.pi / 2:
        theta -= np.pi

    assert d < 1, "d must be less than 1"

    # the function is symmetric, so just work with theta positive
    if theta < 0:
        theta *= -1

    # if the rectangle is vertical, don't try and divide by infinity, just return the max length
    if theta == 0:
        return max_length

    # compute the vertical cross-section height
    vertical_cross_section_height = d / np.abs(np.sin(theta))

    # figure out how far the rectangle extends up and to the right
    right_hit_point = None
    for x in np.arange(0, 1.3 * max_length * np.abs(np.sin(theta)) + 1):
        lower_y = x / np.tan(theta)
        upper_y = x / np.tan(theta) + vertical_cross_section_height

        nearest_integer_y = np.ceil(lower_y + eps)
        if nearest_integer_y <= upper_y - eps:
            right_hit_point = np.array([x, nearest_integer_y])
            break

    # figure out how far the rectangle extends down and to the left
    left_hit_point = None
    for x in np.arange(-1, -1.3 * max_length * np.abs(np.sin(theta)) + 1, -1):
        lower_y = x / np.tan(theta)
        upper_y = x / np.tan(theta) + vertical_cross_section_height

        nearest_integer_y = np.floor(upper_y - eps)
        if nearest_integer_y >= lower_y + eps:
            left_hit_point = np.array([x, nearest_integer_y])
            break

    if right_hit_point is None or left_hit_point is None:
        return max_length

    total_length = (right_hit_point - left_hit_point) @ np.array([np.sin(theta), np.cos(theta)])

    print(left_hit_point, right_hit_point, total_length)
    return min(total_length, max_length)

print(max_length(.5 ** .5 + .001, np.pi/4))