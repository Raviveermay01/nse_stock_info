from flask import Flask, render_template
from scrapy.http import HtmlResponse
import requests

stock = Flask (__name__)


@stock.route("/stock_data")


@stock.route("/stocks/<name>", methods=["GET"])
def stock_data(name):
    
   
    return_data = {}

    
    cookies = {
    'GUC': 'AQEBBwFjS4ljdkIjdwUV&s=AQAAAJlr_b9r&g=Y0pDkg',
    'A1': 'd=AQABBDfqKmMCEKXvQNUUY5ctSrvbbUi1e_oFEgEBBwGJS2N2Y1lQb2UB_eMBAAcIN-oqY0i1e_o&S=AQAAAuNUd0bINqFFuuDBMsqKYt4',
    'A3': 'd=AQABBDfqKmMCEKXvQNUUY5ctSrvbbUi1e_oFEgEBBwGJS2N2Y1lQb2UB_eMBAAcIN-oqY0i1e_o&S=AQAAAuNUd0bINqFFuuDBMsqKYt4',
    'maex': '%7B%22v2%22%3A%7B%7D%7D',
    'A1S': 'd=AQABBDfqKmMCEKXvQNUUY5ctSrvbbUi1e_oFEgEBBwGJS2N2Y1lQb2UB_eMBAAcIN-oqY0i1e_o&S=AQAAAuNUd0bINqFFuuDBMsqKYt4&j=WORLD',
    'PRF': 't%3DSBIN.NS%252BTATAPOWER.NS%252BRELIANCE.NS%252BWIPRO.NS%252BTCS.NS%252BHDB%252BSBI%252BHBI%252BTSLA',
    'cmp': 't=1666151774&j=0&u=1---',
     }

    headers = {
        'authority': 'finance.yahoo.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        'dnt': '1',
        'referer': 'https://finance.yahoo.com/quote/TATAPOWER.NS?p=TATAPOWER.NS&.tsrc=fin-srch',
        'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
    }

    params = {
        'p': 'SBIN.NS',
        '.tsrc': 'fin-srch',
    }

    yahoo_html_url = 'https://finance.yahoo.com/quote/SBIN.NS'
    yahoo_html_url=yahoo_html_url.replace("SBIN",name)
    params["p"]=params["p"].replace("SBIN",name)

    response_html = requests.get(yahoo_html_url, params=params, cookies=cookies, headers=headers)

    with open("D:\PROGRAM\python\Flask_app\yahoo.html","w", encoding="utf-8") as fp:
        fp.write(str(response_html.text))

    response_html = HtmlResponse(url="https://random_url",body=response_html.text, encoding="utf-8")

    

    return_data["Market_Price"] = response_html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]/text()').get()
    return_data["Previous_Close"] = response_html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]/text()').get()
    return_data["Open_Price"] = response_html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]/text()').get()

    return_data["market_cap"] = response_html.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/text()').get()
    return_data["volume"] = response_html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer/text()').get()
    return_data["Beta (5Y Monthly)"] = response_html.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[2]/td[2]/text()').get()
    return_data["PE Ratio (TTM)"] = response_html.xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]/text()').get()
    return_data["Avrage Volume"] = response_html.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]/text()').get()
    return_data["stock_name"]=name



    return return_data

    



   

stock.run("0.0.0.0",debug=True)