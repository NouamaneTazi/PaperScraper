from paperscraper.scrapers.base.base_scraper import BaseScraper

"""A scraper of a PMC articles"""


class PMC(BaseScraper):

    def __init__(self, driver):
        self.driver = driver
        self.website = ["ncbi.nlm.nih.gov"]

    def get_authors(self, soup):
        author_links = soup.find("div", {"class": "contrib-group fm-author"}).findAll("a")
        authors = {};

        for i in range(len(author_links)):
            authors['a' + str(i + 1)] = {'last_name': author_links[i].contents[0].split(" ")[-1],
                                         'first_name': author_links[i].contents[0].split(" ")[0]}

        return authors

    def get_abstract(self, soup):
        # TODO get working
        pass
        # abstract = soup.find("div", id=lambda x: x and x.startswith('__abstract'))
        # print(abstract)
        # print(soup.find("p", id="__p1"))
        # [tag.unwrap() for tag in abstract.findAll(["em", "i", "b", "sub", "sup"])]
        # return abstract.find("p").contents[0]

    def get_body(self, soup):
        # TODO get working
        pass

    def get_doi(self, soup):
        return soup.find("span", {"class": "doi"}).find("a").getText()

    def get_keywords(self, soup):
        keywords = soup.find("span", {"class": "kwd-text"})
        [tag.unwrap() for tag in keywords.findAll(["em", "i", "b", "sub", "sup"])]
        return keywords.getText().split(", ")

    def get_pdf_url(self, soup):
        return "https://www.ncbi.nlm.nih.gov/" + soup.find("div", {"class": "format-menu"}).findAll("li")[3].find("a")[
            'href']

    def get_title(self, soup):
        pass
        # return soup.find("h1", {"class": "content-title"}).getText()

    def get_images(self, soup):
        # find images with tags alts containing "chemical structure"
        images = soup.findAll("img", alt=lambda x: x and "chemical structure" in x.lower())
        # images = [image['src'] for image in images if image['src'].startswith("https") else self.website[0] + image['src']]
        base_url = "https://www." + self.website[0]
        images = [image['src'] if image['src'].startswith("https") else base_url + image['src'] for image in
                  images]
        
        # download images to local directory
        import requests
        import os
        local_dir = "images/"
        os.makedirs(local_dir, exist_ok=True)
        for image_url in images:
            img_data = requests.get(image_url).content
            with open(local_dir + "/" + image_url.split("/")[-1], 'wb') as handler:
                handler.write(img_data)
            

