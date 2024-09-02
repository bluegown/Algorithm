import yfinance as yf
ticker_list = [
    "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "BRK.B", "NVDA", "JPM", "JNJ", "V", 
    "WMT", "PG", "UNH", "DIS", "MA", "HD", "PYPL", "BAC", "VZ", "ADBE", 
    "CMCSA", "NFLX", "PFE", "KO", "PEP", "MRK", "INTC", "T", "ABBV", "XOM", 
    "CVX", "CSCO", "MCD", "NKE", "ABT", "WFC", "LLY", "DHR", "CRM", "ORCL", 
    "ACN", "MDT", "LIN", "UPS", "NEE", "PM", "QCOM", "COST", "TXN", "AVGO"
]

# 심볼을 TradingView 형식으로 변환
symbol_list = []

for tik in ticker_list:
    ticker = yf.Ticker(tik)
    exchange = ticker.info.get('exchange', '')
    if exchange == 'NMS':  # NASDAQ
        symbol_list.append(f'NASDAQ:{tik}')
    elif exchange == 'NYQ':  # NYSE
        symbol_list.append(f'NYSE:{tik}')
    else:
        symbol_list.append(tik)  # 기타 거래소

print(symbol_list)