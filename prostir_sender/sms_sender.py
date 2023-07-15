import logging
from typing import TYPE_CHECKING

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.http.async_http_client import AsyncTwilioHttpClient

if TYPE_CHECKING:
    from prostir_sender.config import Settings

log = logging.getLogger(__name__)


class SmsSender:
    def __init__(self, twilio_client: "Client", attempts: int, from_phone: str):
        self._client = twilio_client
        self._attempts = attempts
        self._from_phone = from_phone

    async def send_sms(self, phone: str, text: str) -> None:
        try:
            await self._client.messages.create_async(
                from_=self._from_phone,
                to=phone,
                body=text,
                attempt=self._attempts,
            )
        except TwilioRestException:
            log.exception(
                f"[PROSTIR] During SMS sending: {phone=}, {text=}, error occurred"
            )

    @classmethod
    def from_settings(cls, settings: "Settings") -> "SmsSender":
        http_client = AsyncTwilioHttpClient()
        twilio_client = Client(
            settings.twilio.account_sid,
            settings.twilio.auth_token,
            http_client=http_client,
        )
        twilio_client.http_client.logger.setLevel(logging.INFO)
        return cls(twilio_client, settings.twilio.attempts, settings.twilio.from_phone)
