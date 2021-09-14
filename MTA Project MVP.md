{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4e31c1ce",
   "metadata": {},
   "source": [
    "# MTA Project MVP"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49379979",
   "metadata": {},
   "source": [
    "### Goal:  Identify street team setup locations which maximize foot traffic"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3f1c8a28",
   "metadata": {},
   "source": [
    "**Procedure:** I differentiated the turnstile data to collect the exits/hour for each turnstile. Then I used exits/hour as the metric for foot traffic which I then attempted to maximize using the following factors: day of the week, time of day, and station."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78e3395c",
   "metadata": {},
   "source": [
    "<div>\n",
    "<img src=\"busiest_day_and_time.png\" width=\"700px\"/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "019fa819",
   "metadata": {},
   "source": [
    "**(left)** According to the data above, the busiest days of the week are weekdays with Monday being the least busy weekday. This makes sense intuitively as work days should see the most commuters and mondays are more likely to be taken off than weekdays in the middle of the week like Wednesday. **(right)** 6-9pm appears to be the busiest time period which corresponds with the post work rush. Interestingly, there are relatively few exits/hour during the morning rush which should be between 6am and 9am. This is cause for alarm and will be investigated."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fa8a072",
   "metadata": {},
   "source": [
    "<div>\n",
    "<img src=\"top_stations_bar_chart.png\" width=\"700px\"/>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "82ec6bda",
   "metadata": {},
   "source": [
    "The busiest stations when ranked by median exits/hour are shown above. A quick google search of busiest new york subway stations mostly agrees with this ranking which provides some confidence in its validity."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae3d0f36",
   "metadata": {},
   "source": [
    "### Current Takeaways\n",
    "- Street teams should operate on a weekday that is not Monday to maximize foot traffic\n",
    "- Street teams should operate during the evening rush (6pm-9pm) to maximize foot traffic\n",
    "- Street teams should operate at the stations in the Busiest Stations figure to maximize foot traffic"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "793a53d9",
   "metadata": {},
   "source": [
    "### Questions Still Pending\n",
    "- Why does my data not show a morning rush?\n",
    "- How many street teams are needed per station to fully cover it?\n",
    "- Which turnstile bays are the most busy within each station? (related to previous question)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:metis] *",
   "language": "python",
   "name": "conda-env-metis-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
