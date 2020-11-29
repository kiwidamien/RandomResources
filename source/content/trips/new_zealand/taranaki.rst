Taranaki region (2020-2021)
===========================

Lake Rotokare
-------------

* `Trip advisor review
  <https://www.tripadvisor.com/Attraction_Review-g15657309-d4235368-Reviews-or10-Lake_Rotokare-Rawhitiroa_Taranaki_Region_North_Island.html#REVIEWS>`__
* `Walkways and lake map <http://www.rotokare.org.nz/Visit/Walkways/>`__

Has Kiwi, open 24 hours, about an `hour from home
<https://www.google.com/maps/dir/New+Plymouth,+New+Zealand/Lake+Rotokare,+Taranaki+4398,+New+Zealand/@-39.2561966,173.9704896,10z/data=!4m14!4m13!1m5!1m1!1s0x6d14f9e62364ce0d:0x500ef6143a2e9a0!2m2!1d174.0630466!2d-39.0611596!1m5!1m1!1s0x6d150dc6a1258f4f:0x2a00ef6165dffd30!2m2!1d174.4103725!2d-39.4516026!3e0>`__

Pouakai
-------

Looking at Pouakai crossing (20 mins from home), the tarns (photo
op), and the huts.

Can stay for free in the clearing (have to pay for the hut).

Plan to visit on Dec 13th (around the time of the new moon).

Terns
~~~~~

* Lens focal lengths, 20mm -- 50mm (50 gets just the mountain)

TPE info (13th)

==========  ======
Event        Time
==========  ======
Moonrise      0448
Sunrise       0552
Moonset       1859
Sunset        2044
==========  ======

Using Stellarium, we see that it gets dark around 10, and the 
milky way lies about 10 degrees above the horizon (horizontally)

The Mliky way is vertical at around 3 am. Will be vertical at
approximately 155 degrees (roughly 25 degrees off due south).

Taranaki basically fills a 50mm field of view, and this is a 
40 degree field of view. Half the mountain is 20 degrees, and
the extra 5 degrees would be 25% of the peak to edge distance.

Minor separation.


Vertical field of view is 27 degrees. Mountain hieght is approx 
40% of image (80% of the 47mm image taken by mountain + reflection)

Mountain has FOV of about 11 degrees. 100 mm star trails.


For the 14th


==========  ======
Event         Time
==========  ======
Moonrise       0509
Sunrise        0551
Moonset        2014
Sunset         2045
==========  ======


Example images
^^^^^^^^^^^^^^

- `Flickr golden hour (47mm)
  <https://www.flickr.com/photos/147095698@N03/46809227804/in/faves-48353814@N05/>`__
- `Flickr wider angle (26mm)
  <https://www.flickr.com/photos/151125234@N05/28793010487/in/faves-48353814@N05/>`__

Longitude and Latitude of Terns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

39.2352° S, 174.0374° E

Tarn location: -39.23140724316514, 174.04817853760065

Peak location: -39.055626, 174.075226

From google maps, the peak is 8 degrees east of south.

Getting the bearing we have, in general

.. math::

   \beta = \arctan(X/Y), \quad\quad X = \cos\theta_b\,\sin\Delta L, \quad\quad Y = \cos\theta_a \sin\theta_b - \sin\theta_a \cos\theta_b \cos\Delta L

where :math:`\beta` is the bearing between the two points.

Limit of close points
:::::::::::::::::::::

If two points are close, we can assume $\Delta L$ is small. If they are far from the poles, we also have small :math:`\Delta \theta`. In radians

.. math::

   X \approx \Delta L\,\, \cos\theta_b

The expression for Y is trickier

.. math::

   Y \approx \sin\theta_b\cos\theta_a - \sin(\theta_a)\cos_\theta_b(1 - \Delta L^2/2) = \sin(\theta_b - \theta_a) + \sin(\theta_a) \cos(\theta_b)(\Delta L)^2/2
   X/Y \approx \frac{\cos\theta_b}{\sin(\theta_b-\theta_a) + \sin(\theta_a) \cos(\theta_b) (\Delta L)^2/2} \Delta L= \frac{2\cos\theta_b}{2\frac{\Delta \theta}{\Delta L} + \sin\theta_a\cos\theta_b\,\Delta L}

Near 
In the limit of small :math:`\Delta L`, we have :math:`X \approx \cos\theta_b \,\Delta L` and :math:`Y\approx \cos\theta_a \sing\theta_b - \sin\theta_a\cos\theta_b = sin(\theta_b - \theta_a)`.  Therefore

.. math::

   \beta \approx \arctan(\Delta L \cos\theta_b/\sin(\theta_b - \theta_a))




.. math::

   X = cos(174.04817853760065^\circ) sin(0.17578^\circ) = (-0.9946)(0.00306797) = -0.00305143
   Y \approx sin(\theta_b - \theta_a) = \sin(-0.027048^\circ) = -0.00047207
   \beta = \arctan(6.4638) 

Resources:
----------
* `How to get to the terns
  <https://destinationlesstravel.com/pouakai-hut-the-best-view-of-mount-taranaki/>`__
