# Create your views here.
import jwt
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler

from bank.models import Branch, Banks
from bank.pagination import LargeResultsSetPagination
from bank.serializers import BankDetailsSerializers
from bankdata_api import settings
from core.response import exception_response, success_message, not_found


class BankDetailsByIFSC(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        """
        :param request:
        :return: bank details according to IFSC code
        """
        try:
            ifsc_code = request.GET.get('ifsc')
            bank_details = Branch.objects.filter(ifsc=ifsc_code)
            bank_data = BankDetailsSerializers(bank_details, many=True)
            return success_message(message='Fetch the bank details according to ifsc code',
                                   data=bank_data.data)
        except Exception as e:
            return exception_response(e)


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class BankDetailsByName(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    pagination_class = LargeResultsSetPagination
    serializer_class = BankDetailsSerializers

    def get(self, request):
        """
        :param request:
        :return: branch detail by city and branch name
        """
        try:
            city = request.GET.get('city_name')
            bank_name = request.GET.get('bank_name')
            branch_data = Branch.objects.filter(city=city)
            page = self.paginate_queryset(branch_data)
            if Banks.objects.filter(name=bank_name):
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)

                serializer = self.get_serializer(branch_data, many=True)
                return success_message(message='Fetch the branch Details according to bank name and city name',
                                       data=serializer.data, )
            else:
                return not_found(message='Bank name not exists')
        except Exception as e:
            return exception_response(e)
