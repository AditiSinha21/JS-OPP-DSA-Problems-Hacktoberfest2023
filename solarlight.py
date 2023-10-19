class SolarLight:
    def __init__(self, solar_panel_capacity, battery_capacity):
        self.solar_panel_capacity = solar_panel_capacity  # In watts
        self.battery_capacity = battery_capacity  # In watt-hours
        self.charge_level = 0  # Current battery charge level in watt-hours
        self.is_daytime = True  # Assume it's daytime initially

    def charge_battery(self, solar_intensity):
        # During the day, the solar panel charges the battery
        if self.is_daytime:
            self.charge_level += solar_intensity
            # Ensure the battery doesn't overcharge
            if self.charge_level > self.battery_capacity:
                self.charge_level = self.battery_capacity

    def turn_on_light(self):
        # Check if it's nighttime and the battery has charge
        if not self.is_daytime and self.charge_level > 0:
            # Calculate the power consumption of the LED light
            led_power = 5  # Example LED power consumption in watts
            # Check if the battery can power the LED light
            if self.charge_level >= led_power:
                self.charge_level -= led_power
                return "Light is on."
            else:
                return "Not enough charge to turn on the light."
        else:
            return "It's daytime or the battery is empty."

    def toggle_daytime(self):
        self.is_daytime = not self.is_daytime

# Example usage
solar_light = SolarLight(solar_panel_capacity=10, battery_capacity=50)

# Simulate a day-night cycle
solar_light.toggle_daytime()  # Nighttime
solar_light.charge_battery(8)  # Simulate solar charging with 8 watts of solar intensity
print(solar_light.turn_on_light())  # Try to turn on the light

solar_light.toggle_daytime()  # Daytime
solar_light.charge_battery(8)  # Simulate solar charging during the day
print(solar_light.turn_on_light())  # Try to turn on the light again
