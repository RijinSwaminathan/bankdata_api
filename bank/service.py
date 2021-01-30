from bank.models import Branch, Banks
from bank.serializers import BankDetailsSerializers
from core.response import success_message, not_found


class BankDetailService:
    # get the bank details of the bank by the ifsc code
    def view_bank_details_by_ifsc(self, ifsc_code):
        bank_details = Branch.objects.filter(ifsc=ifsc_code)
        bank_data = BankDetailsSerializers(bank_details, many=True)
        return success_message(message='Fetch the bank details according to ifsc code',
                               data=bank_data.data)

    # get the branch details according to
    def view_branch_by_name_city(self, city, bank_name):
        branch_data = Branch.objects.filter(city=city)
        if Banks.objects.filter(name=bank_name):
            branch_details = BankDetailsSerializers(branch_data, many=True)
            return success_message(message='Fetch the branch Details according to bank name and city name',
                                   data=branch_details.data)
        else:
            return not_found(message='Bank name not exists')
