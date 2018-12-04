import collections
import sys

import numpy as np


class DesignColours(object):
    def __init__(self, base_colour):
        """Generate the colors used for Nengo logo designs.

        Parameters
        ----------
        base_colour : ndarray shape=(3,), dtype=int
            Desired primary colour as a tuple with 8-bit RGB values (0-255).
        """

        assert isinstance(base_colour, np.ndarray)
        assert base_colour.shape == (3,)
        assert base_colour.dtype.kind == "i"
        self.base_colour = base_colour

        # Default background colours
        self.bg = dict(
            light=np.array((255, 255, 255), dtype=int),
            dark=np.array((0, 0, 0), dtype=int),
        )

        # Define alpha levels for each logo
        self.alpha = collections.OrderedDict()
        self.alpha["full_light"] = np.array((1.0, 0.8, 0.6), dtype=float)
        self.alpha["square_light"] = np.array((1.0, 0.8, 0.6), dtype=float)
        self.alpha["full_dark"] = np.array((1.0, 0.8, 0.6), dtype=float)
        self.alpha["square_dark"] = np.array((0.2, 0.4, 0.6), dtype=float)

        # Generate colours
        self.colours = collections.OrderedDict()
        for logo in self.alpha:
            bg = "dark" if logo == "full_dark" else "light"
            self.colours[logo] = self.rgba2rgb(self.bg[bg], self.alpha[logo])

    def rgba2rgb(self, bg, alpha):
        """Get the overlaid base color as RGB with no transparency.

        Accepts the background color RGB and transparency value
        and returns the base colour with that transparency on that
        background as an RGB value with no transparency.

        Parameters
        ----------
        bg : 3-tuple of int (R, G, B)
            Background color as a tuple with 8-bit RGB values (0-255)
        alpha : float
            alpha value of the desired color as a float between 0 and 1
        """
        alpha = alpha[:, np.newaxis]
        return ((1 - alpha) * bg + alpha * self.base_colour).astype(int)

    def __str__(self):
        output = ""
        longest_logo = max(len(logo) for logo in self.colours)

        for logo in self.colours:
            output += "######### %s #########\n" % (logo.center(longest_logo))
            for i, curve in enumerate(["Top", "Middle", "Bottom"]):
                output += "%-9s" % curve
                output += "#{0:02x}{1:02x}{2:02x} ({0}, {1}, {2})\n".format(
                    *self.colours[logo][i]
                )
            output += "\n"
        return output.rstrip("\n")


if __name__ == '__main__':
    usage = "\n".join([
        "Usage: python generate_colors.py (hex|r g b)",
        "  hex  color hex code",
        "  r    integer value of the red channel (0-255)",
        "  g    integer value of the green channel (0-255)",
        "  b    integer value of the blue channel (0-255)",
    ])

    # Check we have correct inputs
    if len(sys.argv) == 2:
        hexcode = sys.argv[1].lstrip('#')
        rgb = tuple(int(hexcode[i:i+2], 16) for i in (0, 2, 4))
    elif len(sys.argv) == 4:
        rgb = tuple(int(arg) for arg in sys.argv[1:])
    else:
        print(usage)
        sys.exit()

    try:
        base_colour = np.array(rgb, dtype=int)
        assert np.all(base_colour >= 0) and np.all(base_colour <= 255)
    except (ValueError, AssertionError):
        print("Error: color channels must be integers between 0 and 255")
        sys.exit()

    # Generate and print colours
    colours = DesignColours(base_colour)
    print(colours)
