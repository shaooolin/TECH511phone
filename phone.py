# phone.py

class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # constructor
        self.name = name
        self.ios_version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.files = []
        self.messages = []  
        # Stores messages received

    def check_messages(self):
        """Print all messages received."""
        print(f"Messages for {self.name}:")
        if not self.messages:
            print("No new messages.")
        else:
            for message in self.messages:
                print(message)

    def call(self, number):
        """Simulate calling a phone number."""
        print(f"{self.name} is calling {number}...")

    def airdrop(self, filename, recipient):
        """Simulate sending a file via AirDrop."""
        print(f"{self.name} is airdropping '{filename}' to {recipient}.")

    def airreceive(self):
        """Simulate receiving a file via AirDrop."""
        print(f"{self.name} received a file via AirDrop.")

    def set_name(self, new_name):
        """Update the name of the phone."""
        if len(new_name) < 3:
            print("Name must be longer than 3 characters.")
        else:
            self.name = new_name
            print(f"Phone name updated to {self.name}")

    def send_imessage(self, recipient, content):
        """Simulate sending an iMessage."""
        if isinstance(recipient, iPhone):
            print(f"{self.name} is sending iMessage to {recipient.name}: '{content}'")
            recipient.messages.append(f"From {self.name}: {content}")
        else:
            print("Recipient is not a valid iPhone instance.")

# Create two instances of iPhone
phone1 = iPhone(
    name="Phone1",
    version="18",
    phone_number="123-456-7890",
    color="black",
    model="iPhone 16 Pro",
)

phone2 = iPhone(
    name="Phone2",
    version="18",
    phone_number="987-654-3210",
    color="white",
    model="iPhone 16 Pro",
)

# Change iPhone names using set_name()
phone1.set_name("A's iPhone")
phone2.set_name("B's iPhone")

# Send an iMessage from phone1 to phone2
phone1.send_imessage(phone2, "Hello, B! How are you?")

# phone2 checks messages
phone2.check_messages()
