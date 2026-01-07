from langchain_tavily import TavilySearch
from langchain_core.tools import tool
import yfinance as yf 
from dotenv import load_dotenv
load_dotenv(".env")
import os
search = TavilySearch(max_results =  3)
@tool
def web_search(query: str):
    """
    Searches the web for financial news, stock trends, and risk factors.
    Use specific queries like 'NVIDIA stock risks' or 'NVIDIA growth catalysts'.
    """
    search = TavilySearch(max_results=5) 
    return search.run(query)
@tool 
def get_market_data(ticker: str):
    """
    Fetches comprehensive real-time market data for a given stock symbol.
    Provides price, market cap, P/E ratio, and technical trends.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        data = {
            "Price": info.get("currentPrice"),
            "Market_Cap": info.get("marketCap"),
            "PE_Ratio": info.get("trailingPE"),
            "52_Week_High": info.get("fiftyTwoWeekHigh"),
            "52_Week_Low": info.get("fiftyTwoWeekLow"),
            "Average_Volume": info.get("averageVolume"),
            "Recommendation": info.get("recommendationKey"),
            "Currency": info.get("currency")
        }
        return data
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"