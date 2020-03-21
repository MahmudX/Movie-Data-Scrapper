import moviedatascrapper
import scanpage
import csv

pages = scanpage.ScanPage("https://www.themoviedb.org/movie?page=16")
# print("\n".join(pages))
moviedata_csv_file = open('test.csv', 'w+', newline='', encoding="utf-8")
writer = csv.writer(moviedata_csv_file)
writer.writerow(moviedatascrapper.GetTitleRow())
data = []
for page in pages:
    d = moviedatascrapper.GetScrappedData(page)
    data.append(d)
    writer.writerows(data)
