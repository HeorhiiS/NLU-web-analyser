# NLU web analyser
Website analyser for market prediction or other purposes using IBM Watson NLU
## -------------------------------------------------------------------------------
#### Supported languages: Arabic, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish






#### Introductory info: This tool is an analyser for website's data. Original conept is the idea of additional tool for market analysis, however the overall potential is much broader. In a nutshell, webcrawler or other methods of scraping website are used to get the data which is then uses IBM's powerful framework, hence is sent to Watson for analytics. The result returns the sentiment analysis along with other useful data like concepts, emotions and keywords. Furthermore this process becomes automated and instant, allowing for incredibly fast predictions and actions.

Before you start the following are required:

* Matplotlib library
* Json library
* IBM cloud account and access to NLU service as well as required libraries ---> see Watson NLU API guide for more
* Urllib library
* BeautifulSoup4 library (for Python 3.6X and later)



## ------------------------------------------------------------------------------




#### Crawler ---> Web Data ---> Analyser ---> Watson NLU ---> Analyser ---> Graph (Final data output) 





##### In application (example: Cryptocurrency): Web crawler or scrapper gets the news report holding HTML data, this data is converted and sent to Watson, with analytics Watson determines if news is negative or positive along with other useful data that can be used for further analytics. If news on crypto are negative then market as volatile as it is is likely to drop (prices per unit crypto), positive is obviously opposite. (THIS IS A PREDICTION NOT A GUARANTEE).













#### IT IS HIGLY SUGGESTED YOU USE THIS CONCEPT AS AN INSPIRATION AND BUILD UPON IT YOUR CUSTOM TOOLS THAT MIGHT BE SUITABLE FOR YOUR NEEDS.










##### Important Note 1: This code is tailored to the application mentioned above (Cryptocurrency), can be expanded to trading and more;




##### Important Note 2: Suggested use includes improving trading bot agorithms and strategies. 




##### Update Note: Pie chart used to display data
