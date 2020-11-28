Focal length and night photography
==================================

Resources:
----------

* [Estiamtes of exposure time using ioptron](https://www.cloudynights.com/topic/671440-ioptron-skyguider-pro-exposure-time/)
* [NPF rule for sharp stars](https://galleries.aaronpriestphoto.com/Articles/NPF-Rule-for-Sharp-Stars) (article, no-tracking)
* [PhotoPills](https://www.photopills.com/blog/update-photopills-now-and-avoid-trails-your-milky-way-photos) App, for calculating NPF rule in the field
* [How to photograph the milky way](https://photographylife.com/landscapes/how-to-photograph-the-milky-way)


The idea is max exposure time is roughly

.. math:

   Expoure = \frac{(35 \times A + 30 \times P)}{f_{\text{equiv}}}

Here A is the f-stop number, and P is the pixel-pitchi in microns. 
Full-frame is 35.9mm x 23.9mm, so the pixel pitch is

.. math:

   P = (35900\,\mu\text{m}) / 8256\text{ px} = 4.34 \,\mu\text{m}/\text{px}

A better appraoch is to take the sensor area (constant) and divide by the number of megapixels (more easily findable) and then scale:

.. math:
  
   P = \sqrt{A/\text{MP}} = \frac{29291\,\mu\text{m}}{\sqrt{MP}} = \text{29.3}{\sqrt{MP/1MP}}\,\mu\text{m}/\text{px}

So the pixel pitch for the D850 would be

..math
  
  P = \frac{29.3}{\sqrt{45}} = 4.37 \,\mu\text{m}/\text{px}


Understanding?
--------------

$A$ is not the apeture size, it is the f-stop number (e.g. 2.8, 4, 5.6 etc). 

I don't really undestand why the maximum allowable exposure time increases as you decrease the size of the physical apeture (i.e. increase N).

I do understand you need longer exposure times as $A$ increases, but *not* why you are more resistant to blur (and can therefore allow a longer exposure time) as *A* increases.

iOptron specific stuff
======================

Claims on the forum are that you can expect to achieve about 18000 mm-seconds from an iOptron.

Quick table for the D850:

Focal length    NPS (untracked) @ f4    iOptron 
------------    --------------------    ---------------
100mm               2.70 seconds         180 s ~ 3 mins
 85mm               3.19 seconds         211 s ~ 3.5 mins
 50mm               5.42 seconds         360 s ~ 6 mins
 35mm               7.75 seconds         514 s ~ 8.5 mins
 20mm               13.6 seconds         900 s ~ 15 mins


i.e. Exposure times are increased by a factor of roughly 66x over the NPS rule when tracking
with an aligned iOptron.

Exposure
========

Taking a picture from the article above, Nikon D800E @ 20mm, ISO 6400, 15 seconds at f/1.8
This is roughly in-line with the NPS rule (max exposure for 20mm is 13.6 seconds, so ballpark 15 seconds).

If I use the Nikon Z-series lenses, I am looking at f/4, which decreases exposure by 2-and-1/3 stops.
We need to increase the exposure time by a factor of :math:`2**2.3333 = 5`.
That is, roughly 15s x 5 = 75 seconds.

If using the D800, I have access to f2.8, which decreases exposure relative to 1.8 by 1.33 stops.
We would need to increase exposure time by a factor of :math:`2**1.3333=2.6`, to roughly 40 seconds.

The NPS rule should get me close to what I need for landscape to remain sharp if I wanted to do everything
in one shot.
Most likely I will do blended exposures, so this isn't a huge deal.

Looking at the 50mm FL, as a way of baselining:
- 360 seconds with iOptron + good alignment
- 75 seconds needed for exposure @ f4 and ISO 6400
- Expsoure time 4.8 times higher than needed, or roughly 2-and-1/3 stops (technically 2.2)
- Can decrease ISO to 3200 (1 stop) and increase f-number to 5.6 (1 stop) at 360 seconds (more light gathering)
- Can decrease ISO to 3200, increase f-number to 5.6, and exposure time to 200 seconds (3:20 min) for slighly more leeway
- Can decrease ISO to 3200, f-number to 5.0, and exposure time to 180 seconds (3 mins)


