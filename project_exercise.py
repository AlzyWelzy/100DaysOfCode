import requests
import json

# Init
# newsapi = NewsApiClient(api_key="92ca4bca41be423f8302cb4ce0ece13c")


class NewsApiProject:
    def __init__(self):
        self.api = "92ca4bca41be423f8302cb4ce0ece13c"
        self.url_top_headlines = "https://newsapi.org/v2/top-headlines"
        self.url_everything = "https://newsapi.org/v2/everything"
        # self.url_sources = "https://newsapi.org/v2/sources"

    def top_headlines(self, country):
        params = {
            "country": country,
            "apiKey": self.api,
        }
        response = requests.get(self.url_top_headlines, params=params)
        return response.json()

    def sports(self, country, category):
        params = {
            "country": country,
            "category": category,
            "apiKey": self.api,
        }
        response = requests.get(self.url_top_headlines, params=params)
        return response.json()

    def business(self, country, category, language, q):
        params = {
            "country": country,
            "category": category,
            "language": language,
            "q": q,
            "apiKey": self.api,
        }
        response = requests.get(self.url_everything, params=params)
        return response.json()

    def politics(self, country, category, language, q):
        params = {
            "country": country,
            "category": category,
            "language": language,
            "q": q,
            "apiKey": self.api,
        }
        response = requests.get(self.url_everything, params=params)
        return response.json()

    def technology(self, country, category, language, q):
        params = {
            "country": country,
            "category": category,
            "language": language,
            "q": q,
            "apiKey": self.api,
        }
        response = requests.get(self.url_everything, params=params)
        return response.json()

    def interpret(self, data):
        data = data["articles"]
        for i in data:
            print(i["title"])
            print(i["description"])
            print(i["url"])
            print("")
        return 0


def main():
    newsapi_project = NewsApiProject()
    sectors = ["top_headlines", "sports", "business", "politics", "technology"]
    countries = ["us", "gb", "ca", "au", "in", "za"]
    languages = ["en", "fr", "de", "es", "it", "pt"]
    query = ["trump", "biden", "covid", "coronavirus", "election", "china"]

    print("Welcome to the News API Project")

    while True:
        try:
            print("Please select a sector to view news")
            [print(f"{sectors.index(_) + 1}. {_}") for _ in sectors]
            sector = int(input("Enter the number of the sector: "))

            if sector > 5 or sector < 1:
                raise ValueError

            [print(f"{countries.index(_) + 1}. {_}") for _ in countries]
            country = int(input("Enter the number of the country: "))
            if country > 6 or country < 1:
                raise ValueError

            if sector != 1:
                [print(f"{languages.index(_) + 1}. {_}") for _ in languages]
                language = int(input("Enter the number of the language: "))
                if language > 6 or language < 1:
                    raise ValueError

                [print(f"{query.index(_) + 1}. {_}") for _ in query]
                q = int(input("Enter the number of the query: "))
                if q > 6 or q < 1:
                    raise ValueError

                newsapi_project.interpret(
                    newsapi_project.technology(
                        countries[country - 1],
                        sectors[sector - 1],
                        languages[language - 1],
                        query[q - 1],
                    )
                )

            else:
                if sector == "sports":
                    newsapi_project.interpret(
                        newsapi_project.sports(
                            countries[country - 1], sectors[sector - 1]
                        )
                    )
                elif sector == "business":
                    newsapi_project.interpret(
                        newsapi_project.business(
                            countries[country - 1], sectors[sector - 1]
                        )
                    )
                elif sector == "politics":
                    newsapi_project.interpret(
                        newsapi_project.politics(
                            countries[country - 1], sectors[sector - 1]
                        )
                    )
                elif sector == "technology":
                    newsapi_project.interpret(
                        newsapi_project.technology(
                            countries[country - 1], sectors[sector - 1]
                        )
                    )

        except ValueError:
            print("Invalid Input")


if __name__ == "__main__":
    main()
