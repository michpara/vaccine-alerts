import requests
import json

#fetches data from api
vaccine_api = "https://api.covid19tracker.ca/summary"
response = requests.get(vaccine_api)

#parse fetched object
total_vaccinated = response.json()['data'][0]['total_vaccinated']
total_vaccinations = response.json()['data'][0]['total_vaccinations']
change_cases = response.json()['data'][0]['change_cases']

#calculations
one_vaccine_administered = int(total_vaccinations) - int(total_vaccinated)
two_vaccines_administered = int(total_vaccinated)

#calculates the current population of canada
population_api = "https://api.covid19tracker.ca/provinces"
response = requests.get(population_api)
province_data = response.json()

population = 0
for province in province_data:
    if province['id'] > 13:
        break
    population += province['population']
    
#calculates the percentage of people who have received at least one dose of the vaccine, two doses of the vaccine and daily new cases
one_dose = str(round(one_vaccine_administered/population*100, 3))
two_dose = str(round(two_vaccines_administered/population*100, 3))
daily_cases = str(change_cases)

#stores data in variables to be used in Wayscript
variables['one_dose'] = one_dose
variables['two_dose'] = two_dose
variables['daily_cases'] = change_cases
