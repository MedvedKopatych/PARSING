import requests
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

api_link = "https://flyeasy.co/api/search"
start_link = 'https://flyeasy.co/opapi/-fe3-dt1--ht2--ht3--ht4-ctp:magellanjets_list:-/578526bdf6c494c11477ab06/'

opid = start_link.split("/")[-2]

params = {"opIds":[f"{opid}"],"trip":"offers","source":"eq","promoteOpIds":"all"}

with requests.Session() as session:
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    session.headers['Referer'] = start_link
    res = session.post(api_link,json=params)
    for item in res.json()['flights']['departing']:
        print(item['ac']['title'], item['ac']['pax'], item['airportFrom']['name'], item['airportTo']['name'], item['date1'])
