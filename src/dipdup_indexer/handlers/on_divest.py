from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.divest_shares import DivestSharesParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_divest(
    ctx: HandlerContext,
    divest_shares: Transaction[DivestSharesParameter, GamingHallStorage],
) -> None:
    ...