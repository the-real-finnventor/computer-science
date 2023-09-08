from base import *


class Item:
    def __init__(self, name, continent, capital_city, population, government_structure, gdp_per_capita, primary_language, currency):
        self.name = name
        self.continent = continent
        self.capital_city = capital_city
        self.population = population
        self.government_structure = government_structure
        self.gdp_per_capita = gdp_per_capita
        self.primary_language = primary_language
        self.currency = currency


def printList(ll):
    for item in ll:
        print(f"""\n
Country: {item.name}
Continent: {item.continent}
Capital City: {item.capital_city}
Population: {item.population}
Government Structure: {item.government_structure}
GDP per Capita: {item.gdp_per_capita}
Primary Language: {item.primary_language}
Currency: {item.currency}
""")


items = [
    Item("Ecuador", "South America", "Quito", "Approximately 17.6 million",
         "Presidential republic", "Around $6,032 (2020)", "Spanish", "United States Dollar (USD)"),
    Item("Argentina", "South America", "Buenos Aires", "Approximately 45.4 million",
         "Presidential republic", "Around $12,032 (2020)", "Spanish", "Argentine Peso (ARS)"),
    Item("Chile", "South America", "Santiago", "Approximately 19.7 million",
         "Presidential republic", "Around $14,755 (2020)", "Spanish", "Chilean Peso (CLP)"),
    Item("Australia", "Australia (Oceania)", "Canberra", "Approximately 25.8 million",
         "Parliamentary democracy, Constitutional monarchy", "Around $54,806 (2020)", "English", "Australian Dollar (AUD)"),
    Item("Thailand", "Asia", "Bangkok", "Approximately 69.8 million",
         "Constitutional monarchy, Parliamentary democracy", "Around $7,739 (2020)", "Thai", "Thai Baht (THB)"),
    Item("Cambodia", "Asia", "Phnom Penh", "Approximately 16.5 million",
         "Constitutional monarchy, Parliamentary democracy", "Around $1,541 (2020)", "Khmer", "Cambodian Riel (KHR)"),
    Item("Vietnam", "Asia", "Hanoi", "Approximately 97.3 million", "Socialist republic",
         "Around $2,715 (2020)", "Vietnamese", "Vietnamese Dong (VND)"),
    Item("Indonesia", "Asia", "Jakarta", "Approximately 273.5 million",
         "Unitary presidential republic", "Around $4,134 (2020)", "Indonesian", "Indonesian Rupiah (IDR)"),
    Item("Malaysia", "Asia", "Kuala Lumpur", "Approximately 32.9 million",
         "Constitutional monarchy, Parliamentary democracy", "Around $11,502 (2020)", "Malay", "Malaysian Ringgit (MYR)"),
    Item("India", "Asia", "New Delhi", "Approximately 1.39 billion", "Federal parliamentary democratic republic",
         "Around $2,104 (2020)", "Hindi (with multiple official languages)", "Indian Rupee (INR)"),
    Item("Egypt", "Africa", "Cairo", "Approximately 104 million",
         "Semi-presidential republic", "Around $3,020 (2020)", "Arabic", "Egyptian Pound (EGP)"),
    Item("Morocco", "Africa", "Rabat", "Approximately 37 million",
         "Constitutional monarchy, Parliamentary democracy", "Around $3,242 (2020)", "Arabic", "Moroccan Dirham (MAD)"),
    Item("Spain", "Europe", "Madrid", "Approximately 47.4 million",
         "Parliamentary constitutional monarchy", "Around $31,178 (2020)", "Spanish", "Euro (EUR)"),
    Item("Croatia", "Europe", "Zagreb", "Approximately 4 million",
         "Parliamentary republic", "Around $14,981 (2020)", "Croatian", "Croatian Kuna (HRK)"),
    Item("United Kingdom", "Europe", "London", "Approximately 68.2 million",
         "Parliamentary constitutional monarchy", "Around $42,513 (2020)", "English", "Pound Sterling (GBP)")
]

ll = insertItems(items)
LLItems = ll.getLL()
printList(LLItems)

print("Please note that the population, GDP per capita, and other figures provided are approximate and based on data available up to the year 2020.")
