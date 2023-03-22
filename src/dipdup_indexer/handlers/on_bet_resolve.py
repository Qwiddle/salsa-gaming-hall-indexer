import dipdup_indexer.models as models

from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.resolve_bet import ResolveBetParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_bet_resolve(
    ctx: HandlerContext,
    resolve_bet: Transaction[ResolveBetParameter, GamingHallStorage],
) -> None:
    try:
        game_id = resolve_bet.parameter.game_id
        game_info = resolve_bet.storage.game_info[game_id]
        payout = int(game_info.payout)
        winner = game_info.winner

        bet = await models.Bet.get(
            game_id=game_id
        )

        if bet == None:
            print("bet not found")
        else:
            bet.payout = payout
            bet.winner = winner
            await bet.save()
    except Exception as e:
        print("Error in on_bet_resolve:")
        print(e)
