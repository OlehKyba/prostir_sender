import logging
import asyncio

from prostir_sender.config import settings
from prostir_sender.sms_sender import SmsSender

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    sender = SmsSender.from_settings(settings)
    await sender.send_sms(
        phone='+380967539271',
        text='Тестова СМС від PROSTIR!'
    )

asyncio.run(main())
