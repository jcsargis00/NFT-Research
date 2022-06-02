![cryp](https://github.com/jcsargis00/NFT-Research/blob/main/images/cryptotypes.PNG)
#
# NFT Energy Consumption, Environmental Concerns and Price Volatility
### Using Databases and Machine Learning for Cryptocurrency Energy Consumption and Price Volatility Research
#### Importance of Topic
##### NFTs are created using blockchain and many are connected to cryptocurrency.  The environmental concern comes from the estimated carbon footprint generated by the power plants providing the energy used to mine NFTs. In addition to mining, a single Bitcoin transaction is estimated to burn 2,292.5 kilowatt hours of electricity, enough to power a typical US household for over 78 days.   More and more computing power is needed to mine bitcoin, which requires more and more electricity. ASICs can be used to supercharge your mining, which uses even more electricity, and if Bitcoin's price rises, it becomes even more profitable to mine, which causes more miners to jump into the game.  Ref. PC Magazine,John Bogna https://www.pcmag.com/how-to/what-is-the-environmental-impact-of-cryptocurrency
### Outline    
#### Presentation
* Glossary - Let's start with explaining the terminology in plain English with examples
* Why do cryptocurrencies use so much energy?  Let's research how this works
* Why does NFT minting with cryptocurrency use so much energy?
* Which cryptocurrencies are used the most to mint NFTs?
* Do the most used cryptocurrencies use a lot of energy?  Are their prices volatile?  Let's look at the data
* Is cryptocurrency volatile?  Let's look at the data of the top 10 cryptocurrencies and scrape CoinGecko, CoinCapMarket and a few other sites for data
* Do NFTs use a lot of energy to mint?
* Can we predict future energy usage using Machine Learning?
#
#### Let's start with a glossary (Ref. Investopedia https://www.investopedia.com/)
![volt](https://github.com/jcsargis00/NFT-Research/blob/main/images/voltaire.png)
##### Glossary
* Beeple - Pseudonym for Mike Winkelmann, perhaps the most well known digital artist. Beeple’s Everydays: the First 5000 Days sold for $69,400,000, the current record for most expensive NFT.
##### Beeple's Everydays: the First 5000 Days
![beep](https://github.com/jcsargis00/NFT-Research/blob/main/images/everyday.PNG)
* Bitcoin (with a capitalised B) - an open software protocol and peer-to-peer (P2P) network that enables users to transact online without relying on trusted intermediaries. The system is permissionless since it operates without a central authority, allowing anyone in the world to send, store, and receive digital tokens of value without prior approval.
* Bitcoin blockchain is the public ledger that records all Bitcoin transactions. Effectively a shared database, it is collectively maintained by tens of thousands of computers called full nodes. The ledger is organised using a particular data structure which bundles transactions into a data block that is cryptographically linked to the previous block. Over time, this process results in a growing chain of blocks that is extended by special actors called miners, who append new blocks in anticipation of financial rewards. The use of this specific data structure ensures that tampering with the transaction history (e.g. modifying past transactions) will be detected immediately by other network participants as the linked block hashes do not add up.
* Binance Smart Chain - A blockchain compatible with buying and selling NFTs. While Ethereum is the most popular blockchain for NFTs, prominent competitors include Binance, Flow, and Tron.
* Bored Ape Yacht Club (BAYC) - a non-fungible token (NFT) collection built on the Ethereum blockchain. The collection features profile pictures of cartoon apes that are procedurally generated by an algorithm.  Famous Bored Ape Owners include Serena Williams, Justin Bieber, Steph Curry, Tom Brady
###### Steph Curry Bored Ape NFT - purchase price $180,000
![curry](https://github.com/jcsargis00/NFT-Research/blob/main/images/curry.PNG)
* Cryptocurrency - cryptocurrency, crypto-currency, crypto, or coin is a digital currency designed to work as a medium of exchange through a computer network that is not reliant on any central authority, such as a government or bank, to uphold or maintain it.
* CryptoPunk - A unique collectible avatar stored on Ethereum. There are three CryptoPunks listed in the top 10 most expensive NFTs ever sold.
###### CryptoPunk NFTs
![punk](https://github.com/jcsargis00/NFT-Research/blob/main/images/punks.PNG)
* Digital Wallet (or electronic wallet) - a financial transaction application that runs on mobile devices. It securely stores your payment information and passwords. These applications allow you to pay when you're shopping using your device so that you don't need to carry your cards around. You enter and store your credit card, debit card, or bank account information and can then use your device to pay for purchases.
* Discord - An instant messaging platform and the go-to place for discussing NFTs.
* ERC-721 - A token standard that allows for the creation of unique, non-fungible tokens. It differs from ERC-20, for example, which is used to mint fungible tokens.
* Ethereum - A blockchain with smart contract functionality. Ethereum is currently the main platform for NFT projects.
* Floor price - The lowest NFT price in any given category of NFTs. To “buy the floor” is to buy the cheapest NFT in a project / collection.
* Fractional ownership - Partial ownership rights over an NFT. Sellers can sell percentages of a work and buyers can buy what they can afford.
* Fungibility - Replaceability. Dollars are fungible because a dollar owed can be paid using any dollar in existence. Something that is non-fungible, like a painting, is one-of-a-kind.
* Gas fees - Fees that blockchain users pay to compensate for the computational resources used to execute transactions. Gas fees, which are largely specific to Ethereum, ensure that transactions will be genuine and discourages bad actors from spamming the network with a high volume of transactions.
* Hashmasks - Digital paintings made by a global team of 70 artists. Hashmasks are unique because consumers have some control over the art. According to the Hashmasks Manifesto, “Each holder has the ability to contribute to the completion of the art piece by giving a name of their preference to the Hashmasks they hold via the Name Change Token (NCT)”.
* Metadata - The collection of data that defines ownership and differentiates one NFT from another. Metadata can be on-chain or off-chain.  
* Metaverse - A virtual 3D world where people can interact. Popular blockchain-based environments that comprise the metaverse include Decentraland and The Sandbox, virtual gaming worlds where users can buy and sell land as NFTs.
* Mining - The method by which Bitcoin and other cryptocurrencies are generated and the transactions involving new coins are verified is known as mining. It entails massive, decentralised networks of computers all over the world that verify and safeguard blockchains, which are virtual ledgers that record crypto transactions.
* Minting - The process by which an NFT becomes part of the blockchain. Once an asset is put on the blockchain, it is “minted” as a token and cannot be altered.
* NFT - A non-fungible token is a financial security consisting of digital data stored in a blockchain, a form of distributed ledger. The ownership of an NFT is recorded in the blockchain, and can be transferred by the owner, allowing NFTs to be sold and traded.
* OpenSea - Launched in 2018, OpenSea is the first and largest NFT marketplace, boasting four million assets and 135+ DApps.
* Proof-of-work puzzle -Solving the proof-of-work puzzle requires miners to exhaust all possible options until a random number — called a nonce in technical jargon — is found that meets the network difficulty target. Rather than guessing numbers manually, miners use special hardware equipment to quickly generate potential solutions.
* Rarible - A community-owned NFT marketplace founded in 2020. The Moscow-based platform mostly hosts digital art, and is fuelled by its native ERC-20 token RARI.
* Royalties - Money earned by an NFT creator through the token’s resale. Some NFTs automatically pay royalties each time an NFT is sold. An NFT can be hardcoded to pay an artist royalties forever, an interesting use case that has the potential to shake up the music industry.
* Smart Contract - A self-executing digital contract. NFTs are composed of code written in smart contract programming language like Solidity.
*  ASIC (application-specific integrated circuit) - a microchip designed for a special application, such as a particular kind of transmission protocol or a hand-held computer. You might contrast it with general integrated circuits, such as the microprocessor and the random access memory chips in your PC.

### Why Cryptocurrencies Use So Much Energy
![kugler](https://github.com/jcsargis00/NFT-Research/blob/main/images/kugler.png)
##### Bitcoin Carbon Footprint Calculations
![digi](https://github.com/jcsargis00/NFT-Research/blob/main/images/somuchenergy.PNG)
### **"Some people wonder if cryptocurrencies will disrupt the financial system, while others wonder if they will break the environment in the process."**  
#### Why does NFT minting with cryptocurrency use so much energy?
##### How does minting work?
![bite](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinexp.png)
#
Does Ethereum use a lot of energy?
![ethu ](https://github.com/jcsargis00/NFT-Research/blob/main/images/globalethm.PNG)
#
![eth](https://github.com/jcsargis00/NFT-Research/blob/main/images/visa.png)  
#
![ethuse](https://github.com/jcsargis00/NFT-Research/blob/main/images/eth_energy_usage_by_country.png)
#
![bituse](https://github.com/jcsargis00/NFT-Research/blob/main/images/btc_energy_usage_by_country.png)
#
![bit](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinenergy.PNG)
#

![rank](https://github.com/jcsargis00/NFT-Research/blob/main/images/userrankcountry.PNG)
### Ethereum prices are highly volatile and have been for quite some time.
#### 'Potential big move' - but not necessarily up - Ref. Coindesk 9/14/2021
Investors are expecting more volatility in Ethereum (ETH) compared with Bitcoin (BTC), according to a key metric, with the measure of risk at a six-month high amid a boom in decentralized finance (DeFi).
* The three-month spread between Ethereum's volatility and Bitcoin's has risen to 29%, the highest level since Feb. 23, according to data source Skew.  
* The metric, which tracks the difference in implied volatility for at-the-money options in both cryptocurrencies, has risen from -2.4% to 29% in two months. 
* Implied volatility is calculated from options prices and shows the market's opinion of the underlying asset’s potential moves. It is often considered a proxy of market risk.  
#
![ethvola](https://github.com/jcsargis00/NFT-Research/blob/main/images/skew.PNG)
#
![shiraz](https://github.com/jcsargis00/NFT-Research/blob/main/images/shiraz.PNG)
#
### Bitcoin prices are highly volatile.
#
![yah](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinyahoo.png)
#
### How is energy consumed by Bitcoin calculated?
![proc](https://github.com/jcsargis00/NFT-Research/blob/main/images/bitcoinprocess.PNG)
#
### WHAT IS THE REAL CARBON FOOTPRINT OF THE BLOCKCHAIN?
- Proof-of-work blockchain networks consume a very large amount of energy, which results in a very large amount of carbon being emitted. 
- Best estimates place bitcoin around 45.8 TWh, emitting around 45,800,000 Tonnes of CO2 per year. 
- The annual power consumption from Ethereum activity is estimated to be 9.62TWh from September '19 - '20.
##### Ref. Stoll et al., The Carbon Footprint of Bitcoin (2019), digiconomist.net/ethereum-energy-consumption
#
#### Types of Datasets needed for research
* Financial
* Environmental
### Cryptocurrency Price Tracking
Financial Dataset 
- Cryptocurrency Prices by Market Cap - source Coin Gecko
- Cryptocurrency Historical Prices from Yahoo Finance
![geck](https://github.com/jcsargis00/NFT-Research/blob/main/images/coingecko.PNG)
- The global cryptocurrency market cap today (5/26/22) is $1.29 Trillion, a -3.0% change in the last 24 hours.
#### Top 10 Cryptocurrencies
![market](https://github.com/jcsargis00/NFT-Research/blob/main/images/crypmarketcapprice.PNG)
### Financial Data from Coin Gecko
#### BTC Price Today
- Bitcoin price today is $29,069.36 with a 24-hour trading volume of $34,128,213,186. 
- BTC price is down -2.6% in the last 24 hours. 
- It has a circulating supply of 19 Million BTC coins and a total supply of 21 Million. 
- Bitcoin hit an all time high of $69,044.77 on Nov 10, 2021 (7 months).
- Bitcoin had an all time low of $67.81 on Jul 06, 2013 (almost 9 years).
![btceth](https://github.com/jcsargis00/NFT-Research/blob/main/images/btcethpricechart.PNG)
#### ETH Price Today
- Ethereum price today is $1,773.90 with a 24-hour trading volume of $26,337,907,422. 
- ETH price is down -8.8% in the last 24 hours. 
- It has a circulating supply of 120 Million ETH coins and a total supply of ∞.
- Ethereum hit an all time high of $4,878.26 on Nov 10, 2021 (7 months).
- Ethereum had an all time low of $0.432979 on Oct 20, 2015 (over 6 years).
#
![ethbtc](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethbtcprice.PNG)
#
![corr](https://github.com/jcsargis00/NFT-Research/blob/main/images/cryptocorrelation.PNG)
#### Bitcoin Data Mining Map - world locations  Ref-Cambridge Bitcoin Electricity Consumption Index
![map](https://github.com/jcsargis00/NFT-Research/blob/main/images/btcmap.PNG)
#
![hash](https://github.com/jcsargis00/NFT-Research/blob/main/images/hashrate2.PNG)
#
![country](https://github.com/jcsargis00/NFT-Research/blob/main/images/country.PNG)
#
![states](https://github.com/jcsargis00/NFT-Research/blob/main/images/states.PNG)
### Financial Data on Cryptocurrency from Yahoo Finance API
Data for the top ten cryptocurrencies was downloaded and put in data frames.
#
Ethereum DataFrame
#
![ethp](https://github.com/jcsargis00/NFT-Research/blob/main/images/ticketh.PNG)
#
Ethereum Simple plot of prices over 10 years
#
![ethp](https://github.com/jcsargis00/NFT-Research/blob/main/images/tickethplot.PNG)
#
Ethereum Trading volume added to plot
#
![ethp](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethvolume.PNG)
Ethereum Candlestick plot
#
![ethp](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethcandle.PNG)
#
#### Environmental sources pertaining to energy usage
#
Ethereum Emission Tracker
#
![emi](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethem.png)
#
![emi2](https://github.com/jcsargis00/NFT-Research/blob/main/images/ethem2.PNG)
#
### Electric energy consumption prediction using Machine Learning Household Electricity consumption https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set?resource=download
#
#### Database - Postgres and Entity Relationship Diagram
##### ERD 
![erd](https://github.com/jcsargis00/NFT-Research/blob/main/images/erd.PNG)
#
#### Dataset repository directory
https://github.com/jcsargis00/NFT-Research/tree/main/Resources/data
#
### Machine Learning application 
Electric energy consumption prediction using Machine Learning Household Electricity consumption 
##### Data source https://www.kaggle.com/datasets/uciml/electric-power-consumption-data-set?resource=download
They were measurements of electric power consumption in one household with a one-minute sampling rate over almost 4 years, from December 2006 to November 2010. Different electrical quantities and some sub-metering values were available.  Power consumption data was collected every minute.  The dataset is a multivariate time series.
##### Schema for the data
- date
- time
- global_active_power: The total active power consumed by the household (kilowatts).
- global_reactive_power: The total reactive power consumed by the household (kilowatts).
- voltage: Average voltage (volts).
- global_intensity: Average current intensity (amps).
- sub_metering_1: Active energy for the kitchen (watt-hours of active energy).
- sub_metering_2: Active energy for laundry (watt-hours of active energy).
- sub_metering_3: Active energy for climate control systems (watt-hours of active energy).
##### LSTM model was built to predict household electric power consumption. Dropout layers were added to improve the model.  The first year of data (resampled over an hour) was used to train the model and the rest of the data to test the model to reduce the computation time and get some results quickly.
##### Which model did you choose and why?
* Simple Regression/ Clustering, good fit for the  problem.  After plotting each ticker over a period of time, we can use machine learning to predict future pricing.  This calculation will also be performed on energy consumption versus popularity of NFTs, to predict future energy consumption.  Finally, an alternative solution will be presented to create NFTs with green technology.
#
How are you training your model?
* After scaling, 75% of data was used for training, 25% of data was used for testing
#
What is the model's accuracy? 
#
How does this model work? 
### Github communication protocols
I am working solo and performing all of the 4 roles.
* Square role will be responsible for setting up the repository. This includes naming the repository and adding team members, which is just me.
* Triangle role - responsible for creating a simple machine learning model. Creating a simple model this early in the design process helps a team better understand where and how a machine learning model will fit into the project. This also grants more time to work out the specifics related to machine learning.
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
- Postgres
#
#### Data Cleaning and Analysis
* Data Preprocessing involved selection, transformation, and scaling of data.  Pandas was used to clean the data, replace null values and perform an exploratory analysis.

#### Database Storage
* Postgres is the database for energy usage.
* There are 6 tables in the  database, four for power consumption tracking (environmental) and 2 for cyptocurrency price tracking (financial).
The tables include fields for energy usage and price changes
* Python was used to download the data from the Coinbase web site
* Database was created with a table named power for power consumption data
* Data was transformed and then imported into the power table in Postgresql
* A power_id column with incremental integer numbering was added for a primary key
* The data for the date column needed to be converted from the European convention of DD/MM/YYY to MM/DD/YYYY
* SQL commands used to tranform the date column.  
![dates](https://github.com/jcsargis00/NFT-Research/blob/main/images/sqldates.PNG)
* schema for table power
![tabsc](https://github.com/jcsargis00/NFT-Research/blob/main/images/powerschema.PNG)
* sample data in the database table
![table](https://github.com/jcsargis00/NFT-Research/blob/main/images/powertable.PNG)
* number of rows in table power
#
![rows](https://github.com/jcsargis00/NFT-Research/blob/main/images/powerrows.PNG)
#### Postgres is also the database for cryptocurrency pricing.
Fields of crypto pricing  model
- Symbol -  symbol for which the timeseries data refers
- Open -  the opening price of the time period
- High -  the highest price of the time period
- Low -  the lowest price of the time period
- Close - This is the closing price of the time period
- Volume (Crypto) - the volume in the transacted Ccy. Ie. For BTC/USD, this is in BTC amount
- Volume Base Ccy - the volume in the base/converted ccy. Ie. For BTC/USD, this is in USD amount
#### Postgres sample table of crypto pricing model
![pri](https://github.com/jcsargis00/NFT-Research/blob/main/images/cryptopricetable.PNG)
#### Using yahoo finance model from here.  Pull in pricing by cryptocurrency ticker name:
![yah](https://github.com/jcsargis00/NFT-Research/blob/main/images/yahoo.PNG)
#### Select top 6-10 cryptocurrencies used to make NFT's from this chart.
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

Summary and Followup Questions:
* Is energy used related to cryptocurrency price fluctuations?
* Can we predict how much energy will be used in the  future using machine learning?
* Is this an environmental concern?
* If it is, is there an eco friendly solution for NFT minting without cryptocurrency?
