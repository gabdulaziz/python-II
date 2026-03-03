
class App:
    def __init__(self, name: str, version: str, size_mb: int, category: str):
        self.name = name
        self.version = version
        self.size_mb = size_mb
        self.category = category

    def launch(self):
        print(f"Launching {self.name} v{self.version}...")

    def update(self, new_version: str):
        self.version = new_version
        print(f"{self.name} updated to version {self.version}")

    def get_app_info(self):
        return f"{self.name} v{self.version} - {self.category} ({self.size_mb}MB)"


class Contact:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def call(self):
        print(f"Calling {self.name} at {self.phone_number}")

    def send_message(self, message: str):
        print(f"Sending message to {self.name}: {message}")

    def get_contact_info(self):
        return f"{self.name} - {self.phone_number} ({self.email})"


class Network:
    def __init__(self, name: str, signal_strength: int, network_type: str):
        self.name = name
        self.signal_strength = signal_strength
        self.network_type = network_type

    def broadcast_signal(self):
        print(f"{self.name} broadcasting {self.network_type} signal at {self.signal_strength}% strength")

    def get_network_info(self):
        return f"{self.name} ({self.network_type}) - Signal: {self.signal_strength}%"



class Battery:
    def __init__(self, capacity: int):
        self.capacity = capacity  # mAh
        self.current_charge = 85  # default %
        self.is_charging = False

    def charge(self):
        self.is_charging = True
        self.current_charge = min(100, self.current_charge + 10)
        print(f"Battery charging: {self.current_charge}%")

    def drain(self, amount: int):
        self.current_charge = max(0, self.current_charge - amount)
        print(f"Battery drained: {self.current_charge}%")

    def get_battery_info(self):
        return f"Battery: {self.current_charge}% charged, {self.capacity}mAh capacity"


class Screen:
    def __init__(self, size: float, resolution: str):
        self.size = size
        self.resolution = resolution
        self.brightness = 50
        self.is_cracked = False

    def adjust_brightness(self, level: int):
        self.brightness = max(0, min(100, level))
        print(f"Screen brightness adjusted to {self.brightness}%")

    def crack_screen(self):
        self.is_cracked = True
        print("Screen is cracked!")

    def get_screen_info(self):
        status = "Cracked" if self.is_cracked else "Intact"
        return f"Screen: {self.size}\" {self.resolution}, Brightness: {self.brightness}%, Status: {status}"


class Camera:
    def __init__(self, megapixels: int):
        self.megapixels = megapixels
        self.has_flash = True
        self.photos_taken = 0

    def take_photo(self):
        self.photos_taken += 1
        print(f"Photo taken! Total photos: {self.photos_taken}, Camera: {self.megapixels}MP")

    def toggle_flash(self):
        self.has_flash = not self.has_flash
        print(f"Flash {'enabled' if self.has_flash else 'disabled'}")

    def get_camera_info(self):
        flash_status = "Yes" if self.has_flash else "No"
        return f"Camera: {self.megapixels}MP, Flash: {flash_status}, Photos: {self.photos_taken}"



class Device:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"Device {self.brand} {self.model} powered on")

    def power_off(self):
        self.is_on = False
        print(f"Device {self.brand} {self.model} powered off")

    def get_info(self):
        return f"Device: {self.brand} {self.model}"


class MobileDevice(Device):
    def __init__(self, brand: str, model: str, phone_number: str, network_type: str):
        super().__init__(brand, model)
        self.phone_number = phone_number
        self.network_type = network_type
        self.network = None

    def connect_to_network(self, network: Network = None):
        if network:
            self.network = network
        if self.network:
            print(f"Connected to {self.network.signal_strength}% {self.network.network_type} network")
        else:
            print("No network available")

    def disconnect_from_network(self):
        self.network = None
        print("Disconnected from network")

    def get_info(self):
        return f"{super().get_info()} | Mobile: {self.phone_number} ({self.network_type})"


class Smartphone(MobileDevice):
    def __init__(self, brand, model, phone_number, network_type, operating_system, storage_capacity):
        super().__init__(brand, model, phone_number, network_type)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity  # GB


        self.battery = Battery(4000)
        self.screen = Screen(6.1, "1170x2532")
        self.camera = Camera(12)


        self.apps = []
        self.contacts = []


    def get_info(self):
        return f"{super().get_info()} | Smartphone: {self.operating_system}, {self.storage_capacity}GB storage"


    def check_battery(self):
        print(self.battery.get_battery_info())

    def adjust_screen(self, brightness):
        self.screen.adjust_brightness(brightness)

    def use_camera(self):
        self.camera.take_photo()


    def install_app(self, app: App):
        self.apps.append(app)
        print(f"App {app.name} installed ({app.size_mb}MB)")

    def remove_app(self, app_name: str):
        self.apps = [a for a in self.apps if a.name != app_name]
        print(f"App {app_name} removed")

    def list_apps(self):
        for a in self.apps:
            print(a.get_app_info())

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added to smartphone")

    def remove_contact(self, name: str):
        self.contacts = [c for c in self.contacts if c.name != name]
        print(f"Contact {name} removed from smartphone")

    def call_contact(self, name: str):
        contact = next((c for c in self.contacts if c.name == name), None)
        if contact:
            contact.call()
        else:
            print(f"No contact found with name {name}")


    def check_signal(self):
        if self.network:
            print(f"Network signal: {self.network.signal_strength}% ({self.network.network_type} - {self.network.name})")
        else:
            print("No network connected")