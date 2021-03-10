import requests
import json
from datetime import datetime, timedelta

#returns the total # of administered vaccines in canada
vaccine_api = "https://api.covid19tracker.ca/summary"
response = requests.get(vaccine_api)

total_vaccinated = response.json()['data'][0]['total_vaccinated']
total_vaccinations = response.json()['data'][0]['total_vaccinations']

#the total number of people who have received at least one dose of the vaccine
one_vaccine_administered = int(total_vaccinations) - int(total_vaccinated)

#calculates the current population of canada
population_api = "https://api.covid19tracker.ca/provinces"
response = requests.get(population_api)
province_data = response.json()

population = 0
for province in province_data:
    if province['id'] > 13:
        break
    population += province['population']
    
#calculates the percentage of people who have received at least one dose of the vaccine
percentage = str(round(one_vaccine_administered/population*100, 3))

#stores the pecentage as a variable to be used in WayScript
variables['percentage'] = percentage
