import csv
from moviedatascrapper import GetScrappedData
from moviedatascrapper import GetTitleRow
import scanpage
moviedata_csv_file = open('moviedata.csv', 'w+', newline='', encoding="utf-8")
writer = csv.writer(moviedata_csv_file)


def Scrap(start, end):
    writer.writerow(GetTitleRow())
    for x in range(start, end+1):
        url = f'https://www.themoviedb.org/movie?page={x}'
        pages = scanpage.ScanPage(url)
        print("Processing", url)
        data = []
        for page in pages:
            d = GetScrappedData(page)
            data.append(d)
        writer.writerows(data)
        print('Done page', x)
    print("Scrapping complete.")


def main():
    start = int(input("Starting Index:"))
    end = int(input("Ending Index:"))
    Scrap(start, end)


if __name__ == "__main__":
    main()
