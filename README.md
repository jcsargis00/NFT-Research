# NFT-Research
### Presentation
#
#### Selected topic
#
#### Why does NFT minting with cryptocurrency use so much energy?
* Is energy used related to cryptocurrency price fluctuations?
* Can we predict how much energy will be used in the  future using machine learning?
* Is this an environmental concern?
* If it is, is there an eco friendly solution for NFT minting without cryptocurrency?
#
#### Reason topic selected:
#
"The environmental concern comes from the estimated carbon footprint generated by the power plants providing that energy. And it isn't just mining that uses lots of power—a single Bitcoin transaction is estimated to burn 2,292.5 kilowatt hours of electricity, enough to power a typical US household for over 78 days."
#
* add citations

"More and more computing power is needed to mine bitcoin, which requires more and more electricity. ASICs can be used to supercharge your mining, which uses even more electricity, and if bitcoin's price rises, it becomes even more profitable to mine, which causes more miners to jump into the game."
#
There is also a volatility concern.  Add citations.  Add machine learning  algorithm for prediction of cryptocurrency prices.

From  Logan Kugler
Communications of the ACM, July 2018, Vol. 61 No. 7, Pages 15-17
10.1145/3213762, https://cacm.acm.org/magazines/2018/7/229045-why-cryptocurrencies-use-so-much-energy/fulltext
#
Why Cryptocurrencies Use So Much Energy
#
"In recent months, bitcoin and other cryptocurrencies have plunged in value, yet the market capitalization for these digital currencies is still valued at hundreds of billions of dollars. That market cap has grown more than 20 times since last year, when the cryptocurrency boom began.
#
With bitcoin's booming popularity comes problems. Speculation in bitcoin and other cryptocurrencies is rampant. Scams abound, and plenty of initial coin offerings (ICOs) have overpromised or underdelivered spectacularly.
#
Through it all, the world has focused on how bitcoin and other cryptocurrencies could implode and go to zero—or make you rich—depending on who you ask. Yet another aspect to cryptocurrencies has not received as much attention.
#
A major issue that results from increased adoption has not been adequately addressed; they use a lot of energy. The "mining" process that creates bitcoin uses more energy than Serbia, says Digiconomist, a self-described "platform that provides in-depth analysis, opinions, and discussions with regard to bitcoin and other cryptocurrencies ... on a voluntary, best-effort basis.">
#
According to Bitcoinist, another industry site, the average cost in electricity to mine a bitcoin in Serbia is about $3,100, making it quite profitable to mine the coin there (among other countries with low-cost electricity).
#
As cryptocurrencies rise in price, the problem isn't going away. Right now, Digiconomist estimates that bitcoin mining, the process of generating bitcoins, accounts for 0.29% of the world's annual electricity consumption. The mining of a single bitcoin block—a block of tranasaction data on the bitcoin network—consumes enough energy to power more than 28 U.S. homes for a day.
#
Other cryptocurrencies that are structured similarly to bitcoin use energy for mining, too. Bitcoin is the most popular and best known cryptocurrency, but it is not unique in its energy needs.
#
Some people wonder if cryptocurrencies will disrupt the financial system, while others wonder if they will break the environment in the process."  
add glossary, references
#
Ethereum average energy consumption per transaction compared to that of VISA as of January 10, 2022
#
![eth](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethusage.PNG)
#
![bit](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinenergy.PNG)
#
Bitcoin prices are highly volatile.
#
![yah](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinyahoo.png)
#
How is energy consumed by Bitcoin calculated?
![proc](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinprocess.PNG)
#
WHAT IS THE REAL CARBON FOOTPRINT OF THE BLOCKCHAIN?
Proof-of-work blockchain networks consume a very large amount of energy, which results in a very large amount of carbon being emitted. Best estimates place bitcoin around 45.8 TWh, emitting around 45,800,000 Tonnes of CO2 per year [1]. The annual power consumption from Ethereum activity is estimated to be 9.62TWh from September '19 - '20 [2].

