import requests
from bs4 import BeautifulSoup


def GetScrappedData(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        na = "N/A"
        # Get Movie name, Release date, Rating score and Overview
        try:
            titleBox = soup.find('div', attrs={"class": "title"})
            title = titleBox.find('h2').text
            try:
                year = titleBox.find('span', attrs={"class": "release_date"}).text
            except:
                year = na
        except:
            title = na
            year = na

        try:
            score = soup.find('div', attrs={"class": "user_score_chart"})['data-percent']
        except:
            score = na
        try:
            overview = soup.find('div', attrs={"class": "overview"}).find('p').text
        except:
            overview = na

        # Get Featured Crew
        try:
            featured_crew = soup.find('ol', attrs={"class": "people no_image"}).find_all(
                'li', attrs={"class": "profile"})

            featured_crews = []
            for x in featured_crew:
                profileData = x.find_all('p')
                profile = profileData[0].text+" (" + profileData[1].text + ")"
                featured_crews.append(profile)
        except:
            featured_crew = na

        # Get movie genres
        try:            
            genresData = soup.find('section', attrs={
                "class": "genres right_column"}).find_all('li')
            genres = []
            for x in genresData:
                genres.append(x.text)
        except:
            genres = na

        # Gets More informatin
        try:
            left_col = soup.find(
                'section', attrs={"class": "facts left_column"}).find_all('p')
            length = len(left_col) - 1

            # Get Runtime
            try:
                runtime = left_col[length-2].text.split()
                runtime.pop(0)
                runtime = " ".join(runtime)
            except:
                runtime = na

            # Get Budget
            try:
                budget = left_col[length-1].text.split()
                budget.pop(0)
                budget = " ".join(budget)
            except:
                budget = na

            # Get Revenue
            try:
                revenue = left_col[length].text.split()
                revenue.pop(0)
                revenue = " ".join(revenue)
            except:
                revenue = na

            # Get Release Information
            try:
                certifications = []
                release_info = soup.find(
                    'ul', attrs={"class": "releases"}).find_all('li')
                for x in release_info:
                    certificationData = x.find(
                        'div', attrs={"class": "certification"}).text
                    certifications.append(certificationData)
            except:
                certifications = na
        except:
            runtime = na
            budget = na
            revenue = na
            certifications = na

        singleMovie = [title, year, score, overview, ", ".join(featured_crews),
                       ", ".join(genres), runtime, budget, revenue, ", ".join(certifications)]
        return singleMovie

    else:
        print(r.status_code)
        return [r.status_code]


def GetTitleRow():
    return ["Title", "Year", "Score", "Overview", "Featured Crew",
                     "Genres", "Runtime", "Budget", "Revenue", "Certificates"]
