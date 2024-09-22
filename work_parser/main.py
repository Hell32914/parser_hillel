import argparse
from bs4 import BeautifulSoup
from parser import ParserEngine
from request import RequestEngine
import settings


def main(json_mode: bool, db_mode: bool): 
    page = settings.START_PAGE
    result = []

    while True:
        print(f"PAGE {page}")
        request_engine = RequestEngine()
        response = request_engine.get_response(settings.HOST + settings.ROOT_PATH, params={
            "ss": settings.SS,
            "page": page
        })

        parser_engine = ParserEngine(BeautifulSoup(response.text, features="html.parser"))        
        cards = parser_engine.find_cards("card card-hover card-search card-visited wordwrap job-link js-job-link-blank js-hot-block")  
        
        for card in cards:
            name, href = parser_engine.find_name_and_href(card)  # Оновлення для отримання імені та посилання
            print(f"Vacancy: {name}, URL: {settings.HOST + href}")

        if not cards:
            break
        page += 1  # Збільшення лише після обробки всіх карток

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser for work ua")
    parser.add_argument("-json", action="store_true", default=False, help="JSON store opportunity")
    parser.add_argument("-db", action="store_true", default=False, help="DB store opportunity")
    args = parser.parse_args()
    main(args.json, args.db)