[1] Stoll et al., The Carbon Footprint of Bitcoin (2019)
[2] digiconomist.net/ethereum-energy-consumption
#
#### Description of the source of data
2 datasources needed, environmental and  financial
#
Financial Dataset - Cryptocurrency Historical Prices from Kaggle
#
https://github.com/jcsargis00/NFT-Research/tree/main/Resources/data
#
Pull data from yahoo finance:
https://github.com/ranaroussi/yfinance
#### Environmental sources pertaining to energy usage- still looking at data
#
https://github.com/kylemcdonald/ethereum-emissions
#
https://www.eia.gov/totalenergy/data/monthly/

#
Bitcoin energy usage (Cambridge study)
#
https://ccaf.io/cbeci/mining_map
#
https://digiconomist.net/bitcoin-energy-consumption
#
Financial: Bitcoin (and other types of crypto, do stacked csv) price changes
#
#### Datasetcsv file URL
https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory?resource=download&select=coin_Litecoin.csv
#
Github
Description of the communication protocols
I am working solo and performing all of the 4 roles.

* Square role will be responsible for setting up the repository. This includes naming the repository and adding team members, which is just me.
* Triangle role - responsible for creating a simple machine learning model. Creating a simple model this early in the design process helps a team better understand where and how a machine learning model will fit into the project. This also grants more time to work out the specifics related to machine learning.

Which model did you choose and why?
* Simple Regression/ Clustering, good fit for the  problem.
#
How are you training your model?
* After scaling, 75% of data will be used for training, 25% of data will be used for testing
#
What is the model's accuracy? TBD
#
How does this model work? TBD

* Circle role - in charge of the mockup database. 

* X role - selection of technology for the project. 
#
## Technologies Used
- Python
- Pandas
- Numpy
- Tensorflow
- SciKitLearn
- KMeans
- Mongo or DynamoDB
#
#### Data Cleaning and Analysis
* Data Preprocessing  will involve selection, transformation,  and scaling of data.  Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

#### Database Storage
* Mongo or DynamoDb will be the database for energy usage.
* Flask will be used to display the data.
* There will be 2 database tables, one for energy consumption and one for price fluctuation.
The tables will include fields for energy usage and price changes
* use Python to download the data from the Coinbase web site
Postgres will be the database for crypto pricing.
Fields of crypto pricing  model
- Symbol - The symbol for which the timeseries data refers
- Open - This is the opening price of the time period
- High - This is the highest price of the time period
- Low - This is the lowest price of the time period
- Close - This is the closing price of the time period
- Volume (Crypto) - This is the volume in the transacted Ccy. Ie. For BTC/USD, this is in BTC amount
- Volume Base Ccy - This is the volume in the base/converted ccy. Ie. For BTC/USD, this is in USD amount
#
Postgres sample table of crypto pricing model
![pri](https://github.com/jcsargis00/NFT-Research/blob/main/images/cryptopricetable.PNG)
#
Individual currencies will be stacked in the table in order to combine the plots on one chart.
#
Using yahoo finance model from here.  Pull in pricing by cryptocurrency ticker name:
#
![yah](https://github.com/jcsargis00/NFT-Research/blob/main/images/yahoo.PNG)
#
Select top 6-10 cryptocurrencies used to make NFT's from this chart.
#
![market](https://github.com/jcsargis00/NFT-Research/blob/main/images/cryptowissernftmarket.PNG)
There are 51 rows in this table, need to determine the top cryptocurrencies in the NFT marketplace from this information (website https://www.cryptowisser.com/nft-marketplaces/)
#### Machine Learning
* SciKitLearn is the ML library to create a classifier. 
* KMeans clustering algorithm to group similar currencies into classes.
* hvPlot and  Plotly  to create visualizaions in 2D and 3D as scatter plots.

#### Dashboard
In addition to using a Flask template,  D3.js will be integrated for a fully functioning and interactive dashboard. Aleda.store will show an alternative solution. A tutorial and glossary of NFT and cryptocurrency terminology will be included, with links to references.

#### Github Branch location (only 1, since I am a solo team)

https://github.com/jcsargis00/NFT-Research
#
Takes in data from the provisional database
Outputs label for input data, plots and graphs for dashboard.
