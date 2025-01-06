"""Support for SwitchBot sensors."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .coordinator import SwitchBotDataUpdateCoordinator

class SwitchBotSensor(CoordinatorEntity[SwitchBotDataUpdateCoordinator], SensorEntity):
    """Define a SwitchBot sensor."""

    def __init__(self, coordinator: SwitchBotDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("value")