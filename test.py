from paperscraper import PaperScraper
scraper = PaperScraper()
# print(scraper.extract_from_pmid("S0045653521025017"))
# print(scraper.extract_from_url("https://www.sciencedirect.com/science/article/pii/S016635420700469X?via%3Dihub"))
print(scraper.extract_from_url("https://www.ncbi.nlm.nih.gov/books/NBK501290/"))
