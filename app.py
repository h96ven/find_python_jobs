import requests
from bs4 import BeautifulSoup

START_OF_URL = 'https://www.work.ua'
BASE_URL = START_OF_URL + '/jobs-python/'


def scrape_jobs():
    try:
        with open('saved scrapes/jobs.txt', 'w', encoding='utf-8') as f:
            # Navigate each page of pagination
            for page_num in range(1, 11):
                url = f'{BASE_URL}?page={page_num}'

                html_text = requests.get(url, timeout=30).text

                soup = BeautifulSoup(html_text, 'lxml')

                job_titles = soup.select('h2 > a')

                company_names = soup.select('span > b')

                for job_title, company_name in zip(job_titles, company_names):
                    f.write(job_title.text)
                    f.write('\n')
                    f.write(company_name.text)
                    f.write('\n')
                    # Extract hyperlinks
                    f.write(START_OF_URL + job_title['href'])
                    f.write('\n\n')

        print('File saved')

    except requests.exceptions.RequestException as e:
        print(f'An error occurred while making a request: {e}')

    except FileNotFoundError:
        print('The specified file or directory could not be found')

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    scrape_jobs()
