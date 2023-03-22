import dipdup_indexer.models as models

from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.invest import InvestParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_invest(
    ctx: HandlerContext,
    invest: Transaction[InvestParameter, GamingHallStorage],
) -> None:
    try:
        user_address = invest.data.sender_address
        operation = invest.data.hash
        fa2_address = invest.parameter.bankroll_currency.fa2_address
        fa2_id = invest.parameter.bankroll_currency.token_id
        amount = int(invest.parameter.amt)

        await models.Investment.create(
            user_address=user_address,
            operation=operation,
            fa2_address=fa2_address,
            fa2_id=fa2_id,
            amount=amount,
            type="stake"
        )
    except Exception as e:
        print("Error in on_invest:")
        print(e)
