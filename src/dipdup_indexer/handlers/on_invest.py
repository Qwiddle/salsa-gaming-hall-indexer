from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.invest import InvestParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_invest(
    ctx: HandlerContext,
    invest: Transaction[InvestParameter, GamingHallStorage],
) -> None:
    ...