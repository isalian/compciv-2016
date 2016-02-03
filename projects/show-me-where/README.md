#Show Me Where Project

This project shows me something interesting about place.

##About the dataset

The U.S. Geological Survey has posted an earthquake catalog of all earthquakes in the country. There are multiple spreadhseets of varying specificity, but I have chosen a spreadsheet of earthquakes of 4.5 magnitude or higher on the Richter scale. The dataset contains 373 records for the past 30 days and its fields include geolocation information, magnitude, and time. 

I chose this dataset because as a native Californian, I have a vested interest in being aware of nearby earthquakes. 

### Basic facts about the dataset
- The source of the data: [USGS Earthquake Catalog](http://earthquake.usgs.gov/fdsnws/event/1/)
- The data's landing page: [JSON Earthquake Feeds](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- Direct link to the data: [http://http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson)
- The data format: JSON
- Number of rows: 373

### Description of data fields

#### generated

A __float__ that represents the time when the feed was most recently updated in milliseconds since the epoch.

#### url

A __text string__ of the url of the feed.

#### title

A __text string__ representing the title of the field, e.g. `USGS Magnitude 4.5+ Earthquakes, Past Month`

#### api

A __text string__ referring to the version of API that generated the feed.

#### count

An __integer__ representing the number of earthquakes in the feed.

#### status

An __integer__ referring to the HTTP status code of response, e.g. `200`

#### mag

Contains a __float__ representing the Richter-scale magnitude of the earthquake.

#### place

Contains a __text string__ with a textual description of a named geographic region near the earthquake. 

#### time

Contains an __integer__ referring to the time when the event occured in milliseconds since the epoch.

#### updated

Contains an __integer__ referring to the time when the individual event was most recently updated, reported in milliseconds since the epoch.

#### tz

Contains an __integer__ representing the time difference from UTC in minutes at the earthquake's epicenter, e.g. `-360`

#### url

Contains a __text string__ which is a link to the US Geological Survey event page for that earthquake.

#### detail 

Contains a __text string__ with a link to the GEOJSON detail feed from a GEOJSON summary feed.

#### felt

Contains an __integer__ with the total number of felt reports submitted to the system.

#### cdi

Contains a __float__ with the maximum *reported* intensity for the earthquake.

#### mmi

Contains a __float__ with the maxiumum estimated *instrumental* intensity of the earthquake.

#### alert

Contains a __text string__ corresponding to the alert level based on the PAGER earthquake impact scale, e.g. `green` or `red` etc.

#### status

Contains a __text string__ indicating whether the data has been reviewed by a person.

#### tsunami

Contains an __integer__: if the integer value is `1`, it was a large event in an oceanic region. Otherwise, the value is `0`.

#### sig

Contains an __integer__ quantifying how significant the event is on a scale of 0 to 100.

#### net

Contains a __text string__ with an ID referring to the data contributor for the earthquake. 

#### code

Contains a __text string__ representing a unique identification code for the earthquake.

#### ids

Contains a __comma-separated string__ of event ids associated with the event.

#### sources

Contains a __comma-separated string__ of data contributors.

#### types

Contains a __comma-separated string__ of something called "product types" associated with the earthquake. 

#### nst

Contains an __integer__ corresponding to the number of seismic stations that determined the earthquake location.

#### dmin

Contains a __float__ measuring the horizontal distance from the earthquake's epicenter to the nearest station, listed in degrees. The smaller the float, the more reliable the earthquake data.

#### rms

Contains a __float__ representing the root-mean-square of the "travel time residual," which seems to measure the accuracy of the earthquake caluclations.

#### gap

Contains another __float__ where the smaller the number, the  more reliable the earthquake's position data is.

#### magType

Contains a __text string__ representing which algorithm was used to calculate the earthquake magnitude.

#### type

Contains a __comma-separated string__ representing the product types associated with the earthquake.

#### longitude

Contains a __float__ representing a longitude coordinate where negative values are western longitudes.

#### latitude

Contains a __float__ representing a latitude coordinate where negative values are southern longitudes.

#### depth

Contains a __float__ represting the depth of the earthquake in kilometers.

#### id

Contains a __text string__ which is a unique identifier for the earthquake.

### Anticipated data wrangling

Since the dataset is already filtered to contain only earthquakes over 4.5 magnitude for a fixed time period of 30 days, I will only have to extract the coordinates from the dataset, which consists of 1 dictonary per earthquake entry. The latitude and longitude are currently in a `coordinates` field in a list. I may also extract the magnitude of the earthquake to include in the HTML report for the user.