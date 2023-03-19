from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.make_bet import MakeBetParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_bet(
    ctx: HandlerContext,
    make_bet: Transaction[MakeBetParameter, GamingHallStorage],
) -> None:
    ...