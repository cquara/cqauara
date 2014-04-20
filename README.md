cqauara
=======

CQUARA - Coastal Quake Alert Response And Analytics


This project is a design solution to alert members in a remote coastal community about the occurrence of an impending earthquake induced Tsunami. Further we envision methods by which patterns maybe extracted from recent mini-earthquakes around a region to predict a major quake.


Description
Remote costal communities are often inaccessible and have either no or intermittent connectivity to the Internet and GSM Mobile networks. For instance, the Andaman and Nicobar islands which experienced a major Tsunami in 2004, still to this day does not have internet connectivity or mobile phone reception in most regions, barring a few selected private entities that may have a slow internet connection. Such places however have a deep penetration of Cable TV and FM Radio culture.'

The current phase of the CQUARA project features a node based on an open hardware linux board that receives real time USGS earthquake feed very 5 minutes. We then look at the magnitude and location (latitude and longitude) to determine if any quake occurred in a 500mile radius off coast from our current location. We then transmit an audio alert message (VOICE ALERT or a DATA TRANSMISSION on AFSK) over an FM channel.



License: GNU Library or "Lesser" General Public License version 3.0 (LGPL-3.0)
