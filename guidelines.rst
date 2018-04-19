*************************
Nengo branding guidelines
*************************

The core of Nengo's visual identity
is the square logo for light backgrounds.

.. image:: general/square-light.svg
   :width: 200
   :align: center

Logo origin
===========

Neuron tuning curves play a central role
in most models created with Nengo.
By knowing how a neuron responds
to some input signal,
we are able to construct large, dynamic models
that reproduce and predict
neuroscientific and psychological data.
The logo incorporates tuning curves
from four leaky integrate-and-fire neurons
in Nengo's initial letter.

The four tuning curves can be seen
in isolation with the following script.

.. code:: python

   import matplotlib.pyplot as plt
   import nengo
   from nengo.utils.ensemble import tuning_curves
   from nengo.utils.matplotlib import set_color_cycle

   with nengo.Network() as model:
       A = nengo.Ensemble(n_neurons=4, dimensions=1,
                          encoders=[[-1], [-1], [-1], [-1]],
                          intercepts=[-1, -1, -1, -1],
                          max_rates=[40, 65, 90, 120])
   with nengo.Simulator(model) as sim:
       eval_points, activities = tuning_curves(A, sim)

   plt.rc("lines", solid_capstyle="butt")
   set_color_cycle(["#984EA3", "#E7298A", "#4DAF4A", "#212121"])
   plt.figure(figsize=(6, 11))
   plt.plot(eval_points, activities, lw=40)
   plt.xlim(-1.1, 1.1)
   plt.axis("off")
   plt.show()

The font modified to incorporate the tuning curves
is `Sanchez <https://fonts.google.com/specimen/Sanchez>`_.
This font is also used for all text
in the :ref:`general logos <Assets for the Nengo ecosystem>`.

The design process from initial concepts
to a full finished product can be read
`on this Nengo forum thread
<https://forum.nengo.ai/t/help-choose-a-new-nengo-logo/199>`_.

Variations
==========

Each Nengo logo comes in three sizes.
The **full logo** should be used whenever possible.
Use the **square logo** in places like
profile pictures that require square sizes.
The **small square logo** should be used
when the logo will appear at small sizes
(50 pixels and lower),
such as for web page favicons.

Each logo size also contains
dark and light variations.
In all situations,
ensure that there is enough contrast
between the logo and the background.

If none of the logos available here
work for your particular use case,
please `file an issue <https://github.com/nengo/design/issues/new>`_.
*Do not make your own logo variant*
without first consulting with the Nengo team.

Misuses
=======

The available logo variants can been freely
resized to fit the situation.
However, most other image manipulations should be avoided.

Changing aspect ratio
  Do not scale any logo disproportionately.
  Maintain the aspect ratio of the original logo when resizing.
Rasterizing unnecessarily
  Do not convert logos to raster formats like PNG or JPEG
  unless necessary.
  All logos are provided as Scalable Vector Graphics (SVG) files
  that retain sharp lines at any size.
  If rasterization is necessary, use as high a DPI as possible.
Rotating or skewing
  Do not rotate or skew the logo.
Recoloring
  Do not recolor the logo.
  If you would like a different color variant than is currently provided,
  `file an issue explaining your use case
  <https://github.com/nengo/design/issues/new>`_.
Adding effects
  Do not apply any effects,
  such as outlining, beveling, or adding dropshadows,
  to logos.
Busy backgrounds
  Do not use the logo with a busy background.
  There should always be sufficient contrast
  so that all logo elements can be seen.
  If necessary, add a solid colored rectangle
  behind the logo.

Project branding
================

All Nengo projects should have common visual elements
so that they can be easily identified as Nengo projects.
However, they should also look unique
and discernible at a glance.

The primary mechanism that we use for this
is for each project to have a unique primary color.
The tuning curves in the light logos
are all colored with that primary color.
The opacity of the tuning curves
are graded from top to bottom
for visual effect
when the logo is large enough.
For the small square logo,
all the tuning curves
have the same opacity
so as to emphasize the
rest of the logo.

Aside from incorporating the general Nengo logo
and coloring the tuning curves as described above,
the project is free to add their own touches
in terms of how they add the rest of the project name
to the logo.
The primary color
should also be incorporated into
the rest of the project name somehow.

As an example, consider the Nengo DL logo.

.. image:: nengo_dl/full-light.svg
   :width: 100%
   :align: center

The main difference here is the color of the
curves making up the N,
and the additional DL text,
which also uses the primary color, orange.
Orange was chosen
as the primary color for Nengo DL
because it makes heavy use of TensorFlow,
which uses orange in its logo
and other branding material.

.. todo:: Be explicit about opacity values.
          This will have to be played around with
          once we have a project with its own branding.
