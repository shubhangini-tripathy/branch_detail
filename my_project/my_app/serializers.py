from rest_framework.serializers import ModelSerializer
from post.models import  BranchDetail


class BankDetailSerializer(ModelSerializer):
    class Meta:
        model = BankDetail
        fields = [
                'ifsc',
                'bank_id',
                'branch',
                'address'
                'city',
                'district', 
                'state',
                'bank_name'
                ]        
