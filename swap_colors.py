import os
import sys

import numpy as np

from generate_colors import DesignColours


def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError("Hex code must be 6 characters")

    rgb = tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))
    rgb = np.array(rgb, dtype=int)
    if not np.all((rgb >= 0) & (rgb <= 255)):
        raise ValueError("RGB values must be between 0 and 255")

    return rgb


def rgb_to_hex(rgb):
    assert len(rgb) == 3
    return "{0:02x}{1:02x}{2:02x}".format(*rgb)


if __name__ == '__main__':
    usage = "\n".join([
        "Usage: python swap_colors.py dir hex_old hex_new",
        "  dir       Directory containing the assets to swap colors for",
        "  hex_old   Original base color hex code",
        "  hex_new   Replacement base color hex code",
    ])

    # Check we have correct inputs
    print(sys.argv)
    if len(sys.argv) == 4:
        directory = sys.argv[1]
        base_rgb_old = hex_to_rgb(sys.argv[2])
        base_rgb_new = hex_to_rgb(sys.argv[3])
    else:
        print(usage)
        sys.exit()

    # Generate and print colors
    colors_old = DesignColours(base_rgb_old)
    colors_new = DesignColours(base_rgb_new)

    for logo in colors_old.colours:
        path = os.path.join(directory, logo.replace("_", "-") + ".svg")
        with open(path, "r") as fh:
            svg = fh.read()

        logo_colors_old = [base_rgb_old] + list(colors_old.colours[logo])
        logo_colors_new = [base_rgb_new] + list(colors_new.colours[logo])

        for rgb_old in logo_colors_old[1:]:
            hex_old = rgb_to_hex(rgb_old)
            assert hex_old in svg, (logo, hex_old)

        for i, (rgb_old, rgb_new) in enumerate(zip(logo_colors_old, logo_colors_new)):
            # print((rgb_old, rgb_new))
            hex_old = rgb_to_hex(rgb_old)
            hex_new = rgb_to_hex(rgb_new)
            # print((hex_old, hex_new))
            svg = svg.replace(hex_old, hex_new)
            assert hex_old not in svg

        with open(path, "w") as fh:
            fh.write(svg)

        print(f"Wrote {path}")
