import mysql.connector
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np
import seaborn as sns

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sunooja@0218sql",
    database="data_analysis"
)

cursor = mydb.cursor()
cursor.execute("""SELECT * FROM internet_price
               LIMIT 10""")
for row in cursor.fetchall():
    print(row)


#1.Countries having least and highest price for 1 GB
def least_price_1gb():
    country1 = []
    country2 = []
    cheapest_price = []
    highest_price = []
    cursor.execute("""SELECT Country ,cheapest_price  
        FROM internet_price ip 
        WHERE cheapest_price !=0
        order by cheapest_price DESC
        LIMIT 15""")
    for row in cursor.fetchall():
        country2.append(row[0])
        highest_price.append(row[1])
    plt.subplot(211)
    plt.barh(country2, highest_price, color=(0.2, 0.5, 0.9, 0.7))
    cursor.execute("""SELECT Country ,cheapest_price  
    FROM internet_price ip 
    WHERE cheapest_price !=0
    order by cheapest_price
    LIMIT 15""")
    for row in cursor.fetchall():
        country1.append(row[0])
        cheapest_price.append(row[1])
    plt.subplot(212)
    plt.barh(country1, cheapest_price, color=(0.2, 0.5, 0.9, 0.7))
    plt.xlabel("Average price for 1 GB")
    plt.ylabel("Countries")
    plt.title("15 Countries having least price for 1 GB")
    plt.show()
#least_price_1gb()

#2. Expensive Internet price providing countries
def expensive_price_1gb():
    country = []
    expensive_price = []

    cursor.execute("""SELECT Country ,expensive_price  
    FROM internet_price ip 
    WHERE expensive_price !=0
    order by expensive_price DESC
    LIMIT 10""")
    for row in cursor.fetchall():
        country.append(row[0])
        expensive_price.append(row[1])
    plt.pie(expensive_price, labels=country)
    plt.title("Expensive price range (Top 15 Countries)")
    plt.show()

#expensive_price_1gb()

#3.Countries who increased and decreased their internet charge per GB
def price_change():
    country1 = []
    country2 = []
    price_2021_1 = []
    price_2021_2 = []
    price_2020_1 = []
    price_2020_2 = []
#Countries increased their internet price in 2021.
    cursor.execute("""SELECT Country,avg_price_2021 ,avg_price_2020 
        FROM internet_price ip 
        WHERE avg_price_2021>avg_price_2020 and avg_price_2020 !=0
        order by avg_price_2021 DESC
        LIMIT 15""")
    for row in cursor.fetchall():
        country1.append(row[0])
        price_2021_1.append(row[1])
        price_2020_1.append(row[2])
    plt.subplot(121)
    plt.bar(country1, price_2021_1, alpha=0.5, label="2021")
    plt.plot(country1, price_2020_1, color="orange", label="2020")
    plt.ylim(0, 60)
    plt.xlabel("Countries")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylabel("Internet Price ")
    plt.title("Countries changed their internet price in the year 2021 & 2020 \n (Price increased and Decreased)\n")
    plt.legend()
# Countries decreased their internet price in 2021.
    cursor.execute("""SELECT Country,avg_price_2021 ,avg_price_2020 
            FROM internet_price ip 
            WHERE avg_price_2021<avg_price_2020 
            order by avg_price_2021 DESC
            LIMIT 15""")
    for row in cursor.fetchall():
        country2.append(row[0])
        price_2021_2.append(row[1])
        price_2020_2.append(row[2])
    plt.subplot(122)
    plt.plot(country2, price_2021_2, label="2021")
    plt.bar(country2, price_2020_2, color="orange", alpha=0.5, label="2020")
    plt.ylim(0, 60)
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.title("Countries decreased their internet price")
    plt.legend(["2021", "2020"])
    plt.show()

#price_change()

#4. Continents and number of internet plans it has
def continent():
    continent = []
    plans = []
    cursor.execute("""SELECT Continent ,SUM(no_of_plans) as num_plans
        FROM internet_price ip
        GROUP BY Continent
        HAVING num_plans > 0
        ORDER BY num_plans""")
    for row in cursor.fetchall():
        continent.append(row[0])
        plans.append(row[1])
    plt.pie(plans, labels=continent, explode=(.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1))
    plt.show()
#continent()

#5.Countries providing high speed and low speed internet
def avg_speed():
    country = []
    country1 = []
    high_speed = []
    low_speed = []
    cursor.execute("""SELECT Country ,avg_speed 
        FROM internet_price ip
        WHERE avg_speed !=0
        ORDER BY avg_speed DESC
        LIMIT 15""")
    for row in cursor.fetchall():
        country.append(row[0])
        high_speed.append(row[1])

    plt.subplot(121)
    plt.barh(country, high_speed, color="blue", label="Internet Speed", alpha=.5)
    plt.xlabel("Internet Speed((Mbit/s)Ookla)")
    plt.ylabel("Countries")
    plt.title("Countries with high speed and Low speed internet\n")
    #plt.xticks(rotation=45, horizontalalignment='right')
#Countries with low internet speed
    cursor.execute("""SELECT Country ,avg_speed 
        FROM internet_price ip
        WHERE avg_speed !=0
        ORDER BY avg_speed DESC
        LIMIT 15""")
    for row in cursor.fetchall():
        country1.append(row[0])
        low_speed.append(row[1])

    plt.subplot(122)
    plt.barh(country1, low_speed, color="blue", label="Internet Speed", alpha=.5)
    plt.xlabel("Internet Speed( (Mbit/s)Ookla)")
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True, left=False, right=True)


    plt.show()

#avg_speed()

#6. Countries with more internet user and less internet user:
def user_percentage():
    country1 = []
    country2 = []
    less_user_percentage = []
    high_user_percentage = []
    cursor.execute(""" SELECT Country , user_percentage 
        FROM internet_price ip 
        WHERE user_percentage !=""
        Order by user_percentage DESC
        LIMIT 10
        """)
    for row in cursor.fetchall():
        country1.append(row[0])
        high_user_percentage.append(row[1])
    plt.subplot(121)
    plt.bar(country1, high_user_percentage, color="blue", label="User Percentage", alpha=.5)
    plt.title(" Countries with more internet user and Less internet user")
    plt.xlabel(" Countries")
    plt.ylabel(" Internet User Percentage")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.ylim(95, 100)

    # Less Internet users
    cursor.execute(""" SELECT Country , user_percentage 
            FROM internet_price ip 
            WHERE user_percentage !=""
            Order by user_percentage 
            LIMIT 10
            """)
    for row in cursor.fetchall():
        country2.append(row[0])
        less_user_percentage.append(row[1])

    plt.subplot(122)
    plt.bar(country2, less_user_percentage, color="blue", label="User Percentage", alpha=.5)
    plt.xlabel("Countries")
    plt.xticks(rotation=45, horizontalalignment='right')
    plt.show()


#user_percentage()







