# generated by datamodel-codegen:
#   filename:  invest.json

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel
from pydantic import Extra


class BankrollCurrency(BaseModel):
    class Config:
        extra = Extra.forbid

    fa2_address: str
    token_id: Optional[str]


class InvestParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    bankroll_currency: BankrollCurrency
    amt: str