#!/bin/bash

echo POST TO API ENPOINTS...

IP=127.0.0.1
PORT=8000

curl -X POST $IP:$PORT/create/ -d "name=Stock Rice&category=food&stock=True&price=10&quantity=500&manufacturer=House of Rice Inc"
echo
# UPDATE FIRST DATA SENT
curl -X PUT $IP:$PORT/update/1 -H "Content-Type: application/json" -d '{"name":"Common Rice","category":"food", "quantity":200, "description":"Most Common Rice Ever"}'
echo
curl -X POST $IP:$PORT/create/ -d "name=Orange Soda&category=food&stock=True&price=20&quantity=200&manufacturer=SodaMe Inc"
echo
curl -X POST $IP:$PORT/create/ -d "name=Stock Soap&category=cleaning&stock=True&price=15&quantity=20&manufacturer=Some Soap Maker"
echo
curl -X POST $IP:$PORT/create/ -d "name=Ultra Premium Soap&category=cleaning&stock=True&price=50&quantity=30&manufacturer=Ultra Soap Company"
echo
# UPDATE DATA
curl -X PUT $IP:$PORT/update/3 -d "name=Ultra Premium Soap&category=cleaning&stock=True&price=50&quantity=30&manufacturer=Ultra Soap Company&description=A Really Expensive Soap"
echo

