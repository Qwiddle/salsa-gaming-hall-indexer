import dipdup_indexer.models as models

from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.divest_shares import DivestSharesParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage
from dipdup_indexer.util.util import getTagFromToken


async def on_divest(
    ctx: HandlerContext,
    divest_shares: Transaction[DivestSharesParameter, GamingHallStorage],
) -> None:
    try:
        user_address = divest_shares.data.sender_address
        operation = divest_shares.data.hash
        timestamp = divest_shares.data.timestamp
        fa2_address = divest_shares.parameter.bankroll_currency.fa2_address
        fa2_id = divest_shares.parameter.bankroll_currency.token_id
        amount = int(divest_shares.parameter.amt)

        tag = getTagFromToken(fa2_address, fa2_id)

        await models.Investment.create(
            user_address=user_address,
            timestamp=timestamp,
            operation=operation,
            tag=tag,
            amount=amount,
            type="unstake"
        )
    except Exception as e:
        print("Error in on_divest_shares:")
        print(e)
