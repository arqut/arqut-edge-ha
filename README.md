# Arqut Edge Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

This custom integration allows **Home Assistant** to seamlessly communicate with **Arqut Edge (v0.7.0+)**. It registers a native Home Assistant Action (Service) called `arqut_edge.send_event`, allowing you to push real-time notifications and logs to your Arqut mobile app completely via the Home Assistant UI—**Zero YAML configuration required!**

![Icon](images/icon.png)

## Features

- **UI-Based Setup (Config Flow):** Simply input your Arqut Edge API Key directly in the Home Assistant integrations dashboard.
- **Native HA Action:** Send real-time Event Logs with titles, descriptions, types, and rich metadata (like camera snapshots) directly from your automations.
- **Secure Linkage:** Tapping the notification on your smartphone securely routes you back to your Arqut Edge UI over the Arqut VPN.

---

## Installation

### Method 1: HACS (Recommended)

1. Open **HACS** in your Home Assistant instance.
2. Click the three dots `...` in the top-right corner and select **Custom repositories**.
3. Paste your repository URL: `https://github.com/arqut/arqut-edge-ha`
4. Select **Integration** as the category and click **Add**.
5. Find **Arqut Edge Integration** in the HACS list and click **Download**.
6. **Restart** Home Assistant.

### Method 2: Manual Installation

1. Download the latest release source code.
2. Copy the `arqut_edge` folder from `custom_components/` into your Home Assistant's `config/custom_components/` directory.
3. **Restart** Home Assistant.

---

## Setup & Configuration

1. Go to **Settings** -> **Devices & Services** in Home Assistant.
2. Click **Add Integration** in the bottom right.
3. Search for **Arqut Edge Integration**.
4. Enter your configuration details:
   - **API Key:** Your Arqut Edge API authorization token.
   - **Host:** The local URL of your Arqut Edge Add-on (Default: `http://localhost:3030`).
5. Click **Submit**.

---

## How to Use (Automation Example)

Once configured, a new action `arqut_edge.send_event` is available. You can construct automations directly through the Visual Editor without editing `automations.yaml`.

### Example: Motion Alert with Visual UI

When creating a new automation:
1. Set your **Trigger** (e.g., Motion Sensor changes to `on`).
2. For **Actions**, select **Perform Action** and search for `Send Event to Arqut Edge`.
3. Fill in the fields:
   - **Title:** `Security Alert`
   - **Description:** `Motion detected in the Living Room.`
   - **Event Type:** `notification`
   - **Metadata (Optional):** You can pass JSON objects here (e.g., camera URLs).

### YAML Equivalent (For reference)
If you prefer looking at the YAML editor inside the automation UI, it looks like this:

```yaml
alias: "Notify: Motion in Living Room"
trigger:
  - platform: state
    entity_id: binary_sensor.living_room_motion
    to: "on"
action:
  - action: arqut_edge.send_event
    data:
      title: "Security Update"
      description: "Motion detected in the Living Room."
      event_type: "notification"
```

### Troubleshooting & Logs

To enable debug logging for this integration, add the following to your configuration.yaml:

```yaml
logger:
  default: info
  logs:
    custom_components.arqut_edge: debug
```

![Logo](images/logo.png)
