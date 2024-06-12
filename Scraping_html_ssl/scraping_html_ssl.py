#!/usr/bin/env python3
import argparse    # pour gerer les argv argc
import requests
import os                 # pour creer des fichier
from bs4 import BeautifulSoup # pour extraire le html
from datetime import datetime
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Charger et récup les variables d'environnement depuis le fichier .env
load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

def scrapping_html(url):
    try:
        print(LOGIN)
        print(PASSWORD)
        response = requests.get(url, auth=HTTPBasicAuth(LOGIN, PASSWORD), verify=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        print(soup.prettify())

        # Créer le dossier "resultat" s'il n'existe pas
        if not os.path.exists('resultat'):
            os.makedirs('resultat')

        # Obtenir la date et l'heure actuelles pour le filename
        current_time = datetime.now()
        file_name = current_time.strftime("%d_%m_%Y_%H_%M")

        # Vérifier si le fichier existe déjà avec la meme heure
        # sinon incrémenter un compteur a la fin pour le rendre unique
        counter = 1
        base_name = file_name
        while os.path.exists(f"resultat/{file_name}.txt"):
            file_name = f"{base_name}_{counter}"
            counter += 1

        # html recuperer dans soup.prettify
        with open(f"resultat/{file_name}.txt", 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
            print(f"HTML content has been written to resultat/{file_name}.txt")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve URL {url}. Error: {e}")
    except Exception as e:
        print(f"An error occurred while processing URL {url}. Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='scraping_html_new_file.py',
        description='A program to fetch and display the HTML content of a webpage given its URL.',
        epilog='Engie Vianeo Scraping'
    )

    parser.add_argument('URL', type=str, help='The URL of the website to fetch HTML from.')

    args = parser.parse_args()

    scrapping_html(args.URL)