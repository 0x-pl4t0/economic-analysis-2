# economic-analysis-2
# Currency Strength and Mutual Fund Pricing Analysis

This Python project aims to analyze economic data to price the strength of currencies against each other, identify discrepancies, and assess mutual fund performance. The goal is to offer insights into the valuation of currencies and investment portfolios using economic indicators and market data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Dependencies](#dependencies)
- [License](#license)
- [Contact](#contact)

## Installation

To get started with this project, ensure you have Python installed on your system. It is recommended to use a virtual environment for managing dependencies.

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/currency-strength-mutual-funds.git
    ```

2. Navigate into the project directory:
    ```bash
    cd currency-strength-mutual-funds
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the analysis, use the provided scripts. Below is a brief overview of how to use each component:

1. **Currency Strength Analysis**  
   The `currency_strength.py` script calculates the strength of various currencies based on economic data such as GDP, inflation rates, and interest rates. It identifies discrepancies in currency strength by comparing historical data.

   ```bash
   python currency_strength.py
   ```

   Outputs:  
   - Currency Strength Comparison Graph
   - Discrepancy Identifications

2. **Mutual Fund Performance Analysis**  
   The `mutual_fund_analysis.py` script processes data related to mutual fund performance, including returns, risks, and correlations with currency fluctuations. It can provide insights into how currency strength affects mutual fund pricing.

   ```bash
   python mutual_fund_analysis.py
   ```

   Outputs:  
   - Mutual Fund Return and Risk Metrics
   - Currency Impact on Mutual Fund Performance

3. **Economic Data Fetcher**  
   The `data_fetcher.py` script helps download the latest economic data from reliable sources (e.g., World Bank, IMF, or other APIs). Ensure you have an API key for data sources when required.

   ```bash
   python data_fetcher.py
   ```

   Outputs:  
   - Downloaded Economic Data Files (CSV, JSON, etc.)

## Data Sources

This project uses multiple data sources to ensure accurate and up-to-date economic information:

- **World Bank Economic Indicators**  
- **International Monetary Fund (IMF) Data**
- **Bloomberg or Yahoo Finance for Currency Exchange Rates**  

Ensure that you have access to APIs or downloaded datasets from these sources.

## Dependencies

This project uses several Python libraries for data analysis, visualization, and machine learning. Install the required libraries with:

```bash
pip install -r requirements.txt
```

Some of the key dependencies include:
- pandas
- numpy
- matplotlib
- requests
- scikit-learn
- statsmodels

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to open an issue or contact me directly:

- Email: krmolebatsi@icloud.com
- GitHub: [your-github-profile](https://github.com/0x-pl4t0)
