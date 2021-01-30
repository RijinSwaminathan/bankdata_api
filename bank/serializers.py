from rest_framework import serializers

from bank.models import Banks


class BankNameSerializer(serializers.Serializer):
    bank_name = serializers.CharField(read_only=True)


class BankDetailsSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ifsc = serializers.CharField(read_only=True)
    bank_id = serializers.IntegerField(read_only=True)
    branch = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    district = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    bank_name = serializers.SerializerMethodField(read_only=True)

    def get_bank_name(self, obj):
        bank_obj = Banks.objects.filter(bank_id=obj.bank_id)
        bank_ser = BankNameSerializer(bank_obj)
        return bank_ser.data
