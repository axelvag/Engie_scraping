# Scraping_html_new_file

## How to launch

```bash
python3 scraping_html_new_file.py [URL]
```
## Objective

Put the easy html of a page in a new file in the resultat/ directory, which its name is DD_MM_YYYY_HH_MM.txt


# Scraping_html_ssl

## How to launch

```bash
python3 scraping_html_ssl.py [URL]
```
## Objective

Put all the html of a page in a new file in the resultat/ directory, which its name is DD_MM_YYYY_HH_MM.txt



# How to start

### Windows

Install MSYS2 and open

```bash
pacman -S git
pacman -S python
pip install requests
pip install beautifulsoup4
pip install python-dotenv
pacman -S mingw-w64-clang-x86_64-python-pandas
git clone https://github.com/axelvag/Scraping.git
cd Scraping
// now we will create .env file with the secret var, so follow the schema below to fill the file correctly
mkdir .env
// then choose your file you want to launch with "cd ...."
```

### Linux

Launch a bash terminal with the tool installed:
- git
- python
- requests
- beautifulsoup
- python-dotenv

```bash
pip install git
pip install requests
pip install beautifulsoup4
pip install python-dotenv
git clone https://github.com/axelvag/Scraping.git
cd Scraping
// now we will create .env file with the secret var, so follow the schema below to fill the file correctly
mkdir .env
// then choose your file you want to launch with "cd ...."
```


# .ENV

Format to follow ->
```bash
LOGIN=....
PASSWORD=.....
```
