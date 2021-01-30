# Create your views here.
from rest_framework.views import APIView

from bank.service import BankDetailService
from core.response import exception_response

bank_details_service = BankDetailService()


class BankDetailsByIFSC(APIView):
    def get(self, request):
        """
        :param request:
        :return: bank details according to IFSC code
        """
        try:
            ifsc_code = request.GET.get('ifsc')
            return bank_details_service.view_bank_details_by_ifsc(ifsc_code=ifsc_code)
        except Exception as e:
            # log_data.error(f'{e.__str__()}')
            return exception_response(e)


class BankDetailsByName(APIView):
    def get(self, request):
        """
        :param request:
        :return: branch detail by city and branch name
        """
        try:
            city = request.GET.get('city_name')
            bank_name = request.GET.get('bank_name')
            return bank_details_service.view_branch_by_name_city(city=city, bank_name=bank_name)
        except Exception as e:
            # log_data.error(f'{e.__str__()}')
            return exception_response(e)
