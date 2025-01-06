"""The SwitchBot integration."""

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform

from .coordinator import SwitchBotDataUpdateCoordinator
from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.SENSOR]

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the SwitchBot component."""
    hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up SwitchBot from a config entry."""
    coordinator = SwitchBotDataUpdateCoordinator(hass, DEFAULT_SCAN_INTERVAL)

    try:
        await coordinator.async_config_entry_first_refresh()
    except Exception:
        _LOGGER.error("Error fetching initial data")
        return False

    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

# Ajoutez ici les classes et méthodes de l'API SwitchBot
class CannotConnect(Exception):
    """Cannot connect to the SwitchBot API."""

class InvalidAuth(Exception):
    """Invalid auth for the SwitchBot API."""

class DeviceOffline(Exception):
    """Device currently offline."""

# ... (Ajoutez le reste de votre code API ici, y compris les classes Device, Remote, etc.) ...

class SwitchBotAPI:
    """SwitchBot API."""

    def __init__(self, token: str, secret: str) -> None:
        """Initialize."""
        self.token = token
        self.secret = secret

    # ... (Ajoutez toutes les méthodes de l'API ici) ...

    async def get_power_consumption(self, device_id: str):
        """Récupérer les informations de consommation d'énergie pour une prise connectée."""
        try:
            body = await self._request(f"devices/{device_id}/powerConsumption")
            return body
        except Exception as e:
            _LOGGER.error(f"Erreur lors de la récupération de la consommation d'énergie : {e}")
            return None