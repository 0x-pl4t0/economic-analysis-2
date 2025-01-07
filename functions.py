import pandas as pd
import yfinance as yf
from fredapi import fred
import seaborn as sns
import matplotlib.pyplot as plt
import functions as fncts
import numpy as np

import pandas as pd

def fetch_economic_data_helper(country_code, indicators, fred):
    """
    Fetches economic data for the given indicators and resamples them to yearly frequency.
    Args:
    - country_code: The country code (e.g., 'US').
    - indicators: A dictionary of indicators where keys are indicator names and values are FRED series IDs.
    - fred: A FRED object to retrieve data from.
    
    Returns:
    - A pandas DataFrame with yearly resampled data for the requested indicators.
    """
    data = {}
    
    for indicator, series in indicators.items():
        try:
            # Fetch the time series data
            series_data = fred.get_series(series)
            
            # Resample the data to yearly frequency (using the mean for aggregation)
            series_data_yearly = series_data.resample('Y').mean()
            
            # Store the resampled data in the dictionary
            data[indicator] = series_data_yearly
            
        except Exception as e:
            print(f"Warning: No valid data for {series} - {e}")
            data[indicator] = pd.Series(dtype='float64')
    
    # Return the data as a DataFrame
    return pd.DataFrame(data)

# Example usage
indicators = {
    'GDP': 'GDP',
    'CPI': 'CPIAUCSL',  # Consumer Price Index
    'Unemployment': 'UNRATE'  # Unemployment Rate
}

# Assuming 'fred' is an initialized FRED object from the `fredapi` package
# data = fetch_economic_data_helper('US', indicators, fred)

# Print the data to verify
# print(data)




# Define economic indicators and NASDAQ Composite ticker
economic_indicators = {
    'US': {
        'interest_rate': 'FEDFUNDS',  # US Federal Funds Rate
        'cpi': 'CPIAUCSL',  # US Consumer Price Index
        'pci': 'PCEPI',  # US Personal Consumption Expenditures Index
        'GDP': 'GDP'  # NASDAQ Composite Index
    },
    'UK': {
        'interest_rate': 'BOERAI',  # Bank of England Rate
        'cpi': 'GBRCPIALLMINMEI',  # UK CPI
        'pci': 'GBRPFI',  # Placeholder for PCI or related indicator
        'GDP': 'GDP'  # FTSE as a proxy
    },
    'Germany': {
        'interest_rate': 'IR3TIB01DEM156N',  # Germany 3-Month Interbank Rate
        'cpi': 'DEUCPIALLMINMEI',  # Germany CPI
        'pci': 'DEUPCE',  # Germany PCE
        'GDP': 'GDP'  # DAX Index
    },
    'Japan': {
        'interest_rate': 'JPNIR3TIB01STM',  # Japan Interbank Rate
        'cpi': 'JPNCPIALLMINMEI',  # Japan CPI
        'pci': 'JPNPCE',  # Japan PCE
        'nasdaq': '^N225'  # Nikkei 225
    },
    'Canada': {
        'interest_rate': 'IR3TIB01CAM156N',  # Canada 3-Month Interbank Rate
        'cpi': 'CPALCY01CAM661N',  # Canada CPI
        'pci': 'CANPCE',  # Canada PCE
        'nasdaq': '^GSPTSE'  # S&P/TSX Composite Index
    },
    'France': {
        'interest_rate': 'IR3TIB01FRM156N',  # France 3-Month Interbank Rate
        'cpi': 'FRCPIALLMINMEI',  # France CPI
        'pci': 'FRAPCE',  # France PCE
        'nasdaq': '^FCHI'  # CAC 40 Index
    },
    'Australia': {
        'interest_rate': 'IR3TIB01AUM156N',  # Australia 3-Month Interbank Rate
        'cpi': 'AUCPIALLMINMEI',  # Australia CPI
        'pci': 'AUSPCE',  # Australia PCE
        'nasdaq': '^AXJO'  # ASX 200
    },
    'China': {
        'interest_rate': 'CHNIR',  # China Interest Rate
        'cpi': 'CHNCPIALLMINMEI',  # China CPI
        'pci': 'CHNPCE',  # China PCE
        'nasdaq': '000001.SS'  # SSE Composite Index
    },
    'India': {
        'interest_rate': 'INDIR',  # India Interest Rate
        'cpi': 'INDCPIALLMINMEI',  # India CPI
        'pci': 'INDPCE',  # India PCE
        'nasdaq': '^BSESN'  # BSE Sensex
    },
    'Brazil': {
        'interest_rate': 'BRIR',  # Brazil Interest Rate
        'cpi': 'BRACPIALLMINMEI',  # Brazil CPI
        'pci': 'BRAPCE',  # Brazil PCE
        'nasdaq': '^BVSP'  # Bovespa Index
    },
    'Russia': {
        'interest_rate': 'RUIR',  # Russia Interest Rate
        'cpi': 'RUCPIALLMINMEI',  # Russia CPI
        'pci': 'RUPCE',  # Russia PCE
        'nasdaq': 'IMOEX.ME'  # MOEX Russia Index
    },
    'Italy': {
        'interest_rate': 'ITIR',  # Italy Interest Rate
        'cpi': 'ITCPIALLMINMEI',  # Italy CPI
        'pci': 'ITPCE',  # Italy PCE
        'nasdaq': '^FTSEMIB'  # FTSE MIB
    },
    'South Korea': {
        'interest_rate': 'KORIR',  # South Korea Interest Rate
        'cpi': 'KORCPIALLMINMEI',  # South Korea CPI
        'pci': 'KORPCE',  # South Korea PCE
        'nasdaq': '^KS11'  # KOSPI
    },
    'Mexico': {
        'interest_rate': 'MXIR',  # Mexico Interest Rate
        'cpi': 'MXCPIALLMINMEI',  # Mexico CPI
        'pci': 'MXPCE',  # Mexico PCE
        'GDP': 'GDP' # IPC Mexico Index
    }
}