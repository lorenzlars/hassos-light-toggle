entities = data.get("entities")
data = {
    "transition": data.get("transition"),
    "rgb_color": data.get("rgb_color"),
    "color_name": data.get("color_name"),
    "hs_color": data.get("hs_color"),
    "xy_color": data.get("xy_color"),
    "color_temp": data.get("color_temp"),
    "kelvin": data.get("kelvin"),
    "white_value": data.get("white_value"),
    "brightness": data.get("brightness"),
    "brightness_pct": data.get("brightness_pct"),
    "brightness_step": data.get("brightness_step"),
    "brightness_step_pct": data.get("brightness_step_pct"),
    "profile": data.get("profile"),
    "flash": data.get("flash"),
    "effect": data.get("effect"),
}

filtered_data = {k: v for k, v in data.items() if v is not None}


for entity in entities:
    state = hass.states.get(entity)
    if state.state == 'on':
        filtered_data["entity_id"] = state.entity_id
        hass.services.call("light", "turn_on", filtered_data, False)
