from django.contrib.auth.models import Group
from rest_framework import status, generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt

from .models import MutualFund
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getCustomer(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def investment_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        investment = Investment.objects.all()
        serializer = InvestmentSerializer(investment, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getInvestment(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvestmentSerializer(investment,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvestmentSerializer(investment, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def stock_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if  request.method == 'GET':
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getStock(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getStockByCustId(request, pk):
    try:
        stock = Stock.objects.filter(customer_id=pk)
        print(stock)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StockSerializer(stock,context={'request': request}, many=True)
        print(serializer.data)
        return Response({'data': serializer.data})


@api_view(['GET'])
def getInvestmentByCustId(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        investment = Investment.objects.filter(customer_id=pk)
        print(investment)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = InvestmentSerializer(investment,context={'request': request}, many=True)
        print(serializer.data)
        return Response({'data': serializer.data})

@api_view(['GET', 'POST'])
def mutualfunds_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        funds = MutualFund.objects.all()
        serializer = MutualFundSerializer(funds, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = MutualFundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getMutualFunds(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        fund = MutualFund.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MutualFundSerializer(fund,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MutualFundSerializer(fund, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
