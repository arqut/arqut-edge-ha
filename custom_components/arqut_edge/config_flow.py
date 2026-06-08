import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN  # We define DOMAIN here or hardcode it

DOMAIN = "arqut_edge"

class ArqutEdgeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the UI config flow for Arqut Edge."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Initial step when the user adds the Integration via UI."""
        errors = {}

        if user_input is not None:
            # Here you can add logic to send a test request to Arqut Edge v0.7.0
            # to check if the API Key is correct before saving.
            
            # If everything is OK, create the entry and save it
            return self.async_create_entry(
                title="Arqut Edge Server", 
                data=user_input
            )

        # Define the input form for the UI using Voluptuous
        DATA_SCHEMA = vol.Schema({
            vol.Required("api_key"): cv.string,
            vol.Optional("host", default="http://localhost:3030"): cv.string,
        })

        return self.async_show_form(
            step_id="user", 
            data_schema=DATA_SCHEMA, 
            errors=errors
        )