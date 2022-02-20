from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from gateway.settings import CURRENTURLS
from datetime import  datetime
class CarList(APIView):
    def get(self, request):
        page = self.request.query_params.get('page')
        pagesize = self.request.query_params.get('size')
        showAll = self.request.query_params.get('showAll')
        r = requests.get(CURRENTURLS['cars'] + f'?page={page}&size={pagesize}&showAll={showAll}')
        return Response(data=r.json())

class CarDetail(APIView):
    def get(self, request, pk = None):
        r = requests.get(CURRENTURLS['cars'] + '/' + str(pk))
        return Response(data=r.json())

class RentalDetail(APIView):
    def get(self, request, pk = None):
        r = requests.get(CURRENTURLS['rental'] + '/' + str(pk))
        if r.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rental = r.json()
        r = requests.get(CURRENTURLS['cars'] + '/' + rental['carUid'])
        cars = r.json()
        r = requests.get(CURRENTURLS['payments'] + '/' + rental['paymentUid'])
        payment = r.json()
        returnValue = rental
        returnValue['car'] = cars
        returnValue['payment'] = payment

        return Response(data=returnValue)

    def delete(self, reqest, pk = None):
        r = requests.get(CURRENTURLS['rental'] + '/' + str(pk))
        if r.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rental = r.json()
        r = requests.get(CURRENTURLS['cars'] + '/' + rental['carUid'])
        cars = r.json()
        r = requests.get(CURRENTURLS['payments'] + '/' + rental['paymentUid'])
        payment = r.json()

        carsValue = requests.patch(CURRENTURLS['cars'] + '/' + cars['carUid'], data={'availability': True})
        carsValue = carsValue.json()
        rentalValue = requests.patch(CURRENTURLS['rental'] + '/' + str(pk), data={'status': 'CANCELED'})
        rentalValue = rentalValue.json()
        paymentValue = requests.patch(CURRENTURLS['payments'] + '/' + rental['paymentUid'], data={'status': 'CANCELED'})
        paymentValue = paymentValue.json()

        return Response(status = status.HTTP_204_NO_CONTENT)

class RentalList(APIView):
    def get(self, request):
        username = self.request.headers.get('X-User-Name', None)

        r = requests.get(CURRENTURLS['rental'], headers = {'X-User-Name' : username})
        rental = r.json()
        len_rental = len(rental)
        returnValue = []
        for i in range(len_rental):
            returnValue.append(rental[i])
            r = requests.get(CURRENTURLS['cars'] + '/' + rental[i]['carUid'])
            cars = r.json()
            r = requests.get(CURRENTURLS['payments'] + '/' + rental[i]['paymentUid'])
            payment = r.json()
            returnValue[i]['car'] = cars
            returnValue[i]['payment'] = payment

        return Response(data=returnValue)

    def post(self, request):
        username = self.request.headers.get('X-User-Name', None)
        request_body = self.request.data
        caruid = request_body["carUid"]
        r = requests.get(CURRENTURLS['cars'] + '/' + caruid)
        data = r.json()

        if data["availability"] == True:
            requests.patch(CURRENTURLS['cars'] + '/' + caruid, data={'availability':False})
            dateFrom = datetime.fromisoformat(request_body["dateFrom"])
            dateTo = datetime.fromisoformat(request_body["dateTo"])
            rentalDays = abs(dateFrom - dateTo)
            price = int(rentalDays.days) * data["price"]

            r = requests.post(CURRENTURLS['payments'], data = {"status":"PAID", "price": price})
            payment = r.json()
            r = requests.post(CURRENTURLS['rental'], data = {"username" : username,
                "paymentUid":payment['paymentUid'], "carUid":caruid, "dateFrom":request_body["dateFrom"],
                "dateTo":request_body["dateTo"], "status":"IN_PROGRESS"
            })
            rental = r.json()
            returnValue = rental
            returnValue['payment'] = payment
            return Response(data=returnValue)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
  "message": "Арендовано",
  "errors": [
    {
      "field": "не знаю",
      "error": "Да "
    }
  ]
})

class RentalFinish(APIView):
    def post(self, request, pk = None):
        r = requests.get(CURRENTURLS['rental'] + '/' + str(pk))
        if r.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        rental = r.json()
        r = requests.get(CURRENTURLS['cars'] + '/' + rental['carUid'])
        cars = r.json()


        carsValue = requests.patch(CURRENTURLS['cars'] + '/' + cars['carUid'], data={'availability': True})

        rentalValue = requests.patch(CURRENTURLS['rental'] + '/' + str(pk), data={'status': 'FINISHED'})

        return Response(status = status.HTTP_204_NO_CONTENT)



