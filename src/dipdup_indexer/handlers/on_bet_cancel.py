from dipdup.context import HandlerContext
from dipdup.models import Transaction
from dipdup_indexer.types.gaming_hall.parameter.cancel_bet import CancelBetParameter
from dipdup_indexer.types.gaming_hall.storage import GamingHallStorage


async def on_bet_cancel(
    ctx: HandlerContext,
    cancel_bet: Transaction[CancelBetParameter, GamingHallStorage],
) -> None:
    ...