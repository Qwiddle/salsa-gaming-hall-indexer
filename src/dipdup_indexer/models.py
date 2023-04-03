from tortoise import fields
from dipdup.models import Model


class Bet(Model):
    user_address = fields.CharField(36, index=True)
    operation = fields.CharField(51, index=True)
    timestamp = fields.DatetimeField()
    tag = fields.CharField(51, index=True)
    game_id = fields.IntField(index=True)
    game_type = fields.IntField(index=True)
    amount = fields.DecimalField(38, 0)
    payout = fields.DecimalField(38, 0, null=True)
    winner = fields.BooleanField(null=True)


class Investment(Model):
    user_address = fields.CharField(36, index=True)
    operation = fields.CharField(51, index=True)
    timestamp = fields.DatetimeField()
    tag = fields.CharField(51, index=True)
    amount = fields.DecimalField(38, 0)
    type = fields.CharField(12, index=True)
