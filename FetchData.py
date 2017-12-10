import pandas as pd
import urllib, json
def FetchDailyData(equity,export=False):
    #Equity: NVIDIA=NVDA, Alibaba=BABA, Amazon=AMZN
    #get the last 20 years historical price(Open,high,low,close,volume)
    #return data: csv
    url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=7KPKL1K4Y014KDOF&datatype=csv&outputsize=full&symbol="+equity
    DailyPrice = pd.read_csv(url)

    #fetch daily SMA
    #return data: Json
    urlSMA="https://www.alphavantage.co/query?function=SMA&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    ResponseSMA = urllib.urlopen(urlSMA)
    SMA = json.loads(ResponseSMA.read())
    SMA=SMA["Technical Analysis: SMA"]
    #temp array
    ArraySMA=[]
    for key in SMA.keys():
        ArraySMA.append((key,float(SMA[key]["SMA"])))
    DfSMA=pd.DataFrame(ArraySMA,columns=["Date","SMA"])
    DfSMA=DfSMA.sort_values("Date",ascending=False)

    #fetch daily RSI
    #return data: Json
    urlRSI="https://www.alphavantage.co/query?function=RSI&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlRSI)
    RSI = json.loads(response.read())
    RSI=RSI["Technical Analysis: RSI"]
    #temp array
    ArrayRSI=[]
    for key in RSI.keys():
        ArrayRSI.append((key,float(RSI[key]["RSI"])))
    DfRSI=pd.DataFrame(ArrayRSI,columns=["Date","RSI"])
    DfRSI=DfRSI.sort_values("Date",ascending=False)

    #fetch daily ADX
    #return data: Json
    urlADX="https://www.alphavantage.co/query?function=ADX&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlADX)
    ADX = json.loads(response.read())
    ADX=ADX["Technical Analysis: ADX"]
    #temp array
    ArrayADX=[]
    for key in ADX.keys():
        ArrayADX.append((key,float(ADX[key]["ADX"])))
    DfADX=pd.DataFrame(ArrayADX,columns=["Date","ADX"])
    DfADX=DfADX.sort_values("Date",ascending=False)

    #fetch daily EMA
    #return data: Json
    urlEMA="https://www.alphavantage.co/query?function=EMA&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlEMA)
    EMA = json.loads(response.read())
    EMA=EMA["Technical Analysis: EMA"]
    #temp array
    ArrayEMA=[]
    for key in EMA.keys():
        ArrayEMA.append((key,float(EMA[key]["EMA"])))
    DfEMA=pd.DataFrame(ArrayEMA,columns=["Date","EMA"])
    DfEMA=DfEMA.sort_values("Date",ascending=False)

    #fetch daily CCI
    #return data: Json
    urlCCI="https://www.alphavantage.co/query?function=CCI&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlCCI)
    CCI = json.loads(response.read())
    CCI=CCI["Technical Analysis: CCI"]
    #temp array
    ArrayCCI=[]
    for key in CCI.keys():
        ArrayCCI.append((key,float(CCI[key]["CCI"])))
    DfCCI=pd.DataFrame(ArrayCCI,columns=["Date","CCI"])
    DfCCI=DfCCI.sort_values("Date",ascending=False)

    #fetch daily AROON
    #return data: Json
    urlAROON="https://www.alphavantage.co/query?function=AROON&interval=daily&time_period=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlAROON)
    AROON = json.loads(response.read())
    AROON=AROON["Technical Analysis: AROON"]
    #temp array
    ArrayAROON=[]
    for key in AROON.keys():
        ArrayAROON.append((key,float(AROON[key]["Aroon Down"]),float(AROON[key]["Aroon Up"])))
    DfAROON=pd.DataFrame(ArrayAROON,columns=["Date","AROONDOWN","AROONUP"])
    DfAROON=DfAROON.sort_values("Date",ascending=False)

    #fetch daily MACD
    #return data: Json
    urlMACD="https://www.alphavantage.co/query?function=MACD&interval=daily&fastperiod=15&slowperiod=30&series_type=close&apikey=7KPKL1K4Y014KDOF&&outputsize=full&datatype=csv&symbol="+equity
    response = urllib.urlopen(urlMACD)
    MACD = json.loads(response.read())
    MACD=MACD["Technical Analysis: MACD"]
    #temp array
    ArrayMACD=[]
    for key in MACD.keys():
        ArrayMACD.append((key,float(MACD[key]["MACD"]),float(MACD[key]["MACD_Hist"]),float(MACD[key]["MACD_Signal"])))
    DfMACD=pd.DataFrame(ArrayMACD,columns=["Date","MACD","MACD_Hist","MACD_Signal"])
    DfMACD=DfMACD.sort_values("Date",ascending=False)

    #Add all data together and return
    df=pd.DataFrame(columns=["SMA","RSI","ADX","EMA","CCI","AROONDOWN","AROONUP","MACD","MACD_Hist","MACD_Signal"])
    DailyPrice["SMA"]=DfSMA["SMA"]
    DailyPrice["RSI"]=DfRSI["RSI"]
    DailyPrice["ADX"]=DfADX["ADX"]
    DailyPrice["EMA"]=DfEMA["EMA"]
    DailyPrice["CCI"]=DfCCI["CCI"]
    DailyPrice["AROONDOWN"]=DfAROON["AROONDOWN"]
    DailyPrice["AROONUP"]=DfAROON["AROONUP"]
    DailyPrice["MACD"]=DfMACD["MACD"]
    DailyPrice["MACD_Hist"]=DfMACD["MACD_Hist"]
    DailyPrice["MACD_Signal"]=DfMACD["MACD_Signal"]
    if export:
        DailyPrice.to_csv(equity)
    return DailyPrice
