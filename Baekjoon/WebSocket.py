import yfinance as yf
ticker_list = ["A", "AAL", "AAP", "AAPL", "ABBV", "ABC", "ABMD", "ABT", "ACN", "ADBE", "ADI", "ADM", "ADP", "ADS", "ADSK", "AEE", "AEP", "AES", "AFL", "AIG", 
    "AIV", "AIZ", "AJG", "AKAM", "ALB", "ALGN", "ALK", "ALL", "ALLE", "ALXN", "AMAT", "AMCR", "AMD", "AME", "AMGN", "AMP", "AMT", "AMZN", "ANET", "ANSS",
    "ANTM", "AON", "AOS", "APA", "APD", "APH", "APTV", "ARE", "ARNC", "ATO", "ATVI", "AVB", "AVGO", "AVY", "AWK", "AXP", "BA", "BAC", "BAX", "BBY", "BDX", 
    "BEN", "BF.B", "BIIB", "BK", "BKNG", "BKR", "BLK", "BLL", "BMY", "BR", "BRK.B", "BSX", "BWA", "BXP", "C", "CAG", "CAH", "CAT", "CB", "CBOE", "CBRE", 
    "CCI", "CCL", "CDNS", "CDW", "CE", "CERN", "CF", "CFG", "CHD", "CHRW", "CHTR", "CI", "CINF", "CL", "CLX", "CMA", "CMCSA", "CME", "CMG", "CMI", "CMS", 
    "CNC", "CNP", "COF", "COG", "COO", "COP", "COST", "COTY", "CPB", "CPRI", "CPRT", "CRM", "CSCO", "CSX", "CTAS", "CTL", "CTSH", "CTVA", "CTXS", "CVS", 
    "CVX", "CXO", "D", "DAL", "DD", "DE", "DFS", "DG", "DGX", "DHI", "DHR", "DIS", "DISCA", "DISCK", "DISH", "DLR", "DLTR", "DOV", "DOW", "DRE", "DRI", 
    "DTE", "DUK", "DVA", "DVN", "DXC", "EA", "EBAY", "ECL", "ED", "EFX", "EIX", "EL", "EMN", "EMR", "EOG", "EQIX", "EQR", "ES", "ESS", "ETFC", "ETN", 
    "ETR", "EVRG", "EW", "EXC", "EXPD", "EXPE", "EXR", "F", "FANG", "FAST", "FB", "FBHS", "FCX", "FDX", "FE", "FFIV", "FIS", "FISV", "FITB", "FLIR", 
    "FLS", "FLT", "FMC", "FOX", "FOXA", "FRC", "FRT", "FTI", "FTNT", "FTV", "GD", "GE", "GILD", "GIS", "GL", "GLW", "GM", "GOOG", "GOOGL", "GPC", "GPN", 
    "GPS", "GRMN", "GS", "GWW", "HAL", "HAS", "HBAN", "HBI", "HD", "HES", "HFC", "HIG", "HII", "HLT", "HOG", "HOLX", "HON", "HP", "HPE", "HRB", "HRL", 
    "HSIC", "HST", "HSY", "HUM", "IBM", "ICE", "IEX", "IFF", "ILMN", "INCY", "INFO", "INTC", "INTU", "IP", "IPG", "IPGP", "IQV", "IR", "IRM", "ISRG", 
    "IT", "ITW", "IVZ", "J", "JBHT", "JCI", "JKHY", "JNJ", "JNPR", "JPM", "JWN", "K", "KEY", "KEYS", "KHC", "KIM", "KLAC", "KMB", "KMI", "KMX", "KO", 
    "KR", "KSS", "KSU", "L", "LDOS", "LEG", "LEN", "LH", "LHX", "LIN", "LKQ", "LLY", "LMT", "LNC", "LNT", "LOW", "LRCX", "LUV", "LVS", "LW", "LYB", 
    "LYV", "M", "MA", "MAA", "MAR", "MAS", "MCHP", "MCK", "MCO", "MDLZ", "MDT", "MET", "MGM", "MHK", "MKC", "MKTX", "MLM", "MMC", "MMM", "MNST", "MO", 
    "MOS", "MPC", "MRK", "MRO", "MS", "MSCI", "MSFT", "MTB", "MTD", "MU", "MXIM", "MYL", "NBL", "NCLH", "NDAQ", "NEE", "NEM", "NFLX", "NI", "NKE", 
    "NLOK", "NLSN", "NOC", "NOV", "NRG", "NSC", "NTAP", "NTRS", "NUE", "NVDA", "NVR", "NWL", "NWS", "NWSA", "O", "ODFL", "OKE", "OMC", "ORCL", "ORLY", 
    "OXY", "PAYX", "PBCT", "PCAR", "PEAK", "PEG", "PEP", "PFE", "PFG", "PG", "PGR", "PH", "PHM", "PKG", "PKI", "PLD", "PNC", "PNR", "PNW", "PPG", 
    "PPL", "PRGO", "PRU", "PSA", "PSX", "PVH", "PWR", "PXD", "PYPL", "QCOM", "QRVO", "RCL", "RE", "REG", "REGN", "RF", "RHI", "RJF", "RL", "RMD", 
    "ROK", "ROL", "ROP", "ROST", "RSG", "RTN", "SBUX", "SCHW", "SEE", "SHW", "SIVB", "SJM", "SLB", "SLG", "SNA", "SNPS", "SO", "SPG", "SPGI", "SRE", 
    "STE", "STT", "STX", "STZ", "SWK", "SWKS", "SYF", "SYK", "SYY", "T", "TAP", "TEL", "TFC", "TFX", "TGT", "TIF", "TJX", "TMO", "TMUS", "TPR", 
    "TROW", "TRV", "TSCO", "TSN", "TTWO", "TWTR", "TXN", "TXT", "UA", "UAA", "UAL", "UDR", "UHS", "ULTA", "UNH", "UNM", "UNP", "UPS", "URI", "USB", 
    "UTX", "V", "VAR", "VFC", "VIAC", "VLO", "VMC", "VNO", "VRSK", "VRTX", "VTR", "VZ", "WAB", "WAT", "WBA", "WDC", "WEC", "WELL", "WFC", "WHR", 
    "WLTW", "WM", "WMB", "WMT", "WRB", "WRK", "WU", "WY", "WYNN", "XEC", "XEL", "XLNX", "XOM", "XRAY", "XRX", "XYL", "ZBH", "ZBRA", "ZION", "ZTS"
]

sector_list=[]

for tik in ticker_list:
    ticker=yf.Ticker(tik)
    sector=ticker.info.get['']
    sector_list.append(sector)
    
print(sector_list)