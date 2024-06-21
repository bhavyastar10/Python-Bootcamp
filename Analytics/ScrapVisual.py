# Web Scraping : extracting data from website automatically
#       - <url>/robot.txt : what scraping allowed for particular website
#       - pip install beautifulsoup4
#       - pip install requests
#       - from bs4 import BeautifulSoup
#       - response = requests.get(<url>)
#       - response.text : all text data
#       - soup = BeautifulSoup(response.text, 'html.parser')
#       - soup.body : body content
#       - soup.title : title of website
#       - soup.find_all('div') : all occurance of particular thing
#       - soup.select(<class>) : select with class name


# Pandas and LXML for scraping :
#       - data = pd.read_html(<url>)   : in list format
#       - df = data[0]
#       - df.<column-name>     OR   df[<column>]


# Visualization :
#       - import matplotlib.pyplot as plt
#       - plt.pie() : for pie chart
            #   - explode : for space between each piece


# Save scraped data to new db :
#       - df = df.rename(columns = {old : new})
#       - conn = pg2.connect(<db-info>)
#       - from sqlalchemy import create_engine
#       - engine = create_engine('postgresql+psycopg2://<user>:<password>@<ip>:<port>/<db>)
#       - df.to_sql(<table-name> , engine, if_exists='append', index=False)

