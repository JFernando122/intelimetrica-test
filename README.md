# Intelimétrica test

This server is made for a coding challenge from Intelimétrica for the position of back-end developer

## Requirements

- It must contain a README.md file (this one :))
- All CRUD operations for the table (see below)
- A /restaurant/statistics endpoint
  said endpoint recieves 3 params, latitude, longitude and radius and returns the amount of restaurants, the avg rating and the standar deviation of the restaurant found within the circle with center in the given lat and lot and with the specified radius (Note: radius is in meters)

## Database
As suggested the database of use is a PostgreSQL database with the PostGIS extension to manage the spatial query required in the last requirement

For this project the only table needed was the restaurant table which was "pre-made" by the challenge itself

"""
Restaurants (
  id TEXT PRIMARY KEY, -- Unique Identifier of Restaurant
  rating INTEGER, -- Number between 0 and 4
  name TEXT, -- Name of the restaurant
  site TEXT, -- Url of the restaurant
  email TEXT,
  phone TEXT,
  street TEXT,
  city TEXT,
  state TEXT,
  lat FLOAT, -- Latitude
  lng FLOAT -- Longitude
)
"""

## Experiences during this challenge
While i have previous experience with both making API's and with python i didn't have experience with the flask framework, all the previous API's i had worked with were in Nodejs with express

Even tho the challenge didn't specify a programming language nor specific framework i decided to give the extra challenge of doing it in python using flask

In general it was pretty easy, the concepts from express translated relatively seemless to flask so the general CRUD operations was no issue. In the other part, i also didn't have any experience with spacial queries and have mainly worked with MySQL in the past, At the the it wasn't that difficult to implement the main difficulty came of finding the proper tools and the instalation of them

## Conclusion
The challenge was quite fun and it helped me to learn new stuff so regardless of the outcome i at least won't go empty handed :)
I would like to thank Intelimetrica for giving me this opportunity