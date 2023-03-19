from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.resolve_bet import ResolveBetParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_bet_resolve(
    ctx: HandlerContext,
    resolve_bet: Transaction[ResolveBetParameter, GamingHallStorage],
) -> None:
    ...