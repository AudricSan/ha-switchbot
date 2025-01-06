"""Config flow for SwitchBot integration."""

from typing import Any
import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.core import callback
from .const import DOMAIN

class SwitchBotConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for SwitchBot."""

    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult:
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(title="SwitchBot", data={})

        return self.async_show_form(step_id="user")