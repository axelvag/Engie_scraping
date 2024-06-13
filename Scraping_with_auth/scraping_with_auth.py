#!/usr/bin/env python3
import argparse
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

# Charger et récupérer les variables d'environnement depuis le fichier .env
load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

def create_file(soup):
    # Créer le dossier "resultat" s'il n'existe pas
    if not os.path.exists('resultat'):
        os.makedirs('resultat')

    # Obtenir la date et l'heure actuelles pour le filename
    current_time = datetime.now()
    file_name = current_time.strftime("%d_%m_%Y_%H_%M")

    # Vérifier si le fichier existe déjà avec la même heure
    # sinon incrémenter un compteur à la fin pour le rendre unique
    counter = 1
    base_name = file_name
    while os.path.exists(f"resultat/{file_name}.txt"):
        file_name = f"{base_name}_{counter}"
        counter += 1

    # html récupéré dans soup.prettify
    with open(f"resultat/{file_name}.txt", 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
        print(f"HTML content has been written to resultat/{file_name}.txt")

def scraping_html(url):
    try:
        options = Options()
        options.add_argument('--headless')  # Exécuter Chrome en mode headless
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = Service(r'C:\Users\VG6589\OneDrive - ENGIE\Documents\chromedriver-win64\chromedriver.exe')  # Remplacez 'path/to/chromedriver' par le chemin réel vers ChromeDriver
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(url)

        # Remplir et soumettre le formulaire de connexion
        username_input = driver.find_element(By.NAME, 'username')  # Ajustez le sélecteur si nécessaire
        password_input = driver.find_element(By.NAME, 'password')  # Ajustez le sélecteur si nécessaire

        username_input.send_keys(LOGIN)
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)

        # Attendre que la page se charge après la connexion
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Récupérer le HTML de la page
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        create_file(soup)

        driver.quit()

    except Exception as e:
        print(f"An error occurred while processing URL {url}. Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='scraping_with_auth.py',
        description='A program to fetch and display the HTML content of a webpage given its URL.',
        epilog='Engie Vianeo Scraping'
    )

    parser.add_argument('URL', type=str, help='The URL of the website to fetch HTML from.')

    args = parser.parse_args()

    scraping_html(args.URL)
