from url_open import url_open
import json


def address_search(prepared_address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    data = {}
    data['output'] = 'json'
    data['ak'] = 'W1TtPpzCzwDBHIdxpAP1hSzWemZQMC2G'
    data['address'] = prepared_address
    temp = url_open(url, data)
    res = json.loads(temp)
    uri = url + '?callback=renderReverse&location='+str(res['result']['location']['lat'])+','+str(res['result']['location']['lng'])+'&output=json&pois=0&ak=W1TtPpzCzwDBHIdxpAP1hSzWemZQMC2G'
    temp1 = url_open(uri)
    temp_shin = temp1[29:-1]
    res1 = json.loads(temp_shin)
    result = res1['result']['addressComponent']['province'] + res1['result']['addressComponent']['city']
    print(result)

if __name__ == '__main__':
    address_search('炫彩互动网络科技有限公司')
