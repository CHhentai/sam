import requests
import json



if __name__ == "__main__":
    
    dcity = sys.argv[1]
    acity = sys.argv[2]
    dcityname = sys.argv[3]
    acityname = sys.argv[4]
    date = sys.argv[5]
    

    url = "https://flights.ctrip.com/itinerary/api/12808/products"
    # Referer = "https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2019-07-18"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
        #"Referer": "https://flights.ctrip.com/itinerary/oneway/bjs-sha?date=2020-03-18",
        "Content-Type": "application/json"
    }
    request_payload = {
        "flightWay": "Oneway",
        "classType": "ALL",
        "hasChild": False,
        "hasBaby": False,
        "searchIndex": 1,
        "airportParams": [
            {"dcity": dcity, "acity": acity, "dcityname": dcityname, "acityname": acityname, "date": date, "dcityid": 1, "acityid": 2}
        ]
    }

    # post请求
    response = requests.post(url, data=json.dumps(request_payload), headers=headers).text
    #print(response)
    # 很多航班信息在此分一下
    routeList = json.loads(response).get('data').get('routeList')
    print(routeList)
    # 依次读取每条信息
    if routeList is None:
        print()
    for route in routeList:
        # 判断是否有信息，有时候没有会报错
        if len(route.get('legs')) == 1:
            legs = route.get('legs')
            flight = legs[0].get('flight')
            characteristic = legs[0].get('characteristic')
            # 提取想要的信息
            airlineName = flight.get('airlineName')
            flightNumber = flight.get('flightNumber')
            departureDate = flight.get('departureDate')
            arrivalDate = flight.get('arrivalDate')
            departureCityName = flight.get('departureAirportInfo').get('cityName')           
            arrivalCityName = flight.get('arrivalAirportInfo').get('cityName')           
            lowestPrice = characteristic.get('lowestPrice')

            print(airlineName, ",",
                  flightNumber, ",",
                  departureDate, ",",
                  arrivalDate, ",",
                  departureCityName, ",",
                  departureAirportName, ",",
                  arrivalCityName, ",",
                  arrivalAirportName, ",",
                  lowestPrice)
            

