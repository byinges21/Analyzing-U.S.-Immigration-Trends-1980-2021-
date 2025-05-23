# -*- coding: utf-8 -*-
"""project 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AEPQ4uOKt6mQjSqSHVOhx_L_qAvm5Q82
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
url = "US Immigration Statistics (Ver 1.7.23).csv"
data = pd.read_csv(url)
data.head()

# Sample dataset based on the provided data
data = {
    "Year": [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
             1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
             2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
             2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,
             2020, 2021],
    "LPRs": [524295, 595014, 533624, 550052, 541811, 568149, 600027, 599889, 641346, 1090172,
             1535872, 1826595, 973445, 903916, 803993, 720177, 915560, 797847, 653206, 644787,
             841002, 1058902, 1059356, 703542, 957883, 1122257, 1266129, 1052415, 1107126, 1130818,
             1042625, 1062040, 1031631, 990553, 1016518, 1051031, 1183505, 1127167, 1096611, 1031765,
             707362, 740002],
    "Apprehensions": [910361, 975780, 970246, 1251357, 1246981, 1348749, 1767400, 1190488, 1008145, 954243,
                      1169939, 1197875, 1258481, 1327261, 1094719, 1394554, 1649986, 1536520, 1679439, 1714035,
                      1814729, 1387486, 1062270, 1046422, 1264232, 1291065, 1206408, 960673, 1043759, 889212,
                      796587, 678606, 795735, 786223, 805334, 596560, 683782, 607677, 739486, 1175841,
                      609265, 1865379],
    "Removals": [18013, 17379, 15216, 19211, 18696, 23105, 24592, 24336, 25829, 34427,
                 30039, 33189, 43671, 42542, 45674, 50924, 69680, 114432, 174813, 183114,
                 188467, 189026, 165168, 211098, 240665, 246431, 280974, 319382, 359795, 379739,
                 382449, 390413, 415579, 432201, 405026, 324303, 332263, 284298, 327554, 347183,
                 237861, 89191],
    "Refugee Arrivals": [207116, 159252, 98096, 61218, 70393, 67704, 62146, 64528, 76483, 107070,
                         122066, 113389, 115548, 114181, 111680, 98973, 75421, 69653, 76712, 85285,
                         72165, 68920, 26785, 28286, 52840, 53738, 41094, 48218, 60107, 74602,
                         73293, 56384, 58179, 69909, 69975, 69920, 84989, 53691, 22405, 29916,
                         11840, 11454]
}

df = pd.DataFrame(data)

# Flipping the Line Graph for Immigration Trends (LPRs Over Time)
plt.figure(figsize=(8, 10))
plt.plot(df["LPRs"], df["Year"], marker='o', linestyle='-', color='blue')
plt.xlabel("LPRs (Lawful Permanent Residents)")
plt.ylabel("Year")
plt.title("Immigration Trends: LPRs Over Time (Flipped Axes)")
plt.grid()
plt.show()

# Flipping the Bar Chart for Noncitizen Apprehensions, Removals, and Refugee Arrivals
fig, ax = plt.subplots(figsize=(8, 10))
ax.barh(df["Year"], df["Apprehensions"], color='red', label="Apprehensions", alpha=0.6)
ax.barh(df["Year"], df["Removals"], color='blue', label="Removals", alpha=0.6)
ax.barh(df["Year"], df["Refugee Arrivals"], color='green', label="Refugee Arrivals", alpha=0.6)
ax.set_xlabel("Count")
ax.set_ylabel("Year")
ax.set_title("Noncitizen Apprehensions, Removals, and Refugee Arrivals (Flipped Axes)")
ax.legend()
plt.show()