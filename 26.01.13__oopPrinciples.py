


# the parent class
from typing import override


class City:
    def __init__(self, city, region, country, citizens, ziip, area):
        self.city_name = city
        self.region_name = region
        self.country_name = country
        self.number_of_citizens = citizens
        self.zip_code = ziip
        self.area_code = area


    def display_full_info(self):
        return (f"City: {self.city_name}\n"
                f"Region: {self.region_name}\n"
                f"Country: {self.country_name}\n" 
                f"Number of citizens: {self.number_of_citizens}\n"
                f"Zip code: {self.zip_code}, Area code {self.area_code}\n")


    def income(self):
        return self.number_of_citizens * 1000


#------------------------------------------------------------------------


class TuristCity(City):
    def __init__(self, city, region, country, citizens, ziip, area, main_attractions, annual_visitors):
        super().__init__(city, region, country, citizens, ziip, area)
        self.main_attractions = main_attractions
        self.annual_visitors = annual_visitors

    @override
    def income(self):
        return super().income() + self.annual_visitors * 50

    @override
    def display_full_info(self):
        base_info = super().display_full_info()
        attractions = ', '.join(self.main_attractions)
        return (f"{base_info}\n"
                f"Main attractions: {attractions}\n"
                f"Annual visitors: {self.annual_visitors}\n")
    


class IndustrialCity(City):
    def __init__(self, city, region, country, citizens, ziip, area, companies, pollution_level):
        super().__init__(city, region, country, citizens, ziip, area)
        self.main_companies = companies
        self.pollution_level = pollution_level

    @override
    def income(self):
        return super().income() + self.main_companies.__len__() * 50_000

    @override
    def display_full_info(self):
        base_info = super().display_full_info()
        companies = ', '.join(self.main_companies)
        return (f"{base_info}\n"
                f"Main companies: {companies}\n"
                f"Polution level: {self.pollution_level}\n")



class CapitalCity(City):
    def __init__(self, city, region, country, citizens, ziip, area, is_capital, official_language, government_type, gdp):
        super().__init__(city, region, country, citizens, ziip, area)
        self.is_capital = is_capital
        self.official_language = official_language
        self.government_type = government_type
        self.gdp = gdp

    @override
    def income(self):
        return super().income() + self.gdp * 0.1

    @override
    def display_full_info(self):
        base_info = super().display_full_info()
        return (f"{base_info}\n"
                f"Is the capital city: {self.is_capital}\n"
                f"Official language: {self.official_language}\n"
                f"Government type: {self.government_type}\n")





city1 = TuristCity("Poprad", "Presov", "Slovakia", 52000, "05801", "052", ["AquaCity", "High Tatras"], 1000000)
city2 = IndustrialCity("Kosice", "Kosice", "Slovakia", 240000, "04001", "055", ["US Steel", "Kosice IT Valley"], "High")
city3 = CapitalCity("Bratislava", "Bratislava", "Slovakia", 430000, "81101", "02", True, "Slovak", "Parliamentary republic", 10000000000)


cities = [city1, city2, city3]
for city in cities:
    print(city.display_full_info())
    print(f"Income: {city.income():,.0f} eur")
    print()
    print()