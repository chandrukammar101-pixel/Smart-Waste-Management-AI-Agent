#import random
from datetime import datetime

class WasteBin:
    def __init__(self, bin_id, location):
        self.bin_id = bin_id
        self.location = location
        self.fill_level = random.randint(0, 100)
        self.waste_type = random.choice(
            ["Plastic", "Organic", "Paper", "Metal", "Mixed"]
        )

class SmartWasteManagementAgent:
    def __init__(self):
        self.bins = []

    def add_bin(self, waste_bin):
        self.bins.append(waste_bin)

    def analyze_bin(self, waste_bin):
        fill = waste_bin.fill_level

        if fill >= 90:
            priority = "High"
            action = "Immediate Collection Required"
        elif fill >= 70:
            priority = "Medium"
            action = "Schedule Collection Soon"
        else:
            priority = "Low"
            action = "Monitor"

        return {
            "Bin ID": waste_bin.bin_id,
            "Location": waste_bin.location,
            "Waste Type": waste_bin.waste_type,
            "Fill Level": f"{fill}%",
            "Priority": priority,
            "Recommended Action": action
        }

    def generate_report(self):
        print("\nSMART WASTE MANAGEMENT REPORT")
        print("=" * 50)
        print("Generated:", datetime.now())

        for waste_bin in self.bins:
            result = self.analyze_bin(waste_bin)

            print("\nBin ID:", result["Bin ID"])
            print("Location:", result["Location"])
            print("Waste Type:", result["Waste Type"])
            print("Fill Level:", result["Fill Level"])
            print("Priority:", result["Priority"])
            print("Action:", result["Recommended Action"])

            if result["Priority"] == "High":
                print("ALERT: Collection team notified!")

# -------------------------
# Main Program
# -------------------------

agent = SmartWasteManagementAgent()

locations = [
    "City Center",
    "Railway Station",
    "Shopping Mall",
    "Residential Area",
    "Bus Stand"
]

for i in range(5):
    bin_obj = WasteBin(
        bin_id=f"BIN-{i+1}",
        location=locations[i]
    )
    agent.add_bin(bin_obj)

agent.generate_report()
