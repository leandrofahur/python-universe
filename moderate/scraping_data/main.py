import requests
from bs4 import BeautifulSoup
from pprint import pprint


def create_custom_hn(links, subtext):
    hn = []
    
    for index, link in enumerate(links):
        # Check if this link has corresponding subtext
        if index < len(subtext):
            title = link.get_text()
            href = link.get("href", None)
            subtext_score = subtext[index].select(".score")

            if subtext_score:
                points = int(subtext_score[0].getText().replace(" points", ""))
                if points > 99:
                    hn.append({
                        "title": title,
                        "points": points,
                        "link": href,
                    })
                    
            # print(index)
            # print(link)
            # print(subtext[index])
            # print("\n")

    return hn


def main():
    url = "https://news.ycombinator.com/news"    
    response = requests.get(url)
    # print(response.text)
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())


    links = soup.find_all("a")
    subtext = soup.select(".subtext")        

    # print(create_custom_hn(links, subtext))
    # make sure the header links are out
    scraped_data = create_custom_hn(links[11:], subtext)
    pprint(scraped_data)


if __name__ == "__main__":
    main()
