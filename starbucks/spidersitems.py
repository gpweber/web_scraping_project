import scrapy
import re


class StarbucksItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field() 
    state = scrapy.Field() 
    population = scrapy.Field()
    percent_urban = scrapy.Field()
    percent_rural = scrapy.Field()
    age_city = scrapy.Field()
    age_state = scrapy.Field()
    median_income = scrapy.Field() #includes all household members above age 15
    state_median_income = scrapy.Field() ### #state average for same year
    cost_of_living_index = scrapy.Field()  #March 2019 cost of living index - U.S. average 100.0 
    nearest_city_over_1E6pop = scrapy.Field()
    distance_to_nearest_city = scrapy.Field()
    lesbian_couples_percent_self_reported = scrapy.Field() #Likely homosexual households (counted as self-reported same-sex unmarried-partner households)
    gay_couples_percent_self_reported = scrapy.Field() #(see above comment)
    num_grocery_stores = scrapy.Field()
    num_grocery_per_1E5_state = scrapy.Field()
