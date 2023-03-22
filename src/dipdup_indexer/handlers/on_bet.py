import dipdup_indexer.models as models

from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.make_bet import MakeBetParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_bet(
    ctx: HandlerContext,
    make_bet: Transaction[MakeBetParameter, GamingHallStorage],
) -> None:
    try:
        user_address = make_bet.data.sender_address
        operation = make_bet.data.hash
        fa2_address = make_bet.parameter.game_currency.fa2_address
        fa2_id = make_bet.parameter.game_currency.token_id
        amount = int(make_bet.parameter.bet)
        game_id = int(next(iter(make_bet.storage.game_info)))

        await models.Bet.create(
            user_address=user_address,
            operation=operation,
            fa2_address=fa2_address,
            fa2_id=fa2_id,
            amount=amount,
            game_id=game_id
        )
    except Exception as e:
        print("Error in on_bet:")
        print(e)
