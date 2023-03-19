from tortoise import fields
from dipdup.models import Model


class Investment(Model):
    user_address = fields.CharField(36, pk=True)
    fa2_address = fields.CharField(36, index=True)
    fa2_id = fields.IntField()
    amount = fields.IntField()
