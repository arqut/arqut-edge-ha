import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)
DOMAIN = "arqut_edge"

SERVICE_SEND_EVENT_SCHEMA = vol.Schema({
    vol.Required("title"): cv.string,
    vol.Required("description"): cv.string,
    vol.Optional("event_type", default="event"): cv.string,
    vol.Optional("data"): vol.Any(dict, None),
})

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Return True because we will only configure via Config Entry (UI) later."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Arqut Edge integration from a config entry created via UI."""
    
    # Get API Key and Host from the config entry data saved via UI
    api_key = entry.data.get("api_key")
    host = entry.data.get("host", "http://localhost:3030")

    async def async_handle_send_event(call: ServiceCall):
        """Logic called when the service is triggered."""
        title = call.data.get("title")
        description = call.data.get("description")
        event_type = call.data.get("event_type")
        extra_data = call.data.get("data")

        payload = {
            "title": title,
            "description": description,
            "event_type": event_type,
        }
        if extra_data:
            payload["data"] = extra_data

        # Use dynamic host from UI configuration
        url = f"{host.rstrip('/')}/api/events"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        session = async_get_clientsession(hass)
        try:
            async with session.post(url, json=payload, headers=headers, timeout=10) as response:
                if response.status in [200, 201]:
                    _LOGGER.debug("Event sent successfully to Arqut Edge via Config Flow Setup")
                else:
                    _LOGGER.error("Failed to send event. Status code: %s", response.status)
        except Exception as e:
            _LOGGER.error("Error connecting to Arqut Edge API: %s", str(e))

    # Register the service to send events to Arqut Edge
    hass.services.async_register(
        DOMAIN,
        "send_event",
        async_handle_send_event,
        schema=SERVICE_SEND_EVENT_SCHEMA,
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Remove the integration when the user chooses 'Delete' in the UI."""
    hass.services.async_remove(DOMAIN, "send_event")
    return True