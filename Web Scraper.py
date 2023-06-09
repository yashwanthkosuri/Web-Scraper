import requests
import csv
from bs4 import BeautifulSoup

def scrape_imdb(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all movie containers
    movie_containers = soup.find_all('div', class_='lister-item-content')

    # Store the data in a CSV file
    with open('imdb_movies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header row
        writer.writerow(['Title', 'Rating', 'Cast'])

        # Iterate over movie containers
        for container in movie_containers:
            # Extract movie title
            title = container.h3.a.text.strip()

            # Extract movie rating
            rating = container.find('div', class_='ratings-imdb-rating').strong.text

            # Extract cast information
            cast_container = container.find('p', class_='text-muted').find('a')
            cast = cast_container.text.strip() if cast_container else 'N/A'

            # Write data row
            writer.writerow([title, rating, cast])

    print("Scraping completed successfully!")

if __name__ == '__main__':
    url = 'https://www.imdb.com/chart/top'  # IMDb Top Rated Movies
    scrape_imdb(url)
