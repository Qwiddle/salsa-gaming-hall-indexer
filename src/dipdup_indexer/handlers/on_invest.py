import dipdup_indexer.models as models

from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.invest import InvestParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage
from dipdup_indexer.util.util import getTagFromToken


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

        tag = getTagFromToken(fa2_address, fa2_id)

        await models.Investment.create(
            user_address=user_address,
            operation=operation,
            tag=tag,
            amount=amount,
            type="stake"
        )
    except Exception as e:
        print("Error in on_invest:")
        print(e)
