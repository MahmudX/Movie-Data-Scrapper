import csv
from moviedatascrapper import GetScrappedData
from moviedatascrapper import GetTitleRow
import scanpage

pages = scanpage.ScanPage('https://www.themoviedb.org/movie')
data = []
for page in pages:
    d = GetScrappedData(page)
    data.append(d)
print('Done')
with open('moviedata.csv', 'w+', newline='', encoding="utf-8") as moviedata_csv_file:
    writer = csv.writer(moviedata_csv_file)
    writer.writerow(GetTitleRow())
    writer.writerows(data)
