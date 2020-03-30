people = {"Nicolas": {"birth": 1900, "death": 1975},
          "Vladimir": {"birth": 1970, "death": 2000},
          "Julius": {"birth": 1950, "death": 1985},
          "Alexander": {"birth": 1900, "death": 1920},
          "Obama": {"birth": 1910, "death": 1920},
          "George": {"birth": 1915, "death": 1920},
          "Benjamin": {"birth":  1919, "death": 1925}}

populationVariationPerYear = {}
firstYear = 2020
lastYear = 0

for lifeEvents in people.values():

    if firstYear > lifeEvents["birth"]:
        firstYear = lifeEvents["birth"]
    if lastYear < lifeEvents["death"]:
        lastYear = lifeEvents["death"]
    if lifeEvents["birth"] not in populationVariationPerYear.keys():
        populationVariationPerYear[lifeEvents["birth"]] = 0
    if lifeEvents["death"] not in populationVariationPerYear.keys():
        populationVariationPerYear[lifeEvents["death"]] = 0
    populationVariationPerYear[lifeEvents["birth"]] += 1
    populationVariationPerYear[lifeEvents["death"]] -= 1

populationPerYear = {firstYear - 1: 0}
maxPopulation = 0
yearWithMaxPopulation = 0

for year in range(firstYear, lastYear):
    if year in populationVariationPerYear.keys():
        populationPerYear[year] = populationPerYear[year -
                                                    1] + populationVariationPerYear[year]
    else:
        populationPerYear[year] = populationPerYear[year - 1]
    if maxPopulation < populationPerYear[year]:
        maxPopulation = populationPerYear[year]
        yearWithMaxPopulation = year

print(yearWithMaxPopulation)
