import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import bird data
birddata = pd.read_csv('https://d37djvu3ytnwxt.cloudfront.net/assets/'
'courseware/v1/c72498a54a4513c2eb4ec005adc0010c/'
'asset-v1:HarvardX+PH526x+3T2016+type@asset+block/bird_tracking.csv')

# First, use `groupby` to group up the data.
grouped_birds = birddata.groupby("bird_name")

# Now operations are performed on each group.
mean_speeds = grouped_birds.speed_2d.mean()

# The `head` method prints the first 5 lines of each bird.
# This is useful if you are running this in ipython and need to see some data.
# Call this only on pandas data frame.
# mean_speeds.head()

# Find the mean `altitude` for each bird.
# Assign this to `mean_altitudes`.

mean_altitudes = grouped_birds.altitude.mean()


# Convert birddata.date_time to the `pd.datetime` format.
birddata.date_time = pd.to_datetime(birddata.date_time)

# Create a new column of day of observation
birddata["date"] = birddata.date_time.dt.date

# If you're in ipython and want to check the head of the column run:
# birddata.date.head()

grouped_bydates = birddata.groupby("date")
mean_altitudes_perday = grouped_bydates.altitude.mean()




grouped_birdday = birddata.groupby(["bird_name","date"])
mean_altitudes_perday = grouped_birdday.altitude.mean()

# If you're in ipython and want to look at the head of `mean_altitudes_perday` run:
# mean_altitudes_perday.head()


grouped_birdday = birddata.groupby(["bird_name","date"])

eric_daily_speed  = grouped_birdday.speed_2d.mean()["Eric"]
sanne_daily_speed = grouped_birdday.speed_2d.mean()["Sanne"]

nico_daily_speed  = grouped_birdday.speed_2d.mean()["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.ylabel("2D mean speed (m/s)")
plt.show()
