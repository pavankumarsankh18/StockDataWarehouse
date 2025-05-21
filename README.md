# StockDataWarehouse
This repository will have code to get stock data from Kite API, store them in a structured format in postgress database.

* To get Access Token
    * Login - https://kite.trade/connect/login?api_key=6y7l2lw9p8d3tlqf
    * Copy Access Token,
        access_token = LxDR1L07mNqBXLV96bhmeIemNRbd550t

    * api_key=your_api_key
    * request_token=abc123
    * checksum=sha256(api_key + request_token + api_secret)


341249,1333,HDFCBANK,"HDFC BANK",0,,0,0.1,1,EQ,NSE,NSE
779521,3045,SBIN,"STATE BANK OF INDIA",0,,0,0.05,1,EQ,NSE,NSE
738561,2885,RELIANCE,"RELIANCE INDUSTRIES",0,,0,0.1,1,EQ,NSE,NSE


