from tortoise import fields
from dipdup.models import Model


class Bet(Model):
    user_address = fields.CharField(36, pk=True)
    fa2_address = fields.CharField(36, index=True)
    fa2_id = fields.CharField(4)
    game_id = fields.IntField()
    amount = fields.IntField()


class Investment(Model):
    user_address = fields.CharField(36, pk=True)
    fa2_address = fields.CharField(36, index=True)
    fa2_id = fields.IntField()
    amount = fields.IntField()
